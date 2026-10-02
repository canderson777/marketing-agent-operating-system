# Workflow: Campaign Launch

Use this for a multi-channel push around a single offer, promotion, seasonal event, or deadline-driven campaign.

## Goal

Move from campaign brief to a launch-ready, multi-channel package with clear owners, review gates, and a defined close-out plan.

## Trigger

`../master-agent.md` receives the campaign goal, offer, dates, segment, revenue or conversion target, and budget.

## Step 1 - Strategy Lock

- Owner: `../master-agent.md`
- Lock positioning, hero hook, offer, CTA, dates, and kill criteria.
- Approve the main message and channel mix.
- Issue channel briefs to the required sub-masters.

## Step 2 - Asset Production

Parallel work by channel:

- Content builds the cornerstone campaign assets and proof.
- Email builds the send sequence and segment or suppression rules.
- Social builds teaser, proof, push, and close-day posts.
- Paid builds concept tests, prospecting, and retargeting.
- Affiliate, partnerships, or events build co-promotion assets where relevant.
- Compliance reviews any risky claims before approval.

## Step 3 - Pre-Launch Warm-Up

- Email sends value-led warm-up content.
- Social posts teasers and context.
- Paid warms warm audiences when useful.
- Partners and affiliates get kits and send dates.
- Final QA happens before the launch day.

## Step 4 - Launch Day

- Email announcement sends.
- Social hero posts go live.
- Paid prospecting and retargeting switch into launch mode.
- Partners, affiliates, and direct outreach run approved launch touches.

## Step 5 - Mid-Campaign Push

- Email handles proof, objections, FAQ, and reminders.
- Social pushes proof, behind-the-scenes, and urgency.
- Paid scales winners and kills weak creative.
- Each sub-master reports the day's number to the master.

## Step 6 - Close Day

- Email runs morning, mid-day, and last-call sends.
- Social runs final-call posts and countdowns.
- Paid raises urgency and final-hour creative if appropriate.
- Cart-abandonment or follow-up messages run if relevant.

## Step 7 - Post-Mortem

- Owner: `../master-agent.md`
- Pull total revenue, conversions, CAC, ROAS, and channel contribution.
- Each sub-master files a short retro.
- Log winning hooks, segments, creative, and partner learnings into the shared system.

## Output Format

```md
# Campaign Launch Package

## Campaign Summary
[Offer, audience, CTA, dates]

## Agent Assignments
| Agent | Task | Output | Status |
|---|---|---|---|

## Assets
- [Asset]

## Launch Checklist
- [ ] Strategy locked
- [ ] Assets approved
- [ ] Compliance checked
- [ ] Tracking ready
- [ ] Publishing schedule ready
- [ ] Post-mortem date set

## Metrics
[Primary and secondary metrics]

## Next Action
[One action]
```

## Output Location

`outputs/campaigns/[YYYY-MM-DD_campaign-slug]/`

## Kill Criteria

- If launch-day performance is materially below plan, the master agent calls a same-day strategy huddle.
- If complaint, unsubscribe, or compliance risk spikes, pause the affected channel pending review.
