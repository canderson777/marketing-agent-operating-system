# Workflow: Weekly Content Engine

Use this when you want a repeatable publishing rhythm that turns one strong weekly idea into a multi-channel content wave.

## Goal

Ship one core asset per week, repurpose it cleanly, keep social and email active, and create a review rhythm that improves the next week.

## Default Cadence

| Day | Activity |
|---|---|
| Monday | Plan and brief the week |
| Tuesday | Outline and draft the core asset |
| Wednesday | Edit, optimize, and publish |
| Thursday | Repurpose into channel assets |
| Friday | Send newsletter and review the week |

## Step 1 - Plan And Brief

- Owner: `../agents/05-content-marketing/content-marketing-agent.md`
- Pull the next topic from the content plan.
- Confirm audience, CTA, content pillar, and offer.
- If search matters, confirm topic fit with `../agents/03-seo-aeo/seo-aeo-agent.md`.
- Reserve social slots for the week.

## Step 2 - Outline To Draft

- `../agents/03-seo-aeo/blog-outline-agent.md` or `../agents/05-content-marketing/video-script-agent.md` builds the first structure.
- `../agents/05-content-marketing/blog-agent.md` or `../agents/05-content-marketing/video-script-agent.md` creates the core draft.
- Internal links, proof, and CTA are planned before final review.

## Step 3 - Edit, Optimize, Publish

- `../agents/05-content-marketing/content-marketing-agent.md` reviews.
- `../agents/03-seo-aeo/on-page-seo-agent.md` handles pre-publish optimization when relevant.
- `../agents/03-seo-aeo/ai-answer-agent.md` checks answer-engine structure when relevant.
- Compliance checks any sensitive claims.

## Step 4 - Repurpose

- Owner: `../agents/05-content-marketing/repurposing-agent.md`
- Extract 5 to 10 strong atoms from the published asset.
- Adapt them into X, LinkedIn, Instagram, TikTok, short-form video, email, and optional ad-hook angles.
- Queue channel-specific review with the social or email sub-masters.

## Step 5 - Newsletter And Review

- `../agents/01-email-marketing/newsletter-agent.md` creates the newsletter issue, usually anchored to the week's core idea.
- `../agents/01-email-marketing/email-marketing-agent.md` reviews send quality.
- Weekly review captures pageviews, engagement, email performance, and standout atoms.

## Step 6 - Parallel Long-Lead Assets

These should keep moving without blocking the weekly engine:

- lead magnets
- case studies
- long-form video
- backlink outreach
- AI answer retrofits

## Output Format

```md
# Weekly Content Plan

## Weekly Theme
[Theme]

## Goal
[Goal]

## Core Asset
[Asset]

## Channel Assets
| Channel | Asset | CTA | Metric |
|---|---|---|---|

## Publishing Schedule
| Day | Asset | Owner |
|---|---|---|

## Weekly Review Notes
- [Insight]
```

## Output Location

- `outputs/blogs/[YYYY-MM-DD_slug].md`
- `outputs/social-posts/[YYYY-MM-DD_atom-slug].md`
- `outputs/emails/[YYYY-MM-DD_newsletter-slug].md`

## Kill Criteria

- If the cornerstone asset fails quality review, delay it instead of shipping weak content.
- If an atom underperforms across multiple channels, retire it and log the learning.
