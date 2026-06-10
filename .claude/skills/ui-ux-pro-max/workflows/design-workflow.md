# Design Workflow

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If not installed:

**macOS:** `brew install python3`
**Ubuntu/Debian:** `sudo apt update && sudo apt install python3`
**Windows:** `winget install Python.Python.3.12`

## Step 1: Analyze User Requirements

Extract from the user request:
- **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page, etc.
- **Style keywords**: minimal, playful, professional, elegant, dark mode, etc.
- **Industry**: healthcare, fintech, gaming, education, etc.
- **Stack**: React, Vue, Next.js, or default to `html-tailwind`

## Step 2: Generate Design System (REQUIRED)

Always start with `--design-system` for comprehensive recommendations with reasoning:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

This searches 5 domains in parallel (product, style, color, landing, typography), applies reasoning rules from `ui-reasoning.csv`, and returns a complete design system (pattern, style, colors, typography, effects) with anti-patterns to avoid.

**Example:**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

## Step 2b: Persist Design System (Master + Overrides Pattern)

Add `--persist` to save the design system for hierarchical retrieval across sessions:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name"
```

This creates `design-system/MASTER.md` (global source of truth) and a `design-system/pages/` folder.

With a page-specific override:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name" --page "dashboard"
```

This also creates `design-system/pages/dashboard.md` with page-specific deviations from Master.

**Hierarchical retrieval**: when building a specific page, check `design-system/pages/<page>.md` first; if it exists its rules override Master, otherwise use `design-system/MASTER.md`.

## Step 3: Supplement with Detailed Searches (as needed)

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

| Need | Domain | Example |
|------|--------|---------|
| More style options | `style` | `--domain style "glassmorphism dark"` |
| Chart recommendations | `chart` | `--domain chart "real-time dashboard"` |
| UX best practices | `ux` | `--domain ux "animation accessibility"` |
| Alternative fonts | `typography` | `--domain typography "elegant luxury"` |
| Landing structure | `landing` | `--domain landing "hero social-proof"` |

See [../docs/search-reference.md](../docs/search-reference.md) for the full domain and stack list.

## Step 4: Stack Guidelines (Default: html-tailwind)

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

If the user doesn't specify a stack, default to `html-tailwind`.

## Example Workflow

**User request:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

1. **Analyze**: Beauty/Spa service, elegant/professional/soft, Beauty/Wellness, html-tailwind (default)
2. **Generate design system**:
   ```bash
   python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
   ```
3. **Supplement**:
   ```bash
   python3 skills/ui-ux-pro-max/scripts/search.py "animation accessibility" --domain ux
   python3 skills/ui-ux-pro-max/scripts/search.py "elegant luxury serif" --domain typography
   ```
4. **Stack guidelines**:
   ```bash
   python3 skills/ui-ux-pro-max/scripts/search.py "layout responsive form" --stack html-tailwind
   ```
5. **Synthesize** the design system + detailed searches and implement.
