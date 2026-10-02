# Multi-Brand Validation Sprint

Prove that ONE engine can run marketing for all five brands without duplication. This sprint is also the dress rehearsal for selling the system: if a brand folder can be onboarded and produce usable output in under an hour, a paying client can too.

Brands under test: `your-brand`, `acc-network`, `local-glow-up`, `prep2eat`, `scholarship-dashboard`.

## Success Criteria

The sprint passes when, for every brand:

1. The brand folder meets the Minimum Viable Brand Context checklist in `../../brands/README.md` (or is explicitly parked with a reason).
2. The same command template (`COMMANDS.md` with a `BRAND:` field) produces a usable deliverable with zero edits to any engine file.
3. Output lands in the right homes with the brand slug in the filename.
4. The deliverables for two different brands sound like two different brands. If outputs are interchangeable, brand context is not actually steering the engine - that is a FAIL even if files were produced.

## Sprint Plan (5 working days, ~1 brand per day)

### Day 0 prep: Readiness gate

For each brand, check the five minimum files (business-overview, offers, audience, brand-voice, current-priorities) for real content.

- READY brands proceed.
- Placeholder brands (currently `local-glow-up`, `prep2eat`) get a 20-minute operator interview to fill the five files - the operator answers, the AI writes. If the operator cannot or will not fill them, PARK the brand and note it. Do not let an AI invent the answers.

### Days 1-5: One identical test per brand

Run the same request shape through `run-marketing-request.md` for each brand, changing only the BRAND field and the brand-appropriate goal:

```md
/marketing-system

BRAND: <brand>
GOAL: One week of content for the brand's primary channel
AUDIENCE: [from brands/<brand>/audience.md]
OFFER: [from brands/<brand>/offers.md]
CTA: [from brands/<brand>/offers.md]
CHANNELS: [brand's primary channel only - keep scope small]
OUTPUT: 5 posts or 1 newsletter + 3 posts, ready to publish
```

Suggested per-brand focus (adjust to current priorities):

| Brand | Primary channel test | Notes |
|---|---|---|
| your-brand | X week-plan from the AI Daily Journal | Uses the brand's content-source workflow; hardest voice test |
| acc-network | One newsletter issue + 3 X posts | Beginner-friendly, no hype; beehiiv optional, markdown fallback fine |
| scholarship-dashboard | Launch-prep: landing copy + 3 outreach posts | Honesty guardrails from `ideas.md` apply; no overpromising |
| local-glow-up | 5 local-lead posts | Only if Day 0 interview filled context; else PARK |
| prep2eat | 5 posts for its primary channel | Only if Day 0 interview filled context; else PARK |

### Per-brand run log

Record one log per brand at `outputs/reports/weekly/YYYY-MM-DD_<brand>_validation-run.md`:

```md
# Validation Run - <brand> - YYYY-MM-DD

## Context Load
Files loaded, files missing/thin, assumptions made: [list]

## Friction
Every point where the engine did not know what to do for this brand: [list]

## Output Produced
[Paths to deliverables]

## Voice Check
Does it sound like this brand and not like the other four? [PASS/FAIL + why]

## Time
Minutes from request to packaged output: [n]

## Fix-Backs
Engine changes this run suggests (workflow gaps, template gaps) - engine fixes only, never per-brand engine copies: [list]
```

### Day 5 close: Sprint report

Write `outputs/reports/weekly/YYYY-MM-DD_all-brands_validation-sprint.md`:

- Scorecard: per brand PASS / FAIL / PARKED against the four success criteria.
- Total onboarding time for the weakest brand (this number becomes a sales claim: "client onboarded in X minutes").
- Engine fix-backs, deduplicated and ranked - apply the top ones via `fable-project-review-loop.md`.
- One proof note in `brands/your-brand/proof-notes/` summarizing the sprint. "One engine ran marketing for five different businesses in a week" is the consultancy's core pitch - this sprint is the evidence.

## Rules

- Change engine files only to fix engine gaps found by the sprint, never to special-case one brand.
- Keep deliverables small. The sprint validates the pipeline, not a month of content.
- A PARKED brand is a fine outcome; a faked brand is not.
- Publishing the outputs is optional and stays the operator's call.
