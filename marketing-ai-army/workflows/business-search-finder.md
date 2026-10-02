# Business Search Finder

## Purpose
Turn a narrow local-business request into a vetted, scored prospect batch for the brand's lead tracker. Reusable across verticals and cities.

**Command:** `/Business Search For: [vertical] in [location]`

## Command / input format

```
/Business Search For: plumbers in Bronx, NYC
Brand: local-glow-up            (default: local-glow-up)
Count: 15                       (default: 15)
Shortlist: 5                    (default: 5 — ranked audit targets)
Tracker: [Google Sheet URL]     (default: brand's lead tracker)
Exclude: [names already contacted, if any]
```

Only the first line is required. Everything else falls back to the brand's `current-priorities.md`.

### Current Local Glow Up defaults
- Beachhead: independent plumbing companies in the Bronx, NYC.
- Lead tracker: https://docs.google.com/spreadsheets/d/1rjcH0cn7YWakcNMCnbliGx6ql3NWWhKMn0ViLd9f4oQ/edit
- Goal per run: 15 qualified prospects, top 5 ranked for a free video Visibility Audit.

## V1 scope
- One vertical, one geography per run.
- Research and shortlist only. No outreach, no audit recording, no unverified claims.
- Always produce a reviewable table/CSV BEFORE anything touches the Google Sheet.
- Sheet writes are append-only, and only after the operator approves the batch.

## Step 1 — Build search queries
Generate 4–6 service-intent queries from the vertical + geography (what a customer with money in hand would type). Bronx plumber set:
- plumber Bronx NY
- emergency plumber Bronx NY
- drain cleaning Bronx NY
- water heater repair Bronx NY
- sewer repair Bronx NY

For a new vertical, use the pattern: `[core service] [city]`, `emergency [service] [city]`, plus 2–3 high-intent sub-services.

## Step 2 — Collect candidates
Use legitimate public sources only: web search results, the business's own website, its public Google Business Profile page, Yelp/BBB public pages. Manual browser checking is fine in V1.

Hard rules:
- No brittle Google Maps scraping. No bypassing access controls or rate limits.
- Never invent ratings, review counts, emails, or rank positions.
- Anything you could not confirm from a source gets labeled `not verified` in the Notes column.
- Do not claim exact Map Pack positions. Record what was actually observed, e.g. "not in visible top results for 'drain cleaning Bronx NY' on [date]" — an observation, not a rank claim.

## Step 3 — Exclude immediately
- National franchises (Roto-Rooter, Mr. Rooter, Benjamin Franklin, etc.)
- Directories and lead-gen sites (Yelp pages posing as businesses, Angi, HomeAdvisor, Thumbtack listings)
- No meaningful operating history (no reviews, placeholder site, no footprint)
- Dominant top-three results for the searched query (they don't need us)
- No usable contact method

## Step 4 — Qualify (pass/fail gate)
All five required. One `no` = Reject.

| # | Must have | Check |
|---|---|---|
| 1 | 15+ legitimate reviews | Google Business Profile count |
| 2 | 4.0+ rating | Google Business Profile |
| 3 | Working website OR legitimate public business profile | Load it |
| 4 | Usable contact path: email, contact form, or phone | Find it, record it |
| 5 | At least one specific, observable visibility gap | Must name it + evidence URL |

## Step 5 — Score (0–10, qualified businesses only)

| Factor | Points | How to score |
|---|---|---|
| Gap severity + demo-ability | 0–4 | 4 = multiple gaps or one big gap the operator can show on a Loom in 60 seconds (outside visible local results, slow/outdated mobile site, unanswered reviews, generic GBP category, no recent photos, homepage unclear on service+location). 2 = one clear gap. 0 = vague. |
| Contact path quality | 0–3 | 3 = named person + direct email. 2 = generic email or contact form. 1 = phone only. |
| Review base fit | 0–2 | 2 = 15–100 reviews at 4.0–4.7 (established but improvable — best audit audience). 1 = 100+ reviews or 4.8+ (harder to move). |
| Independence confidence | 0–1 | 1 = clearly independent local operator. |

**Priority A** = score 7–10 (audit-ready). **Priority B** = 4–6 (backup pool). Rank the shortlist by score; ties broken by contact path quality.

## Step 6 — Output for review (before any Sheet write)
Produce two things:
1. A ranked review table in chat — shortlist first, then remaining qualified, then rejects with one-line reasons.
2. A CSV saved to `marketing-ai-army/outputs/research/business-search/YYYY-MM-DD-[vertical]-[location].csv` using the exact schema below.

### Output schema (CSV and Sheet — exact columns, this order)
```
Date Added, Business Name, Vertical, City/Borough, Website, Google Profile URL, Rating, Review Count, Contact Name, Email, Phone, Best Contact Path, Search Query, Local Visibility Observation, Visibility Gap, Evidence URL, Audit Angle, Score, Priority, Status, Notes
```
- `Local Visibility Observation` — what was seen, dated, no rank claims.
- `Audit Angle` — one sentence the operator can open the Loom with.
- `Status` — starts as `New`. Pipeline values: New → Audit Recorded → Audit Sent → Replied → Call Booked → Client / Dead.
- Unknown values: leave blank + note `not verified`. Never guess.

Template: `workflows/business-search-finder/prospect-template.csv`

## Step 7 — Append to Google Sheet (after approval only)
1. the operator reviews the table/CSV and approves rows (all, or by name).
2. Open the tracker. **Read the existing header row first.** If it matches the schema, append approved rows below the last used row. If headers differ, map columns to the existing headers, leave unmapped tracker columns blank, and note the mapping in the run log.
3. **Append-only. Never edit, sort, delete, or overwrite existing rows or headers.**
4. Skip any business already present in the sheet (match on Business Name + Phone). Note skips in the run log.

### Fallback — no Sheets access
If the Sheet can't be reached (no browser access, auth failure, permissions), stop there and deliver the CSV from Step 6 as a ready-to-import file. the operator imports via File → Import → Append to current sheet. Say clearly that the Sheet was NOT updated.

## Step 8 — Run log
Copy `workflows/business-search-finder/run-log-template.md` to `marketing-ai-army/outputs/research/business-search/YYYY-MM-DD-[vertical]-[location]-runlog.md` and fill it in. Takes 2 minutes; keeps runs comparable across verticals.

## Success metric
the operator can record five Visibility Audits tomorrow, each with a named gap and evidence URL good enough to personalize the first line of outreach.

## V2 options (do not build until V1 has produced results)
- Google Places API lookup for ratings/review counts (needs the operator's API key, respects ToS, ~free at this volume). Lowest-risk upgrade.
- PageSpeed Insights API to auto-attach mobile speed scores as evidence.
- Duplicate-check script against the tracker before review.
Skip anything resembling Maps scraping or ranking trackers — fragile and against ToS.
