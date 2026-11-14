---
name: wrap-up
description: Close a work session with an evidence-based summary, current handoff, concise memory updates, and next actions.
disable-model-invocation: true
---

# Wrap-up

Read `agentic-os/system/operating-rules.md` and follow its shared run protocol
using `agentic-os/state/skills/wrap-up/`. Session scope: $ARGUMENTS

1. Review the current conversation, changed files, most recent skill outputs,
   validation evidence, unresolved errors and existing notes. Do not infer
   that every changed file belongs to this session.
2. Separate completed work, checks actually run and their results, remaining
   work, blockers, and the next exact action. Distinguish local verification
   from publication or production verification. Cite paths or redacted logs.
3. Update `agentic-os/memory/notes-from-last-run.md`. Update active projects
   and recent decisions when supported. Add to MEMORY.md only stable,
   reusable facts; date them and preserve any superseded decision history.
4. Add a skill learning only if it changes a future decision. Avoid repeating
   generic advice or copying raw chat. Record the previous skill's unresolved
   work in its handoff without claiming the work is finished.
5. Save the wrap-up report, evaluation, handoff and run entry. Do not run
   new builds, commit, publish, or schedule anything just to close a session.

Output: completed changes; evidence; limits; memory changes actually made;
unresolved issues; next action. If evidence is missing, say so.
