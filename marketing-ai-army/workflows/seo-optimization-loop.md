# Workflow: SEO Optimization Loop

The continuous improvement protocol applied to organic search. Start here before generalizing to other channels.

## Loop Card Reference

Save the loop card at: `brands/<brand>/experiments/seo/<loop-name>-loop-card.md`

## Opportunity Types

Prioritize from this list (ranked by leverage and reversibility):

1. **Striking-distance keywords**
   - Keywords ranking 4–20 with meaningful impressions
   - Goal: push to top 3

2. **Weak titles / content**
   - Low CTR on high-impression queries
   - Goal: improve click-through

3. **Keyword cannibalization**
   - Multiple pages competing for the same query
   - Goal: consolidate or differentiate

4. **Content decay**
   - Previously strong pages losing traffic/queries
   - Goal: refresh intent coverage

5. **AEO gaps**
   - Queries where competitors appear in AI answers
   - Goal: add answer blocks, FAQ, schema

6. **Internal linking**
   - Under-linked high-value pages
   - Goal: strengthen topical clusters

7. **Meta / schema cleanup**
   - Missing or misusing structured data
   - Goal: quick technical wins

## Prerequisites

- Google Search Console access (read)
- Optional: DataForSEO, SEMrush, Ahrefs, or ClickFlow for competitive layer
- Access to the content repository (read + PR creation)
- Defined baseline window (e.g., 28 days)
- Defined guardrail metrics (e.g., no loss on branded queries)

## Cycle Steps

### 1: Observe (SEO/AEO Agent)

- Pull Search Console data for the target property.
- Filter: queries with >100 impressions in last 28 days.
- Rank by: traffic value, position gap, CTR opportunity.

### 2: Diagnose

- For each opportunity, propose one small change.
- Attach confidence: high / medium / low.
- Do not propose changes for pages with <500 sessions in the window (too noisy).

### 3: Choose (One per cycle)

- Pick the highest-leverage opportunity.
- Ensure the change is reversible.
- Document in experiment log.

### 4: Draft (On-Page SEO Agent)

- Write the exact title/meta/content change.
- Suggest internal links or FAQ if relevant.
- Do not publish; prepare a PR diff.

### 5: Approve

- Send to master agent for review.
- Operator or channel lead gives final approval.
- Record approval in log.

### 6: Act

- Create a GitHub pull request against the content repository.
- Apply the change to staging/match branch only.
- Do not merge without explicit approval.

### 7: Wait

- Wait 21–28 days for the next full Search Console refresh cycle.
- Do not touch the same page during the wait.

### 8: Verify

- Pull post-change data for the same query/page set.
- Compare:
  - Average position
  - Impressions
  - Click-through rate
  - Clicks
  - Assisted conversions (if available)
  - Newsletter signups (if tracked)

### 9: Learn

- Judge against the loop card’s decision rules.
- Log verdict (win/loss/inconclusive) and decision.

### 10: Decide

- **Win:** Merge and consider similar experiments.
- **Loss:** Close PR; revert if auto-merged (by policy).
- **Inconclusive:** Keep PR open for later; do not stack.
- **Invalid:** Delete PR; record why the hypothesis was flawed.

## Experiment Log Format

Save to: `outputs/experiments/<brand>/seo/YYYY-MM-DD_seo-cycle.md`

```md
# SEO Cycle - YYYY-MM-DD

## Property & Window
- Domain: [example.com]
- Baseline: [last 28 days]

## Opportunity Chosen
- Page: [/blog/...]
- Query: [primary target keyword]
- Position Before: [4–12]
- Impressions Before: [1.2K]
- CTR Before: [2.1%]

## Hypothesis
[Exactly what change is expected to do]

## Change Proposed
- Title change
- Meta description change
- Content section added
- Internal link added
- Schema/structured data change

## Pull Request
[Link or reference]

## Measurement (post-change)
- Position After
- Impressions After
- CTR After
- Clicks After
- Guardrail metrics

## Verdict
- Win | Loss | Inconclusive | Invalid
- Confidence: high | medium | low
- Decision: keep | revert | iterate | stop

## Next Action
[Open follow-up | close PR | merge | pause loop]
```

## When To Pause This Loop

- No page meets opportunity criteria (position 4–20, >100 impressions).
- Sample size drops below threshold.
- No Search Console access.
- Operator explicitly pauses.

## Integration

- SEO/AEO Agent owns this loop.
- On-Page SEO Agent drafts changes.
- Master Marketing Agent reviews and approves.
- Reporting Review Agent summarizes monthly.

## First Proof Loop

- Brand: ACC Network
- Property: accnetwork.xyz
- Cadence: monthly, with weekly opportunity monitoring
- Target: next article in publishing plan or one declining query
- Approval: explicit PR merge required