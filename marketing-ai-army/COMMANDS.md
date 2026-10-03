# Marketing System Commands

This file turns the Marketing Agent Operating System into a command-driven workflow.

Use these commands in a chat or prompt block. They are operating conventions for the system, not terminal commands.

Every command starts with the Master Marketing Agent unless the command says otherwise.

## Core Rule

1. Start at `master-agent.md`.
2. Identify the brand and load its folder from `../brands/<brand>/` first, then the right shared context. Brand files override shared defaults.
3. Choose the best workflow or department.
4. Assign only the agents needed.
5. Review outputs through the master agent.
6. Package the final deliverable.

## Best Starting Command

Use `/marketing-system` when you are not sure which workflow to run.

It is the universal entry point.

## Quick Start

`/marketing-system` is a prompt convention, not a built-in slash command with autocomplete.

Use it by pasting it at the top of your request, then fill in the template below. If your chat surface does not suggest anything while typing it, that is normal.

Example:

```md
/marketing-system

BRAND: acc-network
PROJECT: Marketing Agent Operating System
GOAL: Explain or execute a marketing request
AUDIENCE: Founders, builders, operators
OFFER: My marketing operating system
CTA: Follow, reply, or request a workflow
CHANNELS: X, LinkedIn, email
ASSETS: Screenshots, docs, notes, transcripts
CONSTRAINTS: Match my voice, no em dashes
TOOLS: Keep it markdown-only unless a tool clearly helps
DATA SENSITIVITY: Normal
OUTPUT: One packaged answer or deliverable
```

## Command List

### `/marketing-system`

Use when:
- You have a marketing request and want the master agent to route it.
- You are unsure which workflow or department should handle it.
- You want one packaged answer instead of manually choosing agents.

What it does:
- Starts with the Master Marketing Agent.
- Reviews the request.
- Picks the best workflow, channels, and agents.
- Decides whether the work stays markdown-only or uses an approved external tool from `shared/tool-registry.md`.
- Returns a final package or a structured work plan.

### `/strategy-diagnostic`

Use when:
- You need a ranked strategy for a business, founder, creator, or personal brand.
- You need channel recommendations, first actions, and a roadmap.

What it does:
- Runs `workflows/strategy-diagnostic-workflow.md`.
- Uses the client profile as the main intake document.

### `/campaign-launch`

Use when:
- You already know the offer and want a launch-ready campaign.
- You need assignments, assets, review gates, and a reporting plan.

What it does:
- Runs `workflows/campaign-launch.md`.
- Uses the campaign brief as the main planning document.

### `/weekly-content`

Use when:
- You want a weekly content system across social, email, blog, and video.
- You have one theme or offer and want it repurposed well.

What it does:
- Runs `workflows/weekly-content-engine.md`.
- Routes work through content, social, email, and SEO/AEO as needed.

### `/lead-generation`

Use when:
- You need leads, booked calls, demos, signups, or qualified conversations.
- You want outreach, partnerships, content, or organic lead plays.

What it does:
- Runs `workflows/lead-generation.md`.
- Pulls in outreach, social, content, partnerships, and email where relevant.

### `/product-launch`

Use when:
- You are launching a product, service, offer, course, newsletter, or community.
- You need a more complete launch plan than a single campaign push.

What it does:
- Runs `workflows/product-launch.md`.
- Builds a broader launch package with multiple channel dependencies.

### `/reporting-review`

Use when:
- A campaign already ran and you need to know what happened next.
- You want optimization ideas, next tests, and a post-campaign review.

What it does:
- Runs `workflows/reporting-review.md`.
- Packages results, findings, risks, and next experiments.

### `/linkedin-post`

Use when:
- You need a professional LinkedIn post.
- You want the social team to adapt a topic for LinkedIn.

What it does:
- Starts with the Master Marketing Agent.
- Routes to the Social Media Agent and LinkedIn Agent.
- Pulls in content strategy if source material needs shaping first.

### `/x-thread`

Use when:
- You need an X thread, X post pack, or platform-native X copy.
- You want punchy, opinionated social content.

What it does:
- Starts with the Master Marketing Agent.
- Routes to the Social Media Agent and X/Twitter Agent.
- Pulls in content strategy if source material needs shaping first.

### `/email-campaign`

Use when:
- You need a campaign email, promo sequence, newsletter, or lifecycle flow.
- The list, offer, and CTA already exist or can be inferred.

What it does:
- Starts with the Master Marketing Agent.
- Routes to the Email Marketing Agent and the right specialist.

### `/blog-post`

Use when:
- You need a blog article, outline, repurposed article, or authority asset.
- The content may also need SEO/AEO support.

What it does:
- Starts with the Master Marketing Agent.
- Routes to Content Marketing and SEO/AEO when needed.

### `/Business Search For:`

Use when:
- You need a vetted prospect list for a local-business vertical in one city.
- You want ranked audit targets, not raw search results.

What it does:
- Runs `workflows/business-search-finder.md`.
- Finds, qualifies, and scores prospects; outputs a review table + CSV before any Sheet write.
- Appends approved rows to the brand's lead tracker (append-only), or delivers an import-ready CSV as fallback.

Format: `/Business Search For: [vertical] in [location]` — full template in `workflows/business-search-finder/run-prompt-template.md`.

## Recommended Input Format

Use this shape with any command:

```md
/marketing-system

BRAND: [Folder name under brands/ - acc-network, local-glow-up, prep2eat]
PROJECT: [Business, brand, person, or offer]
GOAL: [What needs to happen]
AUDIENCE: [Who this is for]
OFFER: [What is being promoted]
CTA: [Exact action wanted]
CHANNELS: [LinkedIn, X, email, blog, etc.]
ASSETS: [Screenshots, notes, links, transcripts, docs]
CONSTRAINTS: [Tone, compliance, deadlines, budget, bans]
TOOLS: [Optional preferred tools or banned tools]
DATA SENSITIVITY: [Normal or sensitive]
OUTPUT: [What deliverable you want back]
```

## Fast Examples

### Example 1

```md
/marketing-system

BRAND: acc-network
PROJECT: Marketing Agent Operating System
GOAL: Announce the system and explain how it works
AUDIENCE: Founders, builders, and AI-curious operators
OFFER: Personal operating system for marketing execution
CTA: Follow along and ask about the build
CHANNELS: X, LinkedIn
ASSETS: Folder screenshots, agent docs, journal notes
CONSTRAINTS: Match my voice, no em dashes
TOOLS: Keep it markdown-only
DATA SENSITIVITY: Normal
OUTPUT: X article, LinkedIn post, cover image prompt
```

### Example 2

```md
/weekly-content

BRAND: acc-network
PROJECT: ACC Network
GOAL: Grow newsletter subscribers this week
AUDIENCE: Beginners curious about AI
OFFER: Weekly AI newsletter
CTA: Subscribe
CHANNELS: X, LinkedIn, email, blog
ASSETS: Last newsletter, top 5 links, glossary page
CONSTRAINTS: Beginner-friendly, practical, no hype
TOOLS: beehiiv if newsletter publishing is part of the deliverable
DATA SENSITIVITY: Normal
OUTPUT: Weekly content plan with post drafts
```

## Command Selection Guide

- Use `/marketing-system` if you want the system to decide.
- Use `/strategy-diagnostic` if you need the strategy before the assets.
- Use `/campaign-launch` if the strategy is known and the campaign needs to ship.
- Use `/weekly-content` if the request is primarily content production.
- Use `/reporting-review` if the work already ran and now needs analysis.

## What Good Output Looks Like

The final output should include:

- The chosen workflow.
- The agents used.
- Any external tools used and why.
- Key assumptions.
- The finished deliverable or campaign package.
- Metrics or success criteria.
- The next action.
