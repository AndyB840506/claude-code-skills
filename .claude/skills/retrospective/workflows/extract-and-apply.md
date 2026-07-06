# How It Works

## Step 1: Extract Signals

Scan the conversation for these patterns:

**Silent judgment calls** (check this even if the user never objected):
- Ask explicitly: "What did I decide today by my own judgment that isn't written
  anywhere as a rule?" — e.g. picking a default when the request was ambiguous, filling
  a gap the user didn't spell out, resolving a naming/format/scope choice without asking.
- These are the highest-value learnings for a model that infers less from context: an
  undocumented judgment call is invisible until the next session (or a different model)
  gets it wrong. Absence of a user correction does NOT mean there's nothing to encode —
  it may just mean the judgment call happened to be right this time.

**Corrections** (highest priority when present):
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

## Step 2: Map to Skills

For each learning, identify:
- Which skill file needs updating
- The specific section to modify
- Whether it's a new rule, a fix to an existing rule, or a removal

## Step 3: Propose Diffs

Present findings as a table:

```
| # | Learning | Skill File | Change |
|---|----------|-----------|--------|
| 1 | Tags once, never in opening | x-article.md | Add tag rules section |
| 2 | LinkedIn needs paragraphs | launch.md | Add to formatting rules |
| 3 | Quartz post required | newsletter.md | Add Step 7a |
```

Then show the actual edits for approval.

## Step 4: Apply

After user approves, apply all edits. One edit per skill file, show the diff.
