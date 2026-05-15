---
name: retrospective
description: Analyze the current session to extract reusable learnings and propose updates to relevant skills. Use when the user asks for a retrospective, what did we learn, or how skills should be updated. Triggers: retrospective, what did we learn, update skills.
---

# Retrospective

Analyze the current session and extract learnings that should flow back into skills.

## When to Use

- After completing a multi-step workflow (examples from my setup — replace with your skills: video edit, launch, newsletter, etc.)
- When the user says "retrospective", "what did we learn", "update skills"
- Agent should SUGGEST running this after any session where:
  - Work was redone more than once
  - User corrected the approach ("this is not great", "don't do that")
  - Steps were improvised that aren't in the skill

## Quick Start

```
/retrospective                    # Analyze current session
/retrospective video              # Focus on video skill learnings
/retrospective launch             # Focus on launch skill learnings
```

## How It Works

### Step 1: Extract Signals

Scan the conversation for these patterns:

**Corrections** (highest priority):
- User rejected output: "this is not great", "remove this", "bullshit", "wrong"
- User redirected approach: "no, do it this way", "don't do that", "let's not"
- User added context the agent didn't have: "we have a skill for that", "follow the playbook"

**Redone work:**
- Something generated, rejected, regenerated with different approach
- Multiple iterations on the same artifact (3+ versions)
- Sub-agent output that had to be cleaned up or rewritten

**Missing steps:**
- Things improvised that weren't in the workflow
- Steps that should have been in the checklist but weren't
- Tools/scripts that existed but weren't referenced in the skill

**What worked well:**
- Patterns that produced good results on first try
- New approaches that should become the default
- Shortcuts that saved time

### Step 2: Map to Skills

For each learning, identify:
- Which skill file needs updating
- The specific section to modify
- Whether it's a new rule, a fix to an existing rule, or a removal

### Step 3: Propose Diffs

Present findings as a table:

```
| # | Learning | Skill File | Change |
|---|----------|-----------|--------|
| 1 | Tags once, never in opening | x-article.md | Add tag rules section |
| 2 | LinkedIn needs paragraphs | launch.md | Add to formatting rules |
| 3 | Quartz post required | newsletter.md | Add Step 7a |
```

Then show the actual edits for approval.

### Step 4: Apply

After user approves, apply all edits. One edit per skill file, show the diff.

## What NOT to Encode

- One-off fixes that won't recur
- Content-specific decisions (which diagram to use for THIS video)
- Temporary state (program starts Mar 17 - that changes)
- Things already in the playbook/voice profile

## What TO Encode

- Process changes: "always do X before Y"
- Anti-patterns: "never do X, it causes Y"
- Tool behavior: "NoteTweet doesn't support --media"
- Format rules: "X articles use paragraphs, not one-sentence-per-line"
- Missing steps: "create Quartz post, not just images"
- Proven patterns: "real screenshots + hand-drawn diagrams together"

## Auto-Suggest Convention

After completing any multi-step workflow, check if retrospective is needed:

**SUGGEST retrospective if:**
- More than 2 corrections from the user during the session
- Any artifact regenerated 3+ times
- Steps improvised that aren't documented in the skill
- User explicitly asks "what did we learn"

**DO NOT suggest if:**
- It's the first time using the skill (learning curve is normal)
- User explicitly says "just finish, don't analyze"
- The issue was a one-off bug, not a pattern
- User already ran retrospective recently on this skill

When suggesting: "We iterated a few times here. Want to run `/retrospective` to update the skill so next time is faster?"

The user decides. This is a nudge, not a requirement.
