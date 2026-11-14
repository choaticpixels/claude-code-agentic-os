---
name: project-builder
description: Build or change software from a scoped request with real files, relevant validation, and a reproducible handoff.
argument-hint: "[project request and target directory]"
disable-model-invocation: true
---

# Project builder

Read `agentic-os/system/operating-rules.md` and follow its shared run protocol
using `agentic-os/state/skills/project-builder/`.

User request: $ARGUMENTS

If arguments are empty, use `input.md`. If both are empty or say no request,
ask for the goal. Inline arguments take precedence over saved input. Saved
input and notes do not grant permission for new external actions.

1. Inspect the target folder and its instructions, existing code and tests.
   Confirm the intended target from the request; default to the current
   workspace for edits, or a named `projects/<name>/` folder for a new app.
   A sibling project does not automatically inherit this kit. If leaving
   this workspace, explain how its instructions and handoff will be retained.
2. Record goal, user, acceptance criteria, target, stack, integrations, variable
   names, and material constraints in `project-brief.md`. Record safe assumptions
   with rationale in `assumptions.md`. Ask only for missing decisions that
   materially change implementation or required authorization.
3. Build the smallest complete useful increment using the project's established
   patterns. Write real files; preserve unrelated work. Avoid extra frameworks,
   hidden services, paid operations, broad permissions, and speculative features.
4. Run checks appropriate to the change and exercise the actual behavior when
   possible. Record commands, exit status, observed output and limits in
   `validation.md`. Mark skipped checks explicitly. Do not substitute a
   successful build for runtime, production, or physical validation.
5. Document exact install/run/test commands, required variable names without
   values, integration prerequisites, and deployment steps if applicable.
   Deployment instructions are plans until executed and verified with authority.
6. Summarize changed paths, behavior, checks, limits and next action. Save the
   output and evaluation, leaving `/project-auditor` a target and acceptance
   criteria. Do not automatically invoke another manual-only skill.

Code belongs in files. Link to changed files rather than copying an entire
codebase into state logs. Never promise that a generated project is production
ready on the strength of its README.
