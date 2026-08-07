---
name: 13-editing-style-voice
description: Line-edit and self-edit a blog post draft — cut filler and hedging, remove AI-tell phrasing, keep voice consistent, and prefer active constructions — with a pre-publish editing checklist. Apply after ../00-blog-writing-guardrails/SKILL.md, during the editing pass before a post is marked reader-ready.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Editing for Style and Voice

Apply `../00-blog-writing-guardrails/SKILL.md` first; its hard gates (originality, accuracy, E-E-A-T, accessibility, plain language, structured data, pre-publish QA) apply to every draft this skill line-edits.

## 1. Reader-task and plain-language gate
- Organize each paragraph around what the reader needs to do or know next, not around the writer's own train of thought; lead with the point, not the setup. [DIGITALGOV-PLAIN-01]
- Prefer short sentences and everyday words over long sentences and specialized vocabulary the target reader would not already know; cut a word only if the sentence still says everything it needs to say without it. [DIGITALGOV-PLAIN-01]
- Test the edited draft for clarity — read it as the target reader would, not as the person who already knows what it means — before treating it as finished. [DIGITALGOV-PLAIN-01]

## 2. Filler and hedging gate
- Interrogate every word and phrase for whether it is doing real work; cut deadweight language (throat-clearing openers, redundant modifiers, filler transitions) that adds no meaning the sentence doesn't already carry. [PURDUE-OWL-CONCISION-01]
- Replace a vague, general word or phrase with one specific, powerful word rather than padding the vague version with extra qualifiers; specificity is what makes writing concise, not simply having fewer words. [PURDUE-OWL-CONCISION-01]
- Combine two short, related sentences into one when the second sentence is only adding a fragment of information that fits naturally inside the first, rather than stretching one idea across avoidable extra sentences. [PURDUE-OWL-CONCISION-01]
- Do not strip hedges that are doing real epistemic work (a genuine uncertainty, an unverified claim flagged as such); a plain-language edit must not delete the qualifier that keeps a claim honest under the accuracy gate. [DIGITALGOV-PLAIN-01]

## 3. Active-voice gate
- Default to active voice, where the subject of the sentence performs the action of the verb, so the reader always knows who or what is doing something. [PURDUE-OWL-VOICE-01]
- Reserve passive voice for the cases where it earns its place: the agent performing the action is obvious, unimportant, unknown, or being deliberately de-emphasized in favor of the thing acted upon. [PURDUE-OWL-VOICE-01]
- Do not open a sentence in active voice and then shift to passive partway through; a voice shift inside one sentence is a clarity defect to fix in the edit pass, not a stylistic choice. [PURDUE-OWL-VOICE-01]
- Rewrite any passive construction that leaves a dangling modifier with no clear actor (for example, "To save time, the report was written on a computer") into an active sentence that names who performed the action. [PURDUE-OWL-VOICE-01]

## 4. AI-tell and voice-consistency gate
- Read the full draft in one pass for a single, consistent authorial voice; do not publish a post that shifts tone, formality, or sentence rhythm paragraph to paragraph as if stitched from different sources. [DIGITALGOV-PLAIN-01]
- Treat a mechanically inserted hedge, a generic transition that could preface any paragraph on any topic, or a summary sentence that restates the previous paragraph without adding information as a defect to cut in editing, not a natural part of the writer's voice — the same originality and quality bar the guardrails skill applies to the whole post applies at the sentence level. [GOOGLE-AICONTENT-01]
- Keep the edited voice consistent with the disclosed author's actual expertise and firsthand experience from the E-E-A-T gate; an edit pass that flattens a distinctive, credible voice into generic prose undermines the credibility signal the byline is supposed to carry. [GOOGLE-EEAT-01]

## 5. Pre-publish editing checklist
- Confirm every sentence states who or what performs the action, with passive voice used only where the guardrails above justify it. [PURDUE-OWL-VOICE-01]
- Confirm no sentence contains a word or phrase that could be cut without losing meaning, and that any surviving hedge is protecting a genuine, disclosed uncertainty rather than softening a claim out of habit. [PURDUE-OWL-CONCISION-01][DIGITALGOV-PLAIN-01]
- Confirm the voice reads as one consistent author from the opening line to the closing line, and that this voice matches the byline's disclosed expertise. [DIGITALGOV-PLAIN-01][GOOGLE-EEAT-01]
- Re-run the guardrails skill's pre-publish QA gate after this editing pass, since cuts and rewrites can silently drop an alt-text description, a citation link, or a heading the earlier gates required. [W3C-WCAG-01]
