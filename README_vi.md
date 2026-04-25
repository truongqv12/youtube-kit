# 🎬 Senior Health Video Pipeline — Topic-First v3

> **Pipeline AI-driven tạo video YouTube chất lượng cao cho kênh sức khỏe người cao tuổi.**
> Từ **1 file seed** → sinh toàn bộ profile kênh → nghiên cứu → viết script → sinh prompt ảnh & video → xuất bản.

[![Pipeline](https://img.shields.io/badge/Pipeline-Topic--First%20v3-blue?style=for-the-badge)]()
[![AI Agents](https://img.shields.io/badge/Powered%20by-AI%20Agents-orange?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()

---

## 📖 Tổng quan

Pipeline này tự động hóa toàn bộ quy trình sản xuất video YouTube cho kênh sức khỏe người cao tuổi (60+), sử dụng AI agent (Claude, Gemini, v.v.) để chạy từng bước.

### Điểm nổi bật

- 🌱 **Seed-driven**: Chỉ cần điền 1 file `00_channel_seed.json` (6 trường) → toàn bộ profile kênh được sinh tự động
- 🔬 **Research-first**: Bắt buộc nghiên cứu từ nguồn chính thức trước khi viết script — không bịa, không copy đối thủ
- 🎙️ **TTS-safe script**: Script viết dưới dạng canonical units — mỗi dòng là một câu nói tự nhiên, paste thẳng vào TTS
- 🧑‍🦳 **Character-locked host**: Nhân vật host được khóa bằng character sheet cấp kênh trước khi sinh ảnh/video
- 🖼️ **Line-context locked prompts**: Prompt ảnh (Nano Banana) khóa ngữ nghĩa theo từng dòng script
- 🎥 **Motion-only video prompts**: Prompt video (Veo 3) chỉ mô tả chuyển động, không lặp lại nội dung ảnh
- 📦 **Publication package**: Sinh title, thumbnail concept, description, keyword, và 2 Shorts derivatives
- 📡 **Multi-channel**: Một engine dùng chung, nhiều kênh state riêng biệt

---

## 🏗️ Kiến trúc

```
seniorhealth_pipeline_topic_first_v3/
│
├── core/                          # Tiêu chuẩn & luật chung cho mọi kênh
│   ├── system_principles.md       # Nguyên tắc bất biến
│   ├── canonical_script_unit_standard.md
│   ├── duration_control_standard.md
│   ├── mandatory_research_standard.md
│   ├── policy_guardrails.md       # Rào chắn y tế & nội dung
│   ├── prompt_description_grammar.md
│   ├── character_identity_lock_standard.md
│   ├── topic_strategy_standard.md
│   ├── publication_package_standard.md
│   └── output_conventions.md      # Chuẩn export 3 cột
│
├── bootstrap/                     # Template cho channel & video seed
│   ├── 00_channel_seed.template.json
│   ├── 00_channel_config.template.json
│   ├── 00_editorial_profile.template.json
│   ├── 00_language_profile.template.json
│   ├── 00_publication_profile.template.json
│   ├── 00_visual_profile.template.json
│   ├── 00_host_character_sheet.template.json
│   └── 01_video_intake.template.json
│
├── steps/                         # Định nghĩa từng step
│   ├── 00_build_all_profiles_from_seed.md
│   ├── 01_video_intake.md
│   ├── 02_topic_strategy.md
│   ├── 03_mandatory_research.md
│   ├── 04_policy_gate.md
│   ├── 05_outline_builder.md
│   ├── 06_script_writer_canonical.md
│   ├── 06C_host_character_lock.md
│   ├── 07_image_prompt_builder_reference_first.md
│   ├── 08_video_prompt_builder_non_dialogue.md
│   ├── 09_three_column_exporter.md
│   └── 10_run_publication_package.md
│
├── compiled_prompts/              # Prompt biên dịch sẵn cho AI chạy step
│
├── knowledge/                     # Knowledge base
│   ├── japanese/                  # Ngôn ngữ, kính ngữ, rhythm, lexicon
│   └── visual/                    # Style registry, negative rules
│
├── channels/                      # Dữ liệu riêng từng kênh
│   ├── kenh_1/
│   ├── kenh_2/
│   │   ├── 00_channel_seed.json
│   │   ├── 00_channel_config.json     # (sinh bởi Step 00)
│   │   ├── 00_editorial_profile.json  # (sinh bởi Step 00)
│   │   ├── 00_language_profile.json   # (sinh bởi Step 00)
│   │   ├── 00_publication_profile.json# (sinh bởi Step 00)
│   │   ├── 00_visual_profile.json     # (sinh bởi Step 00)
│   │   ├── 00_host_character_sheet.json
│   │   └── videos/
│   │       └── vid_001/
│   │           ├── 01_intake_spec.json
│   │           ├── 02_topic_strategy.json
│   │           ├── 03_research_brief.json
│   │           ├── 04_policy_report.json
│   │           ├── 05_outline.json
│   │           ├── 06_script_canonical.json
│   │           ├── 06_script_full.md
│   │           ├── 07_image_prompt_table.csv
│   │           ├── 08_video_prompt_table.csv
│   │           ├── 09_final_three_column.csv
│   │           ├── 09_export_qc_report.md
│   │           └── 10_publication_package.json
│   └── kenh_3/
│
├── runbooks/                      # Hướng dẫn vận hành (tiếng Việt)
├── ops/                           # Checklist vận hành kênh & video
└── handoff/                       # Hợp đồng artifact giữa các step
```

---

## 🚀 Bắt đầu nhanh

### Yêu cầu

- **AI Agent**: Claude Code, Gemini CLI, hoặc bất kỳ AI agent nào có thể đọc file và trả artifact
- **Web access**: Cần thiết cho Step 03 (research) và Step 10 (publication package)
- **Không cần cài code**: Pipeline này là hệ thống prompt — AI agent đọc prompt và sinh artifact

### 1. Clone repo

```bash
git clone https://github.com/<your-username>/seniorhealth_pipeline_topic_first_v3.git
cd seniorhealth_pipeline_topic_first_v3
```

### 2. Tạo kênh mới

```bash
# Tạo thư mục kênh
mkdir -p channels/my_channel
```

Copy và điền file seed:

```bash
cp bootstrap/00_channel_seed.template.json channels/my_channel/00_channel_seed.json
```

Nội dung seed chỉ có **6 trường**:

```json
{
  "channel_name": "Tên kênh",
  "channel_description": "Mô tả ngắn kênh giúp người xem hiểu hoặc làm gì.",
  "audience_age": "60+",
  "language_country": "ja-JP / Japan",
  "video_style": "manga editorial clean / seinen soft educational",
  "channel_niche": "senior health daily wellness"
}
```

### 3. Chạy Step 00 — Sinh toàn bộ profile

Dán compiled prompt `00_run_build_all_profiles_from_seed.md` vào AI agent với `TARGET_CHANNEL=my_channel`.

AI sẽ sinh ra:
- `00_channel_config.json`
- `00_editorial_profile.json`
- `00_publication_profile.json`
- `00_visual_profile.json`
- `00_language_profile.json`
- `00_profile_inference_report.md`

### 4. Tạo video mới

```bash
mkdir -p channels/my_channel/videos/vid_001
```

Copy và điền intake:

```bash
cp bootstrap/01_video_intake.template.json channels/my_channel/videos/vid_001/01_video_intake.json
```

### 5. Chạy pipeline theo thứ tự

```
Step 00  →  Build profiles từ seed
Step 01  →  Video intake
Step 02  →  Topic strategy (khóa micro-topic)
Step 03  →  Mandatory research (web access bắt buộc)
Step 04  →  Policy gate (kiểm rào chắn y tế)
Step 05  →  Outline builder
Step 06  →  Script writer canonical (TTS-safe)
Step 06C →  Host character lock (khóa nhân vật cố định)
Step 07  →  Image prompt builder (Nano Banana, line-locked)
Step 08  →  Video prompt builder (Veo 3, motion-only)
Step 09  →  Three-column exporter + QC
Step 10  →  Publication package (web access bắt buộc)
```

---

## 📐 Pipeline chi tiết

| Step | Tên | Input chính | Output chính |
|------|-----|-------------|--------------|
| **00** | Build All Profiles | `00_channel_seed.json` | 5 profile JSON + inference report |
| **01** | Video Intake | `01_video_intake.json` | `01_intake_spec.json` |
| **02** | Topic Strategy | intake spec | `02_topic_strategy.json` |
| **03** | Mandatory Research | topic strategy + **web** | `03_research_brief.json` + source log |
| **04** | Policy Gate | research + guardrails | `04_policy_report.json` |
| **05** | Outline Builder | research + policy | `05_outline.json` |
| **06** | Script Writer | outline + knowledge | `06_script_canonical.json` + full script |
| **06C** | Host Character Lock | visual profile + host references | `00_host_character_sheet.json` |
| **07** | Image Prompt Builder | script + visual profile + character sheet | `07_image_prompt_table.csv` |
| **08** | Video Prompt Builder | image prompts + script | `08_video_prompt_table.csv` |
| **09** | Three-Column Export | prompts + script | `09_final_three_column.csv` + QC report |
| **10** | Publication Package | export + **web** | `10_publication_package.json` |

### Final export — 3 cột duy nhất

| Cột | Mô tả |
|-----|--------|
| `script_text` | Dòng narration TTS-safe, lấy trực tiếp từ canonical units |
| `prompt_img_nano` | Prompt sinh ảnh keyframe (Nano Banana) |
| `prompt_video_veo3` | Prompt sinh video motion-only (Veo 3 image-to-video) |

---

## 🛡️ Rào chắn chất lượng

### Nội dung y tế
- Không bịa thông tin sức khỏe
- Không dùng ngôn ngữ chẩn đoán
- Không hứa chữa bệnh hoặc thay thế bác sĩ
- Ưu tiên framing "thói quen hằng ngày" thay vì tên bệnh gây sốc
- Khuyến cáo tham vấn bác sĩ khi cần

### Script
- Mỗi dòng là một canonical unit — TTS-safe, đọc thành tiếng tự nhiên
- Qua 4 gate: TTS-safe → Naturalness → Rhythm → Breath-group
- Không heading, bullet, emoji, speaker tag, stage direction
- Duration phải nằm trong khoảng `target_min` — `target_max`
- Mỗi dòng cũng phải visual-beat-safe: dễ hỗ trợ bằng 1 ảnh hoặc 1 motion beat rõ ràng cho YouTube

### Nhân vật cố định
- Nếu kênh dùng host, tạo hoặc kiểm `00_host_character_sheet.json` trước Step 07
- Host identity là channel state, không viết lại tùy hứng theo từng video
- Nên có 1-3 ảnh reference trong `assets/host_reference/`
- Prompt host phải dùng identity-lock first: reference → identity packet → scene delta → action delta → drift blockers
- Không đổi tóc, tuổi, outfit family, body type, style, hoặc làm trẻ hóa nhân vật

### Prompt ảnh
- Semantic lock theo từng dòng script — không minh họa chung chung
- Resolve `line_context_frame` trước khi viết prompt
- Nhân vật 60+ phải mô tả rõ dấu hiệu lão hóa (tóc bạc, nếp nhăn, tư thế)
- Locale-correct (kiến trúc, biển hiệu, trang phục phù hợp quốc gia)
- Prompt host phải lấy `prompt_identity_packet` từ character sheet khi có

### Prompt video
- Motion-only — không lặp lại mô tả ảnh
- Silent audio: `(Silent video, no audio).`
- Không lip sync, không thoại trực tiếp
- Không ambience, foley, room tone, music, soundscape, hoặc bất kỳ audio cue nào
- Với host, chỉ preserve identity từ source image/reference; không tạo lại mặt/tóc/trang phục trong video prompt

---

## 📡 Đa kênh

Pipeline hỗ trợ chạy nhiều kênh YouTube trên cùng một bộ engine:

| Dùng chung | Riêng theo kênh |
|------------|-----------------|
| `core/` | `00_channel_seed.json` |
| `knowledge/` | Các profile sinh từ Step 00 |
| `compiled_prompts/` | `00_host_character_sheet.json` |
| `runbooks/` | `assets/host_reference/` |
| `steps/` | `assets/branding/` |
|  | Toàn bộ thư mục `videos/` |

**Khi nào nên tách kênh mới?** Khi muốn khác thực sự ở cấp thương hiệu: khác host, khác style hình ảnh, khác cách kể chuyện, hoặc khác trụ nội dung chính.

---

## ⚙️ Cách chạy với AI Agent

### Quy tắc vàng khi chạy tay

1. **Dán compiled prompt** của step tương ứng vào AI agent
2. **Dán toàn bộ file** liệt kê trong `Required reads` — AI phải đọc trước khi chạy
3. **Yêu cầu Preflight** — AI trả `=== PREFLIGHT START ===` chứng minh đã đọc file và trích luật
4. Chỉ cho chạy tiếp khi Preflight đúng
5. AI trả artifact trong envelope `=== ARTIFACT: filename.ext ===`

### Ví dụ prompt

```
TARGET_CHANNEL=kenh_2
TARGET_VIDEO=vid_001

[Dán nội dung compiled_prompts/06_run_script_writer_canonical.md]
[Dán core/system_principles.md]
[Dán core/canonical_script_unit_standard.md]
[Dán channels/kenh_2/00_channel_config.json]
[Dán channels/kenh_2/00_language_profile.json]
[Dán channels/kenh_2/videos/vid_001/05_outline.json]
...
```

---

## 🗂️ Cấu trúc output

Sau khi chạy xong pipeline, thư mục video chứa artifact từng video. Nếu kênh dùng host, thư mục kênh cũng có `00_host_character_sheet.json`.

```
vid_001/
├── 01_intake_spec.json          # Thông số video
├── 02_topic_strategy.json       # Chiến lược chủ đề
├── 03_research_brief.json       # Tóm tắt nghiên cứu
├── 03_source_log.md             # Log nguồn tham khảo
├── 04_policy_report.json        # Báo cáo rào chắn
├── 05_outline.json              # Outline script
├── 06_script_canonical.json     # Script dưới dạng canonical units
├── 06_script_full.md            # Script đầy đủ dạng markdown
├── 06_script_metrics.json       # Thống kê script (duration, chars)
├── 07_image_prompt_table.csv    # Bảng prompt ảnh
├── 08_video_prompt_table.csv    # Bảng prompt video
├── 09_final_three_column.csv    # ✅ File export chính — 3 cột
├── 09_export_qc_report.md       # Báo cáo QC
├── 10_publication_package.json  # Package xuất bản
└── 10_publication_package.md    # Package xuất bản (readable)
```

---

## 📚 Tài liệu tham khảo

| Thư mục | Mô tả |
|---------|--------|
| `runbooks/` | Hướng dẫn vận hành (tiếng Việt) |
| `ops/` | Checklist kênh & video |
| `handoff/` | Hợp đồng artifact giữa các step |
| `knowledge/japanese/` | Ngôn ngữ tiếng Nhật: kính ngữ, rhythm, lexicon |
| `knowledge/visual/` | Style registry, negative visual rules |

---

## 🤝 Đóng góp

1. Fork repo
2. Tạo branch: `git checkout -b feature/ten-tinh-nang`
3. Commit: `git commit -m "feat: mô tả thay đổi"`
4. Push: `git push origin feature/ten-tinh-nang`
5. Tạo Pull Request

### Quy ước commit

```
feat:     Tính năng mới
fix:      Sửa lỗi
refactor: Tái cấu trúc
docs:     Cập nhật tài liệu
```

---

## 📄 License

MIT License — xem file [LICENSE](LICENSE) để biết chi tiết.

---

## ❓ FAQ

<details>
<summary><b>Pipeline này có cần viết code không?</b></summary>

Không. Đây là hệ thống prompt-driven — bạn điền input JSON, dán prompt vào AI agent, và AI sinh artifact. Không cần cài Python, Node.js, hay bất kỳ runtime nào.
</details>

<details>
<summary><b>Dùng AI agent nào?</b></summary>

Bất kỳ AI agent nào có khả năng: đọc nhiều file cùng lúc, truy cập web (cho Step 03 & 10), và trả artifact dạng structured JSON/CSV. Khuyến nghị: Claude Code, Gemini CLI, hoặc tương đương.
</details>

<details>
<summary><b>Có hỗ trợ ngôn ngữ khác ngoài tiếng Nhật không?</b></summary>

Pipeline thiết kế linh hoạt qua `language_country` trong seed. Tuy nhiên, knowledge base hiện tại (`knowledge/japanese/`) tập trung cho tiếng Nhật. Để dùng ngôn ngữ khác, bạn cần bổ sung knowledge base tương ứng.
</details>

<details>
<summary><b>Có thể dùng cho niche khác ngoài sức khỏe người cao tuổi không?</b></summary>

Có, nhưng cần điều chỉnh `policy_guardrails.md`, knowledge base, và demographic lock trong `prompt_description_grammar.md` cho phù hợp niche mới.
</details>

---

> **Lưu ý**: File `*_vi.md` trong `compiled_prompts/` là bản dịch tiếng Việt để đọc hiểu, **không** dùng để chạy pipeline. Luôn dùng file prompt gốc tiếng Anh.
