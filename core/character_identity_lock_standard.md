# Character Identity Lock Standard

## Goal
Keep a recurring host or character visually stable across image prompts, video prompts, and multiple videos.

The prompt text alone is not enough. Character identity must live in a channel-level artifact and be reused by every downstream visual step.

## Source of truth
For host-enabled channels, the source of truth is:

- `channels/{{TARGET_CHANNEL}}/00_host_character_sheet.json`
- `channels/{{TARGET_CHANNEL}}/assets/host_reference/` when reference images exist

The character sheet is channel state. It is not a per-video creative choice.

## Required character sheet fields
The character sheet must define:

- `character_id`
- `core_identity_statement`
- `reference_images`
- `face_lock`
- `hair_lock`
- `age_lock`
- `body_lock`
- `wardrobe_lock`
- `accessory_lock`
- `expression_policy`
- `pose_policy`
- `continuity_anchors`
- `forbidden_drift`
- `prompt_identity_packet`
- `video_preservation_packet`

## Identity packet
`prompt_identity_packet` is the compact identity text inserted into every host image prompt.

It must be stable, short, and concrete. It should lock:

- same named channel host
- visible age range
- face shape and wrinkle pattern
- hair color, length, and silhouette
- mature posture and body type
- wardrobe family and fixed accessories
- visual style family

Do not rewrite this packet creatively per row.

## Reference image policy
If host reference images exist:

- use 1 primary front-facing image as the minimum reference
- use up to 3 subject images when the generation tool supports subject images
- keep the same character sheet even when new reference images are added
- never mix different host designs in the same channel

Recommended reference set:

- `host_primary_front.png`
- `host_three_quarter.png`
- `host_half_body.png`

## Host prompt construction
Every host image prompt must use this order:

1. reference instruction
2. fixed `prompt_identity_packet`
3. resolved style lock
4. current line's scene delta
5. current line's action delta
6. continuity anchors
7. drift blockers
8. visible text rule

The fixed identity should change less than the action.

## Video preservation packet
Every host video prompt must preserve identity instead of redesigning it.

Use language like:

`Preserve the exact host identity, face, hair silhouette, age cues, wardrobe family, and illustration style from the source image.`

The video prompt must not introduce new face, new hairstyle, new outfit, or new age cues.

## Forbidden drift
Block these explicitly when relevant:

- youth reduction
- smoother skin
- different hairstyle
- different hair color
- outfit redesign
- body-type change
- photorealistic drift
- glamour or idol styling
- lip sync or mouth-performance acting
- direct-to-camera speech unless explicitly enabled

## Quality gate
A host row fails if:

- it uses `host_usage=host` but does not include the identity packet or equivalent concrete anchors
- it changes hair, age, outfit, body type, or host gender without a channel-level update
- it describes a generic senior person instead of the channel host
- it relies only on vague phrases like `same host`, `older woman`, or `friendly character`
- it asks the video model to invent new character details

## Non-host rows
Do not force the host into every scene. Use non-host scenes for:

- object demonstrations
- hazard examples
- process metaphors
- comparison pairs
- environment bridges

This reduces identity drift by limiting host appearances to rows where trust, continuity, reassurance, or transition truly matters.
