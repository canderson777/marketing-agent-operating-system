# Agent Communication Rules

This file defines how agents talk, hand off work, escalate problems, and report performance inside the Marketing Agent Operating System.

## Authority

- The human operator sets business goals.
- The Master Marketing Agent owns strategy, prioritization, assignments, cross-agent routing, and final approval.
- Channel sub-master agents own channel execution.
- Specialist agents own narrow deliverables only.
- Specialists do not freelance across the chain.

If a specialist needs something from another channel, the request should move through the assigned sub-master and then through the master agent when needed.

## Standard Message Format

Use this format for assignments, replies, blocker reports, and handoffs:

```md
TO: [Agent or Master]
FROM: [Agent or Master]
TASK: [One specific task]
CONTEXT: [Why this matters and what campaign/profile it belongs to]
INPUTS: [Files, assets, source material, prior outputs, assumptions]
OUTPUT: [Deliverable or requested deliverable]
STATUS: Draft / Complete / Needs More Info / Blocked / Revision Needed
BLOCKERS: [Missing inputs, risks, or none]
NEXT ACTION: [One clear next step]
```

## Assignment Rules

Every assignment should include:

- One clear task.
- The audience.
- The offer or CTA.
- The channel or format.
- Deadline or timing.
- Required inputs.
- The exact output needed.
- The metric or success condition when relevant.

Do not bundle multiple unrelated tasks into one assignment.

## Reply Rules

When an agent reports back:

- `Complete` means the task is done and ready for review.
- `Needs More Info` means the task can continue only after a specific missing detail is supplied.
- `Blocked` means the task cannot proceed without a material change or decision.
- `Revision Needed` means the prior output exists but needs changes before approval.

Agents should name the missing detail or blocker directly instead of being vague.

## Handoff Rules

Use this when one agent's output becomes another agent's input:

```md
# Handoff

FROM: [Sending Agent]
TO: [Receiving Agent]
APPROVED BY: Master Marketing Agent
SOURCE OUTPUT: [File, draft, table, or asset]
USE THIS FOR: [Specific next task]
DO NOT CHANGE: [Locked audience, offer, CTA, claim language, dates, or price]
OPEN QUESTIONS: [Anything unresolved]
```

Handoffs should be explicit. No silent grabbing of another agent's work.

## Approval Rules

No customer-facing work should go live without the right approval level.

| Asset Type | Approver |
|---|---|
| Recurring social post | Channel sub-master |
| Newsletter issue | Email Marketing Agent |
| Promo email campaign | Master Marketing Agent |
| Live ad creative or budget increase | Paid Ads Agent, plus master for high-impact changes |
| Cornerstone blog, case study, or launch asset | Master Marketing Agent |
| Influencer, affiliate, or partner content with disclosure risk | Master plus compliance review |
| Claims involving earnings, health, legal, or guaranteed outcomes | Master plus compliance review |
| Major launch announcement | Operator plus master |

## Escalation Rules

Escalate when:

- The brief is ambiguous or conflicts with a shared file.
- Compliance is uncertain.
- Data contradicts the assigned tactic.
- A deadline cannot be met without quality loss.
- Two channels need conflicting decisions.
- The requested output is too broad to execute well.

Escalate one level up first.

Use this format:

```md
ESCALATION:
FROM: [Agent]
TO: [One level up]
ISSUE: [One sentence]
EVIDENCE: [Metric, file, source material, or quote]
PROPOSED RESOLUTION: [What should happen next]
URGENCY: Low / Medium / High
```

## Reporting Cadence

| Cadence | Owner | Audience | Purpose |
|---|---|---|---|
| Daily | Channel sub-master | Master | Anomaly detection |
| Weekly | Channel sub-masters and master | Operator | Tactical review |
| Monthly | Master | Operator | Strategic review |
| Quarterly | Operator and master | Leadership | Goal reset and channel allocation |

See `workflows/reporting-review.md` for the full reporting workflow.

## Naming Rules

- Agent files: lowercase kebab-case ending in `-agent.md`
- Shared docs: lowercase kebab-case in `shared/`
- Workflows: lowercase kebab-case in `workflows/`
- Outputs: `outputs/[type]/[YYYY-MM-DD]_[short-slug].md`

Use filenames when referencing agents or shared docs inside assignments.

## Agents Must Never

- Publish without approval.
- Skip compliance review on flagged content.
- Invent stats, proof, quotes, or case studies.
- Change the offer or price without instruction.
- Drift from `brand-voice.md` without a reason.
- Start cross-channel work without master direction.
- Mark work complete when it is only partially done.

## Agents Must Always

- Read the brief and relevant shared docs before starting.
- Surface blockers early.
- Cite or flag claims that need verification.
- Match the requested format unless a better one is proposed first.
- Respect kill criteria and stop weak tactics when thresholds are hit.
- Include a next action in every meaningful reply.
