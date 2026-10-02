# Business Overview

## Brand Name
AccNetwork

## What this brand/business is
ACC Network is an AI newsletter and blog brand focused on helping people stay on top of AI in plain English.

Current positioning from the site and workflow references:
- daily AI signal
- plain-English breakdowns
- beginner-friendly explanations
- newsletter + blog + educational content

## What it sells
Current core product is attention and trust through content.

Likely monetization paths:
- newsletter growth and sponsorships
- partner placements
- affiliate offers
- educational products
- developer or AI implementation services through the "Work With Us" path

## Core problem it solves
AI moves fast and the space is noisy.

ACC Network helps by:
- simplifying AI news and concepts
- curating useful stories
- making updates easier to understand
- giving people a calmer, clearer way to follow the space

## Main transformation / outcome
Help busy readers understand what matters in AI without getting buried in hype or technical jargon.

## Current stage
Verified from the site repo (`the ACC Network site repo`) on 2026-07-07:
- LIVE at https://www.accnetwork.xyz (Vercel, auto-deploys from main).
- Daily weekday newsletter running on MailerLite, with an automated daily draft at 11:15am (sheet -> MailerLite, review and send).
- 7 published blog articles as of 2026-07-06 (5 starter guides + 2 Sunday Deep Dives).
- Live sections: newsletter signup homepage, blog, developer directory, resources, events, glossary, about, contact.

## Key production docs
- Newsletter build format: `docs/newsletter-email-format.md in the ACC site repo` (MailerLite layout, subject pattern, section order).
- Newsletter suggestions sheet (approved items only): linked in that format doc.
- Blog post registry: `AccDevSite/lib/blog/posts.ts`.

## Primary marketing channels
- The newsletter (email via MailerLite) is the product and primary channel; the site/blog feeds it.
- X (@ACC_Official1) is the main fast-moving social channel, amplified by the founder account the founder's personal account.
- LinkedIn now includes an ACC Network company page plus a founder-published LinkedIn newsletter. Use the company page for branded distribution and the founder feed for selected insight-led posts, not daily duplicate announcements.
- Facebook / Meta business page: https://www.facebook.com/profile.php?id=61593689723601. The page uses ACC logo/banner assets and sends signup traffic to https://www.accnetwork.xyz (owner-confirmed 2026-08-19).

## Notes
- website headline (verbatim from layout metadata): "ACC Network: Your Daily AI Signal, in Plain English"
- full meta description: "A daily 5-minute brief on AI model releases, vetted tools, robotics, jobs, and X Spaces, written in plain English for anyone curious about AI, from first project to production."
- founder identity on the site: "Prof. J ... Taxi driver by day, AI builder by night, host of the AI Builders Showcase" (about page).
- audience should feel informed, not overwhelmed
- tone should stay grounded, useful, and beginner-friendly
- Baseline metrics pulled live from MailerLite 2026-07-08 (account 2325093, group "ACC Network Newsletter" 186778608262449057):
  - Active subscribers: 11 (14 total in account incl. unsubscribed/bounced)
  - Lifetime group open rate: 19.12% | click rate: 1.47% (68 sends, 13 opens, 1 click)
  - 8 campaigns sent, all 2026-05-12 to 2026-05-21; NOTHING SENT SINCE MAY 21 - sending paused ~7 weeks, confirming the restart priority
  - Best performer: 5/18 issue "with images" at 40% opens; range 12.5%-40%
  - Sender: newsletter@accnetwork.xyz (custom domain, ~100% delivery)
