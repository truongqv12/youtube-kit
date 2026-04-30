# Artifact Contracts

## Hard contracts
- external research required before script when topic requires it
- `full_script == "\n".join(canonical_script_units)`
- every `canonical_script_unit` must be TTS-safe spoken narration
- final export exact 3 columns
- downstream script source is `06_script_canonical.json` unless a video manifest explicitly sets `script_source_of_truth` to `06B_script_canonical.json`
- `script_text` rows == source-of-truth `canonical_script_units` in order
- final export columns are:
  - script_text
  - prompt_img_nano
  - prompt_video_veo3
- `07A_retention_visual_plan.json` is an intermediate sidecar for retention strategy; it must never add columns to final export
- retention metadata is forbidden in `09_final_three_column.csv`
- `prompt_img_nano` must stay semantically locked to each line, except bounded opening rows approved by `07A_retention_visual_plan.json`
- non-linear visual hook rows are allowed only for first 1-3 rows / first 10-15 seconds and must not rewrite script text
- `prompt_video_veo3` must stay motion-only for image-to-video
- visible text must follow `channel_language` and locale governance
- compiled prompts require mandatory file reads + preflight extraction