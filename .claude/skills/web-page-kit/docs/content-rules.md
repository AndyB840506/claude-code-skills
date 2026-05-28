# Content Rules — No Fabrication, Graceful Degradation & Data Sourcing

These rules apply to every workflow in web-page-kit. They exist to protect the user from publishing false information and to ensure every generated site is based on real data.

---

## Rule 1: No Fabrication

**Never invent content that should come from the user.**

This means:

| Content Type | Rule |
|---|---|
| Services | Only list services the user explicitly describes |
| Prices | Only show prices the user provides. No guessing or "typical price" |
| Testimonials | Only use testimonials the user provides. Never write fake ones |
| Stats & metrics | Only show real numbers the user confirms |
| Features / Benefits | Only list what the user tells you |
| Certifications / Awards | Only if user provides them |
| Client names / logos | Only if user provides them |
| Years in business | Only if user tells you |

**If data is missing:** Use a clearly marked `[PLACEHOLDER]` — never fill it with invented content.

Example:
```html
<!-- Correct -->
<p class="stat">[PLACEHOLDER: Add your real client count here]</p>

<!-- Wrong — never do this -->
<p class="stat">500+ happy clients</p>  ← invented
```

---

## Rule 2: Graceful Degradation

**When information is missing, the page still works — it just uses a fallback.**

| Missing Data | Fallback |
|---|---|
| Profile/logo image | CSS avatar using initials + brand color |
| Hero image | Gradient background using brand colors |
| Testimonials | Omit the section entirely (don't show empty cards) |
| Social links | Omit the icon (don't show broken links) |
| Price | "Contact for pricing" button |
| Stats section | Skip it until user provides real numbers |
| Team photos | CSS placeholder with initials |
| Site URL | Use `example.com` as placeholder, note to update |

**Tell the user** what's missing at the end of each generation. Don't silently use fallbacks without noting them.

---

## Rule 3: Data Sourcing Transparency

**Always show the user where each piece of content came from.**

After generating any page, include a source summary:

```
✅ Page: homepage.html

Content sources:
✅ Site name: from config
✅ Tagline: user-provided
✅ Description: user-provided
✅ Service 1: user-provided
✅ Service 2: user-provided
⚠️ Testimonials: [PLACEHOLDER] — no testimonials were provided
⚠️ Profile photo: CSS placeholder — no image path was provided
⚠️ Stats section: skipped — no real metrics were provided

To complete: Add real testimonials, profile photo, and metrics when available.
```

This prevents the user from accidentally publishing placeholder content.

---

## Rule 4: Social Proof Validation

**Testimonials and reviews must be real and sourced.**

Acceptable testimonial sources:
- User pastes the testimonial directly
- User provides a link to a review (Google, Yelp, LinkedIn, etc.)
- User provides a screenshot of a real message/review

NOT acceptable:
- Writing a testimonial in Claude's voice
- Paraphrasing to "improve" a testimonial without user approval
- Generic testimonials like "Great service!" with made-up names

If the user has no testimonials yet:
```
You don't have testimonials yet — I'll skip that section for now.
When you get real feedback from clients, add it back with workflow 02.
```

---

## Rule 5: Ask, Don't Assume

**If something is unclear or missing, ask the user — don't fill in the gaps.**

Examples:
- Don't assume the business location — ask
- Don't assume service pricing — ask or use "Contact for pricing"
- Don't assume the owner's gender or pronouns — use their name directly
- Don't assume services offered — ask if unsure
- Don't assume audience demographics — ask

**One clarifying question is always better than one invented detail.**

---

## Rule 6: Placeholder Format

All placeholders must be visually distinct and easy to find:

```html
<!-- Text placeholder -->
<p>[PLACEHOLDER: Describe your main service here — 2 sentences]</p>

<!-- Image placeholder -->
<div class="img-placeholder" style="background: [primary-color]; ...">
  <span>[YOUR LOGO]</span>
</div>

<!-- Stats placeholder -->
<div class="stat">[PLACEHOLDER: Add real client count]</div>
```

Search for `[PLACEHOLDER` before publishing — every instance needs real content.

---

## Rule 7: Real Data Improves Results

**The more real information the user provides, the better the output.**

Encourage users to share:
- Real bio written in their own words (not "describe yourself" — ask for what they wrote)
- Actual services they offer (with how it works, not just the name)
- Real testimonials, even short ones ("great work!" from a real client beats a fake paragraph)
- Actual photos (even low-resolution images are better than placeholders)
- Real keywords they know customers use to find them

The goal is a website that truly represents the person or business — not a generic template with made-up details.

---

## Rule 8: Region Expansion Audit

When changing a site's target region (e.g., "US and Canada" → "Americas"), check ALL 8 touchpoints — missing even one creates inconsistent signals to search engines and users:

| # | Location | What to update |
|---|----------|----------------|
| 1 | `<meta name="description">` | Remove old region, add new |
| 2 | `<meta property="og:description">` | Same as above |
| 3 | `<meta property="og:title">` | If region is mentioned |
| 4 | JSON-LD `description` | Match meta description |
| 5 | JSON-LD `areaServed` | Replace with target country list |
| 6 | JSON-LD `availableLanguage` | Add new language if applicable |
| 7 | Hero section subtitle | Where brand pitch references region |
| 8 | FAQ geographic question + answer | Usually "Do you work with X?" |

Run a grep for the old region name (e.g., "United States", "US and Canada", "EE.UU.") before closing — easy to miss Spanish and structured-data copies.
