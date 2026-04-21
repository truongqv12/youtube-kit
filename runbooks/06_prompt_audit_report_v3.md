# Prompt audit report v3

## Compiled prompts

### 00A / 00B
- Vấn đề: logic bị tách nhỏ quá mức, config phải điền tay nhiều file
- Sửa: deprecated, gộp vào Step 00

### 01
- Vấn đề: phụ thuộc nhiều profile file nhưng chưa nói rõ đây là profile sinh ra
- Sửa: làm rõ source state từ Step 00

### 02
- Vấn đề: thiếu ví dụ bad / good cho micro-topic và promise
- Sửa: thêm examples

### 03
- Vấn đề: source labeling còn lỏng
- Sửa: thêm `official / primary / supporting`

### 04
- Vấn đề: actionable warnings chưa nhấn đủ
- Sửa: ép output operational hơn

### 05
- Vấn đề: outline dễ thiên về article structure
- Sửa: buộc spoken-flow thinking

### 06
- Vấn đề: script nghe AI, thiếu rhythm rules, thiếu few-shot
- Sửa: thêm rhythm gate, breath-group gate, spoken-Japanese gate, negative examples

### 07
- Vấn đề: semantic lock có nói nhưng chưa có line-context layer
- Sửa: thêm `line_context_frame`, prompt mode, preservation clause rõ hơn

### 08
- Vấn đề: motion-only đã có nhưng chưa đủ mạnh trong việc cấm scene redesign
- Sửa: thêm i2v mode, preservation, speech blacklist

### 09
- Vấn đề: chỉ export, chưa có QC tối thiểu
- Sửa: gộp minimal QA tail

### 10 / 11 / 12 cũ
- Vấn đề: pipeline dài và lặp
- Sửa: bỏ QA + operator review riêng, renumber publication package thành Step 10

## Core files

### canonical_script_unit_standard.md
- thêm naturalness gate
- thêm rhythm gate
- thêm breath-group gate

### prompt_description_grammar.md
- thêm line-context layer
- thêm preservation / edit logic cho Nano Banana
- thêm first-last-frame logic cho Veo

### output_conventions.md
- thêm universal response envelope
- thêm `09_export_qc_report.md`

### system_principles.md
- thêm nguyên tắc seed → derived profiles
