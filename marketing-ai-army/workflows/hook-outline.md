# Hook Outline — Workflow

**Purpose:** Take a high-performing video → condense it to its **intro + outline structure** → re-apply that exact structure to one of the operator's own video ideas.

**Origin:** Riley Brown interview method — "condense a winning video down to a hook outline, then take that exact format and apply it to a different video."

## When to use
- the operator shares a strong video and wants to borrow its opening/structure.
- Planning any YouTube / IG / long-form video for Local Glow Up, My Brand, or ACC.
- Worst-performing-to-better-packaging pass: one video idea, several winning structures to test.

## Prerequisites
- Transcript of the source video (use the `youtube-content` skill — free, already wired).
- Optionally: the operator's topic + rough idea for the re-applied version.

## Procedure

### 1. Fetch & read the source
Pull the source video's transcript (`youtube-content`), identify its category (interview, tutorial, case study, listicle, essay).

### 2. Extract the Hook Outline (schema below)
Produce a `Hook Outline` doc for the source. Timestamp the segments.

### 3. Score the hook with BRENS
**B**ig · **R**elatable · **E**asy · **N**ew · **S**afe
Mark which boxes the source's opening ticks. More ticks = stronger hook. Note the ONE it leans on hardest.

### 4. Isolate the transferable skeleton
Distill the reusable shape (the part you can copy without copying the content):
- Opening move (cold-open teaser? outcome statement? credential?)
- How the body is ordered (problem → method → demo → proof → offer?)
- Where the credibility/safety lines land
- The close/CTA move

### 5. Re-apply to the operator's idea
Rewrite step by step using the operator's topic, keeping the skeleton identical:
- Hook rewritten with his topic + BRENS
- Body segments re-mapped to his topic
- Close/CTA pointed at his route (Local Glow Up → calendly)
- Always topic-first & tool-agnostic unless the video is explicitly a tool walkthrough

### 6. Verify
Re-read for coherence: real timestamps, the re-applied version actually follows the skeleton (not content), BRENS claims are grounded in what the source actually does.

## Hook Outline schema
```markdown
# Hook Outline — <source title>
Source: <url> | Creator: | Why it performs:
## 1. The Hook (opening N seconds)
- Cold open / opening move:
- Outcome statement:
- BRENS score + the one it leans on:
- Credibility / safety line (long videos):
## 2. Body Outline
- [TS] segment
## 3. Transferable skeleton
## 4. Re-applied version (my topic)
- Hook / Body / Close-CTA
```

## Model routing
- Cheap model: transcript fetch + first draft of the outline (low risk, robust task).
- Strong model only if the source is dense/long or the operator wants the re-applied version made sharp.

## Output location
- Workflow is the template: `marketing-ai-army/workflows/hook-outline.md`
- Filled outputs: `marketing-ai-army/outputs/hook-outlines/<slug>.md`
