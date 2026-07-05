# Moneta Skills

Moneta Skills 是一组面向中文学习者的 agent skills，用来生成、质疑和改进英语词语解析笔记。

这些 skills 不依赖 Ad Fontes Manager 桌面应用。它们把单词解析结果保存为 Obsidian Markdown，并用文学或艺术作品帮助读者进入词义。

## Skills

- `/ask-yanyu`：选择下一步。首次使用、生成单词笔记、质疑怪句、改进 skills 都从这里开始。
- `/setup-moneta-skills`：初始化一个项目里的 Moneta 工作区。
- `/word-disclosure`：生成或更新 `word/` 目录下的英语单词 Obsidian Markdown 笔记。
- `/moneta-critique`：当用户觉得某段内容怪、不自然、AI 味重时，把问题追问成可确认的修改规则。
- `/moneta-skills-improver`：把确认后的反馈反哺到 Moneta skills，并维护纠错样本。

## First Use

在一个新项目里，先运行：

```text
/setup-moneta-skills
```

如果只是想知道该用哪个 skill，运行：

```text
/ask-yanyu
```

## Install

发布到 skills.sh 后，预期安装方式为：

```bash
npx skills add yelanyanyu/moneta-skills
```

## Status

当前优先完善英语单词解析。`phrase-disclosure` 和 `write-review` 会在规则稳定后再加入。
