# Compatibility sources and design attribution

Reviewed on **2026-11-14** against the official Claude Code documentation.
These are compatibility references, not copied documentation or claims of
endorsement. No exact minimum CLI version is claimed: the kit targets current
documented behavior, with runtime verification still required in your environment.

| Source | Decision supported |
| --- | --- |
| [Skills](https://code.claude.com/docs/en/skills) | Project SKILL.md layout, command invocation, manual-only frontmatter and argument substitution |
| [Settings files](https://code.claude.com/docs/en/settings) | Shared project settings location; local and managed settings can affect behavior |
| [All settings](https://code.claude.com/docs/en/settings-reference) | `disableSkillShellExecution` and `permissions.deny` are documented settings |
| [Permissions](https://code.claude.com/docs/en/permissions) | Read patterns, Bash/PowerShell rules and limits of command-based protection |
| [Project memory](https://code.claude.com/docs/en/memory) | CLAUDE.md guidance and the distinction between explicit project files and auto memory |
| [Quickstart](https://code.claude.com/docs/en/quickstart) | CLI installation, sign-in and starting from a project directory |
| [CLI reference](https://code.claude.com/docs/en/cli-reference) | An interactive initial prompt is supported; helpers launch one session |

The original owner-authored conversation design specified heartbeat, wrap-up,
system-review, project-builder, project-auditor and skill-creator; shared business
context; file-based memory; per-skill state; logs; and honest completion rules.
This implementation preserves those elements. It refines readiness language,
uses reviewed settings, adds a conflict-safe offline installer, and makes
scheduling examples explicitly offline structural checks. The private design
conversation is not needed to install or use the public project.

The schema URL in settings is a public editor aid; the offline validator checks
this template's supported key subset rather than claiming full upstream schema
validation. Recheck official references when upgrading. Do not guess new settings.
