# On-Call Handoff Automation

Automate shift start/end handoff document generation and archival.

## Setup: Shift Schedule Triggers

Configure Claude Code to automatically generate handoff templates at shift boundaries.

### Step 1: Add Hooks to settings.json

```json
{
  "hooks": {
    "SessionEnd": [{
      "hooks": [{
        "type": "command",
        "command": "echo 'Shift ending — run /on-call-handoff-patterns to generate handoff doc'"
      }]
    }]
  }
}
```

> **Note:** Claude Code does not support `event:shift-start` / `event:shift-end` hook types.
> Use `SessionEnd` as the closest equivalent. For scheduled shift triggers (e.g. 08:00 UTC daily),
> use `/schedule` to create a cron agent instead.

### Step 2: Configure Shift Times

Add your team's on-call schedule:

```json
{
  "oncall": {
    "schedules": [
      {
        "team": "platform",
        "timezone": "UTC",
        "shifts": [
          { "start": "08:00", "end": "17:00", "primary": "alice" },
          { "start": "17:00", "end": "08:00", "primary": "bob" }
        ]
      }
    ],
    "handoff_folder": "Notes/OnCall/Handoffs/",
    "template_folder": "Notes/OnCall/Templates/"
  }
}
```

### Step 3: Create Initial Templates

In `.claude/skills/on-call-handoff-patterns/templates/`:

**shift-start.md**
```markdown
# On-Call Handoff: {{ team }} Team

**Outgoing**: @{{ outgoing_engineer }} ({{ shift_start }} to {{ shift_end }})
**Incoming**: @{{ incoming_engineer }} ({{ next_shift_start }} to {{ next_shift_end }})
**Handoff Time**: {{ handoff_time }} {{ timezone }}

---

## 🔴 Active Incidents

### None currently active

---

## 🟡 Ongoing Investigations

### None currently active

---

## 🟢 Resolved This Shift

### None

---

## 📋 Recent Changes

### Deployments

| Service | Version | Time | Notes |
|---------|---------|------|-------|
| (none) | - | - | - |

---

## ⚠️ Known Issues & Workarounds

### None currently

---

## 📅 Upcoming Events

| Date | Event | Impact | Contact |
|------|-------|--------|---------|
| (none) | - | - | - |

---

## 🔧 Quick Reference

### Important Links

- [Runbooks](https://wiki/runbooks)
- [Service Catalog](https://wiki/services)
- [Incident Slack](#)
- [PagerDuty](#)
```

---

## Automation Workflow

### Shift Start (Every Day at 08:00 UTC)

1. **Read previous shift's handoff** → `.notes/OnCall/Handoffs/YYYY-MM-DD-prev.md`
2. **Extract ongoing items** → "Ongoing Investigations" and "Upcoming Events"
3. **Generate new handoff** → Fill template with:
   - Outgoing engineer name (from schedule)
   - Incoming engineer name (from schedule)
   - Carry-forward ongoing investigations
   - Carry-forward upcoming events
4. **Create draft** → `.notes/OnCall/Handoffs/YYYY-MM-DD-current.md`
5. **Notify outgoing engineer** → Slack: "Your shift handoff is ready for review"

### Shift End (Every Day at 17:00 UTC)

1. **Read current handoff** → `.notes/OnCall/Handoffs/YYYY-MM-DD-current.md`
2. **Archive** → Copy to `.notes/OnCall/Archive/YYYY-MM/DD-HHMM.md`
3. **Validate completeness** → Check all sections have content
4. **Notify incoming engineer** → Slack: "Read today's handoff: [link]"

---

## For Your Team

**Add to PagerDuty schedule or Google Calendar:**

```
Event: On-Call Shift Start
Time: 08:00 UTC daily
Description: Handoff document auto-generated
Attendees: Current + Incoming on-call engineer

Event: On-Call Shift End
Time: 17:00 UTC daily
Description: Archive previous shift handoff
Attendees: Outgoing on-call engineer
```

---

## Testing Automation

Before deploying to production:

```bash
# Dry run: generate template for test date
claude-code run-skill on-call-handoff-patterns generate-shift-template \
  --team platform \
  --date 2026-05-15 \
  --dry-run

# Review generated file
cat Notes/OnCall/Handoffs/2026-05-15-test.md
```

---

## Fallback (Manual)

If automation fails:
1. Copy `Templates/shift-start.md` manually
2. Fill in engineer names and current incidents
3. Send to incoming engineer before shift starts
4. Archive when shift ends

The skill works without automation; scheduling just prevents manual steps.
