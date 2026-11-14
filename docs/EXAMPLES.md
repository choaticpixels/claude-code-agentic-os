# Example missions

These are prompts to run, not claims about completed sample projects. Type
them inside Claude Code, one at a time, and inspect the resulting evidence.

## Local health API

```text
/project-builder Build a dependency-free Node.js API in projects/health-api. GET /health returns 200 with JSON {"status":"ok"}; unknown routes return 404. Include node:test checks, exact run instructions, and keep it local.
```

Expected review targets: route behavior, valid JSON, clean shutdown, supported
Node version, reproducible commands and a validation record. Then run:

```text
/project-auditor projects/health-api against the builder's acceptance criteria
/wrap-up
```

## Fix an existing bug

```text
/project-builder In projects/my-app, fix the date filter so both selected endpoints are included. Inspect existing tests first. Preserve the current UI and document the timezone assumption. Do not deploy.
```

The builder should inspect the real app, use its established stack, implement
the behavior and test relevant boundaries. If the target does not exist, it
should report that rather than inventing a codebase.

## Audit without repairs

```text
/project-auditor Review projects/my-app's last change for broken setup, behavior regressions and missing validation. Report findings with file references; do not edit the app or call live services.
```

An audit may find no defects while still reporting substantial uncertainty.
Check coverage and evidence before treating it as a release decision.

## Create a reusable procedure

```text
/skill-creator Create a release-notes skill that reads reviewed commit subjects and produces a draft grouped by user-visible changes. Keep it manual. Do not tag releases, push, publish, or send messages.
```

The new skill should define inputs and output, create real files, and mark
any unexecuted validation clearly. The six-skill distribution validator does
not automatically validate newly added workflows.

## Empty input

```text
/project-builder
```

If input.md has no saved request, the builder should ask for the goal. Empty
starter files are not a reason to make up a product.
