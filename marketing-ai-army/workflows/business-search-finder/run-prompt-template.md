# Business Search — Run Prompt Template

Paste this into a NEW chat (fresh context = cheaper, cleaner run). Fill the brackets.

```
/Business Search For: [vertical] in [location]
Brand: [brand folder name, e.g. local-glow-up]
Count: 15
Shortlist: 5
Tracker: [Google Sheet URL, or "none — CSV only"]
Exclude: [businesses already contacted, or "none"]

Follow marketing-ai-army/workflows/business-search-finder.md exactly.
Key rules:
- Public sources only. No Maps scraping. Never invent data; label unknowns "not verified".
- Show me the ranked review table and save the CSV BEFORE touching the Sheet.
- Sheet writes are append-only, and only after I approve rows.
- If the Sheet is unreachable, deliver the import-ready CSV and say so.
- Finish with the filled run log.
```

## Ready-to-use: Bronx plumber run

```
/Business Search For: plumbers in Bronx, NYC
Brand: local-glow-up
Count: 15
Shortlist: 5
Tracker: https://docs.google.com/spreadsheets/d/1rjcH0cn7YWakcNMCnbliGx6ql3NWWhKMn0ViLd9f4oQ/edit
Exclude: none

Follow marketing-ai-army/workflows/business-search-finder.md exactly.
Key rules:
- Public sources only. No Maps scraping. Never invent data; label unknowns "not verified".
- Show me the ranked review table and save the CSV BEFORE touching the Sheet.
- Sheet writes are append-only, and only after I approve rows.
- If the Sheet is unreachable, deliver the import-ready CSV and say so.
- Finish with the filled run log.
```
