# TTS Surface Normalizer Report

## Overview
- **Source Script:** `06_script_canonical.json`
- **Output Script:** `06_script_canonical.json`
- **Units Before:** 113
- **Units After:** 111
- **Characters Before:** 3,215
- **Characters After:** 3,200

## Key Normalizations Applied

### A. Suspended-Ending Resolution (Landing Pass)
- **L26-27 merged:** `では、具体的にどんな習慣が気をつけたいポイントなのか。` + `ひとつ目から見ていきましょう。` → single complete transition: `では、具体的にどんな習慣に気をつけたいのか、ひとつ目から見ていきましょう。`
- **L74 completed:** `血圧が急に上がったり、心臓に余計な負担がかかったり。` → added `ことがあります` to form stable landing.
- **L102-104 resolved:** Three consecutive suspended `〜場合。` lines merged into complete caution sentences with explicit `注意が必要です`, `同じです`, `無理をせず…相談してみてください` endings. Eliminates 3× suspended-ending repetition.

### B. Quote-Fragment Normalization (Reading-Stability Pass)
Decorative `「」` quotes removed or simplified for TTS stability:
- `「年だから仕方ない」` → `年だから仕方ない` (internal thought, natural without quotes aloud)
- `「疲れにつながりやすい習慣」` → `疲れにつながりやすい習慣` (narrative phrase, stable without quotes)
- `「目覚めのスイッチ」` → `目覚めのスイッチ` (metaphor, clear in context)
- `「今日が始まった」` → `今日が始まったと認識します` (indirect speech, natural)
- `「まだ夜」` → `まだ夜のままで` (natural spoken form)
- `「おはよう」` → `おはようの合図` (clear without decorative quotes)
- `「活動モード」` → `活動モードに入れない` (technical term clear in context)
- `「寝ている延長」` → `寝ている延長のような感覚` (metaphor flows naturally)
- `「今日は動いていいんだ」` → `今日は動いていいんだと感じ始めます` (indirect speech)
- `「ペーシング」` → `ペーシングという考え方` (term introduction clear)
- `「疲れ切る前に休む」「一日のやることを…」` → comma-separated direct description
- `「今日は買い物だけにしよう」「掃除は明日にしよう」。` → `というように分けてみてください` (more natural spoken form)

### C. Mimetic Reduction (Rhetoric-to-Speech Pass)
- `きゅっと縮まって` → `縮まって` (removed mimetic, meaning preserved via context)
- `ぐったり` → `ぐったりしてしまう` (completed the suspended ending, kept natural mimetic)
- `ふっと楽に` → `楽になること` (simplified for stable TTS prosody)
- `ぐっと楽に` → `楽にしてくれる` (simplified)

### D. Numeral Normalization (Reading-Risk Pass)
- `10分から15分` → `十分から十五分` (full kanji prevents mixed-script reading wobble)
- `1つか2つ` → `ひとつかふたつ` (hiragana for natural spoken counter stability)

### E. Comma-Chain Simplification (Pause Pass)
- **L57 split:** `座ったままの状態が長く続くと、血のめぐりがゆっくりのまま、筋肉も冷えたままになりやすくなります。` → Split into two lines: `〜ゆっくりのままになりやすくなります。` + `筋肉も冷えたままで〜`
- **L37 simplified:** `特に、たんぱく質が…` → removed leading comma after `特に` for smoother flow

## Preserved Elements
- All policy softeners intact (cold water as preference, clinician guidance, disclaimers)
- All evidence citations preserved (厚生労働省, WHO, フレイル)
- Warm register maintained throughout
- No meaning drift from Step 06
- No new claims introduced

## Final Status
- **Meaning drift:** None
- **Policy boundaries:** Intact
- **TTS readability:** High (Engine-Agnostic, Natural Spoken Japanese)
- **Duration:** 3,200 chars / ~10 min — within target range
