# Research notes cho pipeline v3

## 1. Viết script nghe tự nhiên hơn
Các nguyên tắc chính đã được đưa vào Step 06 và `core/canonical_script_unit_standard.md`:
- viết cho tai nghe, không viết cho mắt đọc
- dùng câu ngắn và vừa là chính
- tránh 3 line liên tiếp cùng khuôn câu
- tách line theo breath group
- ưu tiên ví dụ đời sống thay vì danh từ trừu tượng
- dùng few-shot bad → good để dạy mô hình rõ hơn

## 2. Tiếng Nhật hợp người xem 60+
Các nguyên tắc chính đã được đưa vào:
- `knowledge/japanese/05_spoken_narration_rhythm.md`
- `knowledge/japanese/06_senior_accessibility_and_readability.md`
- `knowledge/japanese/checks/repetition_and_ai_slop.md`

Trọng tâm:
- từ quen tai, gần đời sống
- nhẹ nhàng, không ra lệnh
- tránh youth slang
- tránh cold clinical tone
- không nói xuống giọng với người lớn tuổi

## 3. Prompting cho Nano Banana
Đã đưa vào Step 07 các quy tắc:
- mô tả scene hoàn chỉnh
- nếu dùng reference/edit thì phải nói rõ giữ cái gì, đổi cái gì
- visible text phải exact
- không prompt theo kiểu keyword pile
- phải resolve line-context trước khi viết prompt cuối

## 4. Prompting cho Veo 3 i2v
Đã đưa vào Step 08 các quy tắc:
- prompt motion-only
- không mô tả lại full image
- giữ nguyên subject / setting / visible text
- non-dialogue thì cấm speech
- nếu cần thay đổi mạnh hơn thì dùng first-last-frame transition
