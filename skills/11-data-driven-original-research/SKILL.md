---
name: 11-data-driven-original-research
description: Gates for publishing original-research or data-driven blog posts, covering methodology transparency, sample-size and margin-of-error disclosure, avoiding p-hacking and cherry-picking, correlation-versus-causation labeling, and honest chart design. Apply this skill when planning, drafting, or reviewing a post that presents a survey, study, or any original or third-party dataset.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Data-Driven and Original-Research Blog Posts

Apply `../00-blog-writing-guardrails/SKILL.md` first; its accuracy, claims-substantiation, and E-E-A-T gates apply to every statistic and claim in this skill. The gates below add requirements specific to posts built around survey data, original research, or third-party datasets.

## 1. Methodology-transparency gate
- Before publishing any post built on a survey or study, disclose how the data was collected: the survey mode, the population studied, how the sample was recruited or selected, and the exact question wording behind any reported figure. [AAPOR-DISCLOSURE-01]
- State whether the sample was drawn using probability-based selection or a non-probability method (opt-in panel, convenience sample, scraped dataset); do not present a non-probability sample's results with the same confidence language used for a probability sample. [AAPOR-DISCLOSURE-01]
- Be transparent about the assumptions, methods, limitations, and possible sources of error behind any statistic before publishing it, not only the headline number. [ASA-ETHICS-01]

## 2. Sample-size and margin-of-error disclosure gate
- Report the sample size for every reported statistic, broken out by subgroup when a subgroup figure is cited; a subgroup number with an unstated (and likely small) base is not publication-ready. [AAPOR-DISCLOSURE-01]
- For probability-based samples, disclose the estimated margin of sampling error alongside the headline statistic; if a precision estimate is given for a non-probability sample, describe the model that produced it rather than presenting it as a standard margin of error. [AAPOR-DISCLOSURE-01]

## 3. Anti-p-hacking and anti-cherry-picking gate
- Disclose when multiple comparisons, subgroup cuts, or alternative time windows were tested on the same dataset, and note any adjustment made for that multiplicity; do not report only the one cut that reached significance while silently dropping the others. [ASA-ETHICS-01]
- Resist selectively interpreting or reporting data to fit a predetermined narrative; if the full dataset does not support the post's thesis, revise the thesis rather than the presented slice of data. [ASA-ETHICS-01]

## 4. Correlation-versus-causation gate
- Label an association found in observational or correlational data as a correlation, not a cause, unless the underlying study design (randomized experiment, controlled trial) actually supports a causal claim. [ASA-ETHICS-01]
- Convey statistical results in ways that are honest and meaningful and do not mislead any stakeholder about what the data can and cannot establish; do not let a headline, chart title, or pull quote imply causation that the body copy does not substantiate. [ASA-ETHICS-01]

## 5. Honest chart-design gate
- Build every chart to convey the underlying data honestly and meaningfully; do not choose a truncated, non-zero, or otherwise distorting axis, scale, or visual proportion in order to exaggerate or minimize a difference. [ASA-ETHICS-01]
- Where a claim rendered in a chart is also stated in prose (a comparison, ranking, or trend), the chart's visual proportions must match the substantiated claim behind it. [FTC-ADSUB-01]

## 6. Pre-publish QA addendum
- Before publishing, confirm the post discloses sample size, margin of error (or its non-probability equivalent), survey mode, and question wording for every original statistic, and that every chart's axis and scale were reviewed for distortion. [AAPOR-DISCLOSURE-01][ASA-ETHICS-01]
