# Short-Form Reel Creative Workflow

**Purpose:** Turn one approved idea into a platform-native Reel package with controlled motion production and a review-only handoff.

## Required inputs

- Locked campaign brief
- Source article, newsletter item, or verified talking points
- Audience, platform, length, speaker mode, and CTA
- Brand visual assets and colors
- Motion tool, model, credit budget, and approval status

## Procedure

1. Select one idea and write 3–5 hook options.
2. Choose a 15–30 second cut and, only when justified, a 45–60 second cut.
3. Write a speakable script with a clear first-three-second hook.
4. Convert the script into a timed shot list. Each shot must clarify the spoken point.
5. Define on-screen text separately from voiceover. Keep text short and mobile-safe.
6. Define caption/subtitle treatment and a single CTA end card.
7. Separate generated visuals from controlled text overlays. Never rely on a video model to render exact copy or logos.
8. Prepare the generation prompt, model, parameters, reference assets, and estimated credits.
9. Show the complete proposal and wait for explicit operator approval before calling the generation tool.
10. Generate the smallest useful review asset. Do not create variants until the first pass is reviewed.
11. Assemble captions, logo, CTA card, and audio in the fallback editor/render step.
12. Verify 9:16 dimensions, legibility at mobile scale, timing, claims, logo treatment, and file existence.

## Output package

Use `marketing-ai-army/shared/reel-creative-package-template.md` for the standard package format.

```md
# Reel Creative Package
STATUS:
GOAL:
PLATFORM:
LENGTH:
SOURCE:
HOOK OPTIONS:
SELECTED HOOK:
SCRIPT / VOICEOVER:
SHOT LIST:
ON-SCREEN TEXT:
CAPTION GUIDANCE:
CTA END CARD:
GENERATION PROMPT:
MODEL / PARAMETERS:
ESTIMATED CREDIT COST:
REFERENCE ASSETS:
MANUAL FALLBACK:
QA CHECKLIST:
APPROVAL STATE:
```

## Animated Visuals Direction

When the brief calls for animated visuals (such as ACC Network's editorial motion direction):
1. **Visual Metaphor:** Translate the cognitive shift into motion (e.g. noise to signal, cluttered fragments converging into a single clear forward path).
2. **Pacing & Restraint:** Use smooth, deliberate camera motion and kinetic geometry rather than hyperactive glitching or distracting transitions.
3. **Mobile Safe Margins:** For 9:16 vertical video, keep all core motion and post-production overlays within safe zones:
   - Top 15%: Clear of platform navigation/status bars.
   - Bottom 20%: Clear of audio tags, caption overlays, and action buttons.
   - Sides 10%: Clear of edge clipping.
4. **No Text In Generation:** Maintain clean negative space in the generative layer; strictly render headlines, subtitles, logos, and URLs in local post-production.

## Higgsfield prompt rules

- Describe subject, action, camera, pacing, composition, palette, and negative constraints.
- Ask for clean visual space for post-production text.
- Do not ask for readable statistics, fake interfaces, fake headlines, or exact brand typography inside generated footage.
- Use the logo as a controlled overlay unless the approved workflow explicitly supports a reference image.
- Use `prefers-reduced-motion` only for local web previews; for video, offer a slower-cut fallback.

## Manual fallback

Use the local social renderer for title cards, an ordinary video editor for clip assembly, and burned-in captions. The fallback must preserve the same script, CTA, and approval state.

## QA gate

- First three seconds communicate the problem or promise.
- Voiceover is speakable and factually grounded.
- Visuals support the explanation.
- Captions remain readable without sound.
- CTA appears once and points to the canonical destination.
- No generated visual implies an unverified fact.
- Asset is marked `REVIEW ONLY` until the operator approves publishing.
