import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer, validator = load('install'), load('validate')


class SetupTests(unittest.TestCase):
    def test_clean_install_validates_and_copies_exact_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / 'project with spaces'
            count = installer.install(dest)
            self.assertEqual(count, len(validator.WORKSPACE_FILES))
            self.assertEqual(validator.validate(dest), [])
            for name in validator.WORKSPACE_FILES:
                self.assertEqual((dest / name).read_bytes(), (ROOT / name).read_bytes())

    def test_dry_run_has_no_side_effects(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / 'absent'
            installer.install(dest, dry_run=True)
            self.assertFalse(dest.exists())

    def test_conflict_prevents_all_writes(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)
            settings = dest / '.claude/settings.json'
            settings.parent.mkdir()
            settings.write_text('{"existing":true}', encoding='utf-8')
            before = settings.read_bytes()
            with self.assertRaises(ValueError):
                installer.install(dest)
            self.assertEqual(settings.read_bytes(), before)
            self.assertFalse((dest / 'CLAUDE.md').exists())

    def test_second_install_preserves_handoff(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)
            installer.install(dest)
            handoff = dest / 'agentic-os/state/skills/project-builder/handoff.md'
            handoff.write_text('Real work to preserve', encoding='utf-8')
            with self.assertRaises(ValueError):
                installer.install(dest)
            self.assertEqual(handoff.read_text(), 'Real work to preserve')

    def test_manifest_cannot_escape_target(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'source'
            source.mkdir()
            (source / 'manifest.json').write_text(json.dumps({'workspace_files': ['../escape']}))
            with self.assertRaises(ValueError):
                installer.install(Path(temp) / 'target', source=source)

    def test_missing_file_is_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            installer.install(temp)
            (Path(temp) / '.claude/skills/heartbeat/SKILL.md').unlink()
            self.assertTrue(any('heartbeat/SKILL.md' in e for e in validator.validate(temp)))

    def test_drive_relative_manifest_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'source'
            source.mkdir()
            (source / 'manifest.json').write_text(json.dumps({'workspace_files': ['C:escape']}))
            with self.assertRaises(ValueError):
                installer.install(Path(temp) / 'target', source=source)

    def test_parent_file_conflict_prevents_install(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)
            (dest / '.claude').write_text('preserve this file')
            with self.assertRaises(ValueError):
                installer.install(dest)
            self.assertFalse((dest / 'CLAUDE.md').exists())
            self.assertEqual((dest / '.claude').read_text(), 'preserve this file')

    def test_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            dest, outside = Path(temp) / 'dest', Path(temp) / 'outside'
            dest.mkdir()
            outside.mkdir()
            try:
                (dest / '.claude').symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest('OS does not permit symlink creation')
            with self.assertRaises(ValueError):
                installer.install(dest)
            self.assertEqual(list(outside.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
