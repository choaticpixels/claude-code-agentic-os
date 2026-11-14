# File map

- CLAUDE.md: concise entrypoint and explicit context-read instructions.
- .claude/settings.json: documented settings and partial secret deny rules.
- .claude/skills/{heartbeat,wrap-up,system-review,project-builder,project-auditor,skill-creator}/SKILL.md: the six manually invoked workflows.
- agentic-os/business-brain/business-brain.md: shared supplied business facts.
- agentic-os/memory/{MEMORY,recent-decisions,active-projects,constraints,notes-from-last-run}.md: durable context and current continuity.
- agentic-os/state/skills/<name>/{input,last-output,handoff,learnings}.md and eval.json: per-skill context, results, next steps, lessons and evaluation.
- Builder state additionally includes project-brief.md, assumptions.md and validation.md.
- agentic-os/logs/{runs.md,errors.md,eval-history.jsonl}: append-only run evidence.
- agentic-os/workflows/: human-readable lifecycle and builder maps.
- agentic-os/scripts/: interactive launch helpers and opt-in scheduling examples.
- agentic-os/system/{operating-rules,file-map,verification}.md: shared protocol and verification boundaries.

The source repository also supplies scripts/install.py, scripts/validate.py,
manifest.json, tests/, docs/, assets/, and a manual GitHub Actions check.
Those distribution tools are not copied into target projects. The manifest
lists every workspace file copied by the installer.
