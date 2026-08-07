---
name: 05-educational-clarity-writing
description: Write clear, educational blog explanations using plain-language principles, readability-formula mechanics and their documented limits, cognitive load theory, and worked-example/analogy teaching patterns. Apply when drafting or reviewing a post whose primary job is to teach a concept, process, or skill.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Educational Clarity Writing

Apply [`../00-blog-writing-guardrails/SKILL.md`](../00-blog-writing-guardrails/SKILL.md) first; its gates apply to every post before the guidance below.

## 1. Plain-language foundation
- Organize the explanation around the reader's task ("how do I do X," "what does X mean for me"), not around the writer's own expertise or the order the writer learned the material. [DIGITALGOV-PLAIN-01]
- Use short sentences and everyday words by default; introduce a technical term only when the concept has no everyday equivalent, and define it the first time it appears. [DIGITALGOV-PLAIN-01]
- A plain-language pass must not delete technical precision the target audience actually needs; simplify wording, not the substance of the claim. [DIGITALGOV-PLAIN-01]

## 2. Readability-formula mechanics and limits
- The Flesch Reading Ease and Flesch-Kincaid Grade Level formulas estimate difficulty from sentence length and syllables per word, calibrated against reader comprehension test data; treat a grade-level score as an approximation of decoding difficulty, not a certificate of comprehension. [NAVY-READABILITY-01]
- Because the formulas were derived and calibrated on average sentence and word length statistics against one test population, do not treat a target score (e.g. "grade 8") as sufficient proof a specific audience will understand the post; a passage can score low on grade level while still being conceptually dense, ambiguous, or jargon-heavy. [NAVY-READABILITY-01]
- Use a readability score only as one editing signal alongside direct reader testing or subject-matter review, and re-verify long or restructured sentences by reading them aloud, not by chasing a numeric target alone. [NAVY-READABILITY-01][DIGITALGOV-PLAIN-01]

## 3. Cognitive load gate
- Working memory that processes new information is limited; when the intrinsic difficulty of the material plus the way it is presented exceeds that capacity, learning fails even though every individual fact was stated correctly. [SWELLER-COGLOAD-01]
- Reduce load the presentation itself adds: do not force the reader to hold an undefined term, an unresolved forward reference, or a separated diagram-and-caption pair in memory while decoding a sentence. [SWELLER-COGLOAD-01]
- Sequence a teaching post from the smallest complete sub-concept to the next, adding one new element at a time rather than introducing several interdependent concepts in the same paragraph. [SWELLER-COGLOAD-01]

## 4. Worked examples and analogies
- Prefer showing a fully worked example of a procedure over stating the abstract rule alone; studying a complete worked solution builds a reusable mental schema more reliably than solving from the rule with no modeled example, especially for a reader new to the topic. [SWELLER-COGLOAD-01]
- When an analogy is used to introduce an unfamiliar concept, state explicitly where the analogy holds and where it breaks down; an unqualified analogy transfers the reader's assumptions from the familiar domain into the new one, including the assumptions that do not apply. [DIGITALGOV-PLAIN-01]
- Pair each worked example with a smaller, near-transfer practice case the reader can check themselves before moving to a novel or compound problem. [SWELLER-COGLOAD-01]

## 5. Pre-publish clarity QA
- Confirm a first-time reader in the target audience can restate the core concept in their own words after reading only the post; if a technical reviewer is the only person who can do this, the draft is not yet reader-ready. [DIGITALGOV-PLAIN-01]
- Confirm every newly introduced term is defined before its second use, every worked example resolves to a stated result, and every analogy's stated limits still appear in the published draft. [DIGITALGOV-PLAIN-01][SWELLER-COGLOAD-01]
