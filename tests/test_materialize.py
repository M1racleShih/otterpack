import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('materialize', Path(__file__).resolve().parents[1] / 'scripts/materialize.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MaterializeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.destination = self.root / 'component'
        self.patch = self.root / 'change.patch'
        self.patch.write_text('diff --git a/example.txt b/example.txt\n--- a/example.txt\n+++ b/example.txt\n@@ -1 +1 @@\n-before\n+after\n')
        self.entry = {'id':'fixture', 'repository':'https://github.com/example/fixture', 'commit':'a'*40,
                      'patch':'change.patch','patch_sha256':m.digest(self.patch),
                      'patched_files':{'example.txt':hashlib.sha256(b'after\n').hexdigest()}}

    def fetch(self, entry, work):
        work.mkdir()
        subprocess.run(['git','init','-q',str(work)],check=True)
        (work/'example.txt').write_text('before\n')

    def test_applies_exact_patch_without_installing(self):
        with patch.object(m,'fetch',self.fetch):
            m.materialize(self.entry,self.destination,self.root)
        self.assertEqual((self.destination/'example.txt').read_text(),'after\n')

    def test_preserves_existing_destination(self):
        self.destination.mkdir()
        (self.destination/'keep').write_text('mine')
        with patch.object(m,'fetch') as fetch:
            with self.assertRaises(ValueError):m.materialize(self.entry,self.destination,self.root)
            fetch.assert_not_called()
        self.assertEqual((self.destination/'keep').read_text(),'mine')

    def test_bad_patch_hash_prevents_network(self):
        self.patch.write_text('tampered')
        with patch.object(m,'fetch') as fetch:
            with self.assertRaises(ValueError):m.materialize(self.entry,self.destination,self.root)
            fetch.assert_not_called()

    def test_wrong_output_hash_does_not_publish_destination(self):
        self.entry['patched_files']['example.txt']='0'*64
        with patch.object(m,'fetch',self.fetch):
            with self.assertRaises(ValueError):m.materialize(self.entry,self.destination,self.root)
        self.assertFalse(self.destination.exists())

    def test_rejects_manifest_escape(self):
        with self.assertRaises(ValueError):m.safe_path(self.root,'../outside')
        with self.assertRaises(ValueError):m.safe_path(self.root,'.git/config')

    def test_rejects_destination_symlink(self):
        self.destination.symlink_to(self.root/'absent',target_is_directory=True)
        with self.assertRaises(ValueError):m.materialize(self.entry,self.destination,self.root)


if __name__ == '__main__':unittest.main()
