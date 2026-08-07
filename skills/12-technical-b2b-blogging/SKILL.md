---
name: 12-technical-b2b-blogging
description: Verify code samples actually run, pin technical claims to a specific tool/library version, write for a multi-stakeholder B2B buying committee, and substantiate vendor-superiority claims. Apply this skill when planning, drafting, or reviewing a technical blog post, developer tutorial, or B2B product post aimed at a buying committee.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Technical and B2B Blogging

Apply `../00-blog-writing-guardrails/SKILL.md` first; its gates apply to every post covered here.

## 1. Code-sample verification gate
- Run every code sample against the real tool, library, or API before publishing; do not ship a sample that was typed from memory or adapted from another sample without execution. Documented behavior should have a passing test or an equivalent verification run behind it, the same standard applied to source-code documentation. [GOOGLE-DOCBP-01]
- Treat a code sample as part of the product, not decoration: update it in the same edit pass as any change to the underlying API, flag, or default it demonstrates, so the sample never drifts out of sync with what it claims to show. [GOOGLE-DOCBP-01]
- Where a sample's output is shown (console output, response body, screenshot), verify the shown output was actually produced by running the sample, not reconstructed by hand. [GOOGLE-DOCBP-01]

## 2. Version-pinning gate
- State the specific tool, library, framework, or API version a claim, behavior, or code sample applies to; do not describe version-dependent behavior with only a bare product name. [GOOGLE-TIMELESS-01]
- Avoid anchoring a claim to words like "new," "currently," "latest," or "now supports" without a concrete reference point; give the version number or release date the claim is true as of, since these words go stale the moment a newer version ships. [GOOGLE-TIMELESS-01]
- Where practical, generalize or parameterize version numbers inside long-lived tutorials (for example, a placeholder for a release tag) so routine version bumps do not require rewriting the whole post; where a specific version number is load-bearing to the claim, keep it explicit rather than generalizing it away. [WRITETHEDOCS-PRINCIPLES-01]
- Note the date the post's compatibility claims were last verified so a reader can judge whether they still hold against the tool or library's current release. [WRITETHEDOCS-PRINCIPLES-01]

## 3. Multi-stakeholder B2B buying-committee gate
- Write for the fact that a B2B technical purchase is decided by a multi-person buying group, not a single reader; real buying groups commonly run several people deep and increasingly include senior, budget-holding titles alongside the hands-on technical evaluator. [TRUSTRADIUS-B2BBUYING-01]
- Address the distinct concerns of each stakeholder role the post's topic touches — the technical evaluator (implementation detail, correctness, sample code), the economic buyer (cost, risk, total effort), and the end user (day-to-day workflow impact) — rather than writing only to the role most like the author. [TRUSTRADIUS-B2BBUYING-01]
- Do not assume one stakeholder will relay the full technical argument to the rest of the buying group unedited; make the post's core claim and its evidence legible on its own to a reader outside the original technical audience. [TRUSTRADIUS-B2BBUYING-01]

## 4. Vendor-superiority substantiation gate
- Reuse the guardrails skill's advertising-substantiation gate for every comparative or superiority claim in a technical or B2B post ("faster than X," "the only tool that," "industry-leading"): treat it as an advertising claim requiring a reasonable, pre-existing basis the author can produce on request. [FTC-ADSUB-01]
- Back a benchmark or comparison claim with the actual methodology (versions compared, hardware/environment, date run) alongside the result; a number without its method is not substantiation. [FTC-ADSUB-01]
- Do not restate a competitor's own marketing claim about itself as a bare fact; attribute it to the competitor or independently verify it before repeating it as true. [FTC-ADSUB-01]

## 5. Pre-publish QA gate
- Confirm every code sample was executed against the stated tool/library version in this pass, every version-dependent claim carries its version or date, every stakeholder role the post targets is addressed, and every superiority claim has a documented basis before the post goes live. [GOOGLE-DOCBP-01][GOOGLE-TIMELESS-01][TRUSTRADIUS-B2BBUYING-01][FTC-ADSUB-01]
