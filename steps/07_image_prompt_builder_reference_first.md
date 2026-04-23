# STEP 07 — Image Prompt Builder Reference-First

## Goal
Turn each canonical script unit into one Nano Banana still-image prompt.

## New key rule
Do not jump directly from a script line to an image prompt.
Must resolve `line_context_frame` first, then build `prompt_img_nano`.

## Must decide per row
- scene_group_id
- scene_archetype
- host_usage
- visible_text_policy
- prompt_mode
- line-context-locked prompt

## Output
- `07_image_prompt_table.csv`
