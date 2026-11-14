---
name: system-review
description: Review Agentic OS instructions, memory freshness, evaluations, and workflow continuity for maintenance.
disable-model-invocation: true
---

# System review

Read `agentic-os/system/operating-rules.md` and follow its shared run protocol
using `agentic-os/state/skills/system-review/`. Review scope: $ARGUMENTS

1. Read the six skills, shared rules, workflow maps, business context, memory,
   handoffs, learnings, evaluation files, and bounded recent log entries.
2. Identify contradictions, missing references, duplicated rules, excessive
   context, stale facts, unsupported configuration, or workflow gaps. Trace
   each finding to a path and concrete impact. Separate not_run evaluations
   from failed runs; check any pass result has actual evidence.
3. If checking compatibility, consult current official Claude Code docs.
   If unavailable, label compatibility unverified. Do not invent settings.
4. Produce prioritized findings and small proposed edits. Implement only
   changes within the requested maintenance scope; preserve user preferences,
   durable history, and unrelated work. Do not delete old logs wholesale or
   broaden permissions to make a workflow pass.
5. Verify any changed references/JSON, then save report, evaluation and handoff.

Suggested cadence: every 4–6 weeks or after a workflow change. This is a human
recommendation; no recurring task is registered by this skill.
