# Workflow: X MCP Social Listening + Review

Use this workflow when X/Twitter work needs live platform context, not just internal source docs.

## Goal

Turn X MCP into a supervised X department tool for:
- daily X intelligence
- thread research
- reply options
- bookmark idea inbox
- creator/competitor tracking
- weekly performance review
- X Articles drafts

Default posture: **research + draft + recommend + approval**.

Do not use this as an autonomous posting workflow.

## Required Sources

Before using live X data, gather the brand sources first:

1. Brand docs under `brands/<brand>/`
2. Channel docs:
   - `../agents/02-social-media/social-media-agent.md`
   - `../agents/02-social-media/x-twitter-agent.md`
3. Shared rules:
   - `../shared/tool-registry.md`
   - `../shared/content-rules.md`
   - the brand's `brand-voice.md` and channel strategy when working on a specific brand
4. Brand-specific source material:
   - For My Brand: AI Daily Journal first
   - For My Brand: My Twitter Post doc or post tracker to avoid duplicates

X MCP adds live context. It does not replace brand source-of-truth files.

## Setup Requirement

X MCP requires:
- X Developer app with OAuth 2.0 enabled
- redirect URI: `http://localhost:8080/callback` unless overridden
- `CLIENT_ID` and `CLIENT_SECRET` available to the MCP client
- Node.js / `npx`
- MCP server connection through `xurl mcp https://api.x.com/mcp`

Recommended Hermes MCP setup after credentials exist:

```bash
hermes mcp add xapi \
  --command npx \
  --env CLIENT_ID=YOUR_X_APP_CLIENT_ID CLIENT_SECRET=YOUR_X_APP_CLIENT_SECRET \
  --args -y @xdevplatform/xurl mcp https://api.x.com/mcp

hermes mcp add x-docs --url https://docs.x.com/mcp
hermes mcp test xapi
hermes mcp test x-docs
```

Use placeholders in docs only. Put real `CLIENT_ID` and `CLIENT_SECRET` into Hermes MCP environment config or a local secret source, not committed markdown files.

Never paste OAuth tokens, client secrets, or `~/.xurl` token cache into chats, docs, screenshots, or repo files.

## Operating Modes

### 1. Listen

Use when the operator asks what is happening around a topic.

Inputs:
- topics / keywords
- date range
- accounts to include or avoid
- geography or niche if relevant

Output:

```md
# X Intelligence Brief

## Topic

## What people are talking about
- [point]

## Useful posts/accounts to inspect
- [handle/post/link]

## Content angles
1. [angle]
2. [angle]
3. [angle]

## Risks / noise
- [risk]

## Recommended next action
- [draft / reply / skip / watch]
```

### 2. Research

Use before drafting threads, POV posts, or market-timing content.

Inputs:
- topic
- target audience
- relevant accounts
- proof/source docs
- angle to validate

Output:
- research notes
- common claims
- gaps in the conversation
- contrarian but fair angles
- draft-ready hooks

Rules:
- Do not copy another creator's phrasing.
- Use X data as context, not as the whole argument.
- Tie final drafts back to source docs or real proof when possible.

### 3. Draft

Use when source material is ready and live context can improve the draft.

Output:
- 3-5 standalone X post options
- 1 thread outline when the idea deserves depth
- reply options if the source was a post/mention
- recommended CTA

Rules:
- Standalone X posts stay under 280 characters unless the operator asks for a thread.
- Keep My Brand direct, practical, build-in-public, and specific.
- Avoid fake virality bait.

### 4. Review

Use during weekly audit.

Inputs:
- date range
- recent posts
- engagement signals
- manual notes if API data is incomplete

Output:

```md
# Weekly X Review

## Posted
- [post/link/date]

## Best performers
- [post/link + reason]

## Weak posts
- [post/link + reason]

## Keep / improve / stop / scale
| Decision | Content type | Reason |
|---|---|---|

## Repurpose candidates
- [post] -> [thread/blog/newsletter/video/proof note]

## Next week recommendations
1. [recommendation]
2. [recommendation]
3. [recommendation]
```

### 5. Publish

Approval-only.

Allowed after explicit operator approval:
- publish an approved post if tooling supports it
- publish an approved X Article if tooling supports it
- bookmark / unbookmark if approved

Never do these without explicit approval:
- post
- delete
- like
- repost
- quote
- follow / unfollow
- DM
- modify bookmarks/folders
- publish Articles

## My Brand Weekly Use

For My Brand, the highest-value weekly flow is:

1. Pull the AI Daily Journal.
2. Pull the My Twitter Post doc or post tracker to avoid duplicates.
3. Pull recent X posts/engagement when X MCP is connected.
4. Build the weekly audit:
   - what posted
   - what was missing
   - what performed
   - what should be repurposed
   - what should become proof notes
5. Build next week's schedule from actual work + actual performance.

## Fallback If X MCP Is Not Available

Use:
- AI Daily Journal
- My Twitter Post doc
- manual screenshots/links from X
- proof notes
- existing schedule files
- manual metrics pasted by the operator

Do not block the content system just because X MCP is not connected.

## Kill Criteria

Do not use X MCP when:
- credentials are missing
- scopes are unclear
- rate limits are blocking useful data
- live X data would distract from stronger proof notes
- the task is simple enough from journal/proof docs alone
- the operator has not approved any account-changing action
