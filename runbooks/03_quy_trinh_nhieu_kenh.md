# Quy trình nhiều kênh

## Mô hình đúng
Một engine dùng chung, nhiều channel state riêng.

## Phần dùng chung cho mọi kênh
- `core/`
- `knowledge/`
- `compiled_prompts/`
- `runbooks/`

## Phần riêng theo từng kênh
- `profile/00_channel_seed.json`
- các file profile sinh bởi Step 00
- `assets/host_reference/`
- `assets/branding/`

## Khi nào nên tách thành kênh khác
Chỉ nên tách kênh nếu anh muốn khác thật ở cấp thương hiệu:
- khác host
- khác style hình ảnh
- khác title / thumbnail bias
- khác cách kể chuyện
- khác trụ nội dung chính
