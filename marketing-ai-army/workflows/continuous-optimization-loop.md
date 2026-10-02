# Workflow: Continuous Optimization Loop

A reusable loop that any channel or department can adopt. Each cycle tests one controlled change, measures objectively, and records learning.

## Goal

Create a closed, repeatable optimization process:

> Observe → Compare → Diagnose → Choose → Approve → Act → Wait → Verify → Learn → Decide

## Cadence

See `shared/loop-card-template.md` for cadence rules. Start with weekly observation and monthly decisions for most organic loops.

## Step 1: Observe

- Pull fresh performance data from the declared source.
- Record the exact values and date range.
- Commit the raw data or a link to durable storage.

## Step 2: Compare

- Compare against the declared baseline and previous cycle.
- Flag anomalies, regressions, or strong performers.
- Tag each signal with a confidence level (high / medium / low).

## Step 3: Diagnose

- Generate ranked hypotheses.
- Attach a confidence label and supporting evidence.
- Do not invent causality; label speculation as such.

## Step 4: Choose

- Select ONE experiment from the list.
- Ensure it is reversible and within defined limits.
- Document the exact change in the experiment log.

## Step 5: Approve

- Surface the change to the master agent or human operator.
- Wait for explicit approval before any public/spend/destructive action.
- Record approval in the experiment log.

## Step 6: Act

- Execute the approved change.
- Keep the change as small as possible.
- Pin it to a PR, commit, or controlled action with easy rollback.

## Step 7: Wait

- Respect the minimum sample and wait period defined in the loop card.
- Do not stack overlapping changes on the same target.
- Pause the loop until the waiting period completes.

## Step 8: Verify

- Pull post-change data for the same metric and window.
- Compare before and after.
- Decide whether the change passed guardrail checks.

## Step 9: Learn

Record in the experiment log:

- Date
- Baseline
- Opportunity
- Exact change
- Result (before/after with source links)
- Verdict: win / loss / inconclusive / invalid
- Decision: keep / revert / iterate / stop / scale
- Confidence

## Step 10: Decide

- **Win:** Keep the change; consider scaling if safe.
- **Loss:** Revert or mitigate immediately.
- **Inconclusive:** Either run a follow-up with higher sample size or abandon.
- **Invalid: Discard the hypothesis and log why the test was flawed.

## Output Format

- Loop card: `brands/<brand>/experiments/<channel>/<loop-name>-loop-card.md`
- Cycle log: `outputs/experiments/<brand>/<channel>/YYYY-MM-DD_<loop-name>.md`
- Operator report: sent to master agent or kept in weekly review cycle.

## Rules

1. One experiment per cycle, no matter how tempting multiple changes seem.
2. Guardrails are never optional.
3. Rollback must be as easy as the original action.
4. Do not invent metrics. Link to the source.
5. Silence on a decision is not consent. Require explicit approval.
6. Loops pause automatically when sample or budget drops below the threshold.

## Integration With Existing Workflows

- **SEO/AEO loops:** Run under `workflows/seo-optimization-loop.md`
- **Social loops:** Run under `workflows/social-learning-loop.md` (future)
- **Email loops:** Run under `workflows/newsletter-improvement-loop.md` (future)
- **Ads loops:** Run under `workflows/paid-ads-testing-loop.md` (future)
- **Lead loops:** Run under `workflows/lead-follow-up-loop.md` (future)

This workflow is the shared protocol. Each channel loops under it while defining its own loop card and opportunity set.