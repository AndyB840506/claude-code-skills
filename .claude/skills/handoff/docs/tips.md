# Tips & Best Practices

## When to Use Handoff

- **End of day** — summarize the day's work before closing
- **Mid-session break** — if pausing for a few hours or switching projects
- **Blocking point** — document what's blocking you before moving on
- **Session-close workflow** — this is Step 4 of `/session-close`

## Tips

- **Copy the entire document** — paste it at the start of next session for quick context
- **Customize before closing** — edit the generated document if you want to add personal notes
- **Always backs up** — even minimal handoff documents trigger git push
- **Manual or automatic** — invoke `/handoff` anytime, or let `/session-close` do it
- **Use with session-close** — for full workflow, use `/session-close` which includes retrospective, skill review, and handoff
- **Topic auto-detection** — if you don't specify a topic, it's extracted from git commits
- **Files to read** — document lists recently changed files to orient the next session

## What Gets Included

**Automatically extracted:**
- Recent commits and changes (from git log)
- Modified files (from git diff)
- Topic/theme (from commit messages)

**Requires your input:**
- Where we paused exactly
- Next action to take
- Any blockers or decisions needed

## Customization

The generated document can be edited before the next session:
- Add notes about approach changes you're considering
- Update blockers if you solve them
- Add clarifications about files or decisions

Just paste the updated version at the start of the next session.
