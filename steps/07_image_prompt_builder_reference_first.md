# STEP 07 — Image Prompt Builder Reference-First

## Goal
Turn each canonical script unit into one Nano Banana still-image prompt.
The prompt must work for YouTube voiceover production: one TTS line maps to one clear keyframe.

## New key rule
Do not jump directly from a script line to an image prompt.
Must resolve `line_context_frame` first, then build `prompt_img_nano`.
If host imagery is used, must resolve host identity from `00_host_character_sheet.json` or equivalent channel state before writing the prompt.

## Must decide per row
- scene_group_id
- scene_archetype
- host_usage
- visible_text_policy
- prompt_mode
- visualization_warning
- line-context-locked prompt

## Host identity rule
Host prompts must be identity-lock first:
1. approved reference image instruction
2. fixed host identity packet
3. current line scene delta
4. current line action delta
5. anti-drift blockers

Do not describe a new generic senior person for each host row.

## Output
- `07_image_prompt_table.csv`
