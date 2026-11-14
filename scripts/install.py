#!/usr/bin/env python3
"""Install the reviewed workspace files without replacing existing content."""
import argparse
import json
from pathlib import Path, PureWindowsPath
import sys

SOURCE = Path(__file__).resolve().parents[1]


def install(target, dry_run=False, source=SOURCE):
    target = Path(target).absolute()
    source = Path(source).resolve()
    manifest = json.loads((source / 'manifest.json').read_text(encoding='utf-8'))
    files = manifest['workspace_files']
    planned = []
    for name in files:
        relative = Path(name)
        if (relative.is_absolute() or '..' in relative.parts
                or PureWindowsPath(name).drive or '\\' in name):
            raise ValueError('Unsafe manifest path')
        src, dest = source / relative, target / relative
        for path in [src, *src.parents, dest, *dest.parents]:
            if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
                raise ValueError('Symlinks and junctions are not supported')
        if not src.is_file():
            raise ValueError(f'Missing source: {name}')
        if dest.exists():
            raise ValueError(f'Existing destination: {name}; merge manually in a separate copy')
        for parent in dest.parents:
            if parent.exists() and not parent.is_dir():
                raise ValueError(f'Destination parent is a file: {parent}')
        planned.append((src, dest))
    if dry_run:
        return len(planned)
    # Exclusive creation protects against a file appearing after preflight.
    # An I/O failure can leave a partial install; existing files are never replaced.
    for src, dest in planned:
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open('xb') as stream:
            stream.write(src.read_bytes())
    return len(planned)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, type=Path)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        count = install(args.target, args.dry_run)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print(f'Install stopped: {error}', file=sys.stderr)
        return 1
    print(f'{"Would install" if args.dry_run else "Installed"} {count} workspace files. No Claude CLI, credentials, or scheduler configured.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
