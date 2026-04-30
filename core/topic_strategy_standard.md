# Topic Strategy Standard

## Purpose
Turn a rough topic idea into a clear, scriptable, researchable video thesis before web research starts.

## Core rules
- One video = one micro-topic only.
- Do not start from a competitor video.
- Do not import structure from a competitor as the default outline.
- Define the target viewer problem in plain language.
- Define a safe working promise that stays inside educational framing.
- Define what the video is **not** claiming.
- Define 3 to 7 research questions that can be answered by official or primary sources.
- Prefer daily-life usefulness over disease-name shock.
- Include hook and packaging seeds that follow `core/hook_engineering_standard.md` and stay inside the safe claim boundary.
- Choose a likely hook type from: `relatable_danger`, `surprising_fact`, `self_check_question`, `everyday_mistake_reveal`.
- Define the viewer question that title, thumbnail, and opening visual should answer.
- For this channel phase, default to wellness / routines / mobility / balance / hydration / breakfast / fatigue topics.

## Good micro-topic examples
- `65歳から朝いちばんに見直したい立ち上がり方`
- `夜中のトイレがつらい方が夕方に見直したい水分のとり方`

## Bad micro-topic examples
- `高齢者の健康を守る方法`
- `血圧と食事と運動と睡眠を全部見直す`

## Required output objects
A valid `02_topic_strategy.json` should include at least:
- project_id
- topic_cluster
- topic_angle
- target_viewer
- viewer_problem
- working_promise
- safe_claim_boundary
- forbidden_claims
- research_questions
- planned_sections
- packaging_seeds_longform
- packaging_seeds_shorts
- hook_type_seed
- viewer_question
- opening_visual_seed
- thumbnail_emotion_hint
- notes_for_research

## Failure conditions
Fail the step if:
- the angle is still too broad for one video
- the promise depends on a disease cure / prevention certainty
- the research questions are vague or not evidence-seeking
- the topic is copied from a competitor structure rather than reframed for this channel
