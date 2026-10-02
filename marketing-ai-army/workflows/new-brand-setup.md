# New Brand Setup Workflow

One command/checklist to scaffold a brand so a new business/new client can be
onboarded with a consistent structure, without duplicating the Marketing AI Army.
This is the In-house equivalent of the YouTube "set up a new business folder"
workflow (brand assets + a per-project AI instruction file + optional site).

## When to use

- Adding a brand to `brands/` for the first time.
- A brand that previously had only context files now gets its asset/home structure.
- A new client signing up: this is the repeatable onboarding scaffold.

## Step 0 — prerequisites
1. Read the brand's context first (see `brand-intake-grill.md` if thin).
2. Confirm `brands/README.md` lists the brand with a slug.
3. Decide the folder: `brands/<slug>/` is the default for a managed brand.

## Step 1 — Create the standard asset folder
Create (do not leave empty placeholders; each gets a README unless noted):
```
brands/<slug>/
  assets/
    README.md
    logos/               # official logos, variants, favicons
    brand-guidelines/     # brand voice/style tokens, palettes, guideline notes
    product-shots/        # app/site/device screenshots, product photos
    studio-shots/         # founder/office/real-world imagery
    social/               # ready-to-post social creatives
      post-images/
      thumbnails/
      covers-banners/     # profile/cover/banner images
  outputs/                # finished generated assets (thumbnails, ad creatives)
  strategy/               # created only when real plans exist
  proof-notes/            # created only when real results exist
  positions/three-ps.md    # required first (via three-ps-template)
```
Mirror the structure that My Brand already uses (`assets/logos`, `assets/outputs`,
`Faceshots/`, `screenshots/`) so one asset engine serves every brand.

## Step 2 — Populate social-able assets (the part that enables posting)
For each brand, collect at least the visual essentials for social:
- **Logo** (favicon, square, full, light/dark) -> `assets/logos/`
- **Cover/banner** -> `assets/social/` (or `covers-banners/`)
- **Profile image** -> `assets/social/`
- **Post templates / examples** -> `assets/social/`
- **Product/teardown shots** -> `assets/product-images/`

Grab from existing sources before asking: ACC logo lives in `the ACC site repo's public/images/`; Local Glow Up logo in its project folder; etc. Mark any missing asset `NEEDS OWNER INPUT: <asset>` instead of inventing one.

## Step 3 — Write the per-project AI instruction file
Create `brands/<slug>/hermes.md` (portable; the video used `claude.md`; the
equivalent here is `hermes.md`). It tells any future agent what THIS project is:
```md
# <Brand> — Project Instructions

## What this is
[one-line business] · [stage]

## Files agents must read first
- business-overview.md   — what it sells, stage
- audience.md            — who it serves, pains
- offers.md              — offer + exact CTA
- brand-voice.md         — tone + do/don't rules
- content-pillars.md     — recurring themes
- positions/three-ps.md  — Person / Pain / Promise (REQUIRED before asset work)
- current-priorities.md  — what matters now (dated)

## Assets
[paths to logos/product shots/social assets]

## CTA
[primary CTA + secondary social CTA]

## Approvals
[what is / is not approved to publish — default: nothing auto]
```

## Step 4 — Optional: premio website build (Scroll-world)
If the brand needs a site, point the build at the Oso95 Scroll-world template:
- Repo: `https://github.com/oso95/scroll-world`
- Instruction: "Set up a premium website for <Brand> referencing the assets in
  `brands/<slug>/assets/` and the Scroll-world repo, appealing to <Person>."
Keep this gated: do not push/publish a site without explicit approval.

## Step 5 — Classify readiness and record
Update `brands/README.md` with the brand + status (READY/PARTIAL/PARKED/EMPTY).
Record the onboarding time — this number becomes the managed-service sales claim
("a new business is scaffolded in N minutes").

## Rules / guardrails
- Create only the folders a brand actually needs; do not pre-create `strategy/`
  or `proof-notes/` as empty shells — create them when the brand produces output.
- Never copy the Marketing AI Army engine or its workflows into the brand folder.
- Pull assets before asking; mark anything missing `NEEDS OWNER INPUT`.
- Do not publish, push a site, or enable external tool access without approval.