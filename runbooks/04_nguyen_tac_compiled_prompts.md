# Nguyên tắc cho thư mục compiled_prompts

## Thư mục này để làm gì
Chứa các file prompt thực thi theo từng step.

## Quy tắc mới cho v3
- file prompt thực thi chính giữ bằng tiếng Anh
- cho phép file companion `*_vi.md` trong cùng thư mục
- file `*_vi.md` chỉ để operator đọc hiểu logic
- không dùng file `*_vi.md` để chạy pipeline

## Vì sao
Operator Việt cần hiểu logic mà không bắt buộc phải đọc tiếng Anh chuyên ngành, nhưng prompt chạy thật vẫn cần ổn định bằng tiếng Anh.
