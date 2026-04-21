# Quy trình chạy 1 video

## 1. Tạo video folder
Tạo thư mục video mới theo một mã rõ ràng.

## 2. Chuẩn bị input
- Điền `profile/00_channel_seed.json`
- Chạy Step 00 để sinh toàn bộ profile
- Điền `inputs/01_video_intake.json`

## 3. Chạy prompt theo step
Chạy theo thứ tự:
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10

## 4. Lưu output đúng chỗ
- research lưu vào `research/`
- artifact pipeline lưu vào `artifacts/`
- file 3 cột cuối lưu vào `exports/`
- title / thumbnail / description / shorts notes lưu vào `publication/`

## 5. Chỉ public khi đủ 3 điều
- `09_export_qc_report.md` không có lỗi chặn
- publication package đã có title, thumbnail, mô tả, keyword
- đã có 2 shorts derivatives để kéo traffic vào bản dài
