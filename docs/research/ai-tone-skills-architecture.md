# 去 AI 味 skills 架构调研

> 调研日期：2026-07-19。本文研究写作审改和文风校准架构，不把“像 AI”当作作者身份检测。

## 结论

Moneta 不应照搬一个更长的“AI 痕迹清单”。它现有的优势是已经把发现问题、执行审改和沉淀规则拆成不同动作；下一步应把散落在各业务 skill 中的通用中文坏味提取为共享内核，再补上误报保护、正面文气校准和可回归验证。

建议目标结构是：

```text
ask-yanyu（路由）
  → moneta-critique（把主观不适诊断成候选规则）
  → prose-critique-zh / word-disclosure / 未来 write-review（任务适配器）
       → shared prose kernel（通用错误索引、纠错样本、保留规则）
       → domain extension（词源、引文、翻译、来源等领域规则）
       → STYLE 索引（按一等语言读取用户认可的具体文章）
       → residual audit（改写后的残留坏味复检）
  → moneta-skills-improver（确认、归类、验证、晋升为长期规则）
```

## 外部方案

### blader/humanizer：完整单体规则库

`humanizer` 把触发说明、33 类模式、正反例、误报说明、处理流程和输出格式放在一个 `SKILL.md` 中。最新版最值得借鉴的不是模式数量，而是两个质量闸门：先说明哪些现象不能单独作为 AI 证据、哪些人类写作信号应保留；完成第一稿后，再专门检查残留的 AI 痕迹并二次改写。

它也支持用用户提供的两三段文字校准声音。这个方向和本项目 `STYLE-TMP.md` 的“范文负责文气，规则负责边界”一致。

局限也明显：单文件很长，每次调用都承受完整上下文；部分硬规则（例如一律删除破折号）虽然便于执行，却容易误伤作者习惯和特定文体。

来源：[blader/humanizer SKILL.md](https://github.com/blader/humanizer/blob/main/SKILL.md)、[README 与 voice calibration](https://github.com/blader/humanizer/blob/main/README.md)

### hardikpandya/stop-slop：短入口加分类 reference

`stop-slop` 的入口只有八条核心规则和一组交付前检查，把词语表与句式结构分别放在 `references/phrases.md`、`references/structures.md`。这比 `humanizer` 更符合渐进式披露：入口负责过程和硬约束，细节按问题类型读取。

它的问题是规则过于绝对，例如删除全部副词、全部被动语态和全部破折号。这种方案适合追求强烈统一文风的英文短文，不适合作为 Moneta 的通用中文底座。中文文学、评论、语文学说明需要保留文体差异，不能把“去 AI 味”做成统一的削平器。

来源：[stop-slop SKILL.md](https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md)、[phrases.md](https://github.com/hardikpandya/stop-slop/blob/main/references/phrases.md)、[structures.md](https://github.com/hardikpandya/stop-slop/blob/main/references/structures.md)

## 文风与文笔模仿方案

只做负面清理会把文本推向“没有明显坏味，但也没有作者”的中间态。常见的正面模仿 prompt 大致分成三类。

### 直接 few-shot：给几段样文后要求照此写

这是最常见、成本最低的提示词：提供三到五段作者原文，让模型分析句长、语气、正式程度、开头和结尾，再试写一段确认。它能迅速改善默认文风，却有三个风险：样本过少会把题材特征误认成文风；模型容易复用显眼词汇和句子骨架；单一文体样本无法说明作者在邮件、评论、叙事中的变化。

因此，Moneta 可以把它用于一次性的轻量任务，不宜直接把这种平面 prompt 当成长期架构。

### voice calibration：跨情境采样后生成持久 profile

`voice-calibration-plugin` 不要求用户先准备完整文章，而是给出 6–12 个写作题，覆盖微型故事、意见、随手消息和描述等至少四类情境。随后按句式、词汇、语气、标点、叙事、会话标记和文化标记七个维度分析，生成 `.voice-profile.md`，让用户确认后再保存。应用阶段只读取 profile，不必反复加载全部样本。

这个方案最值得 Moneta 借鉴的是“校准”和“应用”分成两种模式，以及 profile 必须经过用户确认。它还强调样本应跨 register，`What to Avoid` 与正面特征同样重要。

来源：[voice-calibration SKILL.md](https://github.com/raulpetruta/voice-calibration-plugin/blob/main/skills/voice-calibration/SKILL.md)、[项目说明](https://github.com/raulpetruta/voice-calibration-plugin)

### voice profile extraction：先抽取可迁移特征，再写

一份较完整的 Voice Profile Extraction Prompt 要求至少五篇长文，并从篇章结构、句子节奏、情感姿态、思想框架、语域和回避模式中寻找重复证据。它有几条很适合 Moneta：

- 每项特征至少由多个样本支持，不能凭一处现象概括作者；
- 描述“倾向”，不把样本结构变成硬模板；
- 语言规则写类别和语域，不生成供模型机械插入的口头禅表；
- 条件式元素同时说明何时使用、何时不用；
- 用 anti-pattern 防止“像得过头”或只学到表面标记。

来源：[Voice Profile Extraction Prompt](https://gist.github.com/roelven/53d497d4361f7c938533dee06e1a4fa4)

### thinking-style skills：模仿推进方式，不模仿口癖

`article-writing-skills` 明确把目标定义为借用作者的思考框架：先注意什么、删掉什么、如何用类比建立直觉、怎样把材料排成解释顺序，而不是复制句长、常用词或口头禅。`steal-a-writing-voice` 则要求从长文、短文、代码文档和口语转录等不同表面搜集一手样本，用原句为每条机械规则提供证据，并允许项目自己的 house rules 覆盖作者习惯。

对 Moneta 而言，这提示我们把“文气”再拆成两层：

1. **思路与篇章推进**：从具体困惑进入、如何引入原文、怎样从例子走向判断；
2. **表面声音**：句长、停顿、标点、第一人称、口语程度。

前者可以跨题材稳定迁移，后者需要按文体和输出表面调整。只模仿后者最容易产生仿写腔。

来源：[article-writing-skills](https://github.com/IrtezaAsadRizvi/article-writing-skills)、[steal-a-writing-voice](https://gist.github.com/ximihoque/2c681f091887795238b05c2f07224d01)

### context profile 与 voice profile 正交

`avoid-ai-writing` 把“写给谁、写什么”与“像谁说话”作为两个独立轴：context profile 决定文档、技术博客、邮件等场景需要多严格；voice profile 决定 casual、professional、technical、warm 等声音。用户已经提供原文时，应优先从原文推断声音，而不是强加一个预设 persona。

Moneta 也应采用这个分离：`word-disclosure` 的来源、格式和分析路径属于 context；用户范文或项目文风属于 voice。两者不能继续混在同一个 `STYLE.md` 里。

来源：[avoid-ai-writing SKILL.md](https://github.com/conorbronsdon/avoid-ai-writing/blob/main/SKILL.md)

## Moneta 当前架构

### 已经做对的部分

1. `ask-yanyu`、`moneta-critique`、`moneta-skills-improver` 已经构成“路由—诊断—沉淀”的反馈链。尤其是“用户未确认前不写长期规则”和“新增规则门槛要高”，能防止单个坏句污染全局规范。
2. `prose-critique-zh` 使用 `ERROR_INDEX.md → 命中的 CORRECTIONS 小节`，比外部单体 Humanizer 更节省上下文，也更容易扩展。
3. `word-disclosure` 把通用文风检查放在生成之后，并把来源、翻译、词源等问题纳入领域错误类型。这说明本项目已经认识到：AI 味不只是高频词，还可能来自画面、人物动机、来源边界和诠释方法。
4. `STYLE-TMP.md` 已收束为“按一等语言索引具体文章 + 少量硬边界”。它比纯禁词表更接近稳定的正面风格控制，也避免把用户认可的分析再次翻译成复杂抽象规则。

本地来源：`skills/ask-yanyu/SKILL.md`、`skills/moneta-critique/SKILL.md`、`skills/moneta-skills-improver/SKILL.md`、`skills/prose-critique-zh/SKILL.md`、`skills/word-disclosure/SKILL.md`、`STYLE-TMP.md`。

### 当前断点

1. **通用规则重复。** `prose-critique-zh` 的 14 个纠错类型全部也存在于 `word-disclosure/references/CORRECTIONS.md`。同一问题有两个事实来源，后续必然出现修正不同步和样本沉积。
2. **路由没有闭合。** `ask-yanyu` 仍把写作审查指向尚不存在的 `write-review`，没有把已经存在的 `prose-critique-zh` 接进用户路径。
3. **缺少误报保护。** 当前规则说明了要保留原用途和原语气，但尚未形成与错误索引对称的 `PRESERVE.md` 或等价章节。单个破折号、抽象词、长句或文学意象不应自动判为 AI 味；应看多个坏味是否聚集，以及它们是否真的破坏当前文本。
4. **缺少明确的残留复检。** 现有流程有草稿后自检，但没有要求审改 skill 对“改写结果”再做一次独立诊断。外部 Humanizer 的二次审校值得吸收，但输出不必把中间草稿都展示给用户。
5. **反馈沉淀缺少回归证据。** `moneta-skills-improver` 能分类和压缩规则，却没有要求新增规则通过一组正例、反例与保留样本。现在的范文实验只在 `STYLE-TMP.md` 中提出，尚未成为通用晋升门槛。

普通用户意图还需要进一步分流：要求“直接改、润色、去 AI 味”时应进入审改执行；质疑“这句哪里怪、为什么这样写”时才进入反馈澄清；明确“以后都要避免”时再进入规则治理。`moneta-critique` 的一次一问适合采集反馈，不应成为所有普通改写的前置访谈。

## 建议的目标架构

### 1. 建立共享中文 prose kernel

把 14 个通用类型及其样本迁到一个权威位置，例如 `skills/prose-critique-zh/references/`，其他 skill 只保留领域扩展并指向共享内核。不要再复制同名小节。

共享内核至少包含：

- `ERROR_INDEX.md`：症状到错误类型的短索引；
- `CORRECTIONS.md`：按错误类型组织的负面样本；
- `PRESERVE.md`：误报、作者特征和不得误伤的内容；
- `STYLE.md`：按英语、德语、汉语分类，直接索引用户认可或亲自修改过的具体文章，并保留极少量硬边界。

正面文气不再先提炼成一份抽象 profile，也不按原文带动、故事改写、词源分析等写法建立一级分类。更合适的是：

- `STYLE.md`：先按词目的一等语言分流，再指向该语言下的具体文章；
- 具体文章：直接展示分析如何发生，保留文章身份和完整上下文；
- 写法标签：只解释为什么此时应读这篇文章，不成为新的抽象风格说明；
- 少量硬边界：约束准确性、来源身份和不得复制当前文章的意象、人物或句子骨架。

### 2. 让业务 skill 只保留领域增量

`word-disclosure` 继续拥有词源、中文释义、原文与改写、文本细读、近义词等错误类型。它的执行顺序可以是：先跑通用 prose kernel，再跑 word disclosure extension。未来的 `write-review`、`phrase-disclosure` 也采用同样组合方式。

这样能同时满足单一事实来源和按需加载：共享规则只维护一次，领域规则仍贴近领域 skill。

### 3. 把审改变成“诊断—修复—复检”三段

每次执行应有可检查的完成标准：

1. 诊断：只标记有上下文证据的错误类型，避免孤立词触发；
2. 修复：保留含义、用途、叙述视角和作者可辨认的习惯；
3. 复检：重新检查改写结果，确认旧问题已消失、没有引入新口号或把文章削平。

对用户仍可只交付最终文本和最关键的说明，不必暴露内部三段过程。

### 4. 给规则晋升增加小型回归集

每个准备长期化的新规则至少附三类样本：

- 应命中的坏例；
- 不应命中的相似正例；
- 修改后仍应保留的作者特征或文体特征。

规则只有在多个题材、至少两个文体上没有明显误伤，才从候选反馈晋升到共享索引。领域专属问题只在对应 extension 中验证，不要求全局适用。

文章索引的验证不要只看“像不像”。更合适的是盲测三份结果：旧规则、当前语言下的一篇具体文章、当前语言下的多篇索引文章，让用户在不知道配置的情况下选出更自然、最像自己、又没有照搬题材的一份。Anthropic 的 skill-creator 也把主观输出交给定性比较，并建议比较有 skill 与基线结果，而不是强行把所有文风维度变成机械断言。

来源：[Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)

### 5. 先修路由，再做大重构

优先级建议：

1. 让 `ask-yanyu` 正确路由到 `prose-critique-zh`；
2. 定义共享错误类型的唯一归属，消除 14 个重复小节；
3. 增加误报保护和残留复检；
4. 用 `STYLE-TMP.md` 提出的“旧规则／单篇具体文章／同语言多篇文章”做小规模对照实验；
5. 最后再决定是否需要独立的 `write-review` 外壳。

## 不建议直接移植的做法

- 不以“命中某个词”为判定标准，必须结合句子功能和坏味聚集。
- 不全局禁用副词、被动语态、破折号、三项列举或第一人称。
- 不把“更口语、更短、更具体”当作所有文体的共同终点。
- 不用单一总分代替诊断。评分看似客观，但如果没有稳定评测者和基准文本，很容易制造虚假的确定性。
- 不继续给每个业务 skill 复制一份通用纠错库。
