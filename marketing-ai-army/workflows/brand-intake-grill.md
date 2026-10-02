# Brand Intake Grill Workflow

Reusable, one-question-at-a-time interview that turns a new (or under-specified)
business/project into the real brand context the Marketing AI Army needs to run it.
Use whenever a brand folder is empty, placeholder-only, or a new client/business
comes in and we do not have verified context yet.

> This is the In-house equivalent of the "grill me" skill from the YouTube
> workflow video: the operator answers, the agent writes. Never let the agent
> invent business facts, audience claims, or offers.

## When to use

- Adding a brand whose folder is `EMPTY` or `PARTIAL`.
- A `PARKED` brand that now wants marketing started.
- A new client signing up for the managed service (this IS the onboarding demo).

## Workflow

### 1. Read first — do not grill what already exists
Before asking anything, check the discovery order (cheapest to expensive):
1. existing files under `brands/<brand>/`
2. `positions/three-ps.md` (may already be filled)
3. related project/code repo + README + HANDOFF docs
4. live website / social profiles / store listing
5. asset inventory sheets
Only questions whose answers are **not already in a source** reach the grill.

### 2. Set the target status
Decide what we are building toward and tell the operator:
```
We are filling brand context so this brand is READY: business, audience,
offer+CTA, voice, proof, channels, goals, assets, and access. If a topic is
already answered in your files/site, I will pull it and just confirm with you.
```

### 3. Ask one question at a time
Ask the smallest set of questions needed to hit the Minimum Viable Brand
Context in `brands/README.md` plus the Three P's. Do **not** dump all questions
at once — one at a time keeps answers real and fast.

Priority order (highest first):
1. **Business** — what it is, what it sells, current stage. (business-overview.md)
2. **Person / Pain / Promise** — fill `positions/three-ps.md`.
3. **Audience** — primary buyer + their pains (audience.md).
4. **Offer + CTA** — exact offer and exact next step (offers.md).
5. **Voice** — tone + 3–5 do/don't rules (brand-voice.md).
6. **Content pillars** — 3–5 recurring themes (content-pillars.md).
7. **Proof** — testimonials, results, case studies, credibility (proof-notes later).
8. **Channels** — which platforms, handles, existing presence.
9. **Goals** — target metrics, timeline (goals.md, current-priorities.md).
10. **Assets** — logos, product shots, studio shots, brand guidelines.
11. **Access** — what external tools/accounts the engine may use (approval-gated).

### 4. Write answers to the correct files
Save each answer into the right file only:
- business context -> `brands/<brand>/business-overview.md`
- audience -> `audience.md`  ·  offer/CTA -> `offers.md`
- voice -> `brand-voice.md`  ·  pillars -> `content-pillars.md`
- goals/priorities -> `goals.md`, `current-priorities.md` (dated)
- Three P's -> `positions/three-ps.md` (via `shared/three-ps-template.md`)
- proofs -> `proof-notes/` (only when real, dated)
Unknowns stay literal: mark `NEEDS OWNER INPUT:` — never estimate.

### 5. Classify readiness
After the grill, set status in `brands/README.md`:
- `READY` — the 5 minimum files + Three P's have real (non-placeholder) content.
- `PARTIAL` — some real content, some `NEEDS OWNER INPUT` gaps.
- `PARKED` — operator chose not to fill gaps now; note the reason.
- `EMPTY` — nothing filled yet.

### 6. Validate on one small deliverable
Do not expand channels yet. Produce the smallest useful execution package
(e.g. 5 X posts, 1 X thread, 1 LinkedIn post, 1 short-video idea, 1 proof note)
and check it sounds like THIS brand, not the other four. If it sounds generic,
the grill missed a real pain/promise — go back and sharpen it.

## Rules / guardrails

- One question at a time; read sources first; do not re-ask what is on file.
- Never invent business facts, metrics, audience claims, offers, or testimonials.
- Never copy the engine into the brand folder — fill `brands/<brand>/` only.
- Create `strategy/` / `proof-notes/` only when the brand produces real output.
- Publishing, outreach, and spend stay approval-gated regardless of readiness.
- Outcome = a brand both the operator and a new AI session can pick up cold.
