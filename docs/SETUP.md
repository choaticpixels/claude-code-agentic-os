# Setup and maintenance

## Choose your layout

Use a dedicated clone as an operating hub when you want one place for shared
context and projects beneath `projects/`. For an existing app, use the installer
to add the kit directly to the app's repository. Do not assume an app in a
sibling directory inherits this hub's instructions or skills.

Requirements: current Claude Code with supported account access, Git for cloning,
and Python 3.10+ only for the offline installer/validator/tests. Follow the
[official quickstart](https://code.claude.com/docs/en/quickstart) for CLI installation
and sign-in. No API key or extra Python package is required for the kit scripts.
Claude usage is subject to your account's billing and limits.

## Review before trusting

Read [CLAUDE.md](../CLAUDE.md), [settings](../.claude/settings.json),
[operating rules](../agentic-os/system/operating-rules.md) and the six skill files.
The installer does not merge settings. Its manifest contains workspace files
only; it does not copy distribution artwork, docs, tests or root scripts into
your app. Keep the source clone if you want to validate an installed workspace.

Preview with `python scripts/install.py --target "../my-project" --dry-run`.
Remove `--dry-run` to copy files. An ordinary existing target directory is
supported; any existing destination file causes refusal before copying. Install
elsewhere and merge manually if your app already has instructions or settings.
No forced replacement is available. Do not use a target with concurrent writers.
An unexpected I/O failure can leave a partial install; inspect created files
and recover from version control rather than repeatedly retrying blindly.

The installer adds an ignore file for runtime context under `agentic-os/`.
Keep workflow source and non-sensitive initial templates under version control
only when that is intentional. See [Safety](SAFETY.md) for tracked starter files.

## First run

1. Fill in non-sensitive business context and constraints. Leave unknowns unknown.
2. Run `python scripts/validate.py --root "../my-project"` from the source clone.
3. Start `claude` inside the target. Review the folder trust prompt.
4. Invoke `/heartbeat`. Inspect the written report and its stated limits.
5. Try a small local `/project-builder` request, then invoke `/project-auditor`
   with the explicit target. Finish with `/wrap-up`.
6. Inspect reports, handoffs and evals. If a run is blocked or incomplete, its
   status must reflect that. Never change status to pass just to silence a check.

To resume later, reopen Claude in the same workspace and invoke `/heartbeat`.
Read the last-run notes and relevant handoff. The CLI's own conversation-resume
feature is separate from this kit's file-based continuity.

## Updates

Do not pull a new version over valuable uncommitted state without reviewing it.
Fetch changes into a clean source clone, compare the instructions and settings,
and merge selected changes using version control. The installer is deliberately
not an in-place updater. Preserve memory, handoffs, evaluations and local settings.
Run offline checks and a small runtime smoke test after substantial changes.

## Removal

The installer has no global side effects or automatic uninstaller. Review
`manifest.json` against your project history and remove only kit files you
intend to retire. Preserve or archive useful context first. For merged
CLAUDE.md/settings, remove only this kit's sections and rules. Removing the
kit does not uninstall Claude Code. No scheduler exists unless you separately
registered one below.

## Optional offline scheduling

The launch helpers call `claude '/heartbeat'` in an interactive session. They
are for a person at a terminal, not unattended scheduling.

The scheduling examples instead call the **offline Python validator**. They
make no model calls and do not write skill outputs or memory. This avoids
implying that a manual-only skill runs unattended. No cron entry or Windows
task is registered during installation.

### Windows example

From the workspace root in PowerShell, replace all three paths with yours:

```powershell
./agentic-os/scripts/schedule-windows-task-example.ps1 -PythonExe 'C:/Python314/python.exe' -SourceRepository 'C:/src/claude-code-agentic-os' -Workspace 'C:/src/my-project'
```

This previews only. To opt in, run the same command with `-Register`. The
example schedules a daily 09:00 check in the machine's timezone using the
current user, and refuses to replace an existing task of the same name.
Account policies may require additional permissions or an interactive sign-in.
Verify on your own machine; the distribution does not register a task for you.

```powershell
Get-ScheduledTask -TaskName 'ClaudeAgenticOS-OfflineCheck'
Start-ScheduledTask -TaskName 'ClaudeAgenticOS-OfflineCheck'
Get-ScheduledTaskInfo -TaskName 'ClaudeAgenticOS-OfflineCheck'
```

Inspect LastRunTime and LastTaskResult after completion; `0` is the validator's
success exit code. This example does not save stdout; use Task Scheduler history
and run the validator directly for the detailed report. To remove an opted-in task:

```powershell
Unregister-ScheduledTask -TaskName 'ClaudeAgenticOS-OfflineCheck'
```

### cron example

Read `agentic-os/scripts/cron-example.txt`. Replace example paths, create a
private log directory and run the exact command manually first. Then add the
reviewed line using `crontab -e`. Inspect `crontab -l`, the log and the scheduler's
timezone. Remove the line with `crontab -e` to stop it. The cron file itself is
only an example; copying it does not install a schedule.
