# AI Handoff

Context for any AI model (or human) picking up this project. Read this, then `docs/second-brain-map.md`, then start working. Do not ask the operator to re-explain the system.

## What This Project Is

A markdown-based marketing operating system with two layers:

- `marketing-ai-army/` - a shared, brand-agnostic execution engine: one master agent (`master-agent.md`), channel sub-master agents, specialist agents, workflows, and shared templates. Requests enter via the `/marketing-system` convention in `COMMANDS.md`.
- `brands/` - one context folder per business the engine markets for. Each folder holds that brand's audience, offers, voice, priorities, and ideas.

There is no code to build and no tests to run. Validation means checking that referenced paths exist and that conventions are followed.

## The Business Goal

1. Use one engine to run marketing for several brands instead of rebuilding a system per brand.
2. Turn it into a sellable productized / managed service: a new client = a new brand folder, the engine never gets duplicated.
3. Proof notes (`brands/<brand>/proof-notes/`) are the sales ammunition - real work, dated, with results.

The engine is infrastructure. Spend effort making it work across brands, not polishing agent prose.

## Operating Rules for an AI Working Here

1. One engine, many brand folders. Never copy `marketing-ai-army/` per brand or per client.
2. Load `brands/<brand>/` before `shared/` defaults; brand files win conflicts.
3. If a brand's context files are placeholders, stop and ask (or label everything DRAFT WITH ASSUMPTIONS). Do not invent business facts for a brand.
4. Follow the output homes in `docs/second-brain-map.md`. Date and brand-slug every saved file.
5. After meaningful work, write a proof note (`brands/<brand>/proof-notes/`).
6. When you improve the system itself, follow `marketing-ai-army/workflows/fable-project-review-loop.md` and update this handoff doc's "Current State" section.
7. Never commit secrets. No API keys, tokens, passwords, or private credentials in any file.

## Where to Start for Common Jobs

- Run any marketing request: `marketing-ai-army/workflows/run-marketing-request.md`.
- Weekly content for a brand: `marketing-ai-army/workflows/weekly-content-engine.md`.
- Prove the multi-brand model: `marketing-ai-army/workflows/multi-brand-validation-sprint.md`.
- Review and improve this system: `marketing-ai-army/workflows/fable-project-review-loop.md`.
- Onboard a brand cold: `marketing-ai-army/workflows/brand-intake-grill.md`.

## Current State

- Engine routing is internally consistent - all agent file references in workflows resolve.
- Brand-awareness is built in: `master-agent.md` has a "Brand Context First" section, `COMMANDS.md` has a required `BRAND:` field, and output filenames use `YYYY-MM-DD_<brand>_slug.md`.
- Every workflow has a markdown-only fallback; do not block on external tools.

## Open Items the Owner Must Decide

- Pick ONE brand to run the full loop end-to-end as the first sellable case study.
- Decide which external tools (email, ads, analytics, image generation) to connect, and where their credentials live (never in this repo).
- Keep the public template free of any client-specific or personal context.
