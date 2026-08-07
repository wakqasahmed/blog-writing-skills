---
name: 09-geo-generative-engine-optimization
description: Gates for writing blog content that LLM-based answer engines (ChatGPT, Perplexity, Google AI Overviews) are likely to surface and cite, covering passage self-containment, statistic and citation density, and structured quotable claims. Apply after ../00-blog-writing-guardrails/SKILL.md, when a post's success depends on being cited or summarized by a generative answer engine rather than only ranked in traditional search.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Generative Engine Optimization (GEO)

Apply `../00-blog-writing-guardrails/SKILL.md` first; its originality, accuracy, and E-E-A-T gates are hard requirements for any post, independent of whether it also targets answer-engine citation. The gates below are additive, not a substitute.

Generative Engine Optimization (GEO) originates from a controlled black-box experiment showing that specific content interventions can boost a source's visibility in generative-engine responses by up to 40%, with efficacy varying by domain [ARXIV-GEOFOUND-01]. The gates below operationalize the interventions that follow-on research has since tested and qualified.

## 0. Evidence-quality caveat (read before applying any gate below)

- GEO is an early-stage research area. Across the published literature, "terminology, metrics, and evidence standards remain heterogeneous" [ARXIV-GEOSURVEY-01], and controlled benchmarks found that general heuristics "generalize poorly," with only three of fifty-four method-domain combinations tested showing a significant positive effect [ARXIV-GEOSURVEY-01]. Treat every tactic below as a directionally supported hypothesis, not a guaranteed outcome, and re-run your own before/after comparison rather than assuming a cited percentage transfers to your domain or model mix.
- Citation behavior varies substantially by model: one controlled study found Kimi-K2 sensitive to 83% of tested content factors versus 50% for Claude-3.5 and 33% for Gemini-2.5 [ARXIV-GEOCITE-01]. Do not optimize for a single answer engine and assume the result generalizes to all of them.
- Do not present any GEO tactic to a stakeholder as a guaranteed ranking, citation, or traffic outcome. State it as a research-backed direction with cited, dated evidence.

## 1. Passage self-containment gate

- Write the passage most likely to answer the post's core question as a direct, self-contained statement that does not depend on surrounding sentences for its subject, verb, or referents; an answer engine extracts and quotes passages independent of their context. [GOOGLE-SNIPPET-01]
- In controlled testing, topical relevance and a source's position within the retrieved context were "the two most robust factors" in whether a generative engine cited it, with position "equally consequential" to relevance [ARXIV-GEOSURVEY-01]. Place the self-contained answer near the top of the section that addresses it, not buried after preamble.
- Self-containment gains measured in these studies assumed the source was already retrieved into a fixed context window; they say nothing about whether the passage gets discovered or ranked in the first place [ARXIV-GEOSURVEY-01]. Pair this gate with normal SEO crawlability and indexing practice — it does not replace it.

## 2. Statistic and citation density gate

- Back claims with specific, sourced statistics rather than vague assertions; adding statistics produced a "substantial gain" in a controlled generative-engine visibility experiment [ARXIV-GEOSURVEY-01].
- Add direct quotations from primary sources where they strengthen a claim; quotation addition produced "approximately 41% relative gain" in position-adjusted visibility in the same experiment [ARXIV-GEOSURVEY-01].
- Cite sources inline for claims an answer engine might otherwise have to take on faith; explicitly citing sources measurably improved a passage's visibility within a fixed retrieval context [ARXIV-GEOSURVEY-01].
- Every statistic or quotation added under this gate must still pass the accuracy and claims-substantiation gate in `../00-blog-writing-guardrails/SKILL.md` — verify it against a primary source before publishing, not only for citation-bait value.

## 3. Structured, quotable claims gate

- Include explicit, current facts an answer engine can extract verbatim — prices, dates, named entities, specifications, comparisons — since price information and recency each showed a decisive, consistent preference across models in a controlled citation study, with odds ratios exceeding 10,000 for on-topic versus off-topic content [ARXIV-GEOCITE-01].
- Keep timestamps and any time-sensitive figures (pricing, versions, statistics) current at publish time and on every substantive update; "Recent vs Old Timestamp" was one of four factors with decisive, consistent effect on citation likelihood [ARXIV-GEOCITE-01].
- Do not rely on formatting or list structure alone to earn a citation: "formatting-only edits have little impact" once topical relevance, recency, and pricing are accounted for [ARXIV-GEOCITE-01]. Structure claims for clarity because it serves the reader, not as a substitute for substantive, verifiable content.
- Where a post presents a list or ranked set of options, put the most important or recommended item first; list position showed "very large effects" on citation likelihood independent of content quality [ARXIV-GEOCITE-01].

## 4. Answer-engine traffic-impact disclosure gate

- When advising a stakeholder on GEO investment, disclose that answer-engine surfaces measurably suppress organic click-through even for top-ranking pages: one large-scale study of 300,000 keywords found the presence of a Google AI Overview correlated with a 58% lower average click-through rate for position-one results, up from a 34.5% reduction measured roughly eight months earlier [AHREFS-AIOCTR-01]. Do not promise that earning an answer-engine citation restores or exceeds prior organic click volume — the cited data shows the opposite trend over time.
- Frame GEO work to stakeholders as protecting visibility and brand presence inside answer-engine surfaces where clicks are being lost, not as a click-volume growth tactic. [AHREFS-AIOCTR-01]

## 5. Pre-publish GEO QA gate

- Confirm the post still passes every gate in `../00-blog-writing-guardrails/SKILL.md`, especially accuracy and substantiation for any statistic or quotation added under Gate 2.
- Confirm the core-question passage under Gate 1 reads correctly with all surrounding context removed — paste it alone and check it still makes sense.
- Confirm every price, date, or version number visible on the page is current as of publish date, per Gate 3.
- Do not describe any change made under this skill as a guaranteed citation, ranking, or traffic outcome in publish notes, briefs, or stakeholder communication, per the Section 0 caveat.
