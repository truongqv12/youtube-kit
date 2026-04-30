# Step 07A — Retention Visual Plan

## Purpose

Create `07A_retention_visual_plan.json`, a sidecar artifact that guides stronger opening visuals, motion intent, and publication packaging without changing script text or final export columns.

## Inputs

- `core/system_principles.md`
- `core/policy_guardrails.md`
- `core/hook_engineering_standard.md`
- `core/pacing_control_standard.md`
- `core/title_thumbnail_psychology_standard.md`
- `knowledge/visual/00_visual_strategy.md`
- `knowledge/visual/05_negative_visual_rules.md`
- channel config, editorial profile, visual profile
- `01_project_manifest.json`
- `01_intake_spec.json`
- `02_topic_strategy.json`
- `03_research_brief.json`
- `04_policy_report.json`
- `05_outline.json`
- source-of-truth script: `06_script_canonical.json` unless manifest explicitly adopts `06B_script_canonical.json`

## Output

- `07A_retention_visual_plan.json`

## Contract

The artifact must include:

- `script_source_of_truth`
- `opening_strategy`
- `hook_type`
- `viewer_question`
- `allowed_non_linear_rows`
- `tension_curve`
- `daily_life_anchor`
- `thumbnail_emotion_hint`
- `retention_beats`
- `row_visual_overrides`
- `motion_intents`
- `title_thumbnail_angles`
- `safety_guardrails`
- `qc_checks`

## Rules

- Do not rewrite script text.
- Non-linear visual overrides are allowed only for rows 1-3 or first 10-15 seconds.
- Every override must remain connected to the micro-topic, viewer question, and research-backed concern.
- Keep all retention metadata out of `09_final_three_column.csv`.
- No panic, gore, diagnosis, cure promise, or guaranteed prevention framing.
