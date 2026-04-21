# Canonical Script Unit Standard

## Definition
A canonical script unit is one natural spoken narration line that can be pasted directly into TTS with no cleanup.

## Hard rules
- The final script must be authored as canonical script units.
- `full_script` must equal `"
".join(canonical_script_units)`.
- No later step may rewrite `script_text`.
- Final exporter must use canonical units directly.
- If reconstruction fails, rollback to script writer step.
- Every unit must be written for the ear, not for the page.
- Every unit must contain one spoken thought, or two tightly linked clauses only.
- Maximum 2 clauses per unit.

## TTS-safe quality gate
A canonical unit passes only if all checks below pass:
- plain spoken language only
- one spoken thought, or two tightly linked clauses that still read as one natural breath group
- no headings, section labels, chapter markers, bullets, numbering, emojis-as-markers, or markdown syntax
- no speaker tags, no bracketed notes, no parenthetical production notes, no stage directions, no camera directions, no SFX notes
- no title-card language, outline fragments, or CTA inserts unless the CTA itself is natural spoken narration for that exact moment
- normal sentence punctuation for the channel language is allowed
- the unit sounds natural when read aloud in sequence with the neighboring units

## Naturalness gate
A canonical unit fails if any of the following are true:
- it sounds like explanatory prose written for a page instead of spoken narration
- it contains more than one natural pause and would be easier to understand as two lines
- it uses abstract nouns without a concrete everyday hook when the line could be made more direct
- it depends on repeated lecture patterns such as `X は〜です` or stacked formal connectives line after line
- it sounds machine-translated, overly smoothed, or too repetitive

## Rhythm gate
Across a full script:
- mix short, medium, and slightly longer lines
- do not write 3 or more consecutive lines with the same sentence pattern
- do not reuse the same opener more than twice in a 10-line window unless the script truly requires it
- do not reuse the same softener ending more than twice in an 8-line window unless the script truly requires it

## Breath-group gate
- if a line forces an unnatural long inhale, split it
- if a comma-heavy line contains more than one natural pause, split it
- if a line looks better on a slide than in a TTS engine, it fails

## Fail examples
These are NOT canonical units:
- `1. 朝食前の歩き方`
- `【注意】朝食前は無理をしないでください`
- `ポイント1：水分を確認しましょう`
- `(ここで少し間を置く) 朝はゆっくり歩きましょう`
- `司会者: 今日は歩き方のコツを見ていきます`
- `朝の水分補給は重要です。朝の水分補給は血流維持に役立ちます。朝の水分補給は転倒予防にもつながります。`

## Pass examples
These are closer to canonical units:
- `朝は、思ったより水分が足りていないことがあります。`
- `まず一口でも飲んでおくと、動き始めが少し楽な方もいます。`
- `すぐに変わらなくても大丈夫です。無理のない範囲で続けてみましょう。`

## Pass principle
If a line looks better on a slide than in a TTS engine, it fails.
