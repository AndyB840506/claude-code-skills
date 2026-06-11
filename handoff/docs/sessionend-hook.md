# Auto-trigger via SessionEnd Hook

`handoff` can be configured to remind you automatically when a session ends. Add to
`~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionEnd": [{
      "hooks": [{ "type": "command", "command": "echo 'Session ended — run /handoff to transfer context'" }]
    }]
  }
}
```

**Note:** If you also use `session-close`, configure only one as a `SessionEnd` hook —
`session-close` already invokes `handoff` as its step 4, so configuring both creates
duplication.
