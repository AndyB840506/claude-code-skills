# Handoff: Black Armory (D2), S4-S7 closed
**Date:** 2026-10-17 (Saturday)
**Machine:** desktop (C:\Users\andre\repos\black-armory; caches in the repo's `.cache\`, gitignored)
**Status:** Complete. S7 closed at v0.7.0 (`7627dd1`, pushed). S8 not planned yet.
---
## What We Accomplished This Session
- **S4 (v0.4.0):** a stat engine that matches the game on 136/136 pieces, and an armor optimizer that ties or beats DIM in 5 cases.
- **S5 (v0.5.0):** vendor armor (who sells it, where, cost), per-stat targets, and "what to farm" with the Ghost Armorer mod.
- **S6 (v0.6.0):** cleanup v2 (keeps power > 430, infusion pairs, armor cleanup) and the official effects of each stat.
- **S7 (v0.7.0): the app now MOVES items** through Bungie's TransferItem, using server actions. Real tests on Andres's account:
  - Scope test: Austringer moved to the vault.
  - Two infusion pairs sent to the Warlock: 4/4 and 2/2 transfers. Andres then infused one in game: "salio bien".
  - "Clean characters": 44/44 transfers in 16.8 s.
- Rules Andres corrected or added today. All are recorded in `sprints.md` S7 with his words.
  - Infusion fuel must be in the **same slot** as the target. This replaces S6's "any weapon".
  - **Locked** items are never a candidate, never fuel, and are never moved.
  - **Unrated** weapons and build weapons are never moved when cleaning.
  - The **Hunter is left alone** while he levels it (`LEVELING` in `src/lib/move-plans.ts`).
- Bug fixed: the armor dismantle list depended on item order. Ties in the optimizer and in "best exotic copy" now break deterministically. The bug came from S6.
- Memory updated: `project_d2_build_tool`, `reference_bungie_api_gotchas`, plus two new feedback memories (generalize/test the named case; order invariance with ties).

## Where We Paused
**Last action:** S7 closure commit plus the session close.
**Next action:** plan **S8** with Andres (plan + DoD before any code). His two requests:
1. Classify unrated weapons to spot god rolls. DIM's wish list does not cover them, so a source has to be researched first. NO VERIFIED SOURCE YET.
2. Send each build weapon to the character whose class build uses it.

**Blockers:** Andres said he will finish some of the game's stories first "para tener una base mejor". Ask whether he is ready before starting S8.

## Files to Read First
- `C:\Users\andre\repos\black-armory\.agents\build-state\sprints.md`: the source of truth. Read the S7 section and the "Open after S7" list.
- `src/lib/moves.ts`, `src/lib/move-plans.ts`, `src/app/actions.ts`: the move engine and the action.
- `src/lib/cleanup.ts`: every cleanup rule, each with Andres's quote.

## Notes / Gotchas
- **Bungie's profile lags after a move**, from ~0 to ~4 min, and so do DIM and the D2 app. The app records accepted moves in memory and shows them right away. That record is lost on a server restart or when the dev server reloads `moves.ts`.
- Each move action re-reads the whole profile, including vendors, so pages take 3.5-10 s.
- Dev server: https://localhost:3002, started detached and logging to `.cache\dev.log`. It may not be running next session.
- Before going public: regenerate the Bungie client secret (Andres pasted it in a chat), read the API terms, and change logout from GET.

## Questions to Answer
- Is the Bungie app's Redirect URL now :3002? It was never confirmed, although logins worked all session.
- When is the Hunter leveled? Then remove it from `LEVELING`.
- Does the game count vault items for drop power? NOT VERIFIED. It matters for the Hunter rule.
