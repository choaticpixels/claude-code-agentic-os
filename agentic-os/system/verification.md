# Verification boundaries

Run the source repository's `python scripts/validate.py --root <workspace>`
for offline file, JSON, metadata and relative-link checks. It does not invoke
Claude, prove tool permission matching, run a product, or validate a schedule.

For a runtime smoke test, start `claude` in the workspace and invoke
`/heartbeat`. Check that the report cites inspected paths and writes its
last-output.md, handoff.md, eval.json, run log and JSONL history. Then build a
small disposable project, audit it and wrap up. Inspect the generated files
and commands yourself. Keep status not_run until a check actually executes.

Expected denied reads must be checked with dummy files, never real secrets.
Permission rules are not protection against every shell subprocess.
No scheduler or unattended Claude run is enabled in the distribution.
