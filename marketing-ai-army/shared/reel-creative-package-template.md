# Reel Creative Package Template

Use this template to package short-form vertical video creative (Reels, TikTok, Shorts) for any brand before spending generation credits or publishing.

---

## 1. Metadata
- **Brand:** 
- **Campaign Name:** 
- **Asset ID / Title:** 
- **Status:** DRAFT / REVIEW ONLY / APPROVED / REJECTED
- **Target Platform(s):** Facebook Reels / Instagram Reels / TikTok / YouTube Shorts
- **Target Duration:** 15–30s (Default) / 45–60s
- **Primary CTA:** 
- **Canonical Destination URL:** 

---

## 2. Concept & Hooks
- **Core Problem / Angle:** 
- **Hook Options (Choose 1):**
  - *Option 1 (Pain/Direct):* 
  - *Option 2 (Curiosity/Question):* 
  - *Option 3 (Counter-intuitive/Contrarian):* 
- **Selected Hook:** 

---

## 3. Spoken Script / Voiceover (15–30 Seconds)
*Pacing: ~130–150 words per minute. A 20-second script is ~45–55 words.*

- **[00:00 - 00:03] Hook:** 
- **[00:03 - 00:08] Agitation / Clarification:** 
- **[00:08 - 00:15] Core Value / The Shift:** 
- **[00:15 - 00:20] Call to Action:** 

---

## 4. Timed Shot List & Visual Composition

| Timecode | Visual Description / Motion Action | On-Screen Text (Mobile Safe) | Audio / Voiceover Line |
|---|---|---|---|
| `00:00 - 00:03` | [Hook shot: rapid motion/contrast] | [Bold hook headline] | "[Spoken hook line]" |
| `00:03 - 00:08` | [Problem visual / transition] | [Key problem takeaway] | "[Agitation line]" |
| `00:08 - 00:15` | [Solution / resolving motion] | [Core concept pill/bullet] | "[Value explanation]" |
| `00:15 - 00:20` | [Clean end card with logo & URL] | [Canonical CTA + URL] | "[Clear call to action]" |

---

## 5. Visual Layer & Motion Prompting (Generative / Animated)
- **Visual Style:** (e.g., Animated editorial motion graphic, 3D abstract, clean minimalism)
- **Color Palette:** 
- **Generative Motion Tool:** Higgsfield / Other
- **Model Selected:** (e.g., `veo3_1_lite`, `wan2_7`)
- **Generation Parameters:**
  - `aspect_ratio`: `9:16`
  - `duration`: `4` (or `5`)
  - `resolution`: `720p`
  - `generate_audio`: `false`
- **Exact Generative Prompt:**
  ```text
  [Subject and environment description] + [Motion dynamic and transition] + [Palette and lighting] + [Safe space for overlays] + [Negative constraints: no text, no logos, no interfaces, no glitch]
  ```
- **Estimated Credit Cost:** X credits
- **Pre-Generation Balance:** Y credits
- **Operator Approval State:** PENDING / APPROVED

---

## 6. Controlled Post-Production Layer
- **Typography:**
  - Hook font / weight / color:
  - Body caption style: High-contrast subtitles with dark backing or outline.
  - Safe margins: Top 15% and bottom 20% clear of UI buttons and captions.
- **Brand Assets:**
  - Official Logo path: 
  - Logo placement: Top center or bottom-left subtle watermark.
- **Audio:**
  - Voiceover file / TTS / Voice recording:
  - Background music: Low ambient bed (-18dB to -24dB).
- **CTA End Card Specifications:**
  - Clear text: `[CTA Action] → [Canonical URL]`
  - Duration: 3–5 seconds holding still for readability.

---

## 7. Fallback Manual Production (Zero Provider Credits)
- If provider generation is unavailable or rejected:
  1. Use local Pillow/OpenCV renderer to generate branded title and transition cards.
  2. Assemble in a standard video editor with kinetic typography and subtle zoom/pan motion.
  3. Overlay voiceover track and burned-in captions.

---

## 8. QA Checklist (Review-Only Gate)
- [ ] First 3 seconds communicate the pain or promise clearly.
- [ ] Spoken voiceover is natural, concise, and jargon-free.
- [ ] On-screen text stays inside 9:16 mobile-safe margins.
- [ ] Generative visuals contain NO garbled AI text or hallucinated logos.
- [ ] Official logo is sharp, correct aspect ratio, and properly masked.
- [ ] Canonical URL is spelled out character-by-character correctly.
- [ ] Exactly one CTA is presented.
- [ ] File verified: format, dimensions (720x1280 or 1080x1920), duration, audio sync.
- [ ] Marked REVIEW ONLY until explicit publishing authorization is granted.
