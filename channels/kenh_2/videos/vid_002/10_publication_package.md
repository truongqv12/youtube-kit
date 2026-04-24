# Publication Package Report — kenh_2 / vid_002

## Preflight

| # | Check | Status |
|---|-------|--------|
| 1 | files_read (14 required) | ✅ All read |
| 2 | rules_extracted_by_file | ✅ policy_guardrails, publication_package_standard, visual_profile, language_profile |
| 3 | required_inputs_detected | ✅ 09_final_three_column.csv (95 rows), 09_export_qc_report.md (PASS) |
| 4 | target_audience_detected | 60+ Japanese seniors, living alone or with minimal support |
| 5 | channel_language_detected | ja-JP |
| 6 | web_access_detected | ✅ 3 web searches performed |
| 7 | market_scan_plan | ✅ 10 examples inspected, 6 directly relevant, 3 guidance sources |
| 8 | allowed_to_proceed | ✅ YES |

---

## Market Scan Summary

### Web Searches Performed
1. `脱衣所 高齢者 安全 YouTube 動画 タイトル サムネイル`
2. `シニア 入浴 ヒートショック 脱衣所 寒さ対策 YouTube`
3. `YouTube thumbnail best practices senior health Japan 高齢者 サムネイル ガイドライン`

### Key Observed Patterns
- **Numbers work well** — `3つ`, `5選` in titles consistently perform
- **Two tone camps**: fear-framing vs calm educational. Fear-framing gets attention but alienates senior audiences who want reassurance.
- **Thumbnails**: Minimal text (2-4 large words), high contrast, single focal point. Senior viewers need large readable text on mobile.
- **Authority**: Professional channels use white-coat hosts. This channel is illustrated — differentiates naturally.

### Fit for kenh_2
- ✅ Calm domestic object-focused scenes (matches illustrated style)
- ✅ Number anchor (3つ) — proven pattern
- ✅ Retro-clean 2D illustration — unique differentiator
- ✅ '見直し' framing — safe, no overpromise

### Mismatches to Avoid
- ❌ Fear imagery, alarm icons (violates fear_intensity_ceiling=low)
- ❌ Overpromise ('事故ゼロ', 'これで安全')
- ❌ Medical authority framing without credentials
- ❌ Photorealistic thumbnail (channel is illustrated)
- ❌ Dense text overlay (5+ words)

---

## Selected Package

### Title
**脱衣所で気をつけたいこと3つ【60代・70代の暮らし】**

> 3 điều cần chú ý ở phòng thay đồ【Cuộc sống tuổi 60-70】

**Lý do chọn:** Khớp chính xác với nội dung script (3 điểm check), dùng number-anchor pattern (3つ) đã chứng minh hiệu quả, age-band bracket tăng relevance cho target demo 60-70.

### Thumbnail Concept
**Góc phòng thay đồ với 3 đồ vật:** thảm cork, lò sưởi ceramic nhỏ, ghế thấp. Minh họa retro-clean 2D, warm earth tones. Text overlay: `脱衣所 3つの見直し` (4 từ).

**Lý do chọn:** Hiển thị cả 3 practical items trong 1 illustration → truyền tải toàn bộ giá trị video trong 1 ánh nhìn. Không có fear imagery, không overpromise. Phong cách illustrated tạo khác biệt so với đối thủ dùng photo.

### Description (Japanese — publish-ready)
```
脱衣所で気をつけておきたいポイントを3つに絞ってお話しします。

① 床の滑りやすさと段差のこと
② 温度差への備え（ヒートショック予防の工夫）
③ 着替えるときの動作と工夫

それぞれ、今日からできる小さな見直しばかりです。
大掛かりな工事の話ではありません。

■ 介護保険の住宅改修制度についても簡単にご案内しています。

※ この動画は情報提供を目的としたものです。体調に不安がある方は、かかりつけ医にご相談ください。
※ 暖房器具をお使いの際は、メーカーの取扱説明書をご確認ください。

#脱衣所 #シニア #転倒予防 #ヒートショック #高齢者の暮らし #入浴安全 #お風呂の安全 #介護保険住宅改修
```

### Keywords (16 tags)
`脱衣所` `高齢者` `転倒予防` `ヒートショック` `シニア` `入浴安全` `コルクマット` `脱衣所暖房` `着替え 安全` `介護保険 住宅改修` `60代` `70代` `お風呂 安全` `滑り止め` `手すり` `脱衣所 寒さ対策`

---

## Shorts Derivatives (Template Only)

> ⚠️ **Note:** `01_intake_spec.json` chỉ định `derive_shorts = 0` cho video này. Các concept dưới đây là **template concepts** để tham khảo tương lai, KHÔNG được sản xuất cho vid_002.

### Short 1: 脱衣所の温度準備
- **Title:** 脱衣所、暖めてから服を脱いでいますか？
- **Hook:** 冬の脱衣所、そのまま服を脱いでいませんか？
- **Cut angle:** Temperature gap awareness — 15s quick tip pre-heating
- **Bridge to longform:** もっと詳しい3つのチェックポイントは、長い動画でひとつずつ確認しています。

### Short 2: 着替えの安全姿勢
- **Title:** 着替えるとき、片足立ちになっていませんか？
- **Hook:** 脱衣所でズボンを脱ぐとき、片足で立っていませんか？
- **Cut angle:** Safe changing posture — 15s tip about sitting while changing
- **Bridge to longform:** 座って着替えるコツや便利な道具は、長い動画で詳しくお話ししています。

---

## Policy Compliance Check

| Check | Status |
|-------|--------|
| Title không overpromise | ✅ |
| Title không dùng banned phrases | ✅ |
| Title không dùng disease-name shock bait | ✅ |
| Thumbnail emotion = warm_reassuring | ✅ |
| Thumbnail không có fear imagery | ✅ |
| Thumbnail text ≤ 6 words, Japanese only | ✅ (4 từ) |
| Description có soft disclaimer (DN01) | ✅ |
| Description có heater disclaimer (DN04) | ✅ |
| Description match actual script content | ✅ |
| Shorts marked as template-only per intake | ✅ |
| Output bilingual (JA + VI) | ✅ |
