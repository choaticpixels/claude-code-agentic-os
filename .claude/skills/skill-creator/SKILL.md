---
name: skill-creator
description: Turn a recurring workspace procedure into a concise Claude Code project skill with examples and validation criteria.
argument-hint: "[workflow to turn into a skill]"
disable-model-invocation: true
---

# Skill creator

Read `agentic-os/system/operating-rules.md` and follow its shared run protocol
using `agentic-os/state/skills/skill-creator/`. Requested workflow: $ARGUMENTS

1. Resolve request from arguments or `input.md`; ask if absent. Inspect existing
   project, personal and plugin command names when available to avoid collision.
   Edit an existing skill when that better matches the request.
2. Define trigger, inputs, required context, scope, result, success criteria,
   and known failure modes. Verify frontmatter against current official Claude
   Code skills documentation. Use lowercase hyphenated names under 64 chars.
3. Write `.claude/skills/<name>/SKILL.md` with name, description, and a short
   procedure. For this kit's task workflows keep `disable-model-invocation: true`.
   Use argument-hint and $ARGUMENTS if needed. No inline shell interpolation,
   broad allowed-tools, permission bypass, credential values or hidden hooks.
4. Add supporting scripts only if they materially improve reliability; run
   meaningful checks for them. Add per-skill state following the existing
   input/output/handoff/learnings/eval convention. Start eval at not_run.
5. Try a realistic authorized example in a disposable target if practical.
   Otherwise document the example as unexecuted. Metadata checks do not prove
   Claude followed a skill successfully. Preserve that distinction in eval.
6. Update workflow/file maps as relevant. The distribution validator is scoped
   to the six shipped skills; extend it and the manifest only when contributing
   a new packaged skill. Save report, evaluation and handoff.

Do not create an unrelated agent, daemon, scheduler or external integration
merely because the workflow might eventually benefit from one.
