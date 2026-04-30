# STEP 07 — Image Prompt Builder Reference-First

## Goal
Turn each canonical script unit into one Nano Banana still-image prompt.

## New key rule
Do not jump directly from a script line to an image prompt.
Must resolve `line_context_frame` first, then build `prompt_img_nano`.
Read `07A_retention_visual_plan.json` before building opening rows.
Read `01_project_manifest.json`. Always use `06_script_canonical.json`; Step 06B normalizes this artifact in place when used.

## Must decide per row
- scene_group_id
- scene_archetype
- host_usage
- visible_text_policy
- prompt_mode
- line-context-locked prompt

## Output
- `07_image_prompt_table.csv`

## Retention handling
- Normal rows stay line-context locked.
- Rows approved in `07A_retention_visual_plan.json` may use bounded opening visual overrides.
- Optional intermediate metadata may include `retention_beat_type`, `attention_target`, and `visual_hook_override_used`; Step 09 strips all metadata from final export.
