# Step 1: Extract Signals

Scan the conversation for these patterns:

## Corrections (highest priority)

- User rejected output: "this isn't great", "remove this", "wrong"
- User redirected approach: "no, do it this way", "don't do that"
- User added context I didn't have: "we have a skill for that", "follow the playbook"

## Redone Work

- Something generated, rejected, regenerated with different approach
- Multiple iterations on same artifact (3+ versions)
- Sub-agent output that had to be cleaned up

## Missing Steps

- Things improvised that aren't in workflows
- Steps that should've been in checklist but weren't
- Tools/scripts that existed but weren't referenced

## What Worked Well

- Patterns that produced good results first try
- New approaches that should become default
- Shortcuts that saved time

## Output Format

Present as a table:

```
| # | Learning | Skill | Change |
|---|----------|-------|--------|
| 1 | Tags once, never in opening | skill.md | Add section |
| 2 | LinkedIn needs paragraphs | launch.md | Update rules |
```
