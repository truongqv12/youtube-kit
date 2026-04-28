=== PREFLIGHT START ===

## 1. files_read
- core/system_principles.md ✅
- core/policy_guardrails.md ✅
- core/prompt_description_grammar.md ✅
- core/output_conventions.md ✅
- knowledge/visual/00_visual_strategy.md ✅
- knowledge/visual/05_negative_visual_rules.md ✅
- channels/kenh_3/00_channel_config.json ✅
- channels/kenh_3/00_visual_profile.json ✅
- channels/kenh_3/videos/vid_002/01_intake_spec.json ✅
- channels/kenh_3/videos/vid_002/06_script_canonical.json ✅

## 2. rules_extracted
- One canonical unit maps to one still keyframe.
- `prompt_img_nano` is semantically locked to the current narration line.
- Style lock: kamishibai paper theater, hand-painted gouache and watercolor, warm paper texture.
- Non-dialogue mode: no speech bubbles, no lip-sync pose, no mouth-open acting.
- Health topic: no dramatic fall, no panic, no diagnostic proof imagery.
- Visible text avoided by default.

## 3. channel_language_detected
ja-JP

## 4. style_taxonomy_detected
- visual_style_id: kamishibai_paper_theater
- visual_substyle_id: gouache_watercolor_gentle / storytelling alias

## 5. allowed_to_proceed
✅ YES

=== PREFLIGHT END ===

=== ARTIFACT: 07_image_prompt_table.csv ===
File: channels/kenh_3/videos/vid_002/07_image_prompt_table.csv
Row count: 132 data rows, matching canonical_script_units 1:1.
Columns: unit_index, scene_group_id, scene_archetype, host_usage, visible_text_policy, prompt_mode, line_context_frame, prompt_img_nano
=== END ARTIFACT ===
