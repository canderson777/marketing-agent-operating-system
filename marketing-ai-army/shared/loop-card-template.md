# Loop Card Template

Every loop must be declared before it runs. This card defines its purpose, boundaries, and success rules.

## Loop Declaration

```md
# Loop Card: [LOOP NAME]

BRAND: [brand folder name]
BUSINESS GOAL: [e.g., grow organic traffic to qualified article clicks, improve newsletter click rate, reduce CPA, increase qualified replies]

LOOP OWNER: [agent or sub-master responsible]
CADENCE: [daily / weekly / biweekly / monthly / quarterly]

## Data Sources

- Source: [API, tool, or manual source]
- Freshness: [how often data is updated]
- Access: [who or which token provides access]

## Window & Baseline

BASELINE WINDOW: [e.g., last 28 days of performance]
COMPARISON PERIOD: [e.g., same window from 30 days prior]
HISTORICAL LOG: [path to experiment archive]

## Metrics

PRIMARY METRIC: [the one number that decides win/lose]
GUARDRAIL METRICS: [anything that must not degrade]

## Experiment Rules

MINIMUM SAMPLE / WAIT PERIOD: [pageviews, clicks, impressions, budget, or time before judging]
ALLOWED ACTIONS: [the specific actions the agent may take autonomously]
APPROVAL REQUIRED: [publishing, spend changes, positioning, or merge]
MAX CHANGES PER CYCLE: [usually 1–2]
MAX TOKEN / TOOL / AD BUDGET PER CYCLE: [hard caps]

## Decision Rules

ROLLBACK RULE: [conditions that trigger automatic revert or recommendation]
STOP RULE: [conditions that pause the loop]
SCALE RULE: [conditions that let the loop expand]

## Experiment Log

Path: [where each cycle is recorded]
Fields:
- Date
- Baseline
- Opportunity
- Hypothesis
- Exact change (diff, PR)
- Wait date
- Post-change results
- Verdict: win / loss / inconclusive / invalid
- Decision: keep / revert / iterate / stop / scale
- Confidence: high / medium / low

## Next Review Date

[when the next cycle runs]
```

## Loop Card Checklist

- [ ] Primary metric is measurable and source-linked
- [ ] Guardrail metrics will catch regressions
- [ ] Cadence matches the channel’s evidence window
- [ ] Actions allowed are reversible
- [ ] Approval gates prevent dangerous actions
- [ ] Budget/take caps are explicit
- [ ] Baseline and log have concrete paths
- [ ] Decision rules are unambiguous

## How To Use This Card

1. Save as `brands/<brand>/experiments/<channel>/<loop-name>-loop-card.md`.
2. Reference it from the relevant workflow.
3. Update the next review date after each cycle.
4. Keep history in `marketing-ai-army/outputs/experiments/<brand>/<channel>/`.