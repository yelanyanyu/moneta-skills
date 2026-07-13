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

**First-Class Disclosure Language**:
A language that `word-disclosure` supports as a primary entry language with its own note directory, source profile, and output conventions. The initial first-class disclosure languages are English, German, and Chinese.
_Avoid_: supported language, target language

**Source Language Profile**:
A compact reference file that lists dictionaries, corpora, literary sources, and textual traditions to search for one language. Source language profiles should list sources, while the shared `SOURCES.md` router keeps the brief search strategy and decides which profiles to read.
_Avoid_: source file, language sources

**Source Index**:
The shared `SOURCES.md` router for disclosure work. It identifies the entry language, points to the relevant source language profiles, and keeps cross-language search strategy brief enough that individual profiles do not become workflow documents.
_Avoid_: source profile, source file

**Disclosure Analysis Profile**:
A compact reference file that describes how to analyze an entry after sources are found for one language family, script tradition, or philological tradition. Analysis profiles ask language-specific questions; they do not replace source profiles.
_Avoid_: source profile, language method dump

**Philological Path**:
The interpretive route that best fits an entry, such as etymological lineage, character exegesis, allusion, institutional usage, translation-term history, or compound structure. A philological path is chosen per entry instead of assuming every language should follow Indo-European root analysis.
_Avoid_: universal etymology method, word root path

**Auxiliary Source Language**:
A language consulted for etymology, historical background, or source-text verification without being a primary note language. Latin, Ancient Greek, and French can be auxiliary source languages even when the generated note is English, German, or Chinese.
_Avoid_: secondary language, helper language

**Chinese Disclosure Coverage**:
The Chinese first-class disclosure language covers single characters, Classical Chinese words, and modern Chinese words. `SOURCE-ZH` must support all three instead of treating Chinese as only modern vocabulary.
_Avoid_: modern Chinese only
