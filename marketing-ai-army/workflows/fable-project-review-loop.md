# Fable Project Review Loop

How an AI model (Fable, Claude, or any capable model) should review a project in this system, improve it, and leave a trail the next model can pick up without the operator repeating context.

Use this when the operator says some version of: "review this project", "improve what matters", "do a system pass".

## Principles

1. Improve, do not rewrite. Broad rewrites destroy context the operator relies on. Every change needs a one-line reason.
2. High-leverage over cosmetic. Fix things that block reuse, routing, or sales. Skip nice-to-have cleanup unless it is nearly free.
3. Leave receipts. A review that changes files but writes no notes forces the operator to re-explain everything next session. That is a failed review.
4. Do not invent business facts. If brand context is missing, flag it as an operator task. An AI filling in fake audience/offer details poisons the system.
5. Destructive actions (deleting folders, moving referenced files) get flagged, not executed, unless the operator explicitly asked.

## The Loop

### Step 1: Orient (read, no writing)

- `docs/ai-handoff.md` - current state and open items.
- `docs/second-brain-map.md` - where things live.
- The README of whatever area is under review.
- If reviewing a brand: that brand's full folder plus `brands/README.md`.

### Step 2: Audit

Check, in priority order:

1. Can the engine actually run for the target brand(s)? (Context files real or placeholder? Routing references resolve?)
2. Do docs agree with each other? (README vs COMMANDS vs actual folder contents.)
3. Are conventions being followed? (Brand-slugged dated filenames, outputs in the right homes.)
4. Is anything brand-specific leaking into shared files, or engine files leaking into brand folders?
5. Dead weight: unused duplicates, empty folders, oversized non-markdown assets.

Write findings down BEFORE changing anything - a short list with file paths, ranked by leverage.

### Step 3: Improve (smallest set of changes)

- Pick the top 3-5 findings only. Explicitly skip the rest and say so.
- Prefer edits over rewrites, banners over moves (a "DEPRECATED" or "BRAND-SPECIFIC" note is reversible; a file move can break links).
- Match existing file style. This system is plain markdown with dated filenames - keep it that way. No new tooling, no automation, unless it directly improves reuse or sales.

### Step 4: Validate

This is a markdown system, so validation means:

- Every path referenced in files you touched resolves to a real file.
- New files follow naming conventions and live in the homes defined in `docs/second-brain-map.md`.
- Templates you changed still make sense when filled in (walk one example through mentally).

Report exactly what was checked and the result. If something could not be verified, say so plainly.

### Step 5: Document the pass

1. Update `docs/ai-handoff.md` - the "Current State" and "Open Items" sections, with today's date.
2. If the review itself is a marketable proof of work (it usually is), write a proof note in `brands/<brand>/proof-notes/` using the template there. The consultancy sells on these receipts.
3. If you discovered a reusable process, add or update a workflow in `workflows/` (see "Harvesting Custom Workflows" in `WORKFLOWS-AND-USAGE.md`).

### Step 6: Report to the operator

Use this structure:

```md
# Review Pass - YYYY-MM-DD

## Verdict
[One paragraph: overall state and the single most important thing]

## Top Findings
[3-5, ranked, with file paths]

## Changed
[File list with one-line reasons]

## Skipped On Purpose
[What you saw but did not fix, and why]

## Operator Decisions Needed
[Things only the owner can decide - business facts, deletions, spend]

## Next Pass Should
[Where the following review should start]
```

## Cadence

- Run a full loop monthly, or after any burst of changes to the engine.
- Run Steps 1-2 only (audit, no changes) before onboarding any new brand or client - it doubles as a readiness check.

## Anti-Patterns

- Reviewing every specialist agent file. The leverage is in routing, brand context, and workflows - specialists only matter when a workflow routes to them.
- Producing recommendations without making the low-risk changes directly.
- Adding frameworks, scripts, or automation to a system whose selling point is that it is readable markdown.
- Ending a session without updating `docs/ai-handoff.md`.
