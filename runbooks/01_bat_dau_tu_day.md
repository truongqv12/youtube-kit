# Bắt đầu từ đây

## Mục tiêu
File này giải thích cách chạy tay theo kiểu dễ đọc, đúng pipeline v3.

## Quy tắc quan trọng
- hướng dẫn đọc cho operator viết bằng tiếng Việt
- prompt thực thi chính giữ bằng tiếng Anh
- file `*_vi.md` trong `compiled_prompts/` chỉ để đọc hiểu, không dùng để chạy
- artifact mới là nguồn sự thật
- không tin AI đã đọc file chỉ vì nó nói là đã đọc
- step nào có `Required reads` thì phải dán đủ file trước khi cho chạy
- luôn bắt AI trả `Preflight` trước
- kênh chỉ điền 1 file `00_channel_seed.json`

## Quy trình ngắn
1. điền `00_channel_seed.json`
2. chạy step 00 để build toàn bộ profile
3. điền `01_video_intake.json`
4. chạy step 01 intake
5. chạy step 02 topic strategy
6. chạy step 03 mandatory research
7. chạy step 04 policy gate
8. chạy step 05 outline
9. chạy step 06 script canonical
10. chạy step 07 image prompt
11. chạy step 08 video prompt
12. chạy step 09 export + minimal QA
13. chạy step 10 publication package

## Lưu ý vận hành
- Không mở đầu bằng việc đi tìm 1 video đối thủ để bám theo.
- Nếu topic angle còn mơ hồ, dừng ở step 02 trước khi research.
- Nếu script nghe còn máy móc, quay lại step 06 thay vì sửa tay ở step 09.
