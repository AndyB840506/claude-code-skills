# 13 Principles of Great Skills

What makes a skill truly good:

## 1. Never Invent Data

If your skill needs user information, ask. Never make it up.

**Bad:** Generate proposal with fake client name  
**Good:** Ask "What's the client name?"

## 2. Real Data First, Questions Second

If you can fetch data automatically, do it first. Only ask what you can't find.

**Bad:** Ask for everything  
**Good:** Read existing data, ask what's missing

## 3. Auto-Install Dependencies

If you need tools, install them automatically.

Message: "Setting up tools (30 seconds first time)"

## 4. Creative Freedom in Design

If generating HTML/dashboards, don't mandate rigid CSS. Describe the desired result, let Claude design.

Result: More beautiful and unique.

## 5. Adapt to Context

If your skill works for multiple types (e.g., proposals for different industries), adapt your questions.

## 6. Conversational Flow

Should feel like natural conversation, not a form.

**Bad:**
```
1. Client name
2. Services
3. Hours
[long form]
```

**Good:** Natural questions grouped in blocks

## 7. Friendly Fallbacks

If something fails (install, scraping), don't block. Offer alternatives and continue.

## 8. Welcome Message

If the skill goes in a kit, include a welcome message that triggers on any user input.

## 9. No Suggested Pricing

Don't include "as a service" or price suggestions in output.

## 10. Clear Result

At the end, show what was generated, what data was used, what's missing.

Example:
```
✓ Proposal generated: proposal-acme-2026-05-14.html
✓ Data used: name, services, hours
⚠️ Missing: itemized budget (add manually)
Want to adjust anything?
```

## 11. Fixed Models, Configurable API Key

Projects using AI should NOT expose model choice to end users. Always use the best model (Sonnet for chat, Opus for reports).

Only configurable: the API key.

## 12. Progressive Conversational Tone

If creating a conversational agent, start warm and empathetic. Only become more direct if you detect patterns that warrant it (evasive responses, inconsistencies).

## 13. Human Names for Agents

If creating a conversational agent, give it a human name (rotated per session). Humanizes interaction.

Example: "I'm Maria" vs "I'm your assistant" → the second is cold.

## 15. Prompt Caching for All API Bots

Any project that builds a chatbot or API-calling bot using Anthropic must include prompt caching on the system prompt.

**Node.js (Anthropic SDK):**
```js
system: [{ type: 'text', text: SYSTEM_PROMPT, cache_control: { type: 'ephemeral' } }]
```

**PHP (raw cURL):**
```php
// Add header:
'anthropic-beta: prompt-caching-2024-07-31'
// Change system from string to array:
$payload['system'] = [['type' => 'text', 'text' => $system, 'cache_control' => ['type' => 'ephemeral']]];
```

Caching activates when the system prompt exceeds ~4,096 tokens (Sonnet) or ~2,048 tokens (Haiku). Below threshold the header is harmless — add it regardless so the code is future-proof.

## 14. Geographic Validation for Location-Specific Documents

Before drafting any document that depends on a specific province/state/country (government forms, grant applications, legal registrations, compliance documents):

1. Extract location signals from ALL available data: phone area code (+1 587 = Alberta, +1 416 = Ontario, etc.), postal code, explicitly stated city/province/country
2. Confirm with the user: "Confirming you operate in [inferred province]?" before starting
3. Only then begin drafting

**Anti-pattern:** Generate the document and then correct the province — requires a full rewrite of statistics, cities, laws, registration costs, and government references.  
**Better:** Validate first, generate correctly once.
