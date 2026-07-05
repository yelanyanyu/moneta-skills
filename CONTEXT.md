# Moneta Skills

Moneta Skills is a publishable skill package for Chinese-speaking English learners. It keeps reusable agent workflows separate from any one app repository.

## Language

**Skill Package**:
A Git repository prepared for skills.sh installation, with bundled skills and references arranged as the public distribution boundary.
_Avoid_: prompt repo, local skill copy

**Bundled Skill**:
A skill shipped inside this repository under `skills/<name>/SKILL.md`, including any reference files it needs.
_Avoid_: generated skill, setup-created skill

**Setup Skill**:
The bundled skill that checks whether Moneta skills are installed and initializes a user project for Moneta outputs.
_Avoid_: installer, repair script

**Disclosure Skill**:
A Moneta skill that creates Obsidian Markdown notes explaining English words or phrases through concrete literary and artistic scenes.
_Avoid_: vocabulary prompt, word generator
