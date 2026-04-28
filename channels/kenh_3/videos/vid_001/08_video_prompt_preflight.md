=== PREFLIGHT START ===

## 1. files_read
- core/system_principles.md ✅
- core/policy_guardrails.md ✅
- core/prompt_description_grammar.md ✅
- knowledge/visual/00_visual_strategy.md ✅
- knowledge/visual/05_negative_visual_rules.md ✅
- channels/kenh_3/00_channel_config.json ✅
- channels/kenh_3/videos/vid_001/01_intake_spec.json ✅
- channels/kenh_3/videos/vid_001/06_script_canonical.json ✅
- channels/kenh_3/videos/vid_001/07_image_prompt_table.csv ✅

## 2. optional_files_read
- channels/kenh_3/00_visual_profile.json ✅

## 3. rules_extracted_by_file

### system_principles.md
- **narration-support pipeline**: Veo 3 motions must be purely atmospheric and micro-motion.
- **one canonical unit = one keyframe**: 1:1 mapping must be maintained across all asset generation.
- **image prompt is semantically locked**: Veo builds purely motion extensions, no new visual content.

### policy_guardrails.md
- **avoid medical misinformation**: Metaphors must be calm, slow-moving, non-dramatic.
- **prefer calm caution over fear theater**: No sudden transitions or alarming visual distortion mapping to symptoms.

### prompt_description_grammar.md
- **scene archetypes restrict motion**: different archetypes dictate the kind of specific micro-action or camera mapping.

### 00_visual_strategy.md
- **reference-first**: Subject appearance is already locked; Veo must not mutate the age, preserving the identity carefully.

### 05_negative_visual_rules.md
- **no mouth-open acting**: Prohibit speech poses or lip-sync for all characters.
- **no dramatic action**: Prohibit falling, collapsing, or panic. 

### 00_channel_config.json
- `non_dialogue_mode`: `true` -> strictly enforces no audio and no on-screen dialogue.
- `veo_audio_mode`: `silent` 

### 01_intake_spec.json
- **story_character**: Haruko must not exhibit erratic movement; motions must be slow, reflecting age safely.

### 06_script_canonical.json
- **127 units count**: Must be preserved exactly constraint.

### 07_image_prompt_table.csv
- **seed data**: Provides archetypes to drive the targeted motion strategies (e.g. `host_anchor`, `everyday_example`, `process_metaphor`). 

## 4. i2v_mode_detected
`first_frame_only`

## 5. non_dialogue_mode_detected
`true` - Strict enforcement of `(Silent video, no audio).` and specific negative constraints against speech/vocalization.

## 6. voiceover_mode_detected
`narration_only`

## 7. audio_prompt_mode_detected
`silent`

## 8. visible_text_preservation_detected
`none` (All source prompts are locked to `no_readable_text`)

## 9. scene_motion_bias_detected
`subtle_micro_motion` (Calm gentle movements matching the kamishibai paper theater style, such as slow push-ins, subtle parallax, and gentle environmental shifts)

## 10. allowed_to_proceed
✅ YES — all constraints resolved, required files read, negative policies correctly injected to combat `PUBLIC_ERROR_AUDIO_FILTERED`.

=== PREFLIGHT END ===

=== ARTIFACT: 08_video_prompt_table.csv ===
File: channels/kenh_3/videos/vid_001/08_video_prompt_table.csv
Row count: 127 data rows (128 total lines with header), matching exactly the canonical_script_units 1:1.
Columns: unit_index, i2v_mode, motion_strategy, recommended_duration_sec, prompt_video_veo3
=== END ARTIFACT ===
