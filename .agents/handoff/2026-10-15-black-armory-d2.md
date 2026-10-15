# Handoff: Black Armory (Destiny 2 vault + meta build tool)
**Date:** 2026-10-15 (Thursday)
**Machine:** desktop (C:/E:)
**Status:** In progress — S0-S3 closed (v0.3.0); S4 (own armor optimizer) decided, not started
---
## What We Accomplished This Session
- New project **Black Armory**: `C:\Users\andre\repos\black-armory` (Next.js 16.4, TypeScript),
  PRIVATE GitHub repo https://github.com/AndyB840506/black-armory (branch `master`, HEAD `cb00f33`).
- Bungie app registered by Andres (client_id 55810, Confidential). Credentials in `.env.local`
  (gitignored, never committed: checked with a grep over the whole history).
- **S0 research:** Destiny 2 got its last content update on 2026-06-09 (9.7.0 Monument of
  Triumph, per help.bungie.net). Game online; API alive; manifest frozen.
- **S1 (v0.1.0):** OAuth login, encrypted session cookie, slim manifest cache, vault reader.
  Verified against DIM: vault 531 = 531, character power 490/360/10.
- **S2 (v0.2.0):** weapons graded against DIM's voltron wish list. **wishlist 148 = DIM's
  `is:wishlist` 148** (needed the definition-socket fallback). Crafted weapons -> "reshape",
  never dismantle (Andres's rule). Tabs + DIM-style board UI.
- **S3 (v0.3.0):** 9 curated meta builds (3/class, PvE) in `src/data/builds.json`, every name
  gated against the manifest (`scripts/check-builds.mts`), compared with the vault. Andres
  checked in DIM: matches. After close: Collections (component 800) + Bungie's official
  "Source:" text so missing items say where to get them; "pullable" = bits 1 and 64 clear.
- 33 tests, each new area mutation-checked. Gate/diagnostic scripts in `scripts/`.
- Installed `gh` 2.102 on the desktop (logged in as AndyB840506).

## Where We Paused
**Last action:** recorded the S4 decision in `.agents/build-state/sprints.md` (`cb00f33`).
**Next action:** S4 research (official manifest first: Armor 3.0 stat math, tiers, tuning mods,
masterwork, set bonuses, exotic constraints), then propose the S4 plan + Definition of Done
and WAIT for Andres's approval before coding.
**Blockers:** none.

## Files to Read First
- `C:\Users\andre\repos\black-armory\.agents\build-state\sprints.md` — sprint states, every DoD
  with its evidence, decisions. **This is the source of truth for the project.**
- memory `project_d2_build_tool.md` (+ `reference_bungie_api_gotchas.md`,
  `reference_nextjs16_cache_components.md`, `feedback_oracle_parity_bisect.md`).
- `black-armory/src/lib/{profile,wishlist,builds,manifest}.ts` — the core.

## Notes / Gotchas
- **Machine-bound:** `.env.local` (keys) and `.cache/` (manifest, wishlist, raw-profile
  snapshot) are only on THIS desktop. On the laptop: clone, `npm install`, recreate
  `.env.local` (Andres pastes the values from bungie.net/en/Application), first run rebuilds caches.
- Dev: `npm run dev` -> https://localhost:3002 (port 3000 belongs to andyfreelancer).
- **Bungie portal Redirect URL still says :3000** (never confirmed fixed). Workaround used all
  session: after the Bungie login, change 3000 -> 3002 in the URL bar. Ask Andres to fix + screenshot.
- Andres pasted the API key and client secret in chat: **regenerate the secret before going public.**
- Andres's goal: **better than DIM** — own optimizer; DIM is the comparison oracle in every DoD.
- Source rule: official (Bungie) first; Reddit/creators/media allowed, always tagged.
- Next 16 has `cacheComponents` on: read `node_modules/next/dist/docs` before writing code.

## Questions to Answer
- S4 scope: optimize toward a chosen build (exotic + set + stat priority)? Include pieces
  pullable from Collections? (ideas offered, not approved)
- Crafting (weapon patterns) — wanted? Separate system from Collections.
- Minor: on "⇩ pull it" the source text also lists the non-pullable versions (noise).
- `project_d2_build_tool.md` is 63 lines (cap ~60): trim at next memory audit.
