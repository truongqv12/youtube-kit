# Prompt Description Grammar — Podcast / Narration / Explainer

## Goal
Turn each canonical script unit into:
1. one line-locked still-image keyframe prompt for Nano Banana
2. one motion-only image-to-video prompt for Veo 3

This is NOT a film storyboard system.
This is a narration-support visual system for podcast, voiceover, explanation, and educational content.

## Core mode assumptions
- TTS carries the spoken words.
- Visuals support the exact meaning of the current line.
- One canonical unit = one keyframe = one motion beat.
- Educational clarity is more important than cinematic drama.
- Default mode is non-dialogue visuals.
- A prompt builder must first resolve a `line_context_frame` before writing a final prompt.

## Line context frame
Before writing a final prompt, resolve each line into:
- semantic target
- visualizable core
- scene function
- subject lock
- state or action
- context lock
- continuity anchors
- visible text need
- risk guardrails
- demographic_lock: resolve the character's visible age to match channel audience (60+), include at least 2 concrete aging visual cues

A prompt fails if it jumps directly from topic to image without resolving the line's meaning.

## Canonical script unit quality gate
A canonical script unit must be readable aloud as-is.
Hard rules:
- plain spoken narration only
- one natural spoken thought, or two tightly linked clauses
- no headings, section labels, bullets, numbering, markdown, or decorative markers
- no speaker tags
- no bracketed notes or parenthetical production notes
- no camera, edit, or SFX instructions
- no title-card fragments or outline language
- no CTA inserted unless it is natural spoken narration in that exact moment

## Scene archetypes
Choose exactly one per canonical unit.

### 1. host_anchor
Use when trust, warmth, continuity, reassurance, opening, or summary matters.
Default framing: medium shot.
The host should appear present and reassuring, not actively speaking to camera unless the channel explicitly wants that.

### 2. everyday_example
Use when the line describes a daily habit, symptom, action, or common situation.
Default framing: medium shot or full shot.
Show one ordinary person doing one clear action tied to the line.

### 3. object_focus
Use when the line is mainly about an item, label, bottle, medicine box, phone screen, body-area demonstration, document, tool, or household object.
Default framing: close-up or medium close-up.

### 4. process_metaphor
Use when the line explains an invisible process, body mechanism, cause-effect logic, or abstract concept.
Default framing: clean symbolic scene or diagram-like metaphor with low clutter.
Avoid infographic overload.

### 5. comparison_pair
Use when the line contrasts good or bad, before or after, correct or incorrect, more or less.
Default framing: split composition or side-by-side comparison inside one image.

### 6. environment_bridge
Use for calmer transitions, breathing space, place context, time-of-day shifts, or emotional resets between denser lines.
Default framing: wide or medium-wide.

## Continuity system
Adjacent rows that belong to the same scene group must carry forward 2 to 4 anchors, for example:
- same host identity or reference
- same location family
- same primary prop family
- same wardrobe family
- same time-of-day or lighting family

Continuity should stabilize the video without turning rows into clones.
Carry the anchors forward, but change the line-specific semantic action, object, emphasis, or comparison.
Do not repeat the same framing-plus-action template more than twice in an 8-row window unless the script truly repeats.

## Style taxonomy resolution
Never use vague labels such as `manga-style`, `anime-style`, or `watercolor-style` alone.
Resolve both `visual_style_id` and `visual_substyle_id` into a concrete style lock that includes:
- family prompt phrase
- substyle prompt phrase
- render medium
- line treatment
- color system
- texture or screentone behavior
- composition bias
- emotion ceiling

## Locale and visible text governance
- scenery, signage, props, packaging, wardrobe, architecture, and public-space cues must fit the target country or region
- visible text should be avoided by default
- if visible text is required, decide the exact string first
- visible text must stay short, be exact, and use only the channel language unless the exact object authentically requires another script
- if visible text is required, explicitly add `no other readable text`
- do not mix random English into non-English channels

## Image prompt grammar for Nano Banana
Build each `prompt_img_nano` in this order:
1. task mode:
   - `Generate ...`
   - or `Using the provided reference image(s) ...`
2. output format + resolved style lock
3. line-context semantic subject
4. visible state or action
5. locale-correct setting, props, and wardrobe
6. continuity anchors
7. preservation / edit rule
8. visible text instruction if needed
9. exclusions and anti-drift anchors

### Image prompt rules
- one image = one main idea
- one main subject only unless `comparison_pair` is chosen
- the line meaning should be inferable from the image prompt
- no multi-event chains
- no exaggerated movie language
- prefer clear composition over decorative detail
- if `host_reference_mode` is `reference_first`, keep host description light and rely on the uploaded reference first
- if host is not needed, do not force the host into the scene
- if editing from a source image, explicitly state what to preserve and what may change
- if readable text is needed, specify the exact text and add `no other readable text`
- if the character is a senior (60+), EXPLICITLY describe aging features: gray/silver hair, wrinkles, age-appropriate posture, weathered hands — do not rely on the word "older" alone
- manga/illustration style naturally reduces aging cues, so OVER-describe age features to compensate

## Veo 3 image-to-video grammar
The source image already provides subject, setting, lighting, style, and visible text.
The Veo prompt should only add motion and preservation rules.

Build each `prompt_video_veo3` in this order:
1. camera motion
2. subject micro-motion
3. environmental micro-motion
4. mood preservation
5. visible text preservation if applicable
6. silent audio directive: `(Silent video, no audio).`
7. negative motion, performance, and audio constraints

### Motion prompt rules
- one clip = one focused motion beat
- do not re-describe the full image
- use general subject terms such as `the subject`, `the woman`, `the man`, `they`, `the hand`, `the object`
- motion must vary by `scene_archetype` and line meaning
- preserve existing visible text exactly as-is when present
- do not ask Veo to create new readable text
- do not imply identity change, outfit change, or scene redesign
- if a line needs stronger transformation, prefer first-and-last-frame mode rather than overloading a single first-frame prompt

### Motion biases by scene archetype
- `host_anchor`: gentle push, slight lateral drift, blink, breath, small head turn
- `everyday_example`: observational follow, weight shift, hand adjustment, garment movement
- `object_focus`: inspection push, hand interaction, page tilt, steam drift, label preservation
- `process_metaphor`: layered parallax, signal pulse, symbolic drift, restrained particle motion
- `comparison_pair`: controlled parallax across the comparison, emphasis shift without changing the composition
- `environment_bridge`: breathing pan or tilt, leaves, curtains, rain, dust, distant movement

## Non-dialogue audio policy
If `non_dialogue_mode=true` or `voiceover_mode=narration_only`:
- no spoken dialogue
- no on-screen narration voice
- no lip sync
- no direct-to-camera speech
- no singing, chanting, or vocal performance
- audio directive must be `(Silent video, no audio).` — do NOT request ambience, foley, or room tone
- audio is handled entirely by external TTS; Veo must not generate any audio content
- this policy reduces `PUBLIC_ERROR_AUDIO_FILTERED` from Veo 3.1 safety system

## Negative defaults
- no mouth-open speaking pose unless explicitly required
- no subtitles baked into the image
- no random English signage for non-English channels
- no doctor costume unless truly needed
- no fake scientific proof imagery
- no overdramatic film acting
- no busy clutter that weakens explanatory clarity
- no repeated stock-template framing across adjacent rows

## Example
Script line:
`朝食前に速く歩きすぎると、ふらつきを感じることがあります。`

Possible line context frame:
- semantic target: moving too fast before breakfast can feel unsteady
- visualizable core: older Japanese woman slows down and lightly steadies herself
- scene function: everyday_example
- subject lock: same older Japanese woman, same walking outfit
- context lock: ordinary Japanese neighborhood park path, early morning
- visible text need: none

Possible Nano Banana prompt:
Using the provided reference image(s) when available, generate a clean editorial manga illustration in a seinen soft educational style. The same older Japanese woman slows during an early-morning neighborhood walk before breakfast and lightly steadies one hand on a park bench rail, calm but slightly lightheaded expression. Ordinary Japanese residential park path, practical senior walking clothes and shoes, soft morning light, same calm health-explainer visual language. Keep the same character identity and wardrobe family when reference continuity exists. No readable text. Avoid speech pose, avoid doctor costume, avoid photorealistic drift.

Possible Veo 3 i2v prompt:
Gentle forward drift. The woman slows one step and makes a small balancing hand adjustment while her jacket hem and nearby leaves move in the morning breeze. Preserve the calm observational mood, the exact character identity, and the existing appearance of the source image. (Silent video, no audio). No lip sync, no direct-to-camera speech, no new readable text.
