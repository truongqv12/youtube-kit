# Artifact Contracts

## Hard contracts
- external research required before script when topic requires it
- `full_script == "\n".join(canonical_script_units)`
- every `canonical_script_unit` must be TTS-safe spoken narration
- final export exact 3 columns
- `script_text` rows == `canonical_script_units` in order
- final export columns are:
  - script_text
  - prompt_img_nano
  - prompt_video_veo3
- `prompt_img_nano` must stay semantically locked to each line
- `prompt_video_veo3` must stay motion-only for image-to-video
- visible text must follow `channel_language` and locale governance
- compiled prompts require mandatory file reads + preflight extraction