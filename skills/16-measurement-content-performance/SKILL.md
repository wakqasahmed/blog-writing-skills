---
name: 16-measurement-content-performance
description: Measure blog performance with KPIs mapped to funnel stage, detect content decay and set refresh cadence, and run valid headline/CTA A/B tests without peeking-driven false positives. Apply after `00-blog-writing-guardrails`, and before treating any traffic, engagement, or test result as a publishing or refresh decision.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Measurement and Content Performance

Apply `../00-blog-writing-guardrails/SKILL.md` first; its originality, accuracy, and pre-publish gates apply to every claim and every refreshed passage this skill produces.

## 1. KPI-to-funnel-stage gate
- Map each blog KPI to the funnel stage it actually measures before reporting it as a success signal: impressions and average ranking position measure discovery; organic clicks and click-through rate (CTR) measure the search-result decision; and time-on-page, scroll depth, and return visits measure on-page engagement — do not report a discovery-stage metric (e.g., impressions) as proof of an engagement-stage outcome. [BACKLINKO-CTR-01]
- Treat CTR as position-dependent, not a flat conversion target: average organic CTR for the #1 ranking position was 27.6% versus a small fraction of that by position #10 in a first-party analysis of over 4 million Google search results, so compare a page's CTR only against pages holding a similar ranking position, not against a single blanket benchmark. [BACKLINKO-CTR-01]
- Because the top 3 ranking positions captured the majority of clicks in the same analysis, prioritize headline and snippet testing on pages already ranking in or near positions 1-3, where a CTR gain converts into the most absolute clicks; a CTR improvement on a page ranking below position 10 moves little absolute traffic. [BACKLINKO-CTR-01]
- Report engagement metrics (time-on-page, scroll depth) and conversion metrics (email signups, product clicks) as a separate KPI layer from traffic metrics; a page can gain impressions and clicks while engagement or conversion falls, and that split must be visible in the same report, not collapsed into one topline number. [BACKLINKO-CTR-01]

## 2. Content-decay detection and refresh-cadence gate
- Flag a published post for review when its organic clicks or ranking position show a sustained decline (not a single-week dip) relative to its own prior baseline, rather than reacting to normal week-to-week search-visibility noise. [GOOGLE-EEAT-01]
- Distinguish decay caused by stale, outdated, or superseded information from decay caused by external ranking-factor or competitive changes before choosing a fix: a post whose facts, prices, screenshots, or examples are outdated needs a content refresh; a post that is still accurate but has been outranked needs stronger originality, depth, or first-hand evidence, not just a datestamp change. [GOOGLE-EEAT-01]
- When refreshing a decayed post, materially update the substance — corrected facts, new data, added first-hand detail — and update the visible and structured-data modification date to match; do not change only the datestamp without a substantive content change, since freshness signals must reflect real, verifiable updates. [GOOGLE-EEAT-01][GOOGLE-SCHEMA-01]
- Re-verify every statistic and claim carried into a refreshed post against its current primary source before republishing, exactly as required for a new post; a refresh does not exempt a claim from the accuracy gate. [GOOGLE-EEAT-01]

## 3. Valid headline/CTA A/B-testing gate
- Fix the sample size or test duration needed for the test's statistical power before launching a headline or CTA test, and do not stop the test the first time the observed difference crosses significance; continuously monitoring a standard frequentist test and stopping as soon as it looks significant (peeking) inflates the false-positive rate far above the nominal significance level. [JOHARI-PEEKING-01]
- If a test must be checked before its planned end (an early stop for a clear regression, a business deadline), use a sequential-testing method built for continuous monitoring — such as an always-valid p-value or confidence sequence — that stays statistically valid at any inspection time, instead of applying a fixed-sample p-value test at an arbitrary interim point. [JOHARI-PEEKING-01]
- Test only one variable at a time (headline alone, or CTA copy alone) per experiment arm, and hold the ranking position and audience segment constant across variants where possible, since CTR is position-dependent and a position shift between variants would confound the result. [BACKLINKO-CTR-01]
- Report a winning variant only once the test reaches its pre-committed stopping rule; a lift observed mid-test, before that rule is met, is not a validated result and must not be shipped as the new default headline or CTA. [JOHARI-PEEKING-01]

## 4. Reporting-integrity gate
- Do not present a KPI improvement as an advertising or performance claim ("proven to double clicks," "#1 performing headline") to stakeholders or in published content unless the underlying test met its pre-committed stopping rule and the claim can be substantiated on request. [FTC-ADSUB-01][JOHARI-PEEKING-01]
- Carry forward the byline, publish date, and last-reviewed date changes from any content refresh into the post's structured data and visible metadata before reporting the refresh as complete. [GOOGLE-SCHEMA-01]
