# Moneta Skills

Moneta Skills 是一组面向语言学习者和教师的 agent skills，用来生成、质疑和改进各个语言词语解析 markdown 笔记。让你按照自己喜欢的方式来逐渐改进单词的解析。

## Skills

Bundled skills live under `skills/<skill-name>/SKILL.md`.

- `/ask-yanyu`：路由 skills。选择下一步。首次使用、生成单词笔记、质疑、改进都从这里开始。
- `/setup-moneta-skills`：初始化一个项目里的 Moneta 工作区。
- `/word-disclosure`：生成或更新 `word/` 目录下的所有单词 markdown 笔记。
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

该 skills 可以通过以下命令安装，需要安装 npm：

```bash
npx skills@latest add yelanyanyu/moneta-skills
```

维护者本地开发可以用 `scripts/list-skills.sh` 检查技能清单。`scripts/link-skills.sh` 只用于维护者把当前 checkout 软链接进本机 agent skills 目录，不是用户安装方式。

## Status
基本完成了对汉语、英语、德语的词语解析。

当前项目还有 `phrase-disclosure` 和 `write-review`，因为 `/setup-moneta-skills` 待开发。现在的计划主要是完善单个单词的解析。欢迎语言学、哲学专业的研究者或者一线教师参与贡献。
