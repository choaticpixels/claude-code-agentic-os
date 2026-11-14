#!/usr/bin/env python3
"""Offline structural checks, not a Claude runtime or security audit."""
import argparse
import json
from pathlib import Path
import re
import sys

SKILLS = ('heartbeat', 'wrap-up', 'system-review', 'project-builder', 'project-auditor', 'skill-creator')
WORKSPACE_FILES = ['CLAUDE.md', '.claude/settings.json', 'agentic-os/.gitignore']
for skill in SKILLS:
    WORKSPACE_FILES.append(f'.claude/skills/{skill}/SKILL.md')
    WORKSPACE_FILES.extend(f'agentic-os/state/skills/{skill}/{name}' for name in
                           ('input.md', 'last-output.md', 'handoff.md', 'learnings.md', 'eval.json'))
WORKSPACE_FILES.extend(f'agentic-os/{name}' for name in (
    'README.md', 'business-brain/business-brain.md', 'memory/MEMORY.md',
    'memory/recent-decisions.md', 'memory/active-projects.md', 'memory/constraints.md',
    'memory/notes-from-last-run.md', 'workflows/workflow-map.md',
    'workflows/project-builder-workflow.md', 'logs/runs.md', 'logs/errors.md',
    'logs/eval-history.jsonl', 'system/operating-rules.md', 'system/file-map.md',
    'system/verification.md', 'scripts/run-heartbeat.sh', 'scripts/run-heartbeat.ps1',
    'scripts/schedule-windows-task-example.ps1', 'scripts/cron-example.txt'))
WORKSPACE_FILES.extend(f'agentic-os/state/skills/project-builder/{name}.md'
                       for name in ('project-brief', 'assumptions', 'validation'))


def validate(root):
    root = Path(root)
    errors = []
    for name in WORKSPACE_FILES:
        if not (root / name).is_file():
            errors.append(f'Missing: {name}')
    for skill in SKILLS:
        path = root / '.claude/skills' / skill / 'SKILL.md'
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        if not text.startswith('---\n') or len(parts) != 3:
            errors.append(f'{skill}: invalid frontmatter boundary')
            continue
        fields = dict(line.split(':', 1) for line in parts[1].strip().splitlines() if ':' in line)
        if fields.get('name', '').strip() != skill or not fields.get('description', '').strip():
            errors.append(f'{skill}: missing name/description')
        if fields.get('disable-model-invocation', '').strip() != 'true':
            errors.append(f'{skill}: must remain manually invoked')
        if set(fields) - {'name', 'description', 'disable-model-invocation', 'argument-hint'}:
            errors.append(f'{skill}: unreviewed frontmatter fields')
        if '!`' in text or 'allowed-tools:' in text:
            errors.append(f'{skill}: inline execution or tool pre-approval found')
    for path in (root / 'agentic-os/state/skills').glob('*/eval.json'):
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
            if data['status'] not in ('not_run', 'pass', 'partial', 'fail', 'blocked'):
                raise ValueError('invalid status')
            if not isinstance(data['criteria'], list) or not data['criteria']:
                raise ValueError('criteria required')
            if data['status'] == 'pass' and not data.get('evidence'):
                raise ValueError('pass requires evidence')
        except (ValueError, KeyError) as error:
            errors.append(f'{path.name}: {error}')
    settings = root / '.claude/settings.json'
    if settings.is_file():
        try:
            data = json.loads(settings.read_text(encoding='utf-8'))
            if set(data) - {'$schema', 'disableSkillShellExecution', 'permissions'}:
                raise ValueError('unreviewed settings key')
            if data.get('disableSkillShellExecution') is not True:
                raise ValueError('inline shell policy missing')
            if set(data.get('permissions', {})) != {'deny'}:
                raise ValueError('template should contain deny rules only')
        except ValueError as error:
            errors.append(f'settings: {error}')
    history = root / 'agentic-os/logs/eval-history.jsonl'
    if history.is_file():
        for i, line in enumerate(history.read_text(encoding='utf-8').splitlines(), 1):
            if line.strip():
                try:
                    json.loads(line)
                except ValueError:
                    errors.append(f'eval-history line {i}: invalid JSON')
    # Relative Markdown links and images only; external URLs are checked separately.
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if re.match(r'[a-z]+:', link) or link.startswith('#'):
                continue
            local = link.split('#', 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f'{path.relative_to(root)}: broken link {link}')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    issues = validate(args.root)
    print('\n'.join(issues) if issues else 'PASS: workspace structure, JSON, skill metadata, and relative links')
    sys.exit(bool(issues))
