# Asset Production Workflow (Video, Profiles, Images)

The **continued workflow** for turning brand context into videos, profiles, and
images. Adapted for **Hermes Agent** (this system) — not Claude Code. Hermes
fills the same role the "Claude → one-person marketing team" video plays: you
only need to know what to ask for.

## Core principle
Every asset starts from the **Three P's** (`../shared/three-ps-framework.md`).
Without a real Person, Pain, and Promise, output becomes generic AI slop.
The Three P's ground: positioning, messaging, scripts, visuals, thumbnails,
logos, and site copy.

## The chain
```
Three P's (Person/Pain/Promise)
   → Brand positioning doc (positioning statement, message bank, voice)
   → per-brand asset requests (each references the 3 P's)
        → logo / product shots / images
        → YouTube thumbnails (ref scraper + face compositor)
        → video scripts (hook → body → CTA)
        → profiles (X/LinkedIn/IG bios grounded in promise)
```

## Where the assets come from (Hermes-native)
- **Images/logos/product shots** — **OpenAI image model (`gpt-image-1`)** — the
  active backend (verified live 2026-08-24: `images/generations` → HTTP 200,
  saved test to `brands/your-brand/assets/outputs/`). Prompt drafts are grounded
  in the brand's 3 P's + voice. Key: `OPENAI_API_KEY` in profile `.env`.
- **Video scripts** — `marketing-ai-army/agents/05-content-marketing/video-script-agent.md`.
- **YouTube thumbnails** — `PLAN-video-content-skills.md`: reference thumbnails
  captured via **Computer Use** (logged-in Chrome; Supadata is transcript-only,
  [does not do YouTube search]) + face cutouts
  (`brands/<brand>/Faceshots/transparent/`) + OpenAI image backend for
  compositing.
- **Profiles (X/LinkedIn/IG bios)** — written from `positions/three-ps.md` +
  `brand-voice.md`; same person/pain/promise language.

## Per-brand asset output folders
Each brand keeps its own asset folders, named consistently:
```
brands/<brand>/
  positions/three-ps.md      ← required first
  Faces/ or Faceshots/        ← face cutouts for thumbnails
  screenshots/                ← reference thumbnails + designs
  assets/                     ← logos, product shots, images
  output/ (or deliverables/)  ← finished assets the agent generates
```
(The video demo used Claude-created folders; this system mirrors that shape.)

## Step 4 — Minimal social creative renderer

The first reusable creative generator is intentionally local and review-only:
`../shared/social_creative_generator.py`. It uses an existing brand background,
logo, headline, supporting line, and CTA to render a square PNG. It does not
publish, call a paid image API, or modify a source repository.

Example from the central workspace:

```bash
python marketing-ai-army/shared/social_creative_generator.py \
  --background "brands/<brand>/assets/social/covers-banners/<background>" \
  --logo "brands/<brand>/assets/logos/<logo>" \
  --headline "<short headline>" \
  --supporting "<plain-English support line>" \
  --cta "<one CTA>" \
  --eyebrow "<brand name>" \
  --output "brands/<brand>/assets/outputs/social/<dated-name>.png"
```

Use the brand's Three P's and voice before writing the copy. Keep the first
pass to one clear idea and one CTA. Review the image before posting. Record
approved/published variants and performance in the Creative Tracker.

The renderer is the working base for later carousel, UGC, Reel, and ad
creative workflows. Those formats should be added only after a real social
card passes review and the next format has a clear use case.

## Model routing
- Cheap model: transcripts, hook drafts, simple summaries.
- Mid-tier: scripts, ad copy, profile bios, first-pass assets.
- Strong reasoning: positioning, thumbnail template analysis, complex compositing.
- Creative/image model: logo, hero, thumbnail, product-shot generation.

## Guardrails
- **Never invent** pain/person/promise. Read `positions/three-ps.md`; mark gaps
  `NEEDS OWNER INPUT`.
- Posting, publishing, spend, and account changes require explicit approval.
- Ask before generating visuals against a brand whose Three P's aren't filled.

## Definition of done
An asset is done only when it has been **produced, saved** to the right brand
folder, and **verified** (image renders, script read, file exists) — not
described as future work.

## Current status — YouTube thumbnail proof complete
- My Brand's audience, Three P's, and beginner-AI positioning are documented.
- Full-length 16:9 reference boards are collected and visually verified under
  `brands/your-brand/screenshots/full-video-thumbnails/`.
- OpenAI `gpt-image-1` is the verified image backend for generated backgrounds.
- Three review-only thumbnail examples now exist under
  `brands/your-brand/assets/outputs/`: the initial My Brand example, Hermes Agent,
  and OpenAI Codex Platform.
- The transparent face pack and official-logo sourcing rule are in place.

## Remaining setup work
1. Build a reusable thumbnail brief/compositor workflow around a real video topic;
   the current examples prove the visual loop but were not packaged as a
   one-command production tool.
2. Add a lightweight mobile-scale QA and A/B-variant checklist after the first
   real upload cycle.
3. Keep publishing approval-gated and record impressions/CTR before making
   performance claims.