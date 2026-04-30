# STEP 10 — Publication Package Builder

## Purpose
Generate the publication package after the script and final export are stable.

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
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/07A_retention_visual_plan.json
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/09_final_three_column.csv
- channels/{{TARGET_CHANNEL}}/videos/{{TARGET_VIDEO}}/09_export_qc_report.md
- real web access

Read `01_project_manifest.json`. Use `06_script_canonical.json` / `06_script_full.md` by default. If manifest sets `script_source_of_truth` to `06B_script_canonical.json`, use `06B_script_canonical.json` / `06B_script_full.md` consistently.

## Required outputs
- 10_publication_package.json
- 10_publication_package.md

## Retention packaging
- Title candidates must include CTR psychology angle and reasoning.
- Thumbnail candidates must choose an emotion level from the per-video spectrum.
- Selected package must align with the Step 07A viewer question, opening hook, and actual script payoff.
