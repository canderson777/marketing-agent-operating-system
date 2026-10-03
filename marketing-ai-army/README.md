# Marketing Agent Operating System

This is a markdown-based operating system for planning and producing marketing work with coordinated AI agents. It supports businesses, personal brands, creators, influencers, local services, SaaS products, ecommerce offers, newsletters, and early-stage ideas.

Use it when you want to turn a profile or goal into a practical marketing strategy, then delegate the work to specialized agents.

It can also selectively route work through external marketing tools when that improves execution, reporting, or scale.

## Quick Start

Start with `COMMANDS.md`, then paste `/marketing-system` at the top of your request and fill in the template fields.

If nothing pops up while you are typing `/marketing-system`, that is expected. It is a convention the Master Marketing Agent follows, not an app-level autocomplete command.

## Operating Model

The system has three levels:

1. `master-agent.md` - the only human-facing strategist and orchestrator.
2. Channel sub-master agents - translate strategy into channel-specific work.
3. Specialist agents - create narrow, high-quality deliverables.

The master agent owns goal clarification, strategy, prioritization, cross-agent routing, final review, and campaign packaging. Channel agents own their channel plans. Specialists own specific assets only.

## Start Here

Use one of these entry points:

- Universal command entry point: start with `COMMANDS.md`, then run `/marketing-system` with `shared/request-template.md`.
- Strategy for a business or person: start with `shared/client-profile-template.md`, then run `workflows/strategy-diagnostic-workflow.md`.
- A campaign request: start with `master-agent.md`, then use `shared/campaign-brief-template.md`.
- A known workflow: use the matching file in `workflows/`.
- A known channel task: use the relevant channel sub-master in `agents/`.

## File Map

- `master-agent.md` - top-level CMO and project manager.
- `COMMANDS.md` - command layer for routing requests through the system.
- `shared/` - source-of-truth docs used by every agent.
  - `shared/client-profile-template.md`
  - `shared/campaign-brief-template.md`
  - `shared/request-template.md`
  - `shared/tool-registry.md`
  - `shared/agent-communication-rules.md`
  - `shared/brand-voice.md`
  - `shared/customer-avatar.md`
  - `shared/offer-library.md`
  - `shared/content-rules.md`
  - `shared/compliance-rules.md`
  - `shared/metrics-dashboard.md`
- `agents/01-email-marketing/` - email sub-master and specialists.
- `agents/02-social-media/` - social sub-master and platform specialists.
- `agents/03-seo-aeo/` - SEO and AI-answer visibility agents.
- `agents/04-paid-ads/` - paid acquisition and testing agents.
- `agents/05-content-marketing/` - content strategy and asset agents.
- `agents/06-influencer-marketing/` - creator collaboration agent.
- `agents/07-affiliate-referral/` - referral and affiliate growth agent.
- `agents/08-direct-outreach/` - cold email, DM, and sales outreach agent.
- `agents/09-partnerships/` - business and community partnership agent.
- `agents/10-events-community/` - webinars, events, and community agent.
- `workflows/` - repeatable multi-agent playbooks.
  - `workflows/run-marketing-request.md` - universal master-agent intake and routing workflow.
  - `workflows/clickflow-integration.md` - SEO and organic reporting integration playbook.
  - `workflows/beehiiv-integration.md` - newsletter publishing and list operations playbook.
  - `workflows/higgsfield-integration.md` - visual generation and short-form creative playbook.
  - `workflows/social-campaign-brief-workflow.md` - reusable campaign brief and approval-gate workflow.
  - `workflows/short-form-reel-creative-workflow.md` - reusable Reel script, shot-list, prompt, and QA workflow.
  - `workflows/branded-carousel-workflow.md` - reusable 5–7 slide carousel structure and review workflow.
  - `workflows/meta-integration.md` - Meta campaign execution and reporting playbook.
  - `workflows/x-mcp-social-listening-review.md` - X MCP social listening, reply, bookmark, and weekly review playbook.
  - `workflows/multi-brand-validation-sprint.md` - prove the one-engine-many-brands model works across all the example brands.
  - `workflows/fable-project-review-loop.md` - how an AI reviews this system (or any project), improves it, and documents the pass.
- `outputs/` - finished deliverables grouped by asset type.

## Brand Layer

This engine serves every brand in `../brands/` (see `../brands/README.md` for the registry). Each request names a brand, and that brand's folder is loaded before any shared defaults. Brand files (`brand-voice.md`, `audience.md`, `offers.md`, `current-priorities.md`) override the equivalent `shared/` templates. Never copy this engine into a brand folder; brand folders hold context only.

## Required Shared Context

Every agent should load these before producing work:

0. `../brands/<brand>/` - the brand context folder for this request. Loads first and wins conflicts.
1. `shared/client-profile-template.md` or the completed client profile.
2. `shared/campaign-brief-template.md` or the completed campaign brief.
3. `shared/brand-voice.md`.
4. `shared/customer-avatar.md`.
5. `shared/offer-library.md`.
6. `shared/content-rules.md`.
7. `shared/compliance-rules.md`.
8. `shared/agent-communication-rules.md`.
9. `shared/metrics-dashboard.md`.
10. `shared/tool-registry.md` when external tools may improve the workflow.

If a shared file is missing or incomplete, the agent must label assumptions before continuing.

## Communication Rules

All agent messages use this standard format:

```md
TO: [Agent or Master]
FROM: [Agent or Master]
TASK: [One clear task]
CONTEXT: [Relevant brief/profile facts]
INPUTS: [Files, assets, or prior outputs used]
OUTPUT: [Deliverable or requested deliverable]
STATUS: Complete / Needs More Info / Blocked / Draft
BLOCKERS: [Missing inputs or risks]
NEXT ACTION: [One practical next step]
```

The master agent owns cross-agent handoffs. Specialists do not independently redirect work unless a workflow explicitly allows it.

## External Tool Layer

The system can use external tools through a selective routing layer.

- Use `shared/tool-registry.md` to decide whether a tool fits the request.
- Prefer normal markdown planning when a tool adds no real execution advantage.
- Name any tool used in the final package along with why it was selected.
- Fall back to the normal workflow if a tool is unavailable.

## Common Workflows

- Strategy diagnostic for a new business or personal brand.
- Weekly content engine.
- X social listening and weekly review.
- Campaign launch.
- Lead generation sprint.
- Product or offer launch.
- Reporting and optimization review.
- Local service lead generation.
- Creator monetization plan.
- Newsletter growth plan.
- Referral or affiliate program setup.
- Partnership outreach.
- Webinar or community event launch.

## Output Convention

Place finished work in `outputs/` by asset type:

- `outputs/campaigns/`
- `outputs/emails/`
- `outputs/social-posts/`
- `outputs/blogs/`
- `outputs/ads/`
- `outputs/reports/`

Filename format (brand slug required - every brand shares this tree):

```txt
YYYY-MM-DD_<brand>_short-slug.md
```

Strategy docs, plans, and proof notes do not go in `outputs/`. They live with the brand: `../brands/<brand>/strategy/` and `../brands/<brand>/proof-notes/`. See `../docs/second-brain-map.md` for the full map of where everything lives.

## Quality Standard

Before final delivery, every agent checks:

- The work supports the stated goal.
- The audience and offer are clear.
- The CTA is specific.
- The channel format fits the channel.
- Claims are compliant and supported.
- Metrics are defined.
- Handoffs are documented.
- Assumptions are labeled.
