# TTS Surface Normalizer Report

## Overview
- **Source Script:** `06_script_canonical.json`
- **In-place Target Script:** `06_script_canonical.json`
- **Units Before:** 94
- **Units After:** 89
- **Characters Before:** 3,315
- **Characters After:** 3,125

## Key Normalizations Applied

### A. Suspended-Ending Resolution (Merge)
- Merged suspended clauses `朝、布団のなかで目が覚めて、「さあ起きよう」と思ったとき。` with the following line to form a stable question that stands well independently.
- Merged `実は、〜年齢を重ねていくと。` with its main argument for solid grammatical completion and landing support.
- Merged `もし、毎日ゆっくり起き上がるようにしても、強い立ちくらみやめまいが続く場合。` into a complete cautionary thought `〜気をつけてください` or `〜注意が必要です` forming a non-suspended breath.

### B. Mimetic Reduction (Rhetoric-to-Speech Pass)
To eliminate exaggerated, unstable emphases during TTS playback, the following mimetics were removed or simplified:
- `パッと` → removed
- `ふわっと` → removed
- `ギュッと` → removed
- `パーッと` → `大きく`
- `スッと` → removed
- `ヒヤッと` → removed
- `ゴクゴクと` → removed
- `じんわりと` → `少しずつ`

### C. Reading & Visual Risks Removed
- Stripped decorative quotation marks around phrases like `「3つの習慣」`, `「ゆっくり起き上がる」`, `「横になったままの軽い体操」`, and `「喉が渇いた」`.
- Changed `2分から3分` into the simpler, stable `2、3分`.
- Changed unstable metaphorical `カラカラ状態` to a factual, clear `水分不足の状態` preventing ambiguity in intonation.

### D. Comma-Chain & Punctuation Cleanup
- Split long explanatory lines about nighttime dehydration to eliminate multiple commas.
- `ですが、私たちは寝ている間も、呼吸をしたり、目に見えないくらいの寝汗をかいたりして、少しずつ水分を失っています。` 
  → Split into two stable declarative lines: 
  1. `ですが、私たちは寝ている間も、少しずつ水分を失っています。` 
  2. `呼吸をしたり、気づかないうちに汗をかいたりしているからです。`

## Final Status
- **Meaning drift:** None
- **Policy boundaries:** Intact
- **TTS readability:** High (Engine-Agnostic, Natural Spoken Japanese)
