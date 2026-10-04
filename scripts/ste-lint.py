#!/usr/bin/env python3
"""Deterministic structural linter and fidelity checker for the asd-ste100 skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

EXIT_OK = 0
EXIT_VIOLATIONS = 1
EXIT_USAGE = 2

FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
FENCE_CAPTURE_RE = re.compile(r"```[^\n]*\n(.*?)```|~~~[^\n]*\n(.*?)~~~", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
WORD_RE = re.compile(r"\b[\w]+(?:[-'][\w]+)*\b", re.UNICODE)
LIST_ITEM_RE = re.compile(r"^\s*(?:[-+*]|\d+[.)])\s+(.*\S)\s*$")

CONTRACTIONS = {
    "ain't", "aren't", "can't", "couldn't", "didn't", "doesn't", "don't",
    "hadn't", "hasn't", "haven't", "he'd", "he'll", "he's", "i'd", "i'll",
    "i'm", "i've", "isn't", "it's", "let's", "mustn't", "shan't", "she'd",
    "she'll", "she's", "shouldn't", "that's", "there's", "they'd", "they'll",
    "they're", "they've", "wasn't", "we'd", "we'll", "we're", "we've",
    "weren't", "what's", "where's", "who's", "won't", "wouldn't", "you'd",
    "you'll", "you're", "you've",
}
CONTRACTION_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(x) for x in sorted(CONTRACTIONS, key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)
NEGATION_RE = re.compile(r"\b(?:not|no|never|cannot|without)\b", re.IGNORECASE)
NUMBER_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:[.,]\d+)?(?![\w.])")
PERCENT_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:[.,]\d+)?\s*%(?!\w)")
RANGE_PATTERNS = [
    re.compile(r"(?<![\w.])([-+]?\d+(?:[.,]\d+)?)\s*(?:-|–|—|to)\s*([-+]?\d+(?:[.,]\d+)?)(?![\w.])", re.IGNORECASE),
    re.compile(r"\bbetween\s+([-+]?\d+(?:[.,]\d+)?)\s+and\s+([-+]?\d+(?:[.,]\d+)?)\b", re.IGNORECASE),
]
ACRONYM_RE = re.compile(r"\b[A-Z]{2,}(?:[0-9]+)?\b")
ID_RE = re.compile(
    r"\b(?:[A-Za-z]+[_-][A-Za-z0-9_-]*\d[A-Za-z0-9_-]*|[A-Za-z]*\d[A-Za-z0-9]*[-_][A-Za-z0-9_-]+|[A-Z]{1,6}-\d+[A-Z0-9-]*)\b"
)
UNIT_AFTER_NUMBER_RE = re.compile(
    r"(?<![\w.])[-+]?\d+(?:[.,]\d+)?\s*(°[CFK]|%|[A-Za-zµμΩ]{1,10})(?!\w)"
)
UNIT_STOPWORDS = {"and", "to", "or", "for", "with", "from", "through", "at", "in", "on", "of", "by", "between"}


@dataclass(frozen=True)
class Finding:
    rule: str
    line: int
    message: str
    text: str


def read_text(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def strip_fenced_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def replace_inline_code(text: str) -> str:
    return INLINE_CODE_RE.sub(" CODE ", text)


def normalize_number(value: str) -> str:
    value = value.strip().replace(",", ".")
    try:
        number = float(value)
    except ValueError:
        return value
    if number.is_integer():
        return str(int(number))
    return format(number, ".15g")


def sentence_spans(text: str) -> list[tuple[str, int]]:
    """Return sentence-like spans and their 1-based line number."""
    text = strip_fenced_code(text)
    spans: list[tuple[str, int]] = []
    start = 0
    for match in re.finditer(r"[.!?]+(?=(?:[\"'\)\]]*)?(?:\s|$))", text):
        end = match.end()
        segment = text[start:end].strip()
        if segment:
            line = text.count("\n", 0, start) + 1
            spans.append((segment, line))
        start = end
    tail = text[start:].strip()
    if tail:
        line = text.count("\n", 0, start) + 1
        spans.append((tail, line))
    return spans


def word_count(sentence: str) -> int:
    return len(WORD_RE.findall(replace_inline_code(sentence)))


def paragraph_blocks(text: str) -> list[tuple[str, int]]:
    text = strip_fenced_code(text)
    blocks: list[tuple[str, int]] = []
    for match in re.finditer(r"(?:^|\n\s*\n)(.*?)(?=\n\s*\n|\Z)", text, re.DOTALL):
        block = match.group(1).strip()
        if not block:
            continue
        line = text.count("\n", 0, match.start(1)) + 1
        blocks.append((block, line))
    return blocks


def is_list_block(block: str) -> bool:
    lines = [line for line in block.splitlines() if line.strip()]
    return bool(lines) and all(LIST_ITEM_RE.match(line) for line in lines)


def first_alpha(text: str) -> str | None:
    match = re.search(r"[A-Za-z]", re.sub(r"`[^`]+`", "", text))
    return match.group(0) if match else None


def list_blocks(text: str) -> list[tuple[list[tuple[int, str]], str | None, int | None]]:
    lines = text.splitlines()
    results: list[tuple[list[tuple[int, str]], str | None, int | None]] = []
    i = 0
    while i < len(lines):
        if not LIST_ITEM_RE.match(lines[i]):
            i += 1
            continue
        start = i
        items: list[tuple[int, str]] = []
        while i < len(lines):
            match = LIST_ITEM_RE.match(lines[i])
            if not match:
                break
            items.append((i + 1, match.group(1).strip()))
            i += 1
        lead_idx = start - 1
        while lead_idx >= 0 and not lines[lead_idx].strip():
            lead_idx -= 1
        lead = lines[lead_idx].strip() if lead_idx >= 0 else None
        results.append((items, lead, lead_idx + 1 if lead_idx >= 0 else None))
    return results


def lint_text(text: str, text_type: str) -> list[Finding]:
    findings: list[Finding] = []
    clean = strip_fenced_code(text)
    limit = 20 if text_type == "procedure" else 25

    for sentence, line in sentence_spans(clean):
        count = word_count(sentence)
        if count > limit:
            findings.append(Finding(
                "sentence-length",
                line,
                f"{text_type} sentence has {count} words; maximum is {limit}",
                sentence,
            ))

    for block, line in paragraph_blocks(clean):
        if block.startswith("#") or is_list_block(block):
            continue
        count = len(sentence_spans(block))
        if count > 6:
            findings.append(Finding(
                "paragraph-length",
                line,
                f"paragraph has {count} sentences; maximum is 6",
                block,
            ))

    for line_no, line_text in enumerate(clean.splitlines(), start=1):
        for match in CONTRACTION_RE.finditer(line_text):
            findings.append(Finding(
                "contraction",
                line_no,
                f"write the contraction '{match.group(0)}' in full",
                line_text.strip(),
            ))
        if ";" in line_text:
            findings.append(Finding(
                "semicolon",
                line_no,
                "do not use a semicolon; split or restructure the sentence",
                line_text.strip(),
            ))

    for items, lead, lead_line in list_blocks(clean):
        if lead is None or not lead.endswith(":"):
            findings.append(Finding(
                "vertical-list-lead",
                lead_line or items[0][0],
                "introductory text before a vertical list must end with a colon",
                lead or items[0][1],
            ))
        for item_line, item in items:
            alpha = first_alpha(item)
            if alpha is not None and not alpha.isupper():
                findings.append(Finding(
                    "vertical-list-capitalization",
                    item_line,
                    "each vertical-list item must start with an uppercase letter",
                    item,
                ))
            if item.endswith(",") or item.endswith(";"):
                findings.append(Finding(
                    "vertical-list-punctuation",
                    item_line,
                    "a vertical-list item must not end with a comma or semicolon",
                    item,
                ))
        if items and not items[-1][1].endswith("."):
            findings.append(Finding(
                "vertical-list-final-period",
                items[-1][0],
                "the last vertical-list item must end with a period",
                items[-1][1],
            ))

    return sorted(findings, key=lambda item: (item.line, item.rule, item.message))


def multiset_diff(source: Counter[str], target: Counter[str]) -> tuple[list[str], list[str]]:
    missing = list((source - target).elements())
    added = list((target - source).elements())
    return sorted(missing), sorted(added)


def extract_ranges(text: str) -> Counter[str]:
    values: Counter[str] = Counter()
    for pattern in RANGE_PATTERNS:
        for match in pattern.finditer(text):
            left = normalize_number(match.group(1))
            right = normalize_number(match.group(2))
            values[f"{left}..{right}"] += 1
    return values


def extract_units(text: str) -> Counter[str]:
    units: Counter[str] = Counter()
    for match in UNIT_AFTER_NUMBER_RE.finditer(text):
        unit = match.group(1)
        if unit == "%" or unit.lower() in UNIT_STOPWORDS:
            continue
        units[unit] += 1
    return units


def extract_identifiers(text: str) -> Counter[str]:
    values: Counter[str] = Counter()
    for match in INLINE_CODE_RE.finditer(text):
        token = match.group(1).strip()
        if token:
            values[token] += 1
    without_code = INLINE_CODE_RE.sub(" ", text)
    for match in ID_RE.finditer(without_code):
        values[match.group(0)] += 1
    return values


def extract_code_blocks(text: str) -> Counter[str]:
    blocks: Counter[str] = Counter()
    for match in FENCE_CAPTURE_RE.finditer(text):
        content = (match.group(1) if match.group(1) is not None else match.group(2)).strip("\n")
        blocks[content] += 1
    return blocks


def extract_fidelity(text: str) -> dict[str, Counter[str]]:
    code_blocks = extract_code_blocks(text)
    text = strip_fenced_code(text)
    percentages = Counter(re.sub(r"\s+", "", m.group(0)).replace(",", ".") for m in PERCENT_RE.finditer(text))
    ranges = extract_ranges(text)
    numbers = Counter(normalize_number(m.group(0)) for m in NUMBER_RE.finditer(text))
    acronyms = Counter(m.group(0) for m in ACRONYM_RE.finditer(text))
    identifiers = extract_identifiers(text)
    units = extract_units(text)
    negations = Counter({"negation": len(NEGATION_RE.findall(text))})

    return {
        "numbers": numbers,
        "ranges": ranges,
        "percentages": percentages,
        "units": units,
        "acronyms": acronyms,
        "identifiers": identifiers,
        "negations": negations,
        "code_blocks": code_blocks,
    }


def details_compare(source_text: str, target_text: str) -> dict[str, object]:
    source = extract_fidelity(source_text)
    target = extract_fidelity(target_text)
    differences: dict[str, dict[str, list[str]]] = {}

    for category in source:
        missing, added = multiset_diff(source[category], target[category])
        if missing or added:
            differences[category] = {"missing": missing, "added": added}

    return {
        "preserved": not differences,
        "differences": differences,
        "checked_categories": list(source.keys()),
    }


def print_lint(findings: list[Finding], text_type: str, as_json: bool) -> None:
    if as_json:
        print(json.dumps({
            "mode": "lint",
            "text_type": text_type,
            "ok": not findings,
            "violations": [asdict(item) for item in findings],
        }, indent=2, ensure_ascii=False))
        return
    if not findings:
        print("0 violations")
        return
    for item in findings:
        print(f"ERROR [{item.rule}] line {item.line}: {item.message}")
        print(f"  {item.text}")
    print(f"{len(findings)} violation(s)")


def print_details(result: dict[str, object], as_json: bool) -> None:
    if as_json:
        print(json.dumps({"mode": "details", **result}, indent=2, ensure_ascii=False))
        return
    if result["preserved"]:
        print("technical-detail fidelity: PASS")
        return
    print("technical-detail fidelity: FAIL")
    differences = result["differences"]
    assert isinstance(differences, dict)
    for category, diff in differences.items():
        print(f"{category}:")
        missing = diff["missing"]
        added = diff["added"]
        if missing:
            print("  missing: " + ", ".join(missing))
        if added:
            print("  added: " + ", ".join(added))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Deterministic structural linter and technical-detail fidelity checker for ASD-STE100-oriented text."
    )
    parser.add_argument("--json", action="store_true", help="write machine-readable JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)

    lint = subparsers.add_parser("lint", help="check deterministic structural rules")
    lint.add_argument("--type", choices=("procedure", "description"), required=True)
    lint.add_argument("file", help="UTF-8 text file to lint")

    details = subparsers.add_parser("details", help="compare technical details in original and rewritten text")
    details.add_argument("original", help="UTF-8 source text")
    details.add_argument("rewritten", help="UTF-8 rewritten text")

    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        if args.command == "lint":
            findings = lint_text(read_text(args.file), args.type)
            print_lint(findings, args.type, args.json)
            return EXIT_OK if not findings else EXIT_VIOLATIONS

        result = details_compare(read_text(args.original), read_text(args.rewritten))
        print_details(result, args.json)
        return EXIT_OK if result["preserved"] else EXIT_VIOLATIONS
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return EXIT_USAGE


if __name__ == "__main__":
    raise SystemExit(main())
