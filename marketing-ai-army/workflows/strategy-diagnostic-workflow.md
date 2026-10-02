# Strategy Diagnostic Workflow

Use this when adding a business, personal brand, creator, influencer, founder, or mixed profile and asking the system what marketing strategy to use.

## Goal
Turn a client profile into ranked marketing strategies, campaign ideas, content pillars, quick wins, and a 30/60/90-day plan.

## Required Inputs
- Completed or partial `../shared/client-profile-template.md`.
- Offer or monetization model.
- Audience.
- Goal.
- Current channels and metrics when available.
- Budget and timeline when available.

## Agents Used
- Master Marketing Agent.
- SEO/AEO Agent when organic search or discoverability matters.
- Content Marketing Agent when education, authority, or assets are needed.
- Social Media Agent when audience growth or creator presence matters.
- Email Marketing Agent when list growth, nurturing, or launches matter.
- Paid Ads Agent when budget and conversion path exist.
- Direct Outreach, Partnerships, Influencer, Affiliate/Referral, or Events/Community as needed.

## Steps

1. **Profile Intake**
   - Load the client profile.
   - Identify profile type: business, personal brand, creator, influencer, founder, or mixed.
   - List missing high-impact details.
   - Make safe assumptions and label them.

2. **Goal And Funnel Diagnosis**
   - Define the primary goal.
   - Choose the funnel stage: awareness, consideration, conversion, retention, or referral.
   - Define the primary CTA.

3. **Channel Fit Scoring**
   Score each channel from 1 to 5:
   - Audience fit.
   - Offer fit.
   - Speed to result.
   - Budget fit.
   - Asset readiness.
   - Long-term upside.

4. **Strategy Recommendations**
   Return the top three strategies:
   - Why it fits.
   - Agents needed.
   - First deliverables.
   - Risks.
   - Metrics.

5. **Campaign Ideas**
   Create 5 to 10 campaign ideas that match the profile and goal.

6. **Content Pillars**
   Define three to five content pillars with example topics.

7. **Roadmap**
   Build:
   - First 7 days.
   - 30-day plan.
   - 60-day plan.
   - 90-day plan.

8. **Next Inputs Needed**
   List the information that would improve the plan.

## Output Format

```md
# Strategy Diagnostic

## Profile Summary
[Summary]

## Assumptions
- [Assumption]

## Recommended Strategies
| Rank | Strategy | Why It Fits | Agents | First Deliverable | Metric |
|---:|---|---|---|---|---|
| 1 |  |  |  |  |  |

## Campaign Ideas
- [Idea]

## Content Pillars
- [Pillar]: [Example topics]

## First 7 Days
- [Action]

## 30/60/90-Day Roadmap
| Timeframe | Focus | Actions | Metrics |
|---|---|---|---|
| 30 days |  |  |  |
| 60 days |  |  |  |
| 90 days |  |  |  |

## Missing Information
- [Input]
```

## Acceptance Criteria
- Strategy is ranked.
- Recommendations differ for businesses versus personal brands when context differs.
- Each strategy has agents, deliverables, and metrics.
- Assumptions are labeled.
- Plan can start within seven days.
