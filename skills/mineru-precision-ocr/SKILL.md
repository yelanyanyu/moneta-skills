---
name: mineru-precision-ocr
description: Use MinerU Precision Extract to OCR explicitly specified PDF files. Trigger only when the user identifies concrete PDF paths and asks to OCR or precisely parse them; verify or install the MinerU MCP and its API credential, inspect page counts, split files over 200 pages, submit every part, merge successful parts into one verified Markdown file, and safely rotate prior Markdown backups.
---

# MinerU 精准 PDF 解析

只处理用户显式指定的 PDF。使用确定性脚本检查和切分页数，通过官方 MinerU MCP 提交精准解析；全部分卷成功后，再用代码合并并复核完整 Markdown。

## 启动前检查

1. 检查当前环境是否已提供名为 `mineru` 的 MCP，并确认它具有精准解析所需的工具，例如 `parse_documents`。不要只检查配置文件；应以 MCP 工具实际可调用为准。
2. 以不显示密钥内容的方式确认精准解析凭据是否可用。若 MCP 报告 Token 缺失、无效或过期，则视为凭据不可用。
3. 若 MinerU MCP 未安装，安装并配置官方 MCP。优先使用官方远程端点 `https://mcp.mineru.net/mcp`；若当前 MCP 客户端不支持该传输方式，再安装官方 `mineru-open-mcp`。安装过程不得生成或猜测 API Key。
4. 若 API Key 不可用，指引用户登录 [MinerU API 管理页面](https://mineru.net/apiManage/docs)自行创建 Token，并在当前 MCP 客户端的密钥或环境变量配置入口手动填入 `MINERU_API_TOKEN`。不得要求用户把 Key 粘贴到对话中，也不得替用户把 Key 写入 Skill、项目配置或仓库文件。
5. 安装或填写凭据后，重新加载 MinerU MCP，并再次确认工具和精准解析凭据可用；在检查通过前暂停 OCR，不得降级为免 Token 的轻量解析。

## 安全边界

- 不扫描目录寻找“可能需要 OCR”的文件，也不从上下文猜测输入文件。
- 用户未给出明确 PDF 路径时，停止并要求提供路径。
- 不要求用户在对话中粘贴 Token，不读取、打印或记录 `MINERU_API_TOKEN`。
- 不把 Token 写入 `SKILL.md`、脚本、项目配置或输出文件。
- 提交前说明文档将上传至 MinerU，并遵守 MCP 的调用批准提示。
- 不用模型直接拼接分卷文本，必须调用本 Skill 的合并脚本。

## 工作流

1. 确认用户明确指定了一个或多个 `.pdf` 文件，并将路径解析为绝对路径。
2. 对每个 PDF 调用 `scripts/prepare_pdf.py`。该代码路径相对于本 Skill 根目录；自行选择解释器和调用方式，并将 PDF 的绝对路径传给 `--pdf`。

3. 读取脚本输出的 JSON 清单。页数不超过 200 时直接使用源文件；超过 200 时只使用清单中的分卷，禁止再次自行切分。
4. 使用启动前检查已经确认可用的 `mineru` MCP。若提交时 MCP 消失、Token 失效或服务进入轻量模式，停止提交并回到启动前检查；不得用轻量模式替代精准解析。
5. 若 OCR 语言不明确，先调用 `get_ocr_languages`，再根据文档语言选择代码。德语和其他拉丁字母文献使用 `latin`。
6. 一次调用 `parse_documents` 提交当前源文件清单中的全部分卷，并设置：

   - `file_sources`：JSON 清单中各分卷的绝对路径，保持原顺序；
   - `enable_ocr`：`true`；
   - `language`：上一步确认的语言代码；
   - `model`：省略，让精准解析服务自动选择；
   - `output_dir`：`.moneta/mineru-output/<源文件名>/` 的绝对路径。

7. 检查 MCP 返回的每个分卷状态。不得把“任务已提交”误报成“解析已完成”。失败时保留成功分卷结果，逐项报告错误，且不要生成或覆盖完整 Markdown。
8. 全部分卷成功后，将每份结果保存为 `<源文件名>.pages-起始页-结束页.md`。即使 PDF 未切分，也使用相同命名方式保存单份结果，便于统一校验。
9. 调用 `scripts/merge_markdown.py` 合并完整 Markdown。该代码路径相对于本 Skill 根目录；自行选择解释器和调用方式。将 MinerU 结果目录、`.moneta/resources/<源文件名>.md`、`.moneta/backups/mineru/<源文件名>` 分别作为分卷目录、输出文件和备份目录，并采用保留 30 天、至少保留最近 3 份的策略。

10. 只接受脚本返回的 `status: success`。检查分卷顺序和页码连续、最终文件可按 UTF-8 解码、替换字符数为零，并记录 SHA-256。若旧的完整 Markdown 存在，脚本会在覆盖前备份；每次成功合并后，清理超过 30 天的备份，但始终保留最近 3 份。
11. 向用户反馈基本信息：源文件、总页数、分卷及页码范围、成功/失败数量、完整 Markdown 路径、字符数、字节数、SHA-256、备份路径和本次删除的过期备份。

## 完成标准

- 所有明确指定的 PDF 都已处理，或逐项说明未处理原因。
- 任一实际提交均使用精准模式且每份不超过 200 页。
- 只有全部分卷成功并通过合并脚本复核后，才将完整 Markdown 报告为完成。
- 用户能定位完整 Markdown、MinerU 原始分卷和备份目录，并看清失败项与备份清理结果。
