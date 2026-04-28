=== PREFLIGHT START ===

## 1. files_read
- core/system_principles.md ✅
- core/policy_guardrails.md ✅
- core/prompt_description_grammar.md ✅
- core/output_conventions.md ✅
- knowledge/visual/00_visual_strategy.md ✅
- knowledge/visual/01_style_registry.md ✅
- knowledge/visual/05_negative_visual_rules.md ✅
- channels/kenh_3/00_channel_config.json ✅
- channels/kenh_3/videos/vid_001/01_intake_spec.json ✅
- channels/kenh_3/videos/vid_001/06_script_canonical.json ✅

## 2. optional_files_read
- channels/kenh_3/00_language_profile.json ✅
- channels/kenh_3/00_visual_profile.json ✅

## 3. rules_extracted_by_file

### system_principles.md
- narration-support pipeline, not film storyboard
- one canonical unit = one keyframe
- image prompt is semantically locked keyframe; Veo is motion-only
- visible text must follow channel_language & locale governance
- non_dialogue_mode=true → no on-screen spoken dialogue
- veo_audio_mode=silent → "(Silent video, no audio)."
- prompt builders must resolve line context before writing

### policy_guardrails.md
- avoid medical misinformation / cure framing
- prefer calm caution over fear theater
- include soft consult-clinician framing when symptoms mentioned
- no misleading visuals as proof

### prompt_description_grammar.md
- line_context_frame required before each prompt
- scene archetypes: host_anchor, everyday_example, object_focus, process_metaphor, comparison_pair, environment_bridge
- continuity: 2–4 anchors across adjacent related rows
- style taxonomy: must resolve to concrete lock (not vague labels)
- demographic_lock: 60+ characters must show visible aging (2+ concrete cues)
- manga/illustration style → OVER-describe age features

### 00_visual_strategy.md
- reference-first when host imagery is used
- locale fidelity mandatory
- readable text avoided by default
- style must resolve to concrete lock (seed-driven OK)

### 01_style_registry.md
- kenh_3 uses seed-driven lock: kamishibai_paper_theater / gouache_watercolor_gentle
- NOT a pre-defined registry family → custom style lock derived from seed
- seed_image_style_raw preserved in style_lock

### 05_negative_visual_rules.md
- no vague style labels
- no random English signage
- no locale drift
- no photorealistic host when illustrated
- no lip sync / speech pose / mouth-open by default
- no youth drift: must show wrinkles, gray hair, mature posture
- no smooth-skin bias for senior characters

### 00_channel_config.json
- host_mode: host_optional
- host_reference_mode: reference_first
- host_presence_bias: low
- non_dialogue_mode: true
- visual_style_id: kamishibai_paper_theater
- visual_substyle_id: gouache_watercolor_gentle
- veo_audio_mode: silent

### 01_intake_spec.json
- story_character: はるこさん (composite, 68歳)
- style_lock fully specified (seed-driven)
- demographic_anchors: 65-75, HIGH priority
- gouache_age_compensation: must include 2-3 aging cues per human
- locale: Japan, national_neutral
- visible_text: avoid by default, ja-JP only when needed

### 06_script_canonical.json
- 128 canonical_script_units (index 0–127)
- story arc: opening → Haruko intro → morning incident → viewer connection → symptom detail → hesitation → normalization → explanation → blood pressure → hydration → balance → reassurance → practical tips → water habit → evening habits → outcome → medical advisory → closing → farewell

### 00_visual_profile.json
- confirms style_lock, reference_anchor_policy, no_host_strategy, continuity_governance, locale_governance, visible_text_governance, motion_governance

### 00_language_profile.json
- register: warm_polite_educational
- addressing: senior_respectful_neutral
- national_neutral mode

## 4. channel_language_detected
ja-JP

## 5. host_mode_detected
host_optional (host_presence_bias: low, host_reference_mode: reference_first)

## 6. reference_mode_detected
reference_first

## 7. style_taxonomy_detected
- visual_style_id: kamishibai_paper_theater (seed-driven, not registry-based)
- visual_substyle_id: gouache_watercolor_gentle
- style_lock: fully resolved
  - family_prompt_phrase: "kamishibai paper theater illustration"
  - substyle_prompt_phrase: "hand-painted gouache and watercolor, warm paper texture, gentle expressions"
  - render_medium: "hand-painted gouache and watercolor on textured paper"
  - line_treatment: "soft pencil contour with painterly gouache edges, visible brushwork, no hard digital lines"
  - color_system: "muted warm colors, earth tones, soft ochre, gentle greens, faded indigo, warm cream paper base"
  - texture_behavior: "visible paper grain, subtle gouache texture, hand-painted imperfections"
  - composition_bias: "simple framed scenes, kamishibai stage-like border, one clear focal point per card, breathing space"
  - emotion_ceiling: "gentle, warm, reassuring, quietly observant"

## 8. locale_governance_detected
- target_country: Japan
- region_mode: national_neutral
- allowed locations: ordinary Japanese apartments, kitchen, parks, pharmacies, sidewalks, garden, veranda
- wardrobe: ordinary Japanese senior casualwear
- signage: Japanese only unless authentic brand requires roman letters
- forbidden: US/European/Chinese/Korean cross-locale drift

## 9. visible_text_policy_detected
- default: avoid_readable_text
- channel_language: ja-JP
- max_words: 6
- must_append: "no other readable text"

## 10. continuity_policy_detected
- scene_group_continuity: true
- carry_forward_anchors: host_identity, location_family, primary_prop_family, wardrobe_family, time_of_day_family, kamishibai_frame_style
- anchor_count_per_row: 2–4
- variation_rule: change line-specific semantic action/object, keep continuity anchors

## 11. allowed_to_proceed
✅ YES — all required files read, all rules extracted, no failures.

=== PREFLIGHT END ===

=== ARTIFACT: 07_image_prompt_table.csv ===
File: channels/kenh_3/videos/vid_001/07_image_prompt_table.csv
Row count: 127 (header + 127 data rows, indices 0–126 ↔ canonical_script_units)
Columns: unit_index, scene_group_id, scene_archetype, host_usage, visible_text_policy, visible_text_exact, prompt_mode, prompt_img_nano
=== END ARTIFACT ===
