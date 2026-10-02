# Workflows And Usage Guide

Use this file as the quick-start guide for the Marketing Agent Operating System.

## How To Use The System

1. Start with `master-agent.md`.
2. Fill out `shared/client-profile-template.md` for the business, creator, influencer, founder, or personal brand.
3. Run `workflows/strategy-diagnostic-workflow.md` to get recommended strategies.
4. Pick the best strategy and create a campaign brief with `shared/campaign-brief-template.md`.
5. Let the master agent assign the right agents.
6. Review agent outputs using the master agent review gates.
7. Save finished assets in the matching `outputs/` folder.

## Current Workflows

| Workflow | Use When You Need |
|---|---|
| `workflows/continuous-optimization-loop.md` | A closed-loop experiment cycle for any channel. |
| `workflows/seo-optimization-loop.md` | SEO improvement using Search Console data and one controlled page change. |
| `workflows/strategy-diagnostic-workflow.md` | A ranked marketing strategy for a business, creator, influencer, founder, or personal brand. |
| `workflows/campaign-launch.md` | A launch-ready campaign with assets, assignments, review gates, and metrics. |
| `workflows/weekly-content-engine.md` | A repeatable weekly content plan across social, email, blog, and video. |
| `workflows/lead-generation.md` | More leads, booked calls, demos, signups, inquiries, or qualified conversations. |
| `workflows/product-launch.md` | A product, offer, service, course, community, or creator monetization launch. |
| `workflows/podcast-to-content.md` | A podcast, interview, or transcript that should become blog, social, email, or video assets. |
| `workflows/reporting-review.md` | A post-campaign or weekly/monthly performance review with next experiments. |
| `workflows/x-mcp-social-listening-review.md` | X/Twitter social listening, reply queues, bookmark idea inboxes, and weekly post-performance review using X MCP when connected. |
| `workflows/run-marketing-request.md` | The default intake: turn any messy request into a routed, brand-aware plan. |
| `workflows/multi-brand-validation-sprint.md` | Proof that one engine serves all five brands - also the client-onboarding dress rehearsal. |
| `workflows/fable-project-review-loop.md` | An AI reviewing and improving this system itself, with documentation the next model can pick up. |

## Workflow Order For Most Projects

Use this default order:

1. `shared/client-profile-template.md`
2. `workflows/strategy-diagnostic-workflow.md`
3. `shared/campaign-brief-template.md`
4. One execution workflow:
   - `workflows/campaign-launch.md`
   - `workflows/weekly-content-engine.md`
   - `workflows/lead-generation.md`
   - `workflows/product-launch.md`
   - `workflows/podcast-to-content.md`
5. `workflows/reporting-review.md`

## Which Workflow To Pick

- Running a continuous optimization loop in any channel: use `workflows/continuous-optimization-loop.md`.
- SEO improvement using Search Console data and one controlled change: use `workflows/seo-optimization-loop.md`.
- New business or personal brand: use `workflows/strategy-diagnostic-workflow.md`.
- Need ideas and a plan: use `workflows/strategy-diagnostic-workflow.md`.
- Need sales or signups fast: use `workflows/lead-generation.md`.
- Need consistent content: use `workflows/weekly-content-engine.md`.
- Need live X/Twitter context, reply ideas, bookmark mining, or weekly X review: use `workflows/x-mcp-social-listening-review.md`.
- Launching something new: use `workflows/product-launch.md`.
- Promoting an existing offer: use `workflows/campaign-launch.md`.
- Need to turn a podcast or interview into content: use `workflows/podcast-to-content.md`.
- Finished a campaign and need decisions: use `workflows/reporting-review.md`.

## Updating The System

Keep these files updated as the business or person changes:

- `shared/client-profile-template.md` - audience, offer, platforms, metrics, goals, constraints.
- `shared/brand-voice.md` - tone, phrases to use, phrases to avoid.
- `shared/customer-avatar.md` - audience pains, desires, objections, and triggers.
- `shared/offer-library.md` - products, services, pricing, CTAs, proof, and objections.
- `shared/metrics-dashboard.md` - current numbers and campaign results.

After each campaign, update:

- What shipped.
- What worked.
- What did not work.
- Best-performing channels.
- New proof, testimonials, or results.
- Next experiments.

## Harvesting Custom Workflows

When a business, brand, or entrepreneur gets a workflow built specifically for them, bring it back into the master system if it can help other projects.

Use this habit:

1. Check that business folder's `workflows/` directory.
2. Identify net-new workflows or useful upgrades to existing ones.
3. Remove client-specific details unless they belong in the workflow as an example.
4. Add the cleaned workflow to the master `workflows/` folder.
5. Update this guide and `README.md` if the new workflow becomes part of the core library.
6. If the workflow writes to a new output type, add the matching folder under `outputs/`.

Good times to do this:

- after a launch
- after a campaign wrap-up
- after a new content system is created
- once per month as a library cleanup pass

## Communication Rule

All agents should use this format:

```md
TO:
FROM:
TASK:
CONTEXT:
INPUTS:
OUTPUT:
STATUS:
BLOCKERS:
NEXT ACTION:
```

## Simple Operating Habit

Before work starts, ask:

- Who is this for?
- What are we promoting?
- What action do we want?
- Which workflow fits?
- Which agents are actually needed?
- How will we measure success?

If any answer is missing, the master agent should make a clear assumption or ask for the missing detail.
