---
name: verify
description: Evidence-gathering pass before declaring any task complete
---

Before reporting completion, produce a table with one row per claim:

| Claim | Evidence command run | Actual output | Pass/Fail |

Rules:
1. Run `Get-Date` and state today's real date. Never infer it.
2. `git log --oneline -5` and `git status` for each touched repo.
3. For every generated image, Read the file directly and describe ONLY what you literally observe — subjects, their spatial relationships, geometry, aspect ratio, dominant colors. Do NOT reference the prompt you used. Then check that description against the artwork checklist line by line and list every violation. If there are zero violations, say so explicitly. If there are any, regenerate — **at most twice**; if violations survive the second retry, show the image plus the outstanding violations instead of regenerating again.
   - Artwork checklist = `docs/estandar-de-entregables.md` § 4 (brand colors, text-state) **and** the `## Artwork` section of `CLAUDE.md` (banned motifs, aspect ratio, all variants). Item 4 of § 4 grades the prompt, not the render — skip it here.
4. For every deploy, curl the live URL and quote the response.
5. For every length-limited string, print `.Length`.
6. If ANY row is Fail or 'not checked', report the task as INCOMPLETE.
7. **Close with two explicit sections** (non-trivial tasks only — a task that produced an artifact, touched a repo, deployed, or generated an asset; per `~/.claude/CLAUDE.md` the ceremony is skipped on trivial ones):
   - **Verified done** — each claim with the evidence command and its actual output.
   - **Known open issues / anything I did not check** — if empty, state 'nothing unverified' and justify why nothing remains.
8. **Banned words** while section 2 is non-empty: 'final', 'complete', 'production-ready', and 'verified' as a standalone claim about the task. The **'Verified done'** section header is exempt — it labels evidence, it does not assert completion.

