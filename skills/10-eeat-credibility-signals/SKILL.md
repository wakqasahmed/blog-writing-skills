---
name: 10-eeat-credibility-signals
description: Tactical drafting and editing steps for executing E-E-A-T in a blog post — author bios with credentials, disclosed methodology and experience, primary-source linking, original-data callouts, and trust signals such as last-updated dates and a correction policy. Apply when drafting or editing a post's byline, author bio, sourcing, or trust/update footer.
version: 1.0.0
last_reviewed: 2026-08-07
---

# E-E-A-T Credibility Signals

Apply `../00-blog-writing-guardrails/SKILL.md` first; its Originality, Accuracy, and E-E-A-T gates are hard requirements. This skill turns that gate into concrete drafting and editing steps.

## 1. Author bio and credentials
- Write a visible author bio next to or beneath every post that states the author's relevant credentials, role, or track record on the post's topic; do not rely on a generic "Team" byline for topics where the reader needs to know who is speaking. [GOOGLE-EEAT-01]
- Make the author's credentials easy to find, either in the inline bio or a linked profile page, and keep them accurate to the author's actual professional reputation. [TRUSTPROJECT-INDICATORS-01]
- Mark up the byline with `author` structured data pointing to a `Person` (or `Organization` for house content) so the credential signal is machine-readable, not just visible text. [SCHEMAORG-AUTHOR-01]
- Maintain an "About us" or author-profile page that a reader or a Google quality rater can use to independently confirm the stated experience and expertise; do not let the on-page bio claim credentials the profile page contradicts or omits. [GOOGLE-QRG-01]

## 2. Disclosing methodology and first-hand experience
- When the post reports on a test, review, or experiment, state how it was done — what was tested, over what period, under what conditions — so a reader can judge whether the experience behind the claim is real and relevant. [GOOGLE-QRG-01]
- Prefer language that shows direct, first-hand experience with the product, process, or data ("we ran," "we measured," "we used this for X months") over language that only synthesizes other people's claims. [GOOGLE-EEAT-01]
- Disclose any conflict of interest (ownership, sponsorship, affiliate relationship with the subject) next to the claim it affects; a reviewer's own product review is not a trustworthy, independent source without that disclosure. [GOOGLE-QRG-01]

## 3. Linking to primary sources
- Link every statistic, quote, or factual claim to the primary source that backs it — the original study, standards body, or first-party dataset — not to a secondary blog post that merely cites it. [GOOGLE-EEAT-01]
- Place the citation inline or in a references section close enough to the claim that a reader or an AI system can verify it without leaving the page. [GOOGLE-EEAT-01]

## 4. Original-data callouts
- When the post includes data the author collected or generated (a survey, an internal test, a dataset), call it out explicitly as original — do not blend it visually or narratively with third-party statistics — so its firsthand-experience value is legible to readers and raters. [GOOGLE-QRG-01]
- Ship at least one original data point, example, or angle per post rather than a schematic rehash of what already ranks for the same query. [GOOGLE-EEAT-01]

## 5. Trust signals: last-updated dates and correction policy
- Show a visible "published" and, when the post has been materially edited, a "last updated" date so readers and raters can judge currency; keep the visible date consistent with the page's `dateModified` structured data. [GOOGLE-SCHEMA-01]
- Maintain a corrections policy and follow it: when a factual error is found post-publication, correct it quickly, clearly, and prominently rather than silently editing the page. [TRUSTPROJECT-INDICATORS-01]
- Link to the site's corrections policy or a change-log entry from the post when a correction has been made, so the trust signal is verifiable rather than asserted. [TRUSTPROJECT-INDICATORS-01]

## 6. Pre-publish checklist
- Author bio present, accurate, and linked to a profile/About page. [GOOGLE-QRG-01][TRUSTPROJECT-INDICATORS-01]
- `author` structured data matches the visible byline. [SCHEMAORG-AUTHOR-01]
- Every claim traces to a primary source link. [GOOGLE-EEAT-01]
- Original data, if any, is explicitly labeled as such. [GOOGLE-QRG-01]
- Published/updated dates are visible and match structured data; a corrections path exists for future errors. [GOOGLE-SCHEMA-01][TRUSTPROJECT-INDICATORS-01]
