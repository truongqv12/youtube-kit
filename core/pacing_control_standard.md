# Pacing Control Standard

## Purpose

Prevent retention drop from long abstract explanation blocks while keeping senior-friendly calm pacing.

## Narrative pacing rules

- First 10-15 seconds must establish viewer relevance.
- After the opening hook, deliver a clear payoff signal by lines 4-6.
- Prefer daily-life anchors before medical or mechanism explanation.
- Change narrative function every 5-7 seconds where practical: concern, example, explanation, check, adjustment, reassurance.
- Avoid more than 3 consecutive data/stat/mechanism lines without a daily-life example.
- Avoid passive section entries such as `次は〜です` when a viewer-facing question or scene turn would work better.

## Visual pacing rules

- Opening rows may use stronger attention targets when approved by `07A_retention_visual_plan.json`.
- Normal rows should stay line-context locked and avoid generic illustrations.
- Avoid repeated static host or object shots for more than 2 rows unless the script needs calm continuity.
- Motion should vary by row role: reveal, inspect, compare, demonstrate, reassure.

## Warning vs failure

Hard fail:

- generic first-line intro.
- no concrete opening viewer relevance.
- opening concern contradicts policy or research.

Warning:

- long mechanism block.
- repeated transition phrasing.
- repeated visual/motion strategy.
- weak payoff after the hook.

## Metrics to report

- `opening_hook_passed`.
- `promise_payoff_rows`.
- `cold_zone_warnings`.
- `repeated_transition_warnings`.
- `visual_pacing_notes` when applicable.
