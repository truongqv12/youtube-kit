# Output Conventions

## Response envelope
Use this response envelope in every compiled prompt:
- `=== PREFLIGHT START ===`
- `=== PREFLIGHT END ===`
- `=== ARTIFACT: filename.ext ===`
- `=== END ARTIFACT ===`

## Final export
Exactly 3 columns:
- `script_text`
- `prompt_img_nano`
- `prompt_video_veo3`

## Hard rules
- `script_text` must come directly from `canonical_script_units`.
- `script_text` must remain a TTS-safe spoken line with no formatting cleanup required.
- `prompt_img_nano` is the still-image keyframe prompt.
- `prompt_img_nano` must stay semantically locked to the current line.
- `prompt_video_veo3` is the image-to-video motion prompt.
- `prompt_video_veo3` must stay motion-only and must not re-describe the full image.
- If visible text is needed inside the image, it must be exact, short, and correct for `channel_language`.
- If `non_dialogue_mode=true` or `voiceover_mode=narration_only`, `prompt_video_veo3` must forbid spoken dialogue, lip sync, and direct-to-camera speech.
- The final exporter must preserve row order.
- Step 09 must also emit `09_export_qc_report.md`.

## Forbidden in final export
- id
- source
- duration
- notes
- scene
- policy flag
- scene_archetype
- visible_text_policy
- visible_text_exact
- motion_strategy
- line_context_frame
