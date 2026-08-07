---
name: 15-distribution-repurposing
description: Build a pillar/topic-cluster internal-linking structure, repurpose a published post across channels without creating duplicate-content risk, and canonicalize syndicated copies correctly. Apply after `00-blog-writing-guardrails`, and before linking, syndicating, or cross-posting any published post.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Distribution and Repurposing

Apply `../00-blog-writing-guardrails/SKILL.md` first; its duplicate-content/canonicalization gate and accuracy gate apply to every distributed or repurposed version of a post this skill produces.

## 1. Internal-linking cluster-strategy gate
- Organize related posts into a topic cluster: one comprehensive pillar page covering the broad subject, and supporting posts that each address a specific subtopic, long-tail question, or use case and link back to the pillar (and to each other where relevant) with descriptive, topic-consistent anchor text. [HUBSPOT-CLUSTER-01]
- Give every post you care about at least one crawlable internal link from another page on the site, using a real `<a href>` element; a page with no inbound internal link is effectively orphaned from crawling and from the cluster it belongs to. [GOOGLE-LINKS-01]
- Write internal-link anchor text that is descriptive, reasonably concise, and relevant both to the page it appears on and the page it points to; do not use generic anchor text ("click here") or force an unrelated keyword into the anchor. [GOOGLE-LINKS-01]
- Link to a page in context, from the point in the post where that resource actually helps the reader understand the current topic, rather than batching unrelated links at the end for their own sake. [GOOGLE-LINKS-01]
- When publishing a new cluster post, add or update the link from the pillar page (and from sibling cluster posts where relevant) in the same publishing pass, so the cluster's internal-link graph does not lag behind newly published content. [HUBSPOT-CLUSTER-01]

## 2. Cross-channel repurposing gate
- Repurposing a post's ideas, data, or structure into a non-indexed channel (a social post, an email, a video script, a slide deck) is not a duplicate-content risk under Google's indexing rules, since these formats are not competing HTML pages in Google's index; scope duplicate-content mitigation to same-domain or cross-domain web pages, not to every channel a post's content reaches. [GOOGLE-CANON-01]
- If a repurposed piece is itself published as a web page (a syndicated article, a cross-posted blog, a near-duplicate landing page), apply the guardrails' duplicate-content and canonicalization gate to that page before publishing it, exactly as for any other page. [GOOGLE-CANON-01]
- Do not let a channel-specific rewrite drop or alter a factual claim, statistic, or attribution carried over from the original post without re-verifying it; repurposing a claim into a new format does not exempt it from the accuracy gate. [GOOGLE-EEAT-01]

## 3. Syndication canonicalization gate
- Before syndicating or cross-posting a post to another domain or a partner's site, agree in advance which single URL is canonical, and mark every non-canonical copy with a `rel="canonical"` link pointing to that URL. [GOOGLE-CANON-01]
- Keep the original, canonical URL self-referencing (its own canonical tag points to itself), so ranking signals from any syndicated copies consolidate onto the original rather than splitting across duplicate URLs. [GOOGLE-CANON-01]
- If a syndication partner cannot add a canonical tag, request a direct link back to the original URL from the syndicated copy as the next-best signal of the original source. [GOOGLE-CANON-01]

## 4. Pre-distribution QA gate
- Verify every new or updated internal link resolves and that the anchor text is still accurate to the linked page's current content before publishing a cluster update. [GOOGLE-LINKS-01]
- Confirm the canonical tag on every syndicated or cross-posted copy points to the correct original URL before that copy goes live. [GOOGLE-CANON-01]
