# STEP 00 — Build All Profiles From Seed

## Purpose
Từ `00_channel_seed.json`, sinh toàn bộ state profile kiểu cũ mà pipeline downstream vẫn dùng:
- `00_channel_config.json`
- `00_editorial_profile.json`
- `00_publication_profile.json`
- `00_visual_profile.json`
- `00_language_profile.json`
- `00_profile_inference_report.md`

## Required inputs
- `00_channel_seed.json`
- `bootstrap/*.template.json`
- `knowledge/japanese/*`
- `knowledge/visual/*`

## Required outputs
- các file profile legacy
- `00_profile_inference_report.md`

## Key rules
- seed 6 trường là input tay duy nhất của kênh
- mọi profile còn lại là derived state
- phải giữ backward compatibility cho các step sau
