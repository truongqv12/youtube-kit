# STEP 08 — Video Prompt Builder Veo 3 i2v (Non-Dialogue)

## Goal
Turn each still image prompt into one Veo 3 image-to-video motion prompt.

## New key rule
Read `07A_retention_visual_plan.json` and use row-level motion intent when available.
Read `01_project_manifest.json`. Always use `06_script_canonical.json`; Step 06B normalizes this artifact in place when used.
This prompt is motion-only.
Do not re-describe the full image.
Do not add new text.
Do not imply speech if non-dialogue mode is enabled.

## Must decide per row
- i2v_mode
- motion_strategy
- recommended_duration_sec
- motion_role
- attention_target
- prompt_video_veo3

## Output
- `08_video_prompt_table.csv`
