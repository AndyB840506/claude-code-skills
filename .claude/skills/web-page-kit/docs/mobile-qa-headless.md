# Mobile QA with headless Edge on Windows (no devtools, no phone)

Recipe for verifying a page at real phone widths (375px) and hunting
overlap/overflow bugs, using only Edge headless + PowerShell/Bash.
Battle-tested 2026-07-07 (Kuma Talent landing: nav CTA overlapped the
wordmark on phones; found and verified fixed with this exact flow).

## The two Windows gotchas that break naive attempts

1. **You cannot get a 375px viewport from `--window-size` alone.** Edge
   clamps the window to a ~500px minimum AND Windows DPI scaling inflates
   the CSS viewport (`--window-size=375,...` yields `clientWidth` ≈ 492).
   `--force-device-scale-factor=1` is NOT honored in headless. A screenshot
   at that size silently shows a ~492px layout cropped to a 375px bitmap —
   it LOOKS like horizontal overflow that isn't real. Never diagnose from
   that artifact; measure `document.documentElement.clientWidth` first.
2. **PS 5.1 sometimes returns empty stdout from `msedge --dump-dom`.**
   Run it from Bash with `> out.html` redirection instead.

## Working pattern: iframe harness + injected probe

Media queries respond to the IFRAME's width, so wrap the page in a local
harness with `<iframe style="width:375px">` — that gives an exact-width
viewport regardless of window/DPI limits.

- **Overflow probe:** append a script to a local copy of the page that, on
  load, walks `body *`, collects elements whose `getBoundingClientRect()`
  exceeds `clientWidth`, and `parent.postMessage()`s the report; the harness
  writes it into a `<pre>`; read it via `--dump-dom`. `scrollW == vw` and an
  empty list = no overflow, at that exact width, proven.
- **Screenshots:** `transform: scale(1.4); transform-origin: top left` on the
  iframe renders a crisper bitmap; size the window to `width*scale`. Slice
  tall captures into ~1500px strips with System.Drawing before reading them
  (a 9000px screenshot downscales to unreadable otherwise).
- **Live sites that send `X-Frame-Options`:** the iframe will show a blocked
  page. Curl the HTML, rewrite relative asset URLs to absolute
  (`href="assets/` → `href="https://site/assets/`), save locally, iframe the
  local copy.
- **Canvas work on `file://` pages** (e.g. decoding a QR with jsQR):
  `getImageData` throws SecurityError (tainted canvas) unless you launch with
  `--allow-file-access-from-files`. Also vendor the JS lib locally — CDN
  scripts often don't load before `--dump-dom` fires.
- Give each run its own `--user-data-dir` under the scratchpad to avoid
  profile-lock flakiness; add `--virtual-time-budget=9000` so load handlers
  run before the dump.

## Reading the evidence

- Overlap ≠ overflow: a clean probe with a visual overlap usually means a
  flex item shrank below its content (e.g. a logo `<button>`) and its inline
  content slid under a later-painted sibling. Fix with `flex-shrink: 0`,
  `white-space: nowrap`, and compact mobile sizes — then re-run the probe AND
  re-screenshot to confirm.
