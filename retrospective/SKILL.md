---
name: retrospective
description: "Analyze the current session to extract reusable learnings and propose updates to relevant skills. Use when the user asks for a retrospective, what was learned, or how skills should be updated. English triggers: retrospective, what did we learn, update skills, what changed, what to improve, session review, what worked, what did we do. Triggers ES: retrospectiva, qué hicimos hoy, resumen de sesión, qué aprendimos, actualizar skills, qué cambió, qué mejorar, resumen de lo que hicimos, retro."
---

# Retrospective

Analyze the current session and extract learnings that should flow back into skills.

## When to Use

- After completing a multi-step workflow (e.g., lead generation, skill creation, session close, interview scoring)
- When the user says "retrospective", "what did we learn", "update skills"
- Agent should SUGGEST running this after any session where:
  - Work was redone at least twice
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
- Bilingual skill validation patterns (verify Spanish and English triggers activate the correct skill)
- Multi-tier fallback patterns (primary → alternative → skip option with clear user guidance)

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

## Scope Guard (IMPORTANTE)

Este skill modifica **contenido** de skills (reglas, heurísticas, aprendizajes). Alcance:

- ✅ Puede tocar: reglas de negocio, anti-patrones, pasos faltantes, aprendizajes de sesión
- ❌ NO toca: frontmatter `name:`, nombres de triggers, numeración de pasos, conteos de líneas — eso es scope de `/skill-kit-auditor`

**Después de aplicar los cambios:** Sugiere al usuario correr `/skill-kit-auditor` para verificar que los archivos actualizados cumplen las reglas estructurales del kit.

---

## What NOT to Encode

**Red flags — skip these when proposing updates:**

- One-off fixes that won't recur
- Content-specific decisions (which diagram to use for THIS video)
- Temporary state (program starts Mar 17 - that changes)
- Things already documented in the playbook/voice profile

**Why skip them:** They clutter the skill with noise and don't generalize to future sessions.

## What TO Encode

**Green flags — these ARE worth encoding:**

- Process changes: "always do X before Y"
- Anti-patterns: "never do X, it causes Y"
- Tool behavior: "NoteTweet doesn't support --media"
- Format rules: "X articles use paragraphs, not one-sentence-per-line"
- Missing steps: "create Quartz post, not just images"
- Proven patterns: "real screenshots + hand-drawn diagrams together"

**Why encode them:** They apply across multiple future sessions and prevent repeated mistakes.

## Solution Quality: Think Like Mario

Proposed fixes must follow first-principles system design. No quick patches that create technical debt.

**Before proposing a fix, evaluate:**
1. **Root cause vs. symptom**: Fix the underlying issue, not just the visible problem
2. **Data flow vs. flags**: Fix data pipelines rather than adding special cases or validation steps
3. **Registry vs. hardcoding**: Use configurable rules instead of hardcoded exceptions
4. **Sustainability**: Ensure the fix works across different scenarios and state changes

**Avoid these anti-patterns:**
- Adding special cases → find the general rule being violated
- Downstream fixes → address issues at their source
- Hardcoded exceptions → make them configurable rules

**Example:** Don't add category back in build-dashboard.py if merge-tier2.py drops it. Fix merge-tier2.py to preserve the field.

## Auto-Suggest Convention

After completing any multi-step workflow, the agent should check:
1. Were there more than 2 corrections from the user?
2. Was any artifact regenerated 3+ times?
3. Were steps improvised that aren't in the skill?

If yes to any: suggest `/retrospective` before moving on.

This is NOT automatic - just a suggestion. The user decides whether to run it.

## Auto-trigger via SessionEnd Hook

`retrospective` is invoked by `session-close` as step 1, and is typically run at end of session. You can configure it to auto-prompt via a `SessionEnd` hook. Add to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionEnd": [{
      "hooks": [{ "type": "command", "command": "echo 'Session ended — run /retrospective or /session-close'" }]
    }]
  }
}
```

**Note:** If you use `session-close`, configure only that as the `SessionEnd` hook — it already invokes `/retrospective` as its first step. Configuring both creates duplication.
