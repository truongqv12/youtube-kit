# STEP 06 — Script Writer Canonical

## Purpose
Write the final script directly as canonical script units.
The script must:
- meet the target duration
- be TTS-safe
- sound more natural when read aloud
- produce clear visual beats for downstream image/video generation
- be appropriate for viewers aged 60+
- use polite, warm, clear spoken Japanese

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
- no headings / labels / bullets / numbering / production notes
- do not expand scope beyond the locked micro-topic
- must pass rhythm gate and breath-group gate
- must pass visual-beat gate: each line should be easy to support with one image keyframe or one motion beat
