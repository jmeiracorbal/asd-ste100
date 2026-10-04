# ASD-STE100 transformation examples

These examples show the intended behavior of the skill. They demonstrate style and structure. They do not prove formal ASD-STE100 compliance.

## Procedure

Before:

`The component should then be carefully installed into the housing after making sure that the connector has been disconnected.`

After:

`Make sure that the connector is disconnected.`

`Install the component in the housing.`

Why:

- The condition comes before the action.
- The instruction uses direct imperative language.
- The passive construction and unnecessary adverbs are removed.

## Description

Before:

`The unit is responsible for performing the control of the process that is carried out by the system.`

After:

`The unit controls the process.`

Why:

- The sentence uses active voice.
- The nominalized phrase is replaced with a direct verb.
- The technical meaning is unchanged.

## Consistent terminology

Before:

`Start the device. When the equipment is operating, check the indicator.`

After:

`Start the device.`

`When the device operates, check the indicator.`

Why:

- `device` is used consistently for the same concept.
- The text does not alternate between `device` and `equipment` only for style.

## Explicit condition

Before:

`Reset the unit when the indicator stays on.`

After:

`If the indicator stays on, reset the unit.`

Why:

- The reader knows the condition before the required action.

## Direct wording

Before:

`In order to be able to complete the procedure, the operator will need to provide the identifier that was previously assigned to the item.`

After:

`To complete the procedure, the operator must supply the item identifier.`

Why:

- The sentence removes unnecessary wording.
- `item identifier` is an explicit technical noun.
- The required action is clear.

## Complete sentences

Before:

`When the indicator is red, move the control to the OFF position.`

Bad simplification:

`Indicator red. Control to OFF.`

Better:

`If the indicator is red, set the control to OFF.`

Why:

- The shorter fragments remove grammatical information.
- The better version keeps the condition, subject, verb, and action.
- The meaning stays complete.

## Contractions

Before:

`If the surface is wet, don't touch the unit.`

After:

`If the surface is wet, do not touch the unit.`

Why:

- The contraction is written in full.
- The prohibition keeps the same meaning.

## Vertical list

Before:

`Before you start the procedure, make sure that the guard is installed, the access panel is closed, the control is in the OFF position, and the area is clear.`

After:

`Before you start the procedure, make sure that:`

- `The guard is installed`
- `The access panel is closed`
- `The control is in the OFF position`
- `The area is clear.`

Why:

- The list makes multiple conditions easier to scan.
- No condition is removed.
- The relationship between the introduction and the items stays explicit.
- The items do not end with commas or semicolons.
- The last item ends with a period.

## Paragraph length

Before:

`The system has two operating states. The first state is normal operation. The second state is standby. The indicator is green during normal operation. The indicator is amber during standby. The control changes the operating state. The change can take up to five seconds.`

After:

`The system has two operating states. The first state is normal operation. The second state is standby.`

`The indicator is green during normal operation. The indicator is amber during standby. The control changes the operating state. The change can take up to five seconds.`

Why:

- The original paragraph has seven sentences.
- The revised text divides the information at a logical boundary.
- No information is removed to satisfy the paragraph limit.

## Preserve modality and negation

Before:

`The operator must not open the cover while the unit is energized.`

After:

`If the unit is energized, the operator must not open the cover.`

Why:

- `must not` keeps the same prohibition.
- The condition becomes explicit.
- The revision does not weaken the requirement.

## Preserve quantities and units

Before:

`Keep the distance between 10 mm and 15 mm.`

After:

`Keep a distance of 10 mm to 15 mm.`

Why:

- The quantity and unit are preserved.
- The permitted range is unchanged.

## Ambiguous source

Before:

`Move the unit next to the support and inspect it.`

Do not silently rewrite this as if `it` has one certain referent.

Preferred behavior:

`The word "it" is ambiguous. It can refer to the unit or the support. Identify the intended referent before you rewrite the instruction.`

Why:

- The source contains more than one plausible interpretation.
- The skill must identify the ambiguity instead of inventing an answer.

## Non-English output

If the user asks for non-English text in an ASD-STE100 style, apply the same clarity principles but do not call the result formally compliant with ASD-STE100.

Example:

Before:

`En el caso de que la unidad deje de funcionar de manera inesperada, el sistema intentará proceder nuevamente a su puesta en marcha siempre que la configuración permita llevar a cabo dicha operación.`

STE-inspired Spanish:

`Si la unidad se detiene de forma inesperada, el sistema puede iniciarla otra vez.`

`La configuración controla esta acción.`