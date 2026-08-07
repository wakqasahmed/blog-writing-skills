---
name: 07-seo-on-page-optimization
description: On-page SEO gates for title tags, meta descriptions, header hierarchy, URL structure, internal linking, and image optimization, grounded in Google Search Central's own documentation. Apply after the global guardrails skill, before publishing any blog post that should be discoverable and rankable.
version: 1.0.0
last_reviewed: 2026-08-07
---

# On-Page SEO Optimization

Apply `../00-blog-writing-guardrails/SKILL.md` first; its originality, accuracy, E-E-A-T, canonicalization, accessibility, plain-language, and structured-data gates apply to every post before the checks below.

## 1. Title tag gate
- Write a page title that is unique to the page, clear, concise, and accurately describes the page's content; do not reuse the same title across multiple pages. [GOOGLE-SEOSTART-01][GOOGLE-TITLELINK-01]
- Put the most important, page-specific information first and keep site branding minimal or reserved for the homepage; do not pad the title with repeated boilerplate that pushes unique content out of the visible, non-truncated portion. [GOOGLE-TITLELINK-01]
- Do not repeat the same word or phrase multiple times in the title in an attempt to rank for it; a few accurately descriptive terms are enough. [GOOGLE-TITLELINK-01]
- Make the page's main heading visually and structurally prominent (its own `<h1>`) so it is unambiguous which heading is the primary title. [GOOGLE-TITLELINK-01]

## 2. Meta description gate
- Write a meta description that is short, unique to that one page, and states the page's most relevant points in one or two sentences a reader can use to judge relevance before clicking. [GOOGLE-SEOSTART-01]
- Do not ship a generic or duplicated meta description across multiple pages; a missing or duplicate description forfeits control over how the page is summarized in results. [GOOGLE-SEOSTART-01]

## 3. Header hierarchy gate
- Use real `<h1>`-`<h6>` elements in strict nesting order that mirrors the post's actual structure, per the accessibility gate in the guardrails skill; do not skip levels or use headings only for visual size. [W3C-WCAG-01]
- Do not add headings purely to stuff in extra keyword phrasing; write each heading to describe the section that actually follows it. [GOOGLE-SEOSTART-01]

## 4. URL structure gate
- Use a descriptive URL that contains words useful to a reader scanning the address or breadcrumb in search results, rather than an opaque ID or unrelated string; for example `/pets/cats` rather than a query-string identifier. [GOOGLE-SEOSTART-01]
- Group related posts under a consistent directory structure so the site's information hierarchy is legible, and ensure each piece of content is reachable at exactly one URL, per the guardrails' duplicate-content and canonicalization gate. [GOOGLE-SEOSTART-01][GOOGLE-CANON-01]

## 5. Internal-linking gate
- Link to relevant internal and external resources using descriptive anchor text that tells the reader what the destination page is about; do not use generic anchor text like "click here" or "this page." [GOOGLE-SEOSTART-01]
- Implement every link as an `<a>` element with a real `href` attribute; do not rely on `<span>`/`<div>` click handlers or JavaScript-only navigation (`href="javascript:..."`) for links a reader or crawler needs to follow. [GOOGLE-CRAWLLINKS-01]
- Only link out to external sources the author trusts; add `rel="nofollow"` to links the author cannot vouch for, including any user-submitted links in comments. [GOOGLE-SEOSTART-01]

## 6. Image optimization gate
- Write short, descriptive alt text for every meaningful image that explains the image's relationship to the surrounding content, per the guardrails' accessibility gate; mark purely decorative images so they are skipped by assistive technology. [W3C-WCAG-01]
- Use high-quality images placed near the text they support, and give image files descriptive names rather than generic camera-generated filenames, so both readers and image search can understand what the image shows. [GOOGLE-SEOSTART-01]

## 7. Pre-publish on-page QA gate
- Before publishing, confirm the title tag, meta description, and `<h1>` are each unique to the page and not copy-pasted from another post. [GOOGLE-SEOSTART-01][GOOGLE-TITLELINK-01]
- Confirm every internal link resolves to a live, correctly canonical URL and uses descriptive anchor text, per the guardrails' pre-publish QA gate. [GOOGLE-SEOSTART-01][GOOGLE-CANON-01]
