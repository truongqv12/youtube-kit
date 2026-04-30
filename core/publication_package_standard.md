# Publication Package Standard

## Purpose
Build a publish-ready package after the script is stable.
The package must help the operator choose title, thumbnail, description, search-facing metadata, and 2 Shorts derivatives for the target audience.

## Hard rules
- External web research is mandatory for thumbnail and title decisions.
- If there is no real web access, this step must fail.
- Do not choose thumbnail style from intuition alone.
- Separate:
  - observed market patterns
  - recommended patterns for this channel
  - patterns to avoid
- Minimum market scan:
  - at least 8 Japan-targeted YouTube or adjacent-market examples
  - at least 5 directly relevant senior / health / explainer examples when available
  - at least 3 official or primary guidance sources for platform, accessibility, or health-policy constraints
- Title, thumbnail, and description must match the actual script, opening hook, and `07A_retention_visual_plan.json` when present.
- Health framing must remain educational, cautious, and non-alarmist.
- Apply `core/title_thumbnail_psychology_standard.md` for CTR angles and thumbnail emotion selection.
- Thumbnail text must be minimal and readable for older viewers.
- Final output must be bilingual:
  - Japanese for publish use
  - Vietnamese explanation for operator understanding
- Must include 2 Shorts derivatives extracted from the long-form angle.
- Step 10 must read `09_export_qc_report.md` instead of old QA or operator-review artifacts.

## Required research dimensions
1. Target-audience click behavior
2. Niche thumbnail patterns in Japan
3. YouTube official title / metadata / thumbnail guidance
4. Policy or misinformation risk relevant to title and thumbnail claims
5. Readability / accessibility considerations for older viewers

## Required decision objects
- 3 title candidates in Japanese, each with `ctr_psychology_angle`, `viewer_question`, and `ctr_prediction_reasoning`
- 3 thumbnail concepts in Japanese, each with `emotion_level`, `safety_rationale`, and script alignment rationale
- 1 selected final package linked to the opening hook and full script payoff
- 2 Shorts derivatives with hook + cut-angle + CTA back to long-form
- 1 short rationale for why the selected package is strongest for this channel and video
