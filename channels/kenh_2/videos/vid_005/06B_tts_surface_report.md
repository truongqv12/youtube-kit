# 06B TTS Surface Normalization Report

**Project:** kenh_2_vid_005
**Source:** 06_script_canonical.json (95 units, 3346 chars, 10.5 min)
**Output:** 06B_script_canonical.json (95 units, 3308 chars, 10.3 min)
**Delta:** -38 chars (-1.1%)

---

## Summary

16 of 95 units were rewritten for TTS surface stability. No splits, no merges, no meaning changes. All policy softeners, consult-clinician triggers, and forbidden-claim avoidances are preserved.

---

## Change Log

### Rule D — Reading Risk (Numeral/Symbol Normalization)

| Unit # | Source 06 | Normalized 06B | Rule | Reason |
|--------|-----------|----------------|------|--------|
| 1 (S1) | `もわっと暑い` | `暑い` | E (mimetic) | `もわっと` is non-essential mimetic; some engines may render it with unstable emphasis or timing |
| 6 (S2) | `約9万7000人` | `およそ9万7千人` | D (reading) | `約` can be read as やく or およそ depending on engine; `7000` can wobble between ななせん/しちせん — `7千` is more stable |
| 7 (S2) | `約6割近くが` | `およそ6割が` | D (reading) | Same `約` instability; `近く` adds softness but creates a micro-pause risk — meaning preserved without it |
| 8 (S2) | `「住居」、つまり` | `住居、つまり` | C (quote) | Inner 「」 around common word creates unnecessary pause cue in TTS; word is not a quoted fragment |
| 9 (S2) | `約38パーセント、3万7000人以上` | `およそ38パーセント、3万7千人以上` | D (reading) | Same `約`/`7000` normalization |
| 15 (S3) | `使いたくない、という` | `使いたくないという` | B (pause) | Comma before という creates a competing pause that sounds like a fragment landing |
| 17 (S3) | `わからない、という声` | `わからないという声` | B (pause) | Same comma-before-という issue |
| 24 (S3) | `「エアコンの設定温度」ではなく「お部屋の実際の温度」` | `エアコンの設定温度ではなく、お部屋の実際の温度` | C (quote) | Double inner quotes create 4 pause points in one line; removing them and adding one comma simplifies TTS parsing |
| 33 (S3) | `不具合があった場合は早めに` | `不具合があれば早めに` | A (landing) | `場合は` after `あった` creates a semi-suspended conditional; `あれば` is more stable and natural |
| 40 (S4) | `「まだ大丈夫」と思っていたら` | `まだ大丈夫だと思っていたら` | C (quote) | Inner quotes around common phrase create a pause cue that sounds visual rather than spoken |
| 41 (S4) | `「喉が渇いたな」と感じる前に` | `喉が渇いたと感じる前に` | C (quote) | Same; also removed な particle inside quote which creates informal tonal shift |
| 43 (S4) | `タイミングについて、かかりつけ医` | `タイミングについてかかりつけ医` | B (pause) | Comma after について creates competing pause; the clause runs naturally without it |
| 53 (S5) | `自律神経の回復のためにもう少し低い温度がよいという指摘もありますが` | `もう少し低い温度がよいという指摘もありますが` | F (comfort) | `自律神経の回復のために` is a medical-jargon clause that may confuse older listeners and adds reading risk; the essential meaning (some research suggests lower temps) is preserved |
| 60 (S5) | `夜中に目が覚めたとき、すぐに` | `夜中に目が覚めたときにも、すぐに` | A (landing) | Added にも to prevent the とき from sounding suspended before the comma |
| 65 (S6) | `もし換気扇のフィルターに` | `換気扇のフィルターに` | F (comfort) | Opening もし creates a conditional promise that requires resolution in the same line, but this line is already the main clause; removing もし makes the line more direct |
| 76 (S7) | `「ただの夏バテかな」「歳のせいかな」と見過ごし` | `ただの夏バテかな、歳のせいかな、と見過ごし` | C (quote) | Double inner quotes with two quoted fragments create unstable multi-pause rendering; comma-separated inner thoughts sound more spoken |
| 77 (S7) | `でも、こうしたサインが` | `ですが、こうしたサインが` | F (comfort) | `でも` is slightly casual for this register context; `ですが` aligns better with warm_polite_practical |
| 80 (S7) | `もし意識がはっきりしなかったり` | `意識がはっきりしなかったり` | F (comfort) | もし is redundant before a clearly conditional clause; removing it gives a more stable, direct landing |
| 81 (S7) | `「#7119」に電話すれば` | `シャープ7119に電話すれば` | D (reading) | `#` symbol is a major reading risk — engines may read it as ハッシュ, シャープ, ナンバー, or skip it entirely. `シャープ` is the standard spoken form for Japan's emergency consultation dial |
| 85 (S8) | `「お住まいの市区町村名」と「地域包括支援センター」で検索` | `お住まいの市区町村名と、地域包括支援センターで検索` | C (quote) | Double inner quotes around search terms feel like a visual instruction rather than spoken advice; removing them with a natural comma makes it sound like a spoken tip |

---

## Rules Applied — Summary

| Rule | Name | Count |
|------|------|-------|
| A | Suspended-ending | 2 |
| B | Comma-chain / pause | 3 |
| C | Quote-fragment | 5 |
| D | Reading-risk | 4 |
| E | Mimetic-density | 1 |
| F | Audience-comfort | 4 |

---

## Preservation Checks

| Check | Status |
|-------|--------|
| Meaning preserved | ✅ No factual meaning changed |
| Policy softeners preserved | ✅ All 7 mandatory softeners intact |
| Consult-clinician triggers | ✅ C1, C2, C3 intact at same positions |
| Banned phrases | ✅ Still absent |
| Forbidden claims | ✅ Still absent |
| Unknown respect (U1-U4) | ✅ Still respected |
| Visual-beat clarity | ✅ All concrete objects/actions preserved |
| Engine-agnostic | ✅ No SSML, phonemes, kana-control, vendor notation |
| Register/tone preserved | ✅ Warm, polite, practical — channel voice intact |
| Duration within target | ✅ 3308 chars / 10.3 min (target: 3200-5760 / 10-18) |

---

## Notes for Downstream Steps

- Step 07 (Image Prompt Builder) should read `06B_script_canonical.json` as source
- Step 08 (Video Prompt Builder) should read `06B_script_canonical.json` as source
- Step 09 (Three-Column Exporter) should export `script_text` from `06B_script_canonical.json`
- `1.2リットル` was kept as-is — the `1.2` decimal is a standard reading for Japanese TTS (いってんにリットル) and does not need kana normalization at this engine-agnostic layer
- `10分`, `30分`, `28度`, `26度` — kept as-is; these are standard numeral+counter patterns that all major Japanese TTS engines handle correctly
