---
name: word-disclosure
description: 为英语单词生成或更新 `word/` 目录下的 Obsidian Markdown 笔记。正文用中文写作，借文学或艺术作品说明词在具体处境中的语感。
---

# Word Disclosure

当用户要解析英语单词或生成 Obsidian 笔记时，输出 `word/{lemma}.md`。

开始前完整读取 [ERROR\_INDEX.md](references/ERROR_INDEX.md)、[STYLE.md](references/STYLE.md)、[CORRECTIONS.md](references/CORRECTIONS.md)。
需要找来源时读 [SOURCES.md](references/SOURCES.md)。主流程只保留执行骨架，细则按需回到 reference。

## 输出约定

生成或更新 `word/{lemma}.md`。文件使用 UTF-8 编码。

文件开头必须是 Obsidian properties。properties 结束后直接进入正文。正文不写 `# lemma`，也不使用分节标题。

```yaml
---
lemma: "disclose"
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
```

不要在 properties 里写相关词。Obsidian 双链只放进正文；只有当一个词正在被思考、比较或回忆时，才给它加双链。

## 工作流程

1. 确认 lemma、词性、常用义和目标文件 `word/{lemma}.md`。
2. 按 [SOURCES.md](references/SOURCES.md) 先查词源路线，再根据来源词反查文化场景、主要显义来源、最早来源和引文。
3. 读现有 lemma 笔记；需要比较的双链词已有笔记时也读。
4. 起草正文：用故事或诗歌揭示 lemma 诞生的世界；古典、神话、宗教、非现代英语场景按 [STYLE.md](references/STYLE.md) 做本土文化微调。
5. 写词源和意义演变；误用、音译、借用、讹传或跨语言转写要写成来历，不硬解释成稳定词根。
6. 检查中文释义、常用搭配、近义词和双链；中文译法要用例子说明凭什么成立，差异落在动作、路径或人物反应上。
7. 保存前完整读取 [ERROR\_INDEX.md](references/ERROR_INDEX.md)，按索引从第一条到最后一条逐项对照正文。命中或拿不准时，再查 [CORRECTIONS.md](references/CORRECTIONS.md) 的对应样本自检。
8. 保存笔记并汇报路径、主要来源、最早来源、引用和词源是否可验证。

## 细则位置

- 来源、引文、脚注、最早来源和词源查证：读 [SOURCES.md](references/SOURCES.md)。
- 正文语感、中国化改写、近义词、词源处理和 Obsidian 形态：读 [STYLE.md](references/STYLE.md)。
- 自检时先完整读 [ERROR\_INDEX.md](references/ERROR_INDEX.md)，逐项问“这个错误是否出现在正文里”。命中或拿不准时，再按索引去 [CORRECTIONS.md](references/CORRECTIONS.md) 查完整坏例和改法。

## 正文走向

正文通常顺着这些问题往前走，但不要把它们写成标题：

- 日常处境、常用义和人物动作之间有什么关系？
- 这个词是在怎样的世界里诞生、误用、借用、音译或被重新理解的？
- 词源故事、命名故事和主要显义场景是否同一个？哪个更能让读者感到 lemma？
- 显义场景是否需要按 [STYLE.md](references/STYLE.md) 做中国化改写，并补足相关原文上下文？
- 词源、画面和现代用法怎样接成一条可读的线？
- 常见中文译法凭什么成立？它们分别贴着哪个例子、动作或场景？
- 常用搭配、近义词、派生词或同源词是否需要轻轻分开？

## 边界

- 当前只处理英语单词。
- 不输出本项目旧流水线使用的 Word YAML。
- 正文不写标题。
- 正文不写“词源”“近义词”“常用义”“语义演变”这类栏目名。
- 不编造引文、作品出处、译文出处、词源依据或最早来源。只有模糊关联时，就把话说轻；找不到可验证来源时，就明说“暂未找到可验证资料”，或者不写进笔记。

## 汇报

完成后告诉用户：

- 笔记路径。
- 主要显义来源。
- 是否找到了最早来源。
- 引用和词源分析是否都有可验证来源；没有时，说明哪些内容暂时没有资料。
- 哪些想比较的双链词还没有笔记。
