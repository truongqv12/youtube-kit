# STEP 05 — Outline Builder

## Purpose
Create a sufficiently dense outline to support writing a script that meets the target duration for a single micro-topic.

## Target Context
User MUST supply `TARGET_CHANNEL` (e.g. kenh_2) and `TARGET_VIDEO` (e.g. vid_001). Stop and ask if not provided.

## Required reads
Read exactly these paths. DO NOT use global workspace search for abstract filenames to prevent cross-channel configuration contamination.
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/01_intake_spec.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/02_topic_strategy.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/03_research_brief.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/04_policy_report.json
- core/hook_engineering_standard.md
- core/pacing_control_standard.md

## Required outputs
- 05_outline.json

## Retention fields
- `hook_type`
- `viewer_question`
- `hook_quality_reasoning`
- `promise_payoff`
- `tension_level`
- `section_entry_hook`
