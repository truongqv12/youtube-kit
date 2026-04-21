# STEP 06 — Script Writer Canonical

## Purpose
Viết script cuối trực tiếp thành canonical script units.
Script phải:
- đúng duration
- TTS-safe
- tự nhiên hơn khi đọc thành lời
- hợp người xem 60+
- hợp tiếng Nhật nói lịch sự, ấm, rõ

## Required inputs
- core/system_principles.md
- core/duration_control_standard.md
- core/canonical_script_unit_standard.md
- core/policy_guardrails.md
- 00_channel_config.json
- 00_language_profile.json
- 01_intake_spec.json
- 02_topic_strategy.json
- 03_research_brief.json
- 04_policy_report.json
- 05_outline.json
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
