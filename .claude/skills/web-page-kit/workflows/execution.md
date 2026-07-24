# Execution

When `/web-page-kit` is invoked:

1. **Check for `website-config.json`**
   - NOT found → run `workflows/00-welcome.md` (guided wizard)
   - Found → greet returning user, show where they left off, ask where to continue

2. **Detect language from config** → respond in EN or ES throughout

3. **Detect intent** → route to matching workflow (routing table in SKILL.md)

4. **Before generating any HTML** → verify real data exists. If missing, ask — never invent. Then apply the Rule 8 design principles (`docs/design-guide.md`): commit to a specific aesthetic direction (tone, typography, composition) before writing a single line of CSS. Never fall back to generic fonts or predictable layouts — every page must have a deliberate, context-specific design identity. If integration with an external tool is proposed (e.g. a search CLI, API, or library), verify the tool is installed first (glob for key files, check PATH) before designing any workflow around it — do not assume availability.

   **Redesign rule:** A redesign means structural/layout changes — different hero structure, different section order, different content patterns (e.g. cards → numbered list, centered → split). Changing only CSS variables or font families is NOT a redesign and will look identical to the user. If the user says "it looks the same": read both files, compare layout structure (hero type, grid columns, section count, content components), then ask the user which specific sections or patterns they want changed before generating anything.

5. **After each step** → show updated progress map (which steps are ✅ done, which are ⬜ next)

6. **End goal** → every session path leads to `workflows/05-deployment.md` (publish)
