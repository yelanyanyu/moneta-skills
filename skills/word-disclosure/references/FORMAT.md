# Word Disclosure Format

生成或更新 `word/{language}/{entry}.md`。文件使用 UTF-8 编码。

- 文件开头必须是 Obsidian properties。properties 结束后直接进入正文。正文不写 `# entry`，也不使用分节标题，不输出本项目旧流水线使用的 Word YAML。
- `【】` 是占位符，用来提示生成结构，不要在正文中使用。
```yaml
---
entry: "disclose"
language: "en"
part_of_speech: "verb"
aliases:
  - "disclosed"
  - "disclosing"
tags:
  - word/en
status: "draft"
revelatory_sources:
  primary: "King Lear"
  candidates:
    - "King Lear"
earliest_source: "Middle English / Old French lineage"
created: "2026-07-05"
updated: "2026-07-05"
---

>【艺术作品原文或改写】
>【翻译（原文为非中文）】



```

不要在 properties 里写相关词。Obsidian 双链只放进正文；只有当一个词正在被思考、比较或回忆时，才给它加双链。

正文不写“词源”“近义词”“常用义”“语义演变”这类栏目名。
