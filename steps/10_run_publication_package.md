# STEP 10 — Publication Package Builder

## Purpose
Sinh package để public video sau khi script và final export đã ổn định.

## Target Context
User MUST supply `TARGET_CHANNEL` (e.g. kenh_2) and `TARGET_VIDEO` (e.g. vid_001). Stop and ask if not provided.

## Required reads
Read exactly these paths. DO NOT use global workspace search for abstract filenames to prevent cross-channel configuration contamination.
- channels/{{TARGET_CHANNEL}}/00_channel_config.json
- channels/{{TARGET_CHANNEL}}/00_language_profile.json
- channels/{{TARGET_CHANNEL}}/00_visual_profile.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/01_intake_spec.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/02_topic_strategy.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/03_research_brief.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/04_policy_report.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/06_script_full.md
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/06_script_canonical.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/09_final_three_column.csv
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/09_export_qc_report.md
- web access thật

## Required outputs
- 10_publication_package.json
- 10_publication_package.md
