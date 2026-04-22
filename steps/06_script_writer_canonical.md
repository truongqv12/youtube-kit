# STEP 06 — Script Writer Canonical

## Purpose
Viết script cuối trực tiếp thành canonical script units.
Script phải:
- đúng duration
- TTS-safe
- tự nhiên hơn khi đọc thành lời
- hợp người xem 60+
- hợp tiếng Nhật nói lịch sự, ấm, rõ

## Target Context
User MUST supply `TARGET_CHANNEL` (e.g. kenh_2) and `TARGET_VIDEO` (e.g. vid_001). Stop and ask if not provided.

## Required reads
Read exactly these paths. DO NOT use global workspace search for abstract filenames to prevent cross-channel configuration contamination.
- core/system_principles.md
- core/duration_control_standard.md
- core/canonical_script_unit_standard.md
- core/policy_guardrails.md
- channels/{{TARGET_CHANNEL}}/00_channel_config.json
- channels/{{TARGET_CHANNEL}}/00_language_profile.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/01_intake_spec.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/02_topic_strategy.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/03_research_brief.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/04_policy_report.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/05_outline.json
- knowledge/japanese/*

## Required outputs
- 06_script_canonical.json
- 06_script_full.md
- 06_script_metrics.json

## Hard rules
- `full_script == "\n".join(canonical_script_units)`
- không headings / labels / bullets / numbering / production notes
- không mở rộng scope
- phải qua rhythm gate và breath-group gate
