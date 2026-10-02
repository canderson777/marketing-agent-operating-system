# Browser Access Workflow (Computer Use)

How this system reaches social platforms that have **no usable API/MCP** for the user's
personal brand. Uses Hermes `computer_use` driving the user's **already-logged-in Chrome**
session. No API keys, no third-party schedulers, no Meta app approval.

## Platforms & targets

| Platform | Method | Target | Status |
|---|---|---|---|
| LinkedIn | Computer Use | linkedin.com (logged-in session) | ✅ **Proven** — used 2026-07-20 audit (316 connections captured) |
| Instagram | Computer Use | Meta Business Suite (business.facebook.com) | ⚠️ **Not yet practiced** — test planned |
| Facebook | Computer Use | Meta Business Suite (business.facebook.com) | ⚠️ **Not yet practiced** — test planned |

Instagram + Facebook are handled together through **Meta Business Suite** so both feeds live
under one logged-in session.

## Why browser over API
- Meta/IG Graph API for personal posting is gatekept: needs a Business/Creator account linked
  to a Facebook Page, a Meta Developer app, business verification, and app review. Overkill for a
  personal brand.
- Third-party schedulers (Buffer/Later) are a separate subscription outside Hermes.
- Browser path = zero setup, zero credentials, user stays in control.

## Operating rules
1. **User stays signed in / steps in at auth walls.** When computer_use hits a login wall, 2FA,
   or a fresh session, STOP and ask the user to sign in, then continue from the live session.
   Do NOT handle passwords, 2FA codes, or payment/login UI yourself.
2. **Read/audit first, post second.** Capture the signed-in profile (connections, headline,
   location, follower count) as the audit baseline.
3. **Posting requires explicit approval** per the system's execution/approval rules.
4. Use `app='Chrome'` scope for captures to avoid leaking other open windows.
5. If `computer_use` returns `suspected_noop`/`unverifiable`, re-capture fresh state before any
   retry; escalate to foreground only on a returned signal. Stop and hand off after a few failed
   attempts (user's preference — no endless retries).

## Audit baseline pattern (proven on LinkedIn 2026-07-20)
Capture and record: signed-in profile, connection/follower count, headline, location, and recent
activity. Save to the brand folder's `links-and-assets.md` and a dated audit note in
`brands/<brand>/strategy/` or `proof-notes/`.

## Source of truth
All other integrations confirmed live in the `marketing-agent-system` profile:
- Google Drive — OAuth (credentials were copied into the profile dir 2026-08-14 so the token
  resolves under the profile's `HERMES_HOME`)
- X — xapi MCP (verified: `get_users_me` returned the founder's personal account)

See also: `marketing-ai-army/agents/02-social-media/linkedin-agent.md` (content-writing spec,
not a connection).
