---
name: heartbeat
description: Check this Agentic OS workspace for missing files, stale context, unfinished handoffs, and unresolved errors.
disable-model-invocation: true
---

# Heartbeat

Read `agentic-os/system/operating-rules.md` and follow its shared run protocol
using `agentic-os/state/skills/heartbeat/`. Scope or extra context: $ARGUMENTS

1. Inspect required paths using `agentic-os/system/file-map.md`. In this
   distribution, `python scripts/validate.py` provides an optional offline
   check; in installed workspaces use the source clone's validator with
   `--root <workspace>`. Do not install dependencies just for this check.
2. Read memory, the run/error logs, and skill handoffs. Distinguish never-run
   templates from failures. Flag stale dated entries (default: 30 days for
   handoffs, 90 days for decisions); ask whether they still apply rather
   than assuming old facts are false. Undated facts have unknown freshness.
3. Report Healthy, Warning, or Critical with evidence, missing paths,
   unresolved error references, stale items, and one next action. Healthy
   means the inspected workflow files are usable, not that an app is secure
   or deployed. Do not repair files, run app builds, or register schedules
   unless the user included that work in the request.
4. Save the report, handoff, evaluation and run entry per the shared protocol.

This is an on-demand check. A launch script calling this skill is still a
single session. It does not create background monitoring.
