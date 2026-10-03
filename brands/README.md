# Brands Workspace

This directory holds brand-specific context folders that feed the shared `marketing-ai-army` engine.

One engine, many brands. A new client or project means a new folder here, nothing else.

## Brands

| Brand | What it is | Status |
|---|---|---|
| `acc-network` | Daily AI newsletter + blog that teaches beginners to use AI without hype. Live at accnetwork.xyz. | READY |
| `local-glow-up` | Local-business lead-capture and website-visibility service. Live at localglowup.com. | READY |
| `prep2eat` | AI recipe / meal-planning app. Pre-launch. | PARTIAL |

## Rule

Keep one shared marketing system. Update these brand folders as the source of truth for each business. Never copy the `marketing-ai-army` engine into a brand folder.

## Minimum Viable Brand Context

The engine cannot produce on-brand work until a brand folder has real content (not template placeholders) in at least:

1. `business-overview.md` - what it is, what it sells, who it is for.
2. `offers.md` - the current offer and exact CTA.
3. `audience.md` - primary audience and their pain points.
4. `brand-voice.md` - voice summary plus 3 to 5 do/don't rules.
5. `current-priorities.md` - what matters right now, with a date at the top.

If any of these are blank, agents must stop and ask for them or label the whole output DRAFT WITH ASSUMPTIONS.

## Standard Brand Folder Layout

```txt
brands/<brand>/
  README.md               - what this brand is and file map
  business-overview.md    - positioning and stage
  audience.md             - who it serves
  offers.md               - offers and CTAs
  brand-voice.md          - tone and voice rules
  content-pillars.md      - recurring content themes
  goals.md                - current / 30-day / 90-day goals
  current-priorities.md   - what is active right now (dated)
  ideas.md                - backlog of content and campaign ideas
  hermes.md               - project-instruction file agents read to load this brand cold
  positions/three-ps.md   - the Person / Pain / Promise this brand markets to
  links-and-assets.md     - live links, CTAs, and where the assets live
  assets/                 - reusable visual assets (logos, guidelines, product shots, social)
  strategy/               - dated plans and content packages produced FOR this brand
  proof-notes/            - dated receipts of real work and results (fuel for case studies)
```

Create `assets/`, `strategy/`, and `proof-notes/` the first time the engine produces an asset, a plan, or a result worth recording for that brand - do not pre-create empty folders.

## Where Outputs Go

- Plans, calendars, and content packages for a brand: `brands/<brand>/strategy/YYYY-MM-DD-slug.md`
- Finished channel assets (posts, emails, blogs, ads): `marketing-ai-army/outputs/<type>/YYYY-MM-DD_<brand>_slug.md` - the brand slug in the filename is required so every brand can share one outputs tree.
- Results and receipts: `brands/<brand>/proof-notes/YYYY-MM-DD-slug.md`
