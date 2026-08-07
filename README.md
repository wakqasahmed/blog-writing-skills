# Blog Writing Skills

Evidence-backed skills for writing persuasive, educational, clear, and SEO/AEO/GEO-friendly blog posts. Every normative instruction cites a primary academic or industry source in [`SOURCES.md`](SOURCES.md).

## Install

```bash
npx skills@latest add wakqasahmed/blog-writing-skills
```

## Contents

The installable skills live in [`skills/`](skills/). Apply [`00-blog-writing-guardrails`](skills/00-blog-writing-guardrails/SKILL.md) first, before any topic-specific skill.

## Aggregate catalogue

Changes merged to this repository are intended to synchronize to [wakqasahmed/skills](https://github.com/wakqasahmed/skills). Treat this repository as the source of truth for blog-writing skills.

## Outcome-eval harness status

Every skill's `eval/` currently only checks fixture *shape* (required fields, minimum counts) — none score an actual model's decision against an expected outcome, and there is no gated model-harness layer at all yet. [#41](https://github.com/wakqasahmed/blog-writing-skills/issues/41) tracks the core gap (`contract_check.py` greps `SKILL.md` for phrases that exist because `SKILL.md` was written to contain them — self-referential, cannot fail); [#42](https://github.com/wakqasahmed/blog-writing-skills/issues/42) flags dead/drifted fixtures; [#46](https://github.com/wakqasahmed/blog-writing-skills/issues/46) flags a fragile hardcoded `validate.yml`. Building real outcome scoring for all 17 skills is a from-scratch job, not a bug fix.

### Fund the real harness runs

This repo is one of five in the same public skills portfolio going through the same outcome-eval build-out. The full portfolio-wide cost breakdown, funding links, and per-repo targets live in [`email-marketing-skills`'s README](https://github.com/wakqasahmed/email-marketing-skills#fund-the-real-harness-runs) — this repo's share of that shared $300 target is $90 (largest share: 17 skills, most work needed).
