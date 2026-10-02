# Tool Registry

This file defines the external tools the Marketing Agent Operating System can use, when to use them, when to avoid them, and how to fall back when they are unavailable.

## Purpose

The system is built as a markdown-first operating model. Most work should stay inside the system files unless an external tool materially improves execution, reporting, speed, scale, or publishing.

This registry is the source of truth for those decisions.

## Selection Rules

1. **Use a tool only when it adds real value.** Prefer markdown planning when execution can be handled by an agent and manual publishing.
2. **Match the tool to the channel and task.** Do not force a tool into a workflow just because it is listed.
3. **Check availability before routing.** If the tool is not set up, fall back immediately to the normal workflow.
4. **Always document tool use.** Name the tool in the final package and explain why it was selected.
5. **Protect sensitive work.** Use privacy-focused tools when client data, customer data, or proprietary information needs extra care.

## Decision Flow

```
Does the task need live execution, live reporting, or platform publishing?
├── No → Keep it markdown-only.
├── Yes → Is there an approved tool for this channel/task?
        ├── No → Keep it markdown-only and note the gap.
        ├── Yes → Is the tool available and configured?
                ├── No → Fall back to markdown-only workflow.
                └── Yes → Route through the tool and document it.
```

## Approval Levels

| Level | Who Approves | Examples |
|---|---|---|
| Channel | Channel sub-master agent | Routine social post, standard email issue |
| Master | Master Marketing Agent | Promo campaigns, ad creative, live budgets, paid publishing |
| Operator | Human operator | High spend, major launches, sensitive data tools |

## Tool Entry Format

Every tool entry includes:

- **Category**
- **Best for**
- **Use when**
- **Do not use when**
- **Inputs required**
- **Typical outputs**
- **Owner agents**
- **Approval level**
- **Risks and limits**
- **Fallback path**
- **Status** — `ready`, `needs setup`, `optional`, or `planned`

---

## Tool Entries

### X MCP

- **Category:** X/Twitter research, account intelligence, engagement review, and approval-gated publishing support
- **Best for:** Live X research, trend/news scans, full-archive post search, mentions, timelines, bookmarks, creator/competitor tracking, engagement review, and X Articles drafts
- **Use when:**
  - X content should be grounded in live platform context instead of only internal notes
  - The X/Twitter Agent needs trend, keyword, account, bookmark, mention, or performance data
  - Weekly social review needs recent engagement signals
  - The operator wants reply options or thread angles based on active X conversations
- **Do not use when:**
  - The task can be completed from approved source docs, proof notes, and the AI Daily Journal
  - The account is not connected or the needed X Developer app/OAuth setup is missing
  - The task would publish, bookmark, follow, like, repost, quote, or modify account data without explicit operator approval
- **Inputs required:**
  - Topic, keywords, account handles, bookmarks/folders, date range, goal, and approval scope
  - X Developer app with OAuth 2.0, registered redirect URI, and credentials available to the MCP client
  - For Hermes: MCP server connection via `xurl mcp https://api.x.com/mcp` after operator-provided credentials
- **Typical outputs:**
  - X intelligence brief
  - Trend/news summary
  - Research-backed post angles
  - Reply queue in brand voice
  - Thread research notes
  - Bookmark idea inbox
  - Weekly performance notes
  - Draft X Articles for approval
- **Owner agents:** `../agents/02-social-media/social-media-agent.md`, `../agents/02-social-media/x-twitter-agent.md`, `../agents/02-social-media/content-calendar-agent.md`, `../agents/05-content-marketing/repurposing-agent.md`
- **Approval level:** Channel for read-only research and drafts; Operator for publishing or account actions
- **Risks and limits:**
  - Uses real X account permissions; never allow unsupervised publishing or account actions
  - API access, scopes, and rate limits depend on the X app/package
  - OAuth tokens and `~/.xurl` cache are secrets
  - Live X data can pull noisy trends; brand/source filters still apply
- **Fallback path:** Use the AI Daily Journal, My Twitter Post doc, proof notes, manual X review, and markdown-only drafting
- **Status:** `needs setup`

---

### ClickFlow

- **Category:** SEO / AEO optimization and analytics
- **Best for:** Improving organic content, title testing, click-through rate analysis, content refresh prioritization
- **Use when:**
  - SEO or AEO work needs stronger analytics than manual research can provide
  - The task is content optimization, not content creation from scratch
  - There is enough traffic or historical data to make optimization meaningful
- **Do not use when:**
  - The content has not been published yet
  - There is no existing traffic or data to analyze
  - The task is simple keyword research that a free tool could handle
- **Inputs required:**
  - URLs or content to optimize
  - Target keywords or query intent
  - Access to the ClickFlow account
- **Typical outputs:**
  - Optimized title suggestions
  - Content refresh recommendations
  - CTR improvement report
- **Owner agents:** `seo-aeo-agent.md`, `on-page-seo-agent.md`
- **Approval level:** Master
- **Risks and limits:**
  - Requires paid account and site access
  - Recommendations still need brand voice and compliance review
  - Cannot replace editorial judgment
- **Fallback path:** Manual SEO audit using the keyword-research-agent.md and on-page-seo-agent.md workflows
- **Status:** `needs setup`

---

### Google Search Console

- **Category:** SEO / AEO data and performance monitoring
- **Best for:** Direct performance data for owned properties, query rankings, impressions, clicks, CTR, coverage issues
- **Use when:**
  - SEO or AEO work needs first-party verified metrics
  - The site has a verified Search Console property
  - Historical ranking data is needed for loop decisions
- **Do not use when:**
  - The property is not verified or no data exists
  - Competitive data is needed (supplement with DataForSEO or similar)
  - The task is simple title/meta drafting without data context
- **Inputs required:**
  - Google Search Console property verified
  - Read-only service account JSON credentials
  - Target property URL or domain
- **Typical outputs:**
  - Performance report (queries, pages, positions, clicks)
  - Coverage and enhancement reports
  - Baseline and delta comparisons
- **Owner agents:** `seo-aeo-agent.md`, `on-page-seo-agent.md`, `ai-answer-agent.md`
- **Approval level:** Channel for reporting; Master for any write actions
- **Risks and limits:**
  - Requires Google Cloud project and Search Console access setup
  - Data has a 2–3 day lag and weekly refresh cycles
  - Properties must be verified; no speculative data
- **Fallback path:** Manual keyword research, competitor analysis, and site audit without first-party ranking data
- **Status:** `needs setup`

---

### DataForSEO

- **Category:** Competitive SEO / SERP intelligence
- **Best for:** Competitive keyword gaps, live SERP analysis, search volume, feature snippets and AI answer opportunities
- **Use when:**
  - Competitive context is needed to prioritize SEO opportunities
  - Live SERP data is required for content optimization
  - Keyword gap analysis supports the strategy
- **Do not use when:**
  - The task only needs first-party Search Console data
  - Budget for paid tools is unavailable
  - The query set is well understood without external data
- **Inputs required:**
  - DataForSEO API credentials (login and password)
  - Target keywords or competitor domains
- **Typical outputs:**
  - Competitor ranking positions and keywords
  - Keyword search volume and difficulty estimates
  - SERP feature presence and AI answer candidates
- **Owner agents:** `seo-aeo-agent.md`, `keyword-research-agent.md`
- **Approval level:** Channel
- **Risks and limits:**
  - Paid external API with usage-based costs
  - Data is directional; verify critical insights
  - Requires separate signup and credit
- **Fallback path:** Google Search Console data, manual SERP inspection, Ubersuggest or free tools
- **Status:** `needs setup`

---

### SEMrush / Ahrefs

- **Category:** SEO / Competitive analysis
- **Best for:** Site audits, backlink analysis, keyword research, competitor domain overview
- **Use when:**
  - Full SEO audit is required beyond Search Console
  - Backlink opportunities are part of the strategy
  - Comprehensive competitive analysis is needed
- **Do not use when:**
  - Only first-party data is required (use Search Console)
  - Budget or access is unavailable
- **Inputs required:**
  - Tool subscription and API key
  - Target domain or keyword list
- **Typical outputs:**
  - Audit reports
  - Backlink lists
  - Keyword clusters and gaps
- **Owner agents:** `seo-aeo-agent.md`, `backlink-agent.md`, `keyword-research-agent.md`
- **Approval level:** Master
- **Risks and limits:**
  - Paid tools with subscription costs
  - Data is directional; validate before making decisions
- **Fallback path:** Search Console + manual analysis
- **Status:** `needs setup`

---

### beehiiv

- **Category:** Newsletter publishing, list management, and analytics
- **Best for:** Sending newsletters, segmenting subscribers, tracking opens and clicks, growing a publication
- **Use when:**
  - The deliverable includes publishing or scheduling a newsletter
  - Segmentation or subscriber reporting matters
  - Newsletter metrics are part of the workflow output
- **Do not use when:**
  - You only need a newsletter draft
  - The client uses a different email platform
  - There is no active beehiiv account or audience
- **Inputs required:**
  - beehiiv account access
  - Newsletter content
  - Target audience or segment
  - Send time or schedule
- **Typical outputs:**
  - Published or scheduled newsletter
  - Subscriber metrics
  - Segment performance summary
- **Owner agents:** `email-marketing-agent.md`, `newsletter-agent.md`
- **Approval level:** Channel for drafts, Master for sends
- **Risks and limits:**
  - Requires account and audience permissions
  - Sending cannot be undone
  - Must comply with email regulations and platform policies
- **Fallback path:** Export draft to Markdown/email format and provide manual send instructions
- **Status:** `needs setup`

---

### Higgsfield

- **Category:** Visual creative and short-form video generation
- **Best for:** Generating image or video assets for social, ads, and landing pages
- **Use when:**
  - A campaign needs custom visual creative
  - Short-form video content needs generated or assisted production
  - Visual output is faster or cheaper than manual production
- **Do not use when:**
  - The brand requires exact control over every visual detail
  - Generated content may violate platform ad policies
  - The client has not approved AI-generated visuals
- **Inputs required:**
  - Creative brief or asset spec
  - Brand voice and visual direction
  - Platform format requirements
- **Typical outputs:**
  - Generated images or videos
  - Variations for testing
  - Creative prompts and usage notes
- **Owner agents:** `social-media-agent.md`, `paid-ads-agent.md`, `content-marketing-agent.md`
- **Approval level:** Master
- **Risks and limits:**
  - Output may need human refinement
  - Some platforms restrict AI-generated ad creative
  - Copyright and ownership terms vary by tool
- **Fallback path:** Write image/video prompts and hand to a human designer or creator
- **Status:** `ready — official Higgsfield CLI authenticated; workspace selected 2026-08-27; generation remains approval-gated`

---

### Meta

- **Category:** Meta ad execution and reporting
- **Best for:** Running Facebook and Instagram ads, campaign management, audience targeting, performance reporting
- **Use when:**
  - The campaign includes paid Meta ads
  - Live execution, budget management, or reporting is required
  - The client has an active Meta Ads account
- **Do not use when:**
  - The client has no active Meta Ads account or payment method
  - Only ad copy or creative concepts are needed
  - Budget or targeting is undefined
- **Inputs required:**
  - Meta Business / Ads Manager access
  - Campaign brief
  - Budget and targeting parameters
  - Approved creative and copy
- **Typical outputs:**
  - Live or drafted campaign
  - Ad performance report
  - Budget pacing summary
- **Owner agents:** `paid-ads-agent.md`, `meta-ads-agent.md`, `ad-copy-testing-agent.md`
- **Approval level:** Operator for budget live, Master for setup
- **Risks and limits:**
  - Involves real ad spend
  - Account access must be secure
  - Platform policy compliance is required
  - Wrong settings can burn budget fast
- **Fallback path:** Provide campaign structure, ad copy, and manual setup instructions
- **Status:** `needs setup`

---

### ZoomInfo

- **Category:** B2B prospecting and outreach data
- **Best for:** Finding business contacts, building outbound lists, account research
- **Use when:**
  - A B2B campaign needs targeted prospect lists
  - Direct outreach or ABM strategy requires verified contact data
  - The client has a ZoomInfo subscription
- **Do not use when:**
  - The audience is B2C
  - The client does not have ZoomInfo access
  - Data sensitivity prevents external enrichment
- **Inputs required:**
  - ZoomInfo account access
  - Target industry, role, company size, or account list
  - Compliance/usage rules
- **Typical outputs:**
  - Prospect list
  - Account research notes
  - Outreach targeting recommendations
- **Owner agents:** `direct-outreach-agent.md`, `partnerships-agent.md`
- **Approval level:** Master
- **Risks and limits:**
  - Requires paid subscription
  - Must comply with data privacy laws
  - Contact data can become outdated
  - Use must match platform terms
- **Fallback path:** Manual prospecting via LinkedIn, directories, or company websites
- **Status:** `needs setup`

---

### Venice

- **Category:** Privacy-focused AI generation
- **Best for:** Running AI tasks when data sensitivity is higher than normal
- **Use when:**
  - The client has privacy requirements
  - Input data should not go through standard public model APIs
  - The workflow involves customer data, medical data, financial data, or proprietary strategy
- **Do not use when:**
  - Privacy requirements are normal or standard
  - Using Venice adds friction with no real benefit
  - The client has not requested or approved it
- **Inputs required:**
  - Venice access or setup
  - Clear privacy requirements
  - Task brief
- **Typical outputs:**
  - Generated copy, summaries, or analysis
  - Privacy handling notes
- **Owner agents:** Any agent handling sensitive work
- **Approval level:** Master or Operator
- **Risks and limits:**
  - May require separate setup and plan
  - Capabilities may differ from general models
  - Slower than standard routing in some cases
- **Fallback path:** Use internal markdown workflows and avoid sensitive input in standard agents
- **Status:** `needs setup`

---

### Ubersuggest

- **Category:** Keyword research and SEO insights
- **Best for:** Keyword ideas, search volume estimates, competitor keyword analysis
- **Use when:**
  - Manual keyword research needs extra data
  - The task benefits from competitor keyword insights
  - The client uses Ubersuggest
- **Do not use when:**
  - The keyword strategy is simple and free tools are enough
  - Real-time or highly accurate data is required
  - Another SEO tool like ClickFlow is already doing the same job
- **Inputs required:**
  - Ubersuggest account access
  - Seed keywords or competitor URLs
- **Typical outputs:**
  - Keyword list with volume and difficulty
  - Competitor keyword overlap
  - Content opportunity suggestions
- **Owner agents:** `seo-aeo-agent.md`, `keyword-research-agent.md`
- **Approval level:** Channel
- **Risks and limits:**
  - Data is directional, not exact
  - Requires paid access for full features
  - Metrics should not be treated as guarantees
- **Fallback path:** Use Google Keyword Planner, Google Search autocomplete, and manual competitor analysis
- **Status:** `needs setup`

---

## Quick Reference: Tool by Task

|| Task | First Tool to Consider | Fallback ||
||---|---|---|
|| Search Console data / verified rankings | Google Search Console | Manual site audit without data |
|| Competitive keyword / SERP insights | DataForSEO | Manual SERP inspection |
|| Full SEO audit / backlink analysis | SEMrush / Ahrefs | ClickFlow + manual analysis |
|| SEO content optimization | ClickFlow | Manual SEO audit |
|| Newsletter send / analytics | beehiiv | Manual send instructions |
|| Visual / short-form video creative | Higgsfield | Human designer/creator |
|| X research, replies, trends, bookmarks, and performance review | X MCP | AI Daily Journal + My Twitter Post doc + manual X review |
|| Meta ad execution | Meta | Manual campaign setup guide |
|| B2B prospecting | ZoomInfo | Manual LinkedIn/directory research |
|| Sensitive AI generation | Venice | Standard markdown workflow |
|| Keyword research | Ubersuggest | Google Keyword Planner + manual review |

## Status Legend

- `ready` — tool is available and configured
- `needs setup` — listed in the system but not currently connected
- `optional` — nice to have, not required for core workflows
- `planned` — intentionally not implemented yet

## How to Update This File

When a new tool is added or an existing tool is connected:

1. Add the tool entry using the format above.
2. Update the quick reference table if a new category is covered.
3. Update the README.md tool references if needed.
4. Note the change in the weekly review or campaign package.

## Last Updated

2026-06-19 — created initial registry with ClickFlow, beehiiv, Higgsfield, Meta, ZoomInfo, Venice, and Ubersuggest.
2026-06-29 — added X MCP as the planned X/Twitter research, reply, bookmark, and performance-review tool with approval-only publishing guardrails.
2026-07-14 — added Google Search Console, DataForSEO, and SEMrush/Ahrefs; updated quick-reference table; preparing for SEO optimization loop.
