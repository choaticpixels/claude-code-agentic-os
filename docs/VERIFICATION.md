# Verification record

Date: **2026-11-14**. Local environment: Windows, PowerShell, Git Bash and Python
3.14.6. This is a bounded verification record for the initial public kit.

| Check | Actual result | Limits |
| --- | --- | --- |
| Installer behavior suite | 9 tests: 8 passed, 1 skipped | Symlink creation was unavailable on this Windows host; that test did not execute |
| Clean install into a temporary path containing spaces | Passed; copied bytes matched source and installed structure validated | No existing-project semantic settings merge is attempted |
| Dry run and conflict refusal | Passed; dry run made no target; existing settings/handoff/parent-file conflicts preserved content | Mid-copy I/O failure can still leave a partial installation |
| Manifest traversal / drive-relative paths | Rejected in tests | Not an independent security audit |
| Offline validator | Passed for packaged and temporary installed workspace | Checks structure, metadata, JSON and local Markdown targets; not upstream runtime behavior |
| Bash and PowerShell helper syntax | Passed local parser checks | Not a Linux/macOS runtime test |
| Interactive launcher routing | Checked with a dummy Claude command | No real Claude process or model inference used |
| Windows scheduler example | Preview path checked | No task registered or executed |
| Skill/runtime evaluations | **Not run** | All six eval.json files remain not_run |
| GitHub Actions | Manual workflow supplied; not dispatched | No cross-platform CI pass is claimed |

The README's runtime badge is deliberately static and says not yet run. Do not
replace it with a passing runtime claim until you have a reproducible Claude
smoke-test record. Product builds, external integrations, scheduled operations,
deployed apps, real customer usage and production readiness were not verified.

To repeat the offline checks from the repository root:

```text
python scripts/validate.py
python -m unittest discover -s tests -v
```

For a Claude smoke test, follow the README's first workflow in a disposable
copy. Record the CLI version, request, actual outputs and tool results. Check
that outputs and handoffs match the files created, that evaluations have
evidence, and that wrap-up preserves remaining work. A model's self-report
alone is not verification. Test permissions using dummy credential files only.
