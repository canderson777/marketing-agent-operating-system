# Marketing Agent Operating System

**A ready-to-use marketing team that lives in a folder of markdown files.**

You bring a business, a goal, and some context. The system brings the strategy, the
workflows, the channel specialists, and the review process. Any AI assistant that can read
files — Hermes, Claude, Cursor, Codex, and others — can run it.

![no build step](https://img.shields.io/badge/build-none%20needed-2ea44f)
![plain markdown](https://img.shields.io/badge/format-markdown-000000)
![works with any AI](https://img.shields.io/badge/works%20with-any%20AI%20assistant-blue)
![license MIT](https://img.shields.io/badge/license-MIT-lightgrey)

---

## What this is (in plain English)

Most people use AI for marketing by typing one-off prompts and hoping for the best. That
produces generic copy, forgotten context, and no repeatable process.

This is the opposite of that. It is a small, organized system of text files:

- **One master agent** that acts like a marketing director. It asks the right questions,
  picks a plan, and hands work to specialists.
- **Specialist agents** for each channel — email, social, SEO, ads, content, outreach, and more.
- **Workflows** — step-by-step playbooks for common jobs (launch a campaign, write a week of
  content, find leads, review results).
- **Brand folders** — one folder per business, holding that business's audience, offers,
  voice, and goals. The engine is shared; only the context changes.

No apps to install. No database. No build step. It is just markdown, so it is easy to read,
easy to edit, and easy to hand to an AI.

> **The core idea:** write the system once, reuse it for every brand. A new client means a
> new folder, not a new system.

## How it works

```txt
You  ──►  Master agent (marketing director)
                 │
                 ├─►  Brand folder  (audience, offers, voice, goals)
                 │
                 ├─►  Workflow      (the playbook for this job)
                 │
                 └─►  Channel agents + specialists
                              │
                              ▼
                    Drafts, plans, campaigns  ──►  You review & approve
```

Every request follows the same shape:

1. **Name the brand** you are working on.
2. The master agent **loads that brand's context** first.
3. It **picks a workflow** and only the agents that job needs.
4. You get a **finished deliverable plus a short plan**, and you stay in control of what ships.

---

## Table of contents

- [Quick start](#quick-start)
- [Add it to your AI tool](#add-it-to-your-ai-tool)
- [Skills you can use](#skills-you-can-use)
- [Workflows you can use](#workflows-you-can-use)
- [Example: you already have a business](#example-you-already-have-a-business)
- [Example: you are starting something new](#example-you-are-starting-something-new)
- [What's in the repo](#whats-in-the-repo)
- [Screenshots](#screenshots)
- [Safety and privacy](#safety-and-privacy)

---

## Quick start

1. **Download or clone this repo.**
2. **Open the folder in your AI tool** (see the next section).
3. **Paste a request** using this simple template and fill in the blanks:

```md
/marketing-system

BRAND:        acc-network
GOAL:         grow newsletter subscribers this week
AUDIENCE:     beginners curious about AI
OFFER:        a free weekly AI newsletter
CTA:          subscribe
CHANNELS:     X, LinkedIn, email
CONSTRAINTS:  beginner-friendly, no hype, no jargon
OUTPUT:       a weekly content plan with post drafts
```

The master agent reads `marketing-ai-army/master-agent.md`, loads the matching folder in
`brands/`, and runs the right workflow.

> `/marketing-system` is not a built-in app button. It is a plain-text convention the master
> agent recognizes. If nothing autocompletes while you type it, that is expected.

## Add it to your AI tool

The whole system is just files, so any assistant that can read your project folder can use it.
Point the assistant at `marketing-ai-army/master-agent.md` and you are done.

| Tool | How to connect it | First message to send |
|---|---|---|
| **Hermes Agent** | Drop the folder into your workspace. Hermes reads project files directly. | `Read marketing-ai-army/master-agent.md, then run /marketing-system for acc-network` |
| **Claude (Projects or Claude Code)** | Create a Project and add the repo files as project knowledge, or open the folder in Claude Code. | `Use marketing-ai-army/master-agent.md as your instructions. /marketing-system for local-glow-up` |
| **Cursor** | Open the folder as your workspace. Add a project rule that points to the master agent. | `Follow marketing-ai-army/master-agent.md. Plan a week of content for prep2eat.` |
| **Codex / other CLI agents** | Open the repo in the tool's working directory. | `Read marketing-ai-army/master-agent.md and COMMANDS.md, then help me launch a campaign.` |
| **Anything else** | Any AI that can read files: paste `master-agent.md` into the system prompt, or attach the `marketing-ai-army/` folder. | `Act as the master agent. Ask me for the missing details, then give me a plan.` |

**Tip:** the more real context you give a brand folder, the better the output. Start with the
five files listed in `brands/README.md` (business overview, offers, audience, voice,
priorities).

## Skills you can use

Skills are capabilities the system can bring to a job. You do not need all of them — the master
agent pulls in only what fits. A few of the most useful ones:

| Skill | What it does for you |
|---|---|
| **Strategy diagnostic** | Turns a business or idea into a ranked, practical marketing plan with first actions. |
| **Content engine** | Turns one theme or offer into a week of posts, emails, and articles. |
| **Lead generation** | Finds and qualifies prospects, then drafts outreach you can personalize. |
| **Local visibility audit** | Reviews a local business's website, search, and conversion gaps in plain English. |
| **Newsletter growth** | Plans and writes issues that grow and keep subscribers. |
| **Product / offer launch** | Builds a full launch: messaging, channels, sequence, and checklist. |
| **Social repurposing** | Adapts one piece of content into native posts for each platform. |
| **Paid ads** | Writes and structures ad copy and testing plans. |
| **Reporting and review** | Reads results and turns them into the next round of tests. |
| **Proof capture** | Turns real work into dated receipts you can reuse as case studies. |

## Workflows you can use

Workflows are the step-by-step playbooks. These live in `marketing-ai-army/workflows/`. A
selection:

| Workflow | Use it when |
|---|---|
| `run-marketing-request.md` | You have any request and want the system to route it for you. |
| `strategy-diagnostic-workflow.md` | You need a strategy before you make assets. |
| `weekly-content-engine.md` | You want a repeatable weekly content system. |
| `campaign-launch.md` | You know the offer and need a launch-ready campaign. |
| `product-launch.md` | You are launching a product, service, course, or newsletter. |
| `lead-generation.md` | You need leads, booked calls, or qualified conversations. |
| `business-search-finder.md` | You want a vetted local-prospect list for one city and vertical. |
| `seo-optimization-loop.md` | You want to improve a site's search and AI-answer visibility. |
| `social-campaign-brief-workflow.md` | You need a clean brief before writing social copy. |
| `short-form-reel-creative-workflow.md` | You need a reel script, shot list, and prompt. |
| `branded-carousel-workflow.md` | You need a slide carousel built and reviewed. |
| `podcast-to-content.md` | You have a podcast or transcript and want to repurpose it. |
| `reporting-review.md` | A campaign already ran and you need what happened next. |
| `new-brand-setup.md` / `brand-intake-grill.md` | You are onboarding a brand from scratch. |

## Example: you already have a business

**Situation:** you run a local service business. You have a website and a few social profiles,
but leads are inconsistent.

```md
/marketing-system

BRAND:        local-glow-up
GOAL:         book more free visibility audits this month
AUDIENCE:     local business owners who depend on calls and bookings
OFFER:        a free visibility audit
CTA:          book the audit
CHANNELS:     Facebook, email, direct outreach
CONSTRAINTS:  plain English, no fear-based claims
OUTPUT:       a 2-week plan with a post schedule and an outreach message
```

**What happens next:** the master agent loads your brand folder, runs a lead-generation plan,
writes the posts and outreach, and gives you a checklist. You review, approve, and publish —
nothing goes live without you.

## Example: you are starting something new

**Situation:** you have an idea — an app, a newsletter, a course — and no audience yet.

```md
/marketing-system

BRAND:        prep2eat
GOAL:         get the first 100 users before launch
AUDIENCE:     busy people who want easy, healthy meal plans
OFFER:        an AI meal-planning app
CTA:          join the waitlist
CHANNELS:     (not sure yet — recommend some)
CONSTRAINTS:  pre-launch, small budget
OUTPUT:       a launch strategy, then a first week of content
```

**What happens next:** the master agent runs the strategy diagnostic, recommends two or three
channels that fit a pre-launch product, defines the working audience, and gives you a first-week
action list — smallest useful version first.

## What's in the repo

```txt
marketing-agent-operating-system/
├─ README.md                  ← you are here
├─ marketing-ai-army/         the engine (brand-agnostic)
│  ├─ master-agent.md         the marketing director
│  ├─ COMMANDS.md             how to send requests
│  ├─ WORKFLOWS-AND-USAGE.md  how to use and extend it
│  ├─ agents/                 channel agents + specialists
│  ├─ shared/                 templates and rules used by every agent
│  ├─ workflows/              step-by-step playbooks
│  └─ outputs/                finished deliverables, grouped by type
├─ brands/                    one context folder per business
│  ├─ README.md               how brand folders work
│  ├─ acc-network/
│  ├─ local-glow-up/
│  ├─ prep2eat/
│  └─ scholarship-dashboard/
└─ docs/                      orientation docs for you and your AI
```

- **The engine** (`marketing-ai-army/`) is written once and reused.
- **The context** (`brands/`) is the only thing that changes per business.
- **The map** (`docs/`) explains where everything goes.

## Screenshots

_Placeholders below — real screenshots coming soon._

| Preview | What it shows |
|---|---|
| `docs/screenshots/PLACEHOLDER-system-overview.png` | The full system at a glance |
| `docs/screenshots/PLACEHOLDER-request-in-chat.png` | Sending a `/marketing-system` request |
| `docs/screenshots/PLACEHOLDER-output.png` | A finished content plan |
| `docs/screenshots/PLACEHOLDER-brand-folder.png` | A brand context folder |

<!--
To add real screenshots later:
1. Put the image files in docs/screenshots/
2. Replace the placeholder paths above with the real file names.
3. Use:  ![alt text](docs/screenshots/your-file.png)
-->

## Safety and privacy

This is designed to be safe to keep in a public repo and safe to share as a template.

- **No secrets.** No API keys, tokens, passwords, or credentials live in these files.
  `.gitignore` blocks common secret and environment files.
- **No personal or client data.** Brand folders here contain marketing context only — no
  customer records, no private notes, no contact lists.
- **You approve what ships.** Publishing, outreach, and spending always require your explicit
  go-ahead. The system drafts; you decide.
- **One engine, many brands.** Keep client-specific context in that client's brand folder, and
  never copy the engine into a brand.

---

### Status

Early and actively evolving. The structure and workflows are stable; the brand folders are
examples you can copy and replace with your own.

**License:** MIT — use it, fork it, adapt it.
