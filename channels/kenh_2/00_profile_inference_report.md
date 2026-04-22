# Profile Inference Report — kenh_2

## Channel Identity
- **Name:** ひとりでも安心 シニア暮らしノート
- **Niche:** Japanese senior safe living and daily safety
- **Audience:** 60+ (Japan)
- **Language:** ja-JP

## Normalized Inputs

Seed kenh_2 sử dụng format 9-field extended (tách `language` / `target_country`, tách `image_style` / `video_style`) thay vì template gốc 6-field (gộp `language_country`, gộp `video_style`). Tất cả fields đã normalize thành công.

| Seed Field | Raw Value | Normalized |
|------------|-----------|------------|
| `channel_name` | ひとりでも安心 シニア暮らしノート | Giữ nguyên |
| `channel_description` | (xem seed) | Tóm tắt: safe living, home safety, seasonal prep |
| `audience_age` | 60+ | `audience_age_band: "60+"` |
| `language` | ja-JP | `channel_language: "ja-JP"` |
| `target_country` | Japan | Giữ nguyên |
| `channel_niche` | Japanese senior safe living and daily safety | Drives editorial + publication bias |
| `image_style` | illustrated lifestyle handbook, retro-clean 2D, warm domestic scenes... | → Dùng trực tiếp từ seed: `illustrated_lifestyle_handbook` / `retro_clean_2d_domestic` |
| `video_style` | scenario-based checklist explainer, room walkthrough... | → motion governance + story structure |

## Direct Mappings

| Output Field | Source | Mapping |
|--------------|--------|---------|
| `channel_language` | seed `language` | Trực tiếp: `ja-JP` |
| `target_country` | seed `target_country` | Trực tiếp: `Japan` |
| `audience_age_band` | seed `audience_age` | Trực tiếp: `60+` |
| `non_dialogue_mode` | seed `video_style` contains "no lip sync, no direct-to-camera speech" | `true` |
| `lip_sync` | seed `video_style` | `false` |
| `veo_audio_mode` | system principle #16 | `silent` |
| `register_profile` | `01_register_core.md` + audience 60+ | `warm_polite_educational` |
| `addressing_profile` | `02_honorific_and_addressing.md` | `senior_respectful_neutral` |
| `region_profile_mode` | `00_language_strategy.md` — no specific region in seed | `national_neutral` |

## Visual Style Resolution

### Cách tiếp cận: Seed-Driven (không ép vào registry family)

Seed `image_style` mô tả:
> "illustrated lifestyle handbook, retro-clean 2D, warm domestic scenes, senior-friendly, practical Japanese home details, flat soft colors, object clarity, minimal clutter"

Thay vì ép vào 1 trong 4 family cố định trong `01_style_registry.md`, visual profile lấy **trực tiếp từ seed**:
- `visual_style_id`: `illustrated_lifestyle_handbook` — derived từ cụm từ đầu tiên trong seed
- `visual_substyle_id`: `retro_clean_2d_domestic` — derived từ "retro-clean 2D" + "warm domestic scenes"

Seed raw value được giữ nguyên trong `style_lock.seed_image_style_raw` để prompt builders downstream dùng nguyên văn khi cần.

### Style Lock

```
family_prompt_phrase: "illustrated lifestyle handbook"
substyle_prompt_phrase: "retro-clean 2D, warm domestic scenes, senior-friendly"
render_medium: "retro-clean 2D illustration"
line_treatment: "clean flat outlines, minimal detail, object clarity"
color_system: "flat soft colors, warm earth tones, low saturation, selective accent"
seed_image_style_raw: (giữ nguyên toàn bộ image_style từ seed)
```

## Defaults Chosen

| Default | Value | Reasoning |
|---------|-------|-----------|
| `host_presence_bias` | `low` | Channel thiên object-focus/room-walkthrough, host không phải yếu tố chính |
| `host_mode` | `host_optional` | Template default, seed không specify host requirement |
| `content_mode` | `educational_explanatory` | Template default, phù hợp safety explainer niche |
| `channel_strategy_mode` | `topic_first_research_driven` | Template default, phù hợp niche cần research |
| `default_longform_duration_min/max` | 8/12 phút | Template default |
| `default_shorts_derivatives` | 2 | Template default |
| `channel_visual_continuity_level` | `strict` | Template default, cần consistency across videos |
| `lexicon_priority` | `safety_domestic_senior` | Mới — specific cho niche "safe living" thay vì `health_senior` generic |

## Ambiguities

### 1. "room walkthrough feeling" — motion pattern chưa có sẵn trong template
- **Resolution:** Thêm `room_walkthrough` archetype vào `motion_governance.scene_archetype_motion_bias` với `slow_pan_across_room` và `gentle_dolly_into_corner`
- **Operator action:** Review motion patterns xem có cần thêm/chỉnh không

### 2. "before-after comparisons" — cần explicit scene archetype
- **Resolution:** Thêm `before_after_comparison` archetype với `comparison_parallax_hold` và `comparison_reveal_shift`
- **Operator action:** Kiểm tra xem prompt builders có hỗ trợ archetype mới này chưa

## What the Operator May Want to Refine

1. **Host presence:** Hiện tại `low` — nếu channel cần avatar/mascot, tăng lên `medium`
2. **Domain lexicon:** Hiện có 5 topic clusters — bổ sung thêm nếu channel mở rộng sang gardening/pet safety/neighbor interaction
3. **Motion archetypes mới:** `room_walkthrough`, `before_after_comparison`, `checklist_item` là custom cho kenh_2 — prompt builders cần nhận diện được
4. **Language profile:** Thêm `preferred_safety_framing_patterns` — đây là extension ngoài template, kiểm tra downstream pipeline có sử dụng field này không

## Artifact Checklist

| Artifact | Status | Path |
|----------|--------|------|
| `00_channel_config.json` | ✅ Emitted | `channels/kenh_2/00_channel_config.json` |
| `00_editorial_profile.json` | ✅ Emitted | `channels/kenh_2/00_editorial_profile.json` |
| `00_publication_profile.json` | ✅ Emitted | `channels/kenh_2/00_publication_profile.json` |
| `00_visual_profile.json` | ✅ Emitted | `channels/kenh_2/00_visual_profile.json` |
| `00_language_profile.json` | ✅ Emitted | `channels/kenh_2/00_language_profile.json` |
| `00_profile_inference_report.md` | ✅ This file | `channels/kenh_2/00_profile_inference_report.md` |

## Cross-Artifact Consistency Check

| Check | Result |
|-------|--------|
| `channel_config.visual_style_id` == `visual_profile.visual_style_id` | ✅ `illustrated_lifestyle_handbook` |
| `channel_config.visual_substyle_id` == `visual_profile.visual_substyle_id` | ✅ `retro_clean_2d_domestic` |
| `channel_config.language_profile_id` == `language_profile.language_profile_id` | ✅ `jp_senior_safe_living_neutral` |
| `channel_config.editorial_profile_id` == `editorial_profile.editorial_profile_id` | ✅ `jp_senior_safe_living_scenario_checklist` |
| `channel_config.publication_profile_id` == `publication_profile.publication_profile_id` | ✅ `jp_senior_safe_living_handbook_package` |
| `channel_config.non_dialogue_mode` == `visual_profile.non_dialogue_mode` | ✅ `true` |
| `channel_config.veo_audio_mode` == `visual_profile.motion_governance.veo_audio_policy` | ✅ `silent` |
| `visual_profile.locale_governance.target_country` == `channel_config.target_country` | ✅ `Japan` |
| Banned phrases consistent across language + editorial | ✅ No contradiction |
