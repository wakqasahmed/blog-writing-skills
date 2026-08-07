---
name: 08-aeo-answer-engine-optimization
description: Structure blog content to compete for featured snippets, People Also Ask, and voice/answer-engine results using direct-answer paragraphs and question-based headers, without relying on deprecated FAQ schema. Apply when writing or restructuring a post to answer a specific question well.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Answer Engine Optimization (AEO)

Apply [`../00-blog-writing-guardrails/SKILL.md`](../00-blog-writing-guardrails/SKILL.md) first; its gates apply to every post before this skill's guidance.

## 1. Direct-answer gate
- For every question the post targets, answer it in a short, self-contained statement — typically 40-60 words — placed immediately under the question's own heading, before any elaboration, caveats, or background; Google's own systems select and elevate a passage for a featured snippet or related-questions ("People Also Ask") group based on how well the page answers the query, and a scanning reader or extraction system must be able to lift that passage on its own. [GOOGLE-SNIPPET-01]
- Do not bury the direct answer after a story, definition of terms, or throat-clearing; a passage that requires reading prior paragraphs to make sense is a worse extraction candidate. [GOOGLE-SNIPPET-01]
- Google explicitly states there is no markup or declaration that forces a page to become a featured snippet or PAA entry — selection is algorithmic only, and a low `max-snippet` setting does not reliably prevent selection either; write for a good answer, not for a guaranteed placement. [GOOGLE-SNIPPET-01]

## 2. Question-based header gate
- Phrase headings for question-driven sections as the actual question a reader or answer engine would ask ("How does X affect Y?" not "Overview of X and Y"), so the heading itself functions as the query match and the paragraph beneath it functions as the answer. [GOOGLE-SNIPPET-01]
- Keep these question headings in strict, real heading-level nesting per the guardrails' accessibility gate; a bolded question in body text is not a substitute for a real heading. [W3C-WCAG-01]
- Group related questions a reader is likely to ask next under their own headings rather than one long combined answer; Google surfaces People Also Ask as a related-questions group alongside featured snippets, and single-question sections match that pattern. [GOOGLE-SNIPPET-01]

## 3. FAQPage schema deprecation gate
- Do not add `FAQPage` structured data to blog posts expecting a rich result: Google's own documentation states the FAQ rich result feature stopped appearing in Google Search as of May 7, 2026, and the feature's dedicated documentation has been removed; markup that once produced expandable Q&A rich results in the SERP no longer does. [GOOGLE-FAQPAGE-01]
- Before the deprecation, Google had already restricted FAQ rich results to well-known, authoritative government and health sites — most blogs were never eligible even when the feature was active. [GOOGLE-FAQPAGE-01]
- Treat any existing `FAQPage` markup as inert for search-appearance purposes; removing it is not required by these gates, but do not write new FAQ sections on the assumption that adding the schema will win a rich result. [GOOGLE-FAQPAGE-01]

## 4. QAPage schema boundary gate
- Do not use `QAPage` markup for an author-written FAQ or Q&A section: Google explicitly excludes site-authored content with only one answer per question and no user-submission mechanism from `QAPage` eligibility — that is exactly what most blog FAQ sections are. [GOOGLE-QAPAGE-01]
- Reserve `QAPage` for genuine forum- or support-style pages where users submit and vote on alternative answers to a single posted question; do not apply it to a blog post that merely lists several questions and answers. [GOOGLE-QAPAGE-01]

## 5. Evidence-maturity caveat
- Treat specific AEO and GEO (generative-engine optimization) tactics beyond the gates above — citation-count thresholds, optimal answer length, ideal question-heading phrasing for a particular assistant — as an actively developing, heterogeneous evidence base rather than settled, guaranteed-outcome techniques; independent surveys of this literature report inconsistent methodologies and effect sizes across studies. Validate any such tactic against the target answer engine's own current documentation before treating it as a hard rule. [ARXIV-GEOSURVEY-01]

## 6. Pre-publish AEO check
- For each question-based heading, confirm the paragraph beneath it stands alone as a complete answer if read with no other context on the page. [GOOGLE-SNIPPET-01]
- Confirm no `FAQPage` markup was added on the assumption of a rich-result payoff, and any `QAPage` markup present is limited to genuinely user-submitted Q&A content. [GOOGLE-FAQPAGE-01][GOOGLE-QAPAGE-01]
- Confirm this pass does not contradict the guardrails' structured-data and answer-engine hygiene gate or pre-publish QA gate. [GOOGLE-SCHEMA-01][W3C-WCAG-01]
