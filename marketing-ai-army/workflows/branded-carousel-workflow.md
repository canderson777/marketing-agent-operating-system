# Branded Carousel Workflow

**Purpose:** Build a useful, saveable 5–7 slide carousel for social distribution while keeping copy, layout, and approval consistent across channels.

## Required inputs

- Locked campaign brief
- One audience pain and one takeaway
- Source article, newsletter item, or verified notes
- Channel and aspect ratios
- Brand assets, colors, and typography rules
- CTA and approval status

## Procedure

1. Choose one narrow idea. A carousel should teach one thing, not summarize an entire topic.
2. Write the cover hook in one sentence.
3. Build a 5–7 slide sequence: hook, problem, explanation, practical takeaway, and CTA.
4. Keep one idea per slide. Use short lines and high contrast.
5. Create square (1:1) and portrait (4:5) layouts from the same copy system.
6. Keep generated imagery optional. Prefer controlled typography and approved brand assets for factual or branded slides.
7. If an image generator is proposed, show the prompt, model, parameters, reference assets, and estimated credits before generation.
8. Show a complete review board or exported assets. Wait for the operator's approval before publishing or creating additional variants.
9. Verify mobile readability, slide order, CTA destination, alt text, and file paths.

## Output package

Use `marketing-ai-army/shared/carousel-creative-package-template.md` for the standard package format.

```md
# Carousel Creative Package
STATUS:
GOAL:
CHANNELS:
SOURCE:
CORE TAKEAWAY:
SLIDE COPY:
VISUAL SYSTEM:
SQUARE VERSION:
4:5 VERSION:
CAPTION:
ALT TEXT:
OPTIONAL IMAGE PROMPT:
MODEL / PARAMETERS:
ESTIMATED CREDIT COST:
QA CHECKLIST:
APPROVAL STATE:
```

## ACC-friendly structure

1. **Cover:** AI news is noisy. Here is how to find the signal.
2. **Problem:** More headlines do not automatically mean more understanding.
3. **Filter 1:** What changed?
4. **Filter 2:** Who does it help?
5. **Filter 3:** What can you actually do with it?
6. **Takeaway:** Ignore the hype until the practical meaning is clear.
7. **CTA:** Get the daily AI signal in plain English → accnetwork.xyz

## Guardrails

- No invented data points or fake screenshots.
- No tiny paragraphs, dense jargon, or multiple competing CTAs.
- Do not copy the same caption and slide order blindly across Facebook, LinkedIn, and X.
- Keep alt text descriptive and factual.
- Mark all exports `REVIEW ONLY` until approved.
