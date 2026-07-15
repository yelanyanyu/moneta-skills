---
name: word-disclosure
description: 为印欧语或汉语生成或更新 `word/<language>/` 目录下的 Obsidian Markdown 笔记。正文用中文写作，借文学或艺术作品说明词在具体处境中的语感。
---

# Word Disclosure

本入口只保留执行骨架；输出格式、来源、分析、风格和自检都回到 reference。

## 工作流程

1. 确认词语、一等语言和目标文件；读取现有笔记和需要比较的双链笔记。
2. 读取 [ANALYSIS.md](references/ANALYSIS.md)，再按其中的路由只读取当前语言的分析文件。确定当前词语的主要语文学路径后，才进入下一步。
3. 读取 [SOURCES.md](references/SOURCES.md)，再按其中的路由只读取当前语言的来源文件。只有实际涉及辅助语言时，才读取对应的辅助来源；主要来源和正文走向确定后，才进入下一步。
4. 读取 [FORMAT.md](references/FORMAT.md) 和 [STYLE.md](references/STYLE.md)，起草并保存正文。
5. 草稿完成后，按 [ERROR_INDEX.md](references/ERROR_INDEX.md) 逐项自检。只有命中具体错误类型或拿不准时，才读取 [CORRECTIONS.md](references/CORRECTIONS.md) 中对应的小节。
6. 汇报路径、主要来源、最早来源、引用和词源是否可验证。

## 边界
- 不编造引文、作品出处、译文出处、词源依据或最早来源。只有模糊关联时，就把话说轻；找不到可验证来源时，就明说“暂未找到可验证资料”，或者不写进笔记。
