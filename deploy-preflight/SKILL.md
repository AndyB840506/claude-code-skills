---
name: deploy-preflight
description: >
  Deployment preflight agent. Runs before any deploy to GitHub, DigitalOcean, or Vercel.
  Validates env var IDs, checks port conflicts, scans for BOM/JSON errors, verifies SSL/auth,
  and emits only PowerShell-5.1-safe fix commands. Outputs a pass/fail checklist and
  auto-fixes everything fixable before proceeding.
  Triggers: deploy preflight, preflight check, pre-deploy, antes de deployar, verificar deploy,
  validar deploy, chequeo pre-deploy, pre-despliegue, verificar antes de publicar,
  check before deploy, validate deployment, deploy check, deployment validation,
  /deploy-preflight, preflight deploy, deploy readiness check.
---

# Deploy Preflight

Run this before any deploy to GitHub, DigitalOcean, or Vercel. Catches the entire class of
env-var typos, BOM corruption, JSON parse failures, port conflicts, and auth gaps that cause
failed deploys and 45-minute debugging sessions.

## Two-part setup (required for auto-blocking)

This skill works in two parts:

1. **The skill** (`/deploy-preflight`) — runs the 6-check preflight and writes a flag file on success.
2. **The gate hook** (`deploy-preflight-gate.ps1`) — a PreToolUse hook that automatically blocks
   `vercel`, `git push`, and `doctl` deploy commands until the flag file exists and is <60 min old.

**The skill alone does NOT auto-block deploys.** Without the hook configured in `~/.claude/settings.json`,
deploy commands will run unguarded. Both parts must be present.

- Flag file: `C:\Users\andre\.claude\.preflight-passed` (valid 60 min after passing run)
- Gate script: `C:\Users\andre\.claude\deploy-preflight-gate.ps1`
- Hook config: `C:\Users\andre\.claude\settings.json` → `hooks.PreToolUse` → matcher `Bash`

On activation, greet the user and confirm the target:

> Running deploy preflight. Which target?
> 1. GitHub (push / PR)
> 2. DigitalOcean App Platform
> 3. Vercel
> 4. All three
>
> Reply with the number or name.

---

## Step 1 — Collect env var names and values

**Rule: never read .env files directly. Ask the user to paste values.**

Ask:

> Paste each env var you plan to set — name and value on the same line, one per line.
> Copy values directly from their source (browser URL bar, service dashboard) — do not retype.
>
> Example:
> ```
> GOOGLE_SHEET_ID  1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
> DO_APP_ID        abc123def456
> VERCEL_PROJECT   my-project-name
> ```
>
> If there are no env vars, type "none".

Once pasted, echo each name+value back for confirmation:

> Confirming values — verify each one against your source:
>
> GOOGLE_SHEET_ID → `1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms`
> DO_APP_ID       → `abc123def456`
>
> Any corrections? (Reply "ok" to continue.)

**Do not proceed to checks until the user confirms.**

---

## Step 2 — Run all preflight checks

Run all checks in this order. Track each result as PASS, FAIL (auto-fixable), or FAIL (manual).

---

### CHECK 1 — Env var ID format validation

For each env var value provided, apply these heuristics to flag likely typos:

**Google IDs (Sheet, Drive, Doc, Form):**
- Google Sheet/Doc IDs: 44 alphanumeric chars (letters, digits, hyphens, underscores). Flag if outside 40–50 chars or contains spaces.
- Google Drive folder IDs: same 33–44 char pattern.
- Google Form IDs: typically 44 chars.
- Flag if the value looks like a URL fragment (contains `/`, `#`, or `?`) — user probably copied the full URL instead of just the ID segment.

**DigitalOcean IDs:**
- App IDs: UUID format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`. Flag if not UUID-shaped.
- Database cluster IDs: same UUID format.
- Droplet IDs: numeric only (8–12 digits). Flag if non-numeric.

**Vercel:**
- Project names: lowercase, hyphens allowed, no spaces. Flag if contains uppercase or spaces.
- Team IDs: `team_` prefix followed by alphanumeric. Flag if missing prefix.

**API Keys (generic):**
- Flag if value is shorter than 16 chars (likely truncated).
- Flag if value contains obvious placeholder text: `your_`, `INSERT`, `xxx`, `test`, `example`.
- Flag if value ends with `...` (truncated copy).

**Port values:**
- Must be a number between 1024–65535. Flag if outside range or non-numeric.

Output for this check:

```
CHECK 1 — Env var format validation
  GOOGLE_SHEET_ID  → PASS  (44 chars, valid pattern)
  DO_APP_ID        → FAIL  (not UUID format — paste from DO dashboard URL)
  PORT             → PASS  (3000)
```

---

### CHECK 2 — Port conflict detection

**Only runs if the project uses a PORT env var or if a port is mentioned in config files.**

Detect platform:

```powershell
# Run this to check what's using the target port
netstat -ano | findstr ":3000"
```

If the port is in use, suggest the next available port from this list:
- 3000 → 3001 → 3002 → 8080 → 8081 → 8888

Emit the PS 5.1-safe fix:

```powershell
# In your .env or config, change:
PORT=3001
```

If no port conflict: `CHECK 2 — Port conflicts → PASS (port 3000 is free)`

---

### CHECK 3 — BOM scan

Scan all JSON and env files in the project for UTF-8 BOM (byte order mark `0xEF 0xBB 0xBF`).
BOM causes JSON parse errors and corrupts API responses.

**Detection command (PS 5.1-safe):**

```powershell
Get-ChildItem -Recurse -Include *.json,*.env,.env* | ForEach-Object {
    $bytes = [System.IO.File]::ReadAllBytes($_.FullName)
    if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        Write-Output ("BOM found: " + $_.FullName)
    }
}
```

**Auto-fix command (PS 5.1-safe, UTF-8 without BOM):**

```powershell
Get-ChildItem -Recurse -Include *.json,*.env,.env* | ForEach-Object {
    $bytes = [System.IO.File]::ReadAllBytes($_.FullName)
    if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        $stripped = $bytes[3..($bytes.Length - 1)]
        [System.IO.File]::WriteAllBytes($_.FullName, $stripped)
        Write-Output ("Fixed BOM: " + $_.FullName)
    }
}
```

Execute the detection command. If BOM files are found, apply the fix automatically and report:

```
CHECK 3 — BOM scan
  .env            → FIXED (BOM stripped automatically)
  config.json     → PASS  (no BOM)
```

---

### CHECK 4 — JSON parse validation

Parse every `.json` file in the project. Flag files that fail to parse.

**Detection command (PS 5.1-safe):**

```powershell
Get-ChildItem -Recurse -Filter *.json | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    try {
        $null = ConvertFrom-Json $content -ErrorAction Stop
        Write-Output ("PASS: " + $_.FullName)
    } catch {
        Write-Output ("FAIL: " + $_.FullName + " -- " + $_.Exception.Message)
    }
}
```

For any FAIL:
1. Read the file and identify the parse error location (line number from the exception message).
2. Check for: trailing commas, unquoted keys, single quotes instead of double, truncated content, HTML injection (look for `<!DOCTYPE` or `<html`).
3. If the error is trailing commas or misquoted keys: auto-fix and report.
4. If the error is HTML injection: this means a PHP or API endpoint returned an error page. Flag as MANUAL — the server-side issue must be fixed first.

```
CHECK 4 — JSON parse validation
  package.json        → PASS
  .claude/settings.json → FAIL (trailing comma on line 14) → FIXED automatically
  config/api.json     → FAIL (HTML content on line 1) → MANUAL (server returning error page)
```

---

### CHECK 5 — SSL / Auth prerequisites

Run auth checks for each selected target.

**GitHub:**

```powershell
gh auth status
```

PASS if output contains `Logged in to github.com`. FAIL if not — output fix:

```powershell
gh auth login
```

**DigitalOcean:**

```powershell
doctl auth list
```

PASS if at least one context is listed and marked `(current)`. FAIL if command not found:

```
doctl not installed or not authenticated.
Fix: download from https://docs.digitalocean.com/reference/doctl/how-to/install/
Then: doctl auth init
```

If doctl is installed but no current context:

```powershell
doctl auth switch --context [context-name]
```

**Vercel:**

```powershell
vercel whoami
```

PASS if returns a username. FAIL if `Error: Not authenticated`:

```powershell
vercel login
```

```
CHECK 5 — Auth / SSL
  GitHub      → PASS (logged in as AndyB840506)
  DigitalOcean → PASS (context: default)
  Vercel      → FAIL (not authenticated) → run: vercel login
```

---

### CHECK 6 — Windows shell safety (emitted commands only)

Before emitting any fix command in Steps 1–5, verify it is PS 5.1-safe:

**Rules for emitted commands:**
- No backtick-quoted strings (`` ` `` used as escape inside quotes)
- No Unicode characters in variable names, string literals, or comments
- No inline ternary: no `$x ? $a : $b` pattern
- No `&&` or `||` pipeline chaining — use `; if ($?) { }` instead
- No `xcopy` — use `Copy-Item`
- No `pwsh` — use `powershell.exe`
- No `2>/dev/null` — use `2>$null`
- `Set-Content` with `-Encoding UTF8` writes UTF-8 WITH BOM — use `[System.IO.File]::WriteAllText` with `[System.Text.UTF8Encoding]::new($false)` instead

If you catch yourself about to emit a non-compliant command: rewrite it before outputting.

This check has no output unless a command was rewritten — then note it:

```
CHECK 6 — Shell safety
  2 commands rewritten to PS 5.1-safe syntax
```

---

## Step 3 — Final checklist output

After all checks, output the full preflight report:

```
====================================
  DEPLOY PREFLIGHT — [TARGET]
  [date]
====================================

  CHECK 1  Env var format    [PASS|FAIL|FIXED]
  CHECK 2  Port conflicts    [PASS|FAIL|FIXED]
  CHECK 3  BOM scan          [PASS|FAIL|FIXED]
  CHECK 4  JSON validity     [PASS|FAIL|FIXED]
  CHECK 5  Auth / SSL        [PASS|FAIL|FIXED]
  CHECK 6  Shell safety      [PASS|N/A]

  Auto-fixed: [N]  Manual required: [N]
====================================
```

If any check is FAIL (manual):

> These items require manual action before deploying:
>
> 1. [Specific item] — [What to do]
>
> Re-run /deploy-preflight after fixing.

If all checks are PASS or FIXED:

Write the preflight flag so the gate hook allows deploys for the next 60 minutes:

```powershell
[System.IO.File]::WriteAllText("C:\Users\andre\.claude\.preflight-passed", (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), [System.Text.UTF8Encoding]::new($false))
```

Then confirm:

> Preflight passed. Deploy desbloqueado por 60 minutos.
> Puedes correr tu comando de deploy ahora.

---

## Rules

- Never read `.env` files or display secret values. Only ask the user to paste, echo back for confirmation, and validate format.
- If the user says "skip [check N]", skip that check and continue.
- All emitted commands must be tested mentally for PS 5.1 parse errors before output.
- If a fix command would overwrite data (beyond BOM removal), ask for confirmation first.
- Re-run all checks after applying fixes — confirm the fix actually resolved the issue before marking FIXED.
