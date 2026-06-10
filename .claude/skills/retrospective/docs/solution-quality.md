# Encoding Guidelines

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

# Solution Quality: Think Like Mario

Proposed fixes must follow first-principles system design principles. No quick patches that create debt.

**Before proposing a fix, ask:**
1. Is this fixing the symptom or the cause? (Principle #1: minimal core)
2. Should this be a registry entry, not a hardcoded check? (#2: registry over inheritance)
3. Am I adding a field/flag when I should fix the data flow? (#11: extend views not data model)
4. Will this fix survive the next state run, or will it break again? (#6: boundary transformation)

**Anti-patterns in retrospective fixes:**
- "Add a special case for X" → find the general rule X violates
- "Check for X after the fact" → prevent X from entering the pipeline
- "Add a validation step" → fix the source of invalid data
- "Hardcode this exception" → make it a registry entry or classification rule

**Example:** "merge-tier2.py drops category" is not fixed by "add category back in build-dashboard.py." It's fixed by making merge-tier2.py preserve the field. Fix at the source, not downstream.
