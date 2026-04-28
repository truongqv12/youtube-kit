# Profile Inference Report — kenh_3

## Channel Identity
- **Name:** シニア健康かみしばい
- **Niche:** Japanese senior health storytelling in kamishibai format
- **Audience:** 60+ (Japan)
- **Language:** ja-JP

## Normalized Inputs

Seed kenh_3 sử dụng format 9-field extended (tách `language` / `target_country`, tách `image_style` / `video_style`). Tất cả fields đã normalize thành công.

| Seed Field | Raw Value | Normalized |
|------------|-----------|------------|
| `channel_name` | シニア健康かみしばい | Giữ nguyên |
| `channel_description` | (xem seed) | Tóm tắt: kamishibai storytelling, daily senior health topics (食事, 転倒, 水分不足, 疲れ, 足腰) |
| `audience_age` | 60+ | `audience_age_band: "60+"` |
| `language` | ja-JP | `channel_language: "ja-JP"` |
| `target_country` | Japan | Giữ nguyên |
| `channel_niche` | Japanese senior health storytelling in kamishibai format | Drives editorial + publication bias |
| `image_style` | kamishibai paper theater, hand-painted gouache and watercolor... | → Seed-driven: `kamishibai_paper_theater` / `gouache_watercolor_gentle` |
| `video_style` | story-first paper theater, slow page-turn rhythm... | → motion governance + story structure |

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

### Cách tiếp cận: Seed-Driven (không khớp registry family nào)

Seed `image_style` mô tả:
> "kamishibai paper theater, hand-painted gouache and watercolor, warm paper texture, Japanese educational storytelling, muted colors, simple framed scenes, gentle expressions"

Không khớp với 4 registry families (`manga_editorial_clean`, `anime_editorial`, `ghibli_inspired_pastoral`, `watercolor_documentary`). Lý do:
- **watercolor_documentary** gần nhất nhưng thiếu kamishibai framing, paper theater staging, gouache medium
- Seed mô tả rất cụ thể — dùng seed-driven approach

Visual profile lấy **trực tiếp từ seed**:
- `visual_style_id`: `kamishibai_paper_theater` — derived từ cụm "kamishibai paper theater"
- `visual_substyle_id`: `gouache_watercolor_gentle` — derived từ "hand-painted gouache and watercolor" + "gentle expressions"

Seed raw value giữ nguyên trong `style_lock.seed_image_style_raw`.

### Style Lock

```
family_prompt_phrase: "kamishibai paper theater illustration"
substyle_prompt_phrase: "hand-painted gouache and watercolor, warm paper texture, gentle expressions"
render_medium: "hand-painted gouache and watercolor on textured paper"
line_treatment: "soft pencil contour with painterly gouache edges, visible brushwork, no hard digital lines"
color_system: "muted warm colors, earth tones, soft ochre, gentle greens, faded indigo, warm cream paper base"
texture_behavior: "visible paper grain, subtle gouache texture, hand-painted imperfections"
composition_bias: "simple framed scenes, kamishibai stage-like border, one clear focal point per card"
emotion_ceiling: "gentle, warm, reassuring, quietly observant"
style_drift_to_avoid: "digital anime rendering, glossy CG, photorealism, action manga, moe aesthetics"
seed_image_style_raw: (giữ nguyên toàn bộ image_style từ seed)
```

## Motion Governance — Video Style Resolution

Seed `video_style` mô tả:
> "story-first paper theater, slow page-turn rhythm, stage-like parallax, one scene one beat, calm narration, no lip sync, no direct-to-camera speech"

Derived motion archetypes mới cho kamishibai format:
- `kamishibai_page_turn`: `slow_page_slide_reveal`, `gentle_card_pull_transition`
- `stage_parallax`: `stage_like_parallax_drift`, `foreground_background_layer_shift`
- `story_beat`: `scene_hold_with_subtle_drift`, `gentle_zoom_to_detail`

Giữ lại các archetypes standard: `host_anchor`, `everyday_example`, `object_focus`, `environment_bridge`.

## Defaults Chosen

| Default | Value | Reasoning |
|---------|-------|-----------|
| `host_presence_bias` | `low` | Kamishibai thiên về scene/story illustration, không cần host prominent |
| `host_mode` | `host_optional` | Template default, seed không specify host requirement |
| `content_mode` | `educational_storytelling` | Khác template default — seed niche là "storytelling" thay vì pure "explanatory" |
| `channel_strategy_mode` | `topic_first_research_driven` | Template default, phù hợp health niche cần evidence |
| `default_longform_duration_min/max` | 8/12 phút | Template default |
| `default_shorts_derivatives` | 2 | Template default |
| `channel_visual_continuity_level` | `strict` | Template default, cần consistency across videos |
| `lexicon_priority` | `health_storytelling_senior` | Mới — specific cho niche "health storytelling" thay vì `health_senior` generic |
| `fear_intensity_ceiling` | `low` | Kamishibai format inherently gentle, lower than template's `low_to_moderate` |

## Editorial Differentiation từ kenh_2

| Aspect | kenh_2 | kenh_3 |
|--------|--------|--------|
| Format | Scenario checklist, room walkthrough | Kamishibai story arc |
| Story bias | `scenario_checklist_then_safety_review` | `kamishibai_story_arc_then_reflection` |
| Host trust role | `gentle_companion_narrator` | `gentle_kamishibai_narrator` |
| Niche focus | Safe living, domestic safety | Health wellness, daily habits |
| Visual style | Illustrated lifestyle handbook, retro-clean 2D | Kamishibai paper theater, gouache/watercolor |
| Motion feel | Room walkthrough, object close-ups | Page-turn rhythm, stage parallax |
| Publication title | Warning framing allowed | Warning framing disabled (storytelling tone) |

## Ambiguities

### 1. `content_mode` — "educational_storytelling" vs "educational_explanatory"
- **Resolution:** Changed from template default `educational_explanatory` to `educational_storytelling` — seed niche explicitly says "storytelling" and "kamishibai format" which is narrative-driven
- **Operator action:** Nếu downstream steps dùng `content_mode` để switch logic, kiểm tra có hỗ trợ `educational_storytelling` enum value không

### 2. Kamishibai motion archetypes — mới, chưa có trong template
- **Resolution:** Thêm `kamishibai_page_turn`, `stage_parallax`, `story_beat` archetypes
- **Operator action:** Kiểm tra prompt builders có nhận diện các archetypes mới này không

### 3. `publication_profile.title_bias.allow_warning_framing` — set `false`
- **Resolution:** Kamishibai storytelling tone không phù hợp warning-style titles, khác kenh_2 và template
- **Operator action:** Nếu muốn occasional warning titles, set lại `true`

## What the Operator May Want to Refine

1. **Content mode enum:** `educational_storytelling` là custom value — nếu pipeline code dùng enum validation, thêm vào allowed list
2. **Host character design:** Kamishibai có thể dùng 1 recurring character (ông/bà kể chuyện) — xác định host reference nếu muốn
3. **Domain lexicon:** Hiện có 5 topic clusters — bổ sung thêm khi channel mở rộng sang oral care, breathing, mental wellness
4. **Kamishibai border/frame:** Visual profile mô tả "stage-like border" — prompt builders cần include frame instruction cho mỗi keyframe
5. **Paper texture intensity:** Gouache render có thể quá textured — điều chỉnh nếu AI image gen không capture well
6. **Warning framing disabled:** Nếu một số video cần soft warning title, override per-video

## Artifact Checklist

| Artifact | Status | Path |
|----------|--------|------|
| `00_channel_config.json` | ✅ Emitted | `channels/kenh_3/00_channel_config.json` |
| `00_editorial_profile.json` | ✅ Emitted | `channels/kenh_3/00_editorial_profile.json` |
| `00_publication_profile.json` | ✅ Emitted | `channels/kenh_3/00_publication_profile.json` |
| `00_visual_profile.json` | ✅ Emitted | `channels/kenh_3/00_visual_profile.json` |
| `00_language_profile.json` | ✅ Emitted | `channels/kenh_3/00_language_profile.json` |
| `00_profile_inference_report.md` | ✅ This file | `channels/kenh_3/00_profile_inference_report.md` |

## Cross-Artifact Consistency Check

| Check | Result |
|-------|--------|
| `channel_config.visual_style_id` == `visual_profile.visual_style_id` | ✅ `kamishibai_paper_theater` |
| `channel_config.visual_substyle_id` == `visual_profile.visual_substyle_id` | ✅ `gouache_watercolor_gentle` |
| `channel_config.language_profile_id` == `language_profile.language_profile_id` | ✅ `jp_senior_health_kamishibai_neutral` |
| `channel_config.editorial_profile_id` == `editorial_profile.editorial_profile_id` | ✅ `jp_senior_health_kamishibai_story` |
| `channel_config.publication_profile_id` == `publication_profile.publication_profile_id` | ✅ `jp_senior_health_kamishibai_package` |
| `channel_config.non_dialogue_mode` == `visual_profile.non_dialogue_mode` | ✅ `true` |
| `channel_config.veo_audio_mode` == `visual_profile.motion_governance.veo_audio_policy` | ✅ `silent` |
| `visual_profile.locale_governance.target_country` == `channel_config.target_country` | ✅ `Japan` |
| Banned phrases consistent across language + editorial | ✅ No contradiction |
