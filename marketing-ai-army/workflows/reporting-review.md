# Workflow: Reporting Review

Use this after campaigns, weekly content cycles, launches, ads, outreach sprints, or recurring monthly work.

## Goal

Turn marketing activity and performance data into decisions, reallocations, and next experiments.

## Cadence

| Cadence | Owner | Audience | Purpose |
|---|---|---|---|
| Daily | Channel sub-master | Master | Anomaly detection |
| Weekly | Master | Operator | Tactical reallocation |
| Monthly | Master | Operator | Strategic assessment |
| Quarterly | Operator and master | Leadership | Goal reset and kill/double-down decisions |

## Daily Check

- Compare yesterday against the trailing baseline.
- Flag anomalies, deliverability issues, compliance issues, or spend problems.
- Keep it short unless a real issue exists.

## Weekly Review

- Pull channel reports from the sub-masters.
- Update actuals versus targets.
- Identify channels to scale, improve, pause, or stop.
- Each sub-master contributes what worked, what did not, and one decision needed.
- The master produces the weekly operator brief.

## Monthly Review

- Review four weeks together.
- Compare against the north-star goal and prior periods.
- Review per-channel ROI, contribution, and payback.
- Reconcile attribution where possible.
- Recommend budget or effort shifts.

## Quarterly Reset

- Review whether the 90-day goals were met.
- Update `../shared/customer-avatar.md`, `../shared/offer-library.md`, and `../shared/metrics-dashboard.md` if reality changed.
- Lock the next 90-day focus, channel priorities, and kill criteria.

## Output Format

```md
# Reporting Review

## Period
[Dates]

## Goal
[Goal]

## What Shipped
- [Asset]

## Performance
| Metric | Target | Actual | Decision |
|---|---:|---:|---|

## What Worked
- [Insight]

## What Did Not Work
- [Insight]

## Decisions
- Keep:
- Improve:
- Stop:
- Scale:

## Next Experiments
| Experiment | Owner | Metric | Deadline |
|---|---|---|---|
```

## Reports Archive

- `outputs/reports/weekly/[YYYY-WW].md`
- `outputs/reports/monthly/[YYYY-MM].md`
- `outputs/reports/quarterly/[YYYY-Q].md`

## Rules

- No report without a decision.
- Numbers should have a source.
- Bad news comes first.
- Do not kill a channel after one bad week.
- Do not scale a winner too aggressively before the economics are stable.
