# `writing-dna-skill` 调研：对 Moneta 论述文风格校准的启发

> 调研日期：2026-07-22  
> 资料范围：只阅读 `larashero3-dotcom/writing-dna-skill` 仓库的 README、`SKILL.md`、中文详述 skill、模板和 format-only 示例。以下“仓库事实”均附该仓库的一手链接；“Moneta 建议”是结合本项目现有文件后的设计判断。

## 先说结论

`writing-dna-skill` 最值得借鉴的不是多写一份抽象风格说明，而是把“范文”处理成一个可复查的语料库，再将风格拆成“语言、篇章结构、选题/材料、认知框架、呈现”几个层次，最后整合成一个写作前可重读的入口。仓库明确要求提炼“可操作的规则集”，而不是摘要；其入口 skill 还要求写作前重新读取全部风格文档，并在输出不像时按各层文档逐项自检。[`SKILL.md`](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/SKILL.md) · [`写作蒸馏器.skill.md`](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md)

这正好补上 Moneta 当前“`STYLE.md` 指向一篇范文，但没有把多篇 `asset` 论述文的稳定共同点登记出来”的空隙。建议保留 `STYLE.md` 的最后路由职责，把 `asset` 作为中文论述文语料，另做一套轻量的 `Writing-DNA` 资料；生成单词笔记时，先完成来源、分析和格式，最后才按 `STYLE.md` 读取目标语言范文，再读取与任务匹配的 DNA 片段。不要把 DNA 变成新的硬模板，也不要让它覆盖词源、引文和事实边界。

## 一、仓库本身采用了什么架构

### 1. “风格”被拆成六个层次

仓库把风格分为：L1 表层语言（词频、句长、标点、修辞）；L2 文章结构（开头 hook、正文架构、结尾）；L3 选题逻辑；L4 素材策略；L5 认知框架；L6 视觉风格。它把 L1-L2 概括为“怎么写”、L3-L5 概括为“怎么想”、L6 概括为“怎么呈现”，并强调只模仿语言会“读着像但想法不像”。[六层定义与原则](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#二蒸馏的六个层次)

**对 Moneta 的映射：**

| `writing-dna-skill` 层次 | `asset` 论述文中要观察的对象 | 对 `word-disclosure` 的作用 |
| --- | --- | --- |
| L1 语言 | 句长交替、第一/第二人称、口语插入、引号/括号/破折号、段落密度 | 控制正文的表面文气，不强行替换词源术语 |
| L2 结构 | 从一个具体误读或问题进入，给出反例，再回到词源/原文，最后回扣学习或理解 | 作为“论述段落的推进顺序”参考，而非每个词都套同一故事 |
| L3 选题 | 为什么从这个学习困惑、词义冲突或原著问题切入 | 帮助选择解释入口，避免开头直接抛抽象定义 |
| L4 材料 | 原文、译文、词源、古籍/作品、例句各自承担什么证明或展示任务 | 让文学材料成为论证的一部分，同时保持来源可核验 |
| L5 认知 | 对“词典标签”“语境”“意义如何成形”等反复出现的判断 | 让解释保留项目自己的问题意识，而不是只复制句式 |
| L6 呈现 | 标题层级、引用块、脚注、分段留白；当前 `asset` 以 Markdown 为主 | 约束 Obsidian 笔记的阅读节奏；图片层可暂不启用 |

### 2. 先做语料和元数据，再做风格归纳

仓库要求至少准备 20 篇完整文章，放入 `raw/` 或 `raw-corpus/`；每篇文章在 `_meta/` 记录标题、日期、作者/账号、文章类型、主题标签、hook 类型、结构模式、材料来源、字数和特殊特征，并明确说元数据不可跳过。[语料要求与工作流](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/SKILL.md#corpus-requirements) · [元数据字段](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#step-2元数据标注_meta目录)

当前项目 `asset/` 下有 15 篇 Markdown 论述文（其中有修订版和同主题文章），尚未达到该仓库所建议的 20 篇。因此第一版只能称为“中文论述文风格初稿”，不能把偶然习惯晋升为全局规则。补足语料时应优先加入用户认可、类型不同的论述文，而不是用重复版本凑数。

### 3. 输出拆成多个可按需加载的文件

推荐目录包含 `_meta/`、`语言DNA.md`、`文章结构模板.md`、`写作视角与认知框架.md`、`视觉风格指南.md` 和最终入口 `Writing-DNA.md`。模板仓库把这些文件作为空白骨架，`Writing-DNA.md` 只保留六个聚合栏目，便于写作前快速重读。[作者语料模板](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/templates/author-corpus/README.md) · [`Writing-DNA.md` 模板](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/templates/author-corpus/Writing-DNA.md)

这比把所有抽象描述堆进 `STYLE.md` 更适合 Moneta：`STYLE.md` 只按语言索引具体范文；DNA 文档按需提供共同规律；范文自身仍是最后的正面校准材料。

### 4. 结构和“怎么想”不能由词频统计代替

仓库对 L1 允许脚本统计词频、句长、短长句比例、段落句数、标点比例和标题长度；但 L2 要人工标注“开头 hook → 第一转折/问题 → 正文结构 → 结尾处理”，L3-L5 则明确说需要深度阅读、无法用脚本替代。[L1 指标](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#step-3脚本分析l1-表层语言) · [L2 结构标注](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#step-4结构标注l2-文章结构) · [L3-L5 深读](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#step-5选题与认知框架归纳l3-l5)

这与本项目的经验一致：`陈述` 之所以像目标文风，不是因为某几个高频词，而是因为它把《宫山僧》的原文、译文、解释和近义词比较按“可追问、可查验”的方向推进。[`word/zh/陈述.md`](../../word/zh/陈述.md) · [`references/templates/陈述.md`](../../skills/word-disclosure/references/templates/陈述.md)

### 5. 视觉层只在材料确实承载论证时启用

仓库提醒截图、评论、表格和对话图片可能是证据链的一部分，要求图文文章抽样查看图片内容，而不是把图片当装饰；同时允许仅有 Markdown 时从标题、加粗、引用和图片标记提取排版规律。[图片跨层原则](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#跨层原则图片内容必须纳入分析) · [视觉分析方法](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#step-6视觉风格与排版分析l6)

`asset` 当前是以 Markdown 为主的论述文，没有必要为了“完整六层”虚构图片规范。第一版只记录标题、引用块、脚注、加粗和留白；以后若 `asset` 出现截图或图表，再把图片作为 L4 证据和 L6 呈现一起分析。

## 二、对当前 Moneta 文件布局的具体映射

### 1. 现有文件各自负责什么

| 当前文件 | 继续保留的职责 | 不应新增的职责 |
| --- | --- | --- |
| [`skills/word-disclosure/SKILL.md`](../../skills/word-disclosure/SKILL.md) | 执行顺序、来源/格式/错误索引路由 | 不塞入完整中文文风规则 |
| [`skills/word-disclosure/references/STYLE.md`](../../skills/word-disclosure/references/STYLE.md) | 最后读取；按一等语言指向具体文章 | 不改成抽象 profile 或禁词清单 |
| [`skills/word-disclosure/references/templates/`](../../skills/word-disclosure/references/templates/) | 存放语言模板/范文副本 | 不把所有 `asset` 原文复制进每次上下文 |
| [`asset/`](../../asset/) | 中文论述文语料和用户认可的写作资产 | 不直接当作无条件硬规则 |
| [`word/zh/`](../../word/zh/) | 词条成品和可供复读的具体分析 | 不把每篇词条的偶然题材当作通用模板 |

### 2. 建议的最小目录（只新增资料，不改变业务流程）

```text
skills/word-disclosure/references/
├── STYLE.md                         # 语言 → 具体范文的最后路由
└── templates/
    ├── README.md
    ├── zh/
    │   ├── 陈述.md                   # 已确认的单篇范文（可保留现有副本）
    │   └── 论述文-DNA.md              # 从 asset 语料归纳的中文论述文 profile
    └── _meta/
        └── asset-zh.json             # 每篇 asset 的类型、结构、材料等元数据
```

这里的 `论述文-DNA.md` 是建议名称，不要求本次立即创建。若未来建立多个语言语料，应在 `templates/` 下按语言分目录，符合当前 `STYLE.md` 的语言索引思路；`STYLE.md` 只登记入口链接，具体规则放到 DNA 文档，避免索引再次膨胀。

### 3. `STYLE.md` 的调用顺序不变，但读取对象增加一层

当前 `word-disclosure` 已规定：先读分析、来源、格式；信息搜集完成后最后读 `STYLE.md`，再解析当前语言范文。[`SKILL.md` 工作流程](../../skills/word-disclosure/SKILL.md)

建议把最后一步细化为：

1. 读取 `STYLE.md`，按目标语言找到范文入口。
2. 读取该语言的 `论述文-DNA.md`（若存在），只取与本次词条相匹配的结构/语气模块。
3. 读取 `STYLE.md` 指向的一篇具体范文；它负责“让模型看到成品如何展开”，DNA 负责“提醒哪些倾向可迁移”。
4. 生成正文；不要照抄范文的故事人物、意象、句子或论证结论。
5. 按现有 `ERROR_INDEX.md` 自检，再增加一项“是否仍像论述文资产而不是抽象说明书”的轻量复检。

换言之，DNA 是路由后的辅助上下文，不能提前参与事实搜集，也不能替代原文、词源或字形依据。

## 三、如何从 `asset` 论述文蒸馏出可用规则

### L1：记录倾向，不做禁词表

外部仓库建议记录高频名词/动词/副词、平均句长、短长句占比、段落平均句数、标点比例、小标题长度和中英文混用。[语言 DNA 产物说明](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/templates/author-corpus/%E8%AF%AD%E8%A8%80DNA.md)

迁移到中文论述文时，建议写成“常见倾向 + 适用条件 + 反例”，例如：

- 经常在抽象判断前插入一个可感知场景或可翻译的例句；不是每个段落都必须写故事。
- 长句用于把问题的来路、限制和转折连在一起；短句用于落地、反驳或回扣，不把全文切成同一长度。
- 第一人称可以承担“我如何读到这个问题”的经验位置，但不自动增加“我认为”“我们可以”等口头禅。
- 引号、括号、破折号、脚注分别服务于术语、补充、停顿和来源，不按数量机械模仿。

### L2：把“论证推进”单独登记

外部模板把结构记录为 hook、第一转折、正文架构、结尾处理，甚至按内容类型给出不同模板，并以“自然收束、无刻意升华”作为一种合法结尾。[结构模板示例](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#step-4结构标注l2-文章结构)

`asset` 的初步结构标签可以从以下候选开始，最终以多篇文章交叉验证为准：

```text
具体困惑/误读
→ 例句或原文展示问题
→ 先承认直译/词典标签为什么失效
→ 引入词源、语境或原著材料
→ 构造一个能让意义显现的场景
→ 回到最初例句或词语，说明它为何在此处被召唤
→ 保留余地的收束（体验、回读或开放问题）
```

这是对 `asset` 论述文的待验证假设，不是 `word-disclosure` 的硬模板。遇到纯字形辨析、短语比较或来源考据时，可只借用其中一段推进方式。

### L3-L5：把“怎么想”与“怎么说”分开

仓库把选题时机、切入角度、材料偏好、权威对象、争议信息处理、核心假设和反复命题放在“写作视角与认知框架”中，而不混入句式清单。[写作视角与认知框架模板](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/templates/author-corpus/%E5%86%99%E4%BD%9C%E8%A7%86%E8%A7%92%E4%B8%8E%E8%AE%A4%E7%9F%A5%E6%A1%86%E6%9E%B6.md)

对 Moneta 而言应登记三类可迁移判断：

1. **问题意识：** 从读者真实的误读、翻译不通或概念冲突进入，而不是先宣布抽象定义。
2. **材料观：** 原文、译文、词源和文学场景不是平行装饰；每一项都要说明它在理解链条中承担什么作用。
3. **解释姿态：** 允许依据不足时放轻语气；不把《说文》、词源学或单一译法当教条，也不靠无来源的宏大解释填空。

这些是与 `moneta-critique` 反馈相容的风格资产：它们约束论述如何展开，却不会把事实核验让位给文气。

### L6：先做 Markdown 排版 DNA

由于当前 `asset` 没有稳定的图片资产，第一版可以只记录 Markdown 层的标题、引用块、脚注、加粗、空行和段落长度。外部仓库也明确允许从 Markdown 标记提取排版规律，而不是强行使用 HTML 或图片分析。[Markdown 排版提取](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#提取方法)

## 四、写作时怎样使用，才能更贴近范文而不变成仿写腔

### 推荐的两层上下文

`Writing-DNA.md` 适合给模型快速重读；具体范文适合在起草前提供成品证据。外部仓库也要求写作前重读 `Writing-DNA.md`、语言、结构、认知和视觉文档，而不是只在首次蒸馏时读取。[写作时重读风格文档](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/SKILL.md#writing-with-a-distilled-style)

在本项目里应这样组合：

```text
已核验的词语信息
  + 当前语言的论述文 DNA（可迁移倾向）
  + STYLE.md 指向的一篇具体模板（成品参照）
  + 当前词条需要的原文/译文/脚注
→ 起草
→ 错误索引自检
→ 文气复检：推进是否具体、材料是否真正参与解释、结尾是否过度升华
```

### 必须保留的“反模仿”边界

- 不复制模板中的人物、地点、比喻、故事冲突或句子骨架；只迁移它们如何进入问题、如何安排材料。
- 不为了像 `asset` 而每个词都制造一段陶器、集市或古籍故事；若来源材料不支持场景，就回到来源搜集或用平实说明。
- 不把高频词、长句比例或标点频率当成通过条件；它们只是诊断线索。
- 不把一篇词条的事实性判断提升为所有词条的认知框架；规则需要多篇语料支持。
- 不让“更像”压过来源可靠性、译文自然度和当前词语的真实差异。

## 五、质量检查与落地优先级

仓库给出的质量标准包括：至少三种内容类型的结构覆盖、至少三条非显而易见的核心命题、元数据覆盖 80% 以上语料、视觉分析覆盖三个维度，以及 `Writing-DNA.md` 控制在 4000 字以内。[质量标准](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/%E5%86%99%E4%BD%9C%E8%92%B8%E9%A6%8F%E5%99%A8.skill.md#五质量标准)

Moneta 可采用较小的版本：

1. **先标注语料：** 为 15 篇 `asset` 建立 `_meta`，记录文章类型（语言学习/原著精读/经验说明）、hook、结构、材料来源和字数；把修订版标为同一主题的不同版本。
2. **再做两份核心资料：** `语言DNA.md` 与 `文章结构模板.md`；L3-L5 可先合并为 `写作视角与认知框架.md`，视觉暂只写 Markdown 排版。
3. **最后做入口：** `论述文-DNA.md` 控制在 4000 字以内，只保留经多篇文章支持的倾向、适用条件和反模式；`STYLE.md` 仍只负责按语言索引范文。
4. **用对照样本回归：** 同一词语分别用“旧 STYLE”“单篇模板”“DNA + 单篇模板”生成，盲看哪一份更接近 `asset` 的论述推进且没有复制题材；将用户选择的版本和反例加入模板目录。
5. **规则晋升要谨慎：** 只有在不同类型文章中反复出现、并且不会伤害来源准确性的规律，才写入长期 DNA；一次漂亮的句子只保留为范文，不升级为规则。

## 六、边界与不直接照搬的部分

仓库自己区分“format-only”目录和真实蒸馏，并提醒不要把未经授权的第三方原文放进公共仓库。[format-only 示例](https://github.com/larashero3-dotcom/writing-dna-skill/tree/main/examples/format-only) · [版权边界](https://github.com/larashero3-dotcom/writing-dna-skill#重要边界)

因此本项目更适合：

- 将用户自己的 `asset` 作为内部语料，不把外部作者文章复制进 skill；
- 在 `references/templates/` 保存用户确认过的模板或必要副本，并由 `STYLE.md` 索引；
- 在 DNA 文档中写“倾向/条件/反模式”，不写成“所有文章都必须如此”；
- 把词源、原文和脚注的真实性放在风格之前，避免为了追求像而生成无依据的故事或解释。

**最终判断：** `writing-dna-skill` 可以作为 Moneta 的“范文资产化”和“论述推进抽取”参考，但不宜整体替换现有 `STYLE.md`。最小有益改造是：为 `asset` 建立带元数据的中文语料层，输出一份精简 `论述文-DNA.md`，让 `STYLE.md` 在信息搜集完成后同时加载“DNA 倾向 + 一篇具体范文”，并保留来源核验与错误自检作为更高优先级。
