---
name: 03-structure-scannability
description: Structure a blog post for scanning readers using the inverted pyramid, layer-cake heading hierarchy, TL;DR/summary boxes, and bullet or table formatting. Apply when outlining, drafting, or restructuring a post so most readers get its core value even if they only scan it.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Structure and Scannability

Apply [`../00-blog-writing-guardrails/SKILL.md`](../00-blog-writing-guardrails/SKILL.md) first; its gates apply to every post before this skill's guidance.

## 1. Inverted-pyramid gate
- Put the post's core answer, conclusion, or most important point in the first two paragraphs, before supporting detail, background, or methodology; do not make the reader scroll past setup to reach the point. [NNGROUP-FPATTERN-01]
- Order the remaining sections from most to least important to a scanning reader, not in the order the author discovered or wrote them. [NNGROUP-FPATTERN-01]

## 2. Heading and layer-cake structure gate
- Give every major section a visually distinct, descriptive subheading that leads with its most important words, so a reader scanning headings alone still gets the gist; this produces the efficient "layer-cake" scan instead of the low-efficiency F-pattern that forms on unstructured text. [NNGROUP-LAYERCAKE-01]
- Keep headings in strict, real `<h1>`–`<h6>` nesting order per the guardrails' accessibility gate; do not use bold paragraph text as a substitute for a real heading. [W3C-WCAG-01]
- Break each section into short paragraphs or lists rather than dense blocks of text, and add whitespace between sections so a scanning reader can tell which content belongs under which heading. [NNGROUP-LAYERCAKE-01]

## 3. TL;DR and summary-box gate
- For posts answering a specific question, place a short, self-contained direct-answer statement near the top or under its own heading, in plain language, so the passage can stand alone if extracted; this is also what makes a passage eligible for featured-snippet or related-question placement. [GOOGLE-SNIPPET-01]
- Keep a TL;DR or summary box to a few sentences of the actual conclusion, not a teaser that withholds the answer to keep the reader scrolling. [NNGROUP-FPATTERN-01]

## 4. Bold, list, and table gate
- Bold the specific key phrase or number a scanning reader needs from a paragraph, not whole sentences; over-bolding defeats the purpose of drawing the eye. [NNGROUP-FPATTERN-01]
- Convert sequences, steps, comparisons, or option sets into bulleted or numbered lists instead of comma-separated prose; use a table when comparing the same attributes across three or more items. [NNGROUP-FPATTERN-01]
- Write link text and list items that are informative on their own ("compare pricing tiers," not "click here"), since a scanning reader reads link text and list items in isolation from surrounding prose. [NNGROUP-FPATTERN-01]

## 5. Pre-publish scannability check
- Read only the headings, the TL;DR, and any bolded phrases in the draft, in order; if that pass alone does not deliver the post's core value, restructure before publishing rather than adding more prose. [NNGROUP-LAYERCAKE-01]
- Confirm this scannability pass does not contradict the guardrails' pre-publish QA gate on heading order, links, and structured data. [W3C-WCAG-01]
