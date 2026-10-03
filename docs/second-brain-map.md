# Second Brain Map

One-page answer to "where does this go?" for the Marketing Agent Operating System. If a file does not fit one of these homes, question whether it should exist.

## The Two-Layer Model

```txt
Marketing Agent Operating System/
  marketing-ai-army/    THE ENGINE  - how marketing gets done (brand-agnostic)
  brands/               THE CONTEXT - who marketing is done for (one folder per brand)
  docs/                 THE MAP     - orientation docs for humans and AI operators
```

The engine is written once and reused. Brand folders are the only thing that changes per business. This split is the product: a new client = a new brand folder, nothing else.

## Where Each Thing Lives

| Thing | Home | Example |
|---|---|---|
| Marketing strategy for a brand | `brands/<brand>/strategy/` | `brands/local-glow-up/strategy/2026-09-04-facebook-ad-test-plan.md` |
| Brand context (voice, audience, offers, priorities) | `brands/<brand>/*.md` | `brands/acc-network/brand-voice.md` |
| Proof of work / results / receipts | `brands/<brand>/proof-notes/` | `brands/acc-network/proof-notes/2026-07-18-newsletter-automation.md` |
| Reusable workflows (how-to playbooks) | `marketing-ai-army/workflows/` | `workflows/weekly-content-engine.md` |
| Agent role definitions | `marketing-ai-army/agents/<category>/` | `agents/02-social-media/x-twitter-agent.md` |
| Reusable prompts and templates | `marketing-ai-army/shared/` | `shared/campaign-brief-template.md`, `shared/request-template.md` |
| Finished channel assets (posts, emails, blogs, ads) | `marketing-ai-army/outputs/<type>/` | `outputs/social-posts/2026-07-07_acc-network_launch-thread.md` |
| Performance reviews and reports | `marketing-ai-army/outputs/reports/{weekly,monthly,quarterly}/` | `outputs/reports/weekly/2026-06-18_tool-registry-kickoff.md` |
| Tool/integration decisions | `marketing-ai-army/shared/tool-registry.md` | one registry, per-tool status |
| Orientation for a new AI or human operator | `docs/` | `docs/ai-handoff.md` |

## Naming Rules

- Dated files everywhere: `YYYY-MM-DD-slug.md` (brand folders) or `YYYY-MM-DD_<brand>_slug.md` (shared `outputs/` tree - brand slug required because every brand shares it).
- Brand folder names are the canonical brand IDs: `acc-network`, `local-glow-up`, `prep2eat`.

## The Flow of a Piece of Work

1. A request arrives with a `BRAND:` field (`marketing-ai-army/COMMANDS.md`).
2. The master agent loads `brands/<brand>/` context, then the shared templates (`marketing-ai-army/master-agent.md`, "Brand Context First" section).
3. A workflow from `marketing-ai-army/workflows/` runs with only the agents it needs.
4. Plans and calendars land in `brands/<brand>/strategy/`. Finished assets land in `marketing-ai-army/outputs/<type>/`.
5. When the work produces a real result, write a proof note in `brands/<brand>/proof-notes/` - these are the raw material for case studies and sales pages.
6. Anything reusable learned along the way gets folded back into `workflows/` or `shared/` (see "Harvesting Custom Workflows" in `marketing-ai-army/WORKFLOWS-AND-USAGE.md`).

## What Does NOT Belong Where

- No engine copies inside brand folders. Brand folders hold context and brand-specific outputs only.
- No brand-specific voice or strategy in `shared/`. Shared files are fallback templates only; a brand's own files always win.
- No large binary archives inside the engine. Raw exports and media archives are reference material, not system files - keep them outside the repo.
- No untitled or undated working files. If it is worth saving, it gets a date and a slug.
- No secrets. No API keys, tokens, passwords, or private credentials in any committed file (see `.gitignore`).

## External Sources That Feed the System

- A daily journal or notes doc can be the primary content fuel for a personal brand (see the brand's `content-source-workflow.md` if present).
- Product repos (for example a live site or app) are linked from the brand README, never copied in.
