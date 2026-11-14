---
name: project-auditor
description: Review an implementation against its request and observable evidence, with prioritized findings and validation gaps.
argument-hint: "[target directory or change to audit]"
disable-model-invocation: true
---

# Project auditor

Read `agentic-os/system/operating-rules.md` and follow its shared run protocol
using `agentic-os/state/skills/project-auditor/`. Audit target: $ARGUMENTS

1. Resolve target from arguments, otherwise the builder brief and handoff. If
   ambiguous, ask. Read target instructions, acceptance criteria, changed files,
   dependency declarations, setup docs and existing validation evidence.
2. Check implementation against requested behavior: broken paths, incomplete
   setup, correctness, error handling, dependency assumptions, unsafe trust
   boundaries, and missing meaningful verification. Inspect variable names
   and access patterns without opening credential files or printing secrets.
3. Run safe, relevant checks when authorized and available. Review scripts
   before executing them. Record command, location, result, and coverage.
   Do not run deployment, migrations against live data, paid services, or
   destructive scenarios without scope covering them. Mark those unverified.
4. Report findings by severity with file/line references, concrete trigger,
   impact and suggested fix. Distinguish observed defects from hypotheses.
   If there are no findings, say what was checked and what remains unknown.
5. Write report, evaluation and handoff. Leave a repair plan; do not silently
   edit audited code unless repairs were also requested. State this is an
   agent review, not an independent professional security audit.

An overall pass requires acceptance evidence and no unresolved blocking
findings. Passing tests alone do not establish deployment or security readiness.
