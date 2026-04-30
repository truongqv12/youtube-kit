# 06B TTS Surface Normalization Report

**Project:** kenh_2_vid_001  
**Generated:** 2026-04-22T12:15:00+07:00  
**Source:** 06_script_canonical.json (113 units, 3696 chars)  
**Output:** 06_script_canonical.json (116 units, 3672 chars)  

## Summary

Engine-agnostic surface normalization applied. No meaning drift, no policy weakening, no engine-specific notation introduced. Script remains warm, natural, and TTS-portable.

## Changes Applied

### 1. Landing Stability (Rule A — Suspended Endings)

| Lines | Issue | Action |
|-------|-------|--------|
| 4–6 (orig) | 3 consecutive lines ending `〜こと。` — suspended fragment pattern | **Rewritten:** Line 4–5 changed to `〜たり。` pattern (listing); Line 6 changed to complete sentence `〜方もいらっしゃるかもしれません。` |
| 7 (orig) | Quote fragment `「あれ？」という瞬間` felt slightly written | **Simplified:** Removed quote marks, used plain wording |
| 23 (orig) | `「じゃあ、どこを見直しておけばいいか」` — embedded quote fragment | **Rewritten:** Removed quotes, direct phrasing |

### 2. Pause Stability (Rule B — Comma Chains)

| Line | Issue | Action |
|------|-------|--------|
| 99 (orig) | 4+ commas: `手すりの設置や床材の変更などが対象になることがあり、上限20万円で自己負担は1割から3割程度が目安とされています。` | **Split** into 2 units: one for coverage scope, one for cost details |
| 89 (orig) | 3 actions joined in 1 unit: `滑り止めマットを敷いてみる。手すりの場所を確認してみる。脱衣所を少し暖めておく。` | **Split** into 3 separate units for natural breath groups |

### 3. Reading Stability (Rule D — Numerals & Mixed Scripts)

| Surface | Issue | Normalized To |
|---------|-------|---------------|
| `41度` | TTS may read as `よんじゅういちど` or `しじゅういちど` | `よんじゅういち度` |
| `40度` | Same ambiguity | `よんじゅう度` |
| `10分` | May read as `じゅっぷん` or `じっぷん` | `じゅっぷん` |
| `20万円` | Stable but normalized for uniformity | `にじゅうまんえん` |
| `1割` | May vary across engines | `いちわり` |
| `3割` | Same | `さんわり` |
| `I字タイプ` | Roman letter `I` reading risk | Removed roman label; described by function only |
| `L字型` | Roman letter `L` reading risk | `エル字型` |
| `自沈式` | Uncommon compound that may cause reading wobble | Removed label; described by function: `自重で沈むタイプ` |

### 4. Rhetoric-to-Speech (Rule E & F)

| Line | Issue | Action |
|------|-------|--------|
| 52 (orig) | `まず、縦型のI字タイプ。これは、` — fragment + restart | **Merged** into one flowing sentence |
| 53 (orig) | `次に横型。横に体を` — same fragment pattern | **Rewritten** as complete sentence |
| 81 (orig) | Long line with embedded `「お風呂に入りますよ」` quote | **Split** into narration + natural paraphrase |
| 42 (orig) | Comma before `ぐらつく` could create unstable pause | **Removed** unnecessary comma |
| 63 (orig) | `無理をせず、専門の方に` — comma before continuation | **Removed** comma for smoother flow |

### 5. Portability Check
- No SSML tags: ✅
- No phoneme strings: ✅
- No kana-only control syntax: ✅
- No vendor dictionary formats: ✅
- No AquesTalk notation: ✅
- No ruby/furigana markup: ✅

## What Was Preserved
- All policy softeners (SF01–SF05) intact
- All `かかりつけ医` consultation guidance intact
- All `ケアマネジャー` consultation guidance intact
- All `事前申請` warning intact
- Same section flow and emotional arc
- Same register (warm_polite_educational)
- Same scope (3 bath safety check items only)
- No new claims introduced
- No certainty inflation

## Metrics Comparison

| Metric | Step 06 | Step 06B | Delta |
|--------|---------|----------|-------|
| Units | 113 | 116 | +3 |
| Chars (no newlines) | 3,696 | 3,672 | −24 |
| Duration (est.) | 11.6 min | 11.5 min | −0.1 |
| Max unit length | 57 | 53 | −4 |
| Reconstruction | PASS | PASS | — |

Duration remains within target range [3,200–5,760 chars].
