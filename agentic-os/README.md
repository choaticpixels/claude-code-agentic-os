# Workspace data

This directory contains shared business context, project-managed memory,
workflow maps, run logs, per-skill state and verification instructions.
Read system/operating-rules.md for the shared run protocol.

These files start empty with explicit not-run markers. Skills write results
when you invoke them; no process continuously updates this directory.

The distribution tracks starter state so clones work immediately. In your
working copy, keep sensitive context out of version control. The installer
copies a .gitignore under this directory to ignore runtime data in a new
project. Already tracked files remain tracked: see docs/SAFETY.md in the source
repository before publishing a clone you have used for private work.
