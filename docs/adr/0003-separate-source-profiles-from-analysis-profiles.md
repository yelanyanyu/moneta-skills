# Separate source profiles from analysis profiles

Moneta will keep `SOURCE-*` files as compact lists of places to search, and add `ANALYSIS-*` files for language-specific ways of interpreting an entry after sources are found. This separates the question "where do we look?" from "how do we understand what we found?", which matters because Chinese words, German compounds, English borrowings, and future language families cannot all be handled by the same Indo-European root-analysis habit.

**Consequences**

`word-disclosure` should read both a source profile and an analysis profile for the entry's first-class disclosure language. Analysis profiles should stay short and question-driven; they are not full grammars, etymology textbooks, or style guides.
