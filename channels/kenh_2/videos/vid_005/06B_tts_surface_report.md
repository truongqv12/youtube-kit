# TTS Surface Normalization Report — kenh_2_vid_005

## Summary

| Metric | Source (06) | Normalized (06B) |
|--------|------------|-------------------|
| Units | 94 | 95 |
| Characters | 3,220 | 3,223 |
| Duration | 10.1 min | 10.1 min |
| In range | ✅ | ✅ |

## Changes Applied

### A. Landing Stability Fixes

| # | Source Line | Issue | Fix |
|---|-----------|-------|-----|
| 1 | `暑さの影響って、外出のときだけとは限りません。` | `って` is mildly colloquial but stable | Changed to `暑さの影響は、` — calmer, more stable landing |
| 2 | `おうちの中で暑さにやられてしまう方が一番多いんですね。` | Slightly casual ending | Changed to `いちばん多いということです。` — cleaner TTS landing |
| 3 | `暑さに体が順応するまでには、少し時間がかかるんですね。` | `んですね` can wobble | Changed to `すこし時間がかかります。` — stable declarative landing |

### B. Comma-Chain Splits

| # | Source Line | Issue | Fix |
|---|-----------|-------|-----|
| 1 | `40パーセントから60パーセントくらいが快適とされていますが、湿度が80パーセントを超えると、温度が28度以下でも体に…` | 3 clauses in one line | Split into 2 lines: guideline statement + exception warning |
| 2 | `「のどが渇いたな」と思ったときには、実はもう体の水分が…` | Quote + explanation in one line | Simplified: removed inner quote, direct statement |

### C. Reading-Stability Fixes (Numeral Normalization)

| # | Source Surface | Normalized Surface | Reason |
|---|--------------|-------------------|--------|
| 1 | `1,000ミリリットルから1,500ミリリットル` | `千ミリリットルから千五百ミリリットル` | Comma-separated numerals cause reading instability across TTS engines |
| 2 | `200ミリリットル` | `二百ミリリットル` | Consistent with kanji numeral normalization |
| 3 | `5杯から7杯` | `五杯から七杯` | Small numerals with counters more stable in kanji |
| 4 | `100円ショップ` | `百円ショップ` | Standard spoken form |

### D. Quote-Fragment Stabilization

| # | Source | Fix | Reason |
|---|-------|-----|--------|
| 1 | `「電気代がもったいない」とか「風が苦手」と感じて` | Removed inner quotes | Quoted fragments create pause instability in TTS |
| 2 | `「まだ大丈夫かな」と思ったまま` | Removed quotes | Direct speech without quotes reads more stably |
| 3 | `「地域包括支援センター」` | Removed quotes | Proper noun reads fine without quotes in spoken form |
| 4 | `「民生委員」` | Removed quotes | Same reason |

### E. Suspended-Fragment Fixes

| # | Source | Fix | Reason |
|---|-------|-----|--------|
| 1 | `部屋の温度、水分のとり方、そして体の変化サイン。` | Added `です。` | Fragment line now has complete landing |
| 2 | `たとえば、めまいや立ちくらみ。` | Added `があります。` | Fragment → complete sentence |
| 3 | `体がだるくて力が入らない。` | Added `こともあります。` | Fragment → complete sentence |
| 4 | `足がつったり、こむら返りが起きたりする。` | Added `こともあります。` | Fragment → complete sentence |
| 5 | `軽い頭痛や、なんとなく気持ちが悪い。` | Added `と感じることもあります。` | Fragment → complete sentence |

### F. Rhetoric-to-Speech Simplifications

| # | Source | Fix | Reason |
|---|-------|-----|--------|
| 1 | `体が暑さを感じるセンサーが少し鈍くなる` | `暑さを感じる力がすこし弱くなる` | `センサー` is a metaphor that may confuse literal TTS prosody |
| 2 | `結果的には安心です` | `安心です` | Removed `結果的には` — unnecessary written connector |
| 3 | `〜だという話もあります` | `〜だとも言われています` | More natural spoken form |

## Policy Compliance

All 4 mandatory softeners (MS1–MS4) preserved. No claim strengthening. No new medical instructions.

## Engine-Agnostic Confirmation

- No SSML tags
- No phoneme strings
- No kana-only control syntax
- No vendor dictionary formats
- No ruby/furigana markup
- Output is generic Japanese spoken text
