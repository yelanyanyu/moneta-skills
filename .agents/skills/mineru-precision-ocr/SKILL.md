---
name: mineru-precision-ocr
description: "Precisely OCR explicitly specified PDFs with MinerU MCP: split files over 200 pages, parse every part, merge verified Markdown, and rotate backups. Use when the user requests OCR or precision parsing of a concrete PDF."
---

# MinerU 精准 PDF 解析

1. 只接受用户显式指定的 PDF；未给出路径时索取路径，提交前说明文件将上传至 MinerU。密钥仅由用户在 MCP 客户端录入，不经对话或项目文件传递。
2. 调用 MinerU MCP；若不可用或鉴权失败，安装官方 MCP，并引导用户在 [MinerU API 管理页](https://mineru.net/apiManage/docs)创建 Token、在 MCP 客户端手动配置 `MINERU_API_TOKEN` 后重试，全程使用精准解析。
3. 对每个 PDF 调用 `scripts/prepare_pdf.py` 并传入绝对路径；按其 JSON 清单顺序使用源文件或每份不超过 200 页的分卷。
4. 语言不明时调用 `get_ocr_languages`；德语等拉丁字母文献使用 `latin`。一次调用 `parse_documents` 提交清单中的全部文件，设置 `enable_ocr: true`、语言及 `.moneta/mineru-output/<源文件名>/` 绝对输出目录，省略 `model`。
5. 等待并检查每份结果；任一失败时保留成功结果、报告错误，不生成或覆盖完整 Markdown。
6. 全部成功后，将结果命名为 `<源文件名>.pages-起始页-结束页.md`，再调用 `scripts/merge_markdown.py`：结果目录作为 `--parts-dir`，`.moneta/resources/<源文件名>.md` 作为 `--output`，`.moneta/backups/mineru/<源文件名>` 作为 `--backup-dir`，备份保留 30 天且至少保留最近 3 份。
7. 仅在合并脚本返回 `status: success` 后报告完成，并反馈源文件、总页数、分卷范围、成功/失败数、完整 Markdown 路径、SHA-256、任务 ID、备份及清理结果。
