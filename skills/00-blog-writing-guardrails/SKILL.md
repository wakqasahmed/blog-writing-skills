---
name: 00-blog-writing-guardrails
description: Mandatory originality, accuracy, credibility, accessibility, clarity, and answer-engine hygiene gates for any blog post. Apply this skill first, before any topic-specific blog-writing skill, when planning, drafting, reviewing, or publishing a blog post.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Global Blog Writing Guardrails

Apply these gates before every topic-specific `SKILL.md` in this pack. A draft that fails a hard gate must be marked `BLOCK`, not published as reader-ready.

## 1. Originality and AI-disclosure gate
- Ship an original angle, example, data point, or firsthand experience in every post; do not publish a schematic rehash of existing top-ranking answers to the same question. [GOOGLE-EEAT-01]
- Quality and originality are judged on the finished content, not on whether AI assisted in producing it; using automation to mass-produce or reword existing content without adding value is treated as spam, not efficiency. [GOOGLE-AICONTENT-01]
- Record who wrote or substantially edited the post and disclose material use of automation where the publication's own editorial policy requires it. [GOOGLE-EEAT-01]

## 2. Accuracy and claims-substantiation gate
- Verify every factual claim, statistic, and quote against a primary or authoritative source before publishing; do not carry forward an unverified number from a secondary blog post. [GOOGLE-EEAT-01]
- Treat any express or implied claim of superiority, results, or performance ("fastest," "#1," "proven to") as an advertising claim requiring a reasonable, pre-existing basis; do not publish a claim the author cannot substantiate on request. [FTC-ADSUB-01]
- Link claims to their source inline or in a references section so a reader or an AI system can verify them without leaving the page. [GOOGLE-EEAT-01]

## 3. E-E-A-T and author-credibility gate
- Attribute every post to a named author or organization with visible, relevant experience or expertise in the topic; anonymous or generic "Team" bylines weaken trust signals on topics where the reader needs to know who is speaking. [GOOGLE-EEAT-01]
- Show first-hand experience where the topic calls for it (used the product, ran the experiment, shipped the code) rather than only synthesizing other people's claims. [GOOGLE-EEAT-01]
- Keep the post current: correct or date-stamp material updates so the page continues to reflect accurate, trustworthy information after publication. [GOOGLE-EEAT-01]

## 4. Duplicate-content and canonicalization gate
- Before publishing, check whether the same or near-duplicate content already exists at another URL on the site; if it does, consolidate or set a self-referencing canonical tag rather than letting two URLs compete for the same query. [GOOGLE-CANON-01]
- When syndicating or cross-posting the same post to another domain, agree in advance which URL is canonical and mark the non-canonical copies accordingly. [GOOGLE-CANON-01]

## 5. Accessibility gate
- Give every meaningful image equivalent alternative text, and mark purely decorative images so assistive technology skips them. [W3C-WCAG-01]
- Use real `<h1>`–`<h6>` heading elements in strict nesting order that mirrors the post's actual structure; never skip a level or use headings for visual styling alone. [W3C-WCAG-01]

## 6. Plain-language and clarity gate
- Write for the reader's task, not the writer's expertise: lead with what the reader needs, use short sentences and everyday words, and test drafts for clarity before publishing. [DIGITALGOV-PLAIN-01]
- Define or cut jargon a general reader in the target audience would not already know; a plain-language rewrite must not remove technical precision the audience actually needs. [DIGITALGOV-PLAIN-01]

## 7. Structured-data and answer-engine hygiene gate
- Mark up every post with `Article` structured data (author, `datePublished`, `dateModified`, publisher) that matches what is visibly on the page; never mark up content that is not actually present. [GOOGLE-SCHEMA-01]
- Answer the post's core question in a direct, self-contained statement near the top or under its own heading, in plain language, so the passage is extractable on its own. [GOOGLE-SNIPPET-01]

## 8. Pre-publish QA gate
- Verify every internal and external link resolves, every image has alt text, every heading level is correct, and every statistic has a live source link before the post goes live. [W3C-WCAG-01][GOOGLE-EEAT-01]
- Confirm the byline, publish date, canonical tag, and structured data all agree with each other and with the visible page before publishing. [GOOGLE-SCHEMA-01][GOOGLE-CANON-01]
