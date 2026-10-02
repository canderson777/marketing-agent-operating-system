# Workflow: Podcast to Content

Turn a podcast episode, interview, or transcript into a canonical content asset plus a distribution package. Use this when you want to extract ideas from a podcast and reshape them into a blog post, X thread/posts, newsletter copy, and optional LinkedIn or short-form video assets.

## Trigger

`../master-agent.md` receives one of these:

- a full transcript
- a cleaned episode summary with timestamps and key quotes
- a podcast URL plus a separately provided transcript or notes

If only a URL is provided and no transcript or notes exist, stop and request a transcript first. This operating system does strategy and content transformation. It is not the audio ingestion layer.

## Required Inputs

| Input | Required | Notes |
|---|---|---|
| Episode title | Yes | Working title is fine if exact title is unknown |
| Source link | Preferred | Apple Podcasts, Spotify, YouTube, site URL, etc. |
| Transcript or notes | Yes | Full transcript preferred; detailed notes acceptable |
| Audience | Yes | Pull from `../shared/customer-avatar.md` if not explicitly given |
| Goal | Yes | Educate, drive traffic, grow newsletter, support offer, etc. |
| CTA | Yes | One CTA per asset, per `../shared/content-rules.md` |
| Canonical asset choice | Yes | Blog, X thread, newsletter essay, or video script |

## Operator Intake Format

Use this package when starting the workflow:

```md
# Podcast Content Intake

## Episode
Title:
Source URL:
Host / guest:
Publish date:

## Goal
Primary objective:
Canonical asset:
Target audience:
CTA:

## Notes
Why this episode matters:
Any angle to avoid:
Any claim requiring extra verification:

## Source Material
[Paste transcript or structured notes]
```

## Step 1 - Source Normalization

- Owner: `../master-agent.md`
- Confirm the business goal, audience, CTA, and canonical asset.
- Label whether the piece is:
  - reaction content
  - summary content
  - insight extraction
  - thought-leadership riff inspired by the source
- Strip filler from the transcript: intros, sponsor reads, repeated banter, housekeeping.
- Flag claims, stats, or quotes that need verification before they can ship.

Output: a one-page brief for `content-marketing-agent.md`.

Hand off: normalized source asset plus brief.

## Step 2 - Angle and Atom Extraction

- Owner: `content-marketing-agent.md` to `repurposing-agent.md`
- Read the full transcript or cleaned notes.
- Extract 5 to 10 atoms:
  - sharp claims
  - useful frameworks
  - stories
  - mistakes
  - contrarian takes
  - quotable lines
- Score each atom against:
  - audience fit
  - novelty
  - proof strength
  - conversion potential
  - repurposing range
- Pick:
  - 1 canonical angle
  - 2 backup angles
  - 1 angle to reject, if the source is too weak or too off-brand

Output format:

```md
SOURCE ASSET: [title + URL + type]
PRIMARY ANGLE: [one sentence]

ATOM SCORECARD:
| Atom | Why it matters | Proof strength | Best format |
|---|---|---|---|

WINNING ANGLE:
[one paragraph]

BACKUP ANGLES:
- ...
- ...
```

## Step 3 - Canonical Asset Production

- Owner: `content-marketing-agent.md`
- Route based on the chosen canonical asset.

### Route A - Blog-first

- `seo-aeo-agent.md` decides whether the piece should be SEO-led or editorial.
- If SEO-led: `blog-outline-agent.md` creates the outline and `blog-agent.md` writes the draft.
- If editorial: `content-marketing-agent.md` briefs `blog-agent.md` directly.
- The blog should not read like a transcript recap. It must become a useful argument, framework, or lesson.

### Route B - X-thread-first

- `social-media-agent.md` briefs `x-twitter-agent.md`.
- The thread becomes the canonical expression of the idea.
- `blog-agent.md` may later expand the thread into a utility or opinion post.

### Route C - Newsletter-first

- `newsletter-agent.md` writes the main essay.
- `repurposing-agent.md` extracts follow-on social atoms.

### Route D - Video/script-first

- `video-script-agent.md` turns the episode's strongest angle into a script.
- `repurposing-agent.md` builds social and email follow-through from the script.

## Step 4 - Distribution Package

- Owner: `repurposing-agent.md`
- Create a documented repurposing pass from the canonical asset or directly from the source transcript if needed.
- Minimum package:
  - 1 email blurb or newsletter feature
  - 3 LinkedIn posts
  - 5 X posts
  - 1 X thread
  - 1 short-form video script
- Optional package:
  - Instagram carousel concept
  - TikTok/Reels talking-head script
  - lead magnet seed idea

Hand off:

- `social-media-agent.md` for platform-specific QA and queueing
- `email-marketing-agent.md` or `newsletter-agent.md` for email formatting
- `content-calendar-agent.md` for scheduling

## Step 5 - Review and Compliance

- Owner: channel sub-masters, then `../master-agent.md`
- Review every asset for:
  - voice match against `brand-voice.md`
  - structure and CTA discipline against `../shared/content-rules.md`
  - quote accuracy
  - claim verification
  - whether the content adds interpretation instead of copying the speaker's phrasing
- If the episode contains unverified numbers, controversial advice, or platform-risky claims, either source them or cut them.

## Step 6 - Packaging

- Owner: `../master-agent.md`
- Approve the final asset set.
- Save deliverables to:
  - `outputs/research/podcasts/[YYYY-MM-DD_episode-slug].md` - intake, summary, atom scorecard
  - `outputs/blogs/[YYYY-MM-DD_slug].md` - blog draft if produced
  - `outputs/social-posts/[YYYY-MM-DD_atom-slug].md` - X/LinkedIn/social drafts
  - `outputs/emails/[YYYY-MM-DD_slug].md` - newsletter or email draft

## Recommended Decision Rules

- Use blog-first when the episode contains a durable framework, teachable process, or searchable topic.
- Use X-thread-first when the best value is a sharp opinion, breakdown, or narrative with clear beats.
- Use newsletter-first when the value is curation, commentary, or a relationship-building POV piece.
- Use video/script-first when the source is story-rich and better spoken than read.

## Kill Criteria

- If the transcript is too thin, repetitive, or generic, do not multiply weak source material. Return it to `../master-agent.md` and request a stronger angle.
- If more than 30% of the candidate atoms rely on unsourced or unverifiable claims, do not publish until fixed.
- If the output reads like a cleaned transcript instead of a transformed asset, send it back for rewrite.

## Fast-Start Prompt For The Operator

```md
Use `podcast-to-content.md`.

Goal: Turn this podcast transcript into:
- 1 blog post
- 1 X thread
- 3 X posts
- 1 newsletter blurb

Audience: [who this is for]
CTA: [what action we want]
Canonical asset: [blog / X thread / newsletter / video]
Source URL: [link]

Transcript:
[paste transcript here]
```
