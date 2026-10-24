#!/usr/bin/env python3
"""Offline integrity, theme-format and local-document-link checks. Python 3.11+."""
import hashlib
import json
from pathlib import Path
import plistlib
import re
import sys
import tomllib
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '.local', 'node_modules', '.venv', '__pycache__', 'dist'}


def files(root, pattern):
    return (p for p in root.rglob(pattern) if not IGNORED.intersection(p.relative_to(root).parts))


def verify(root=ROOT):
    catalogue = json.loads((root / 'catalog.json').read_text())
    assert catalogue['schema_version'] == 1
    for entry in catalogue['repositories']:
        assert re.fullmatch(r'[0-9a-f]{40}', entry['commit']), entry['id']
        if entry.get('patch'):
            file = root / entry['patch']
            assert hashlib.sha256(file.read_bytes()).hexdigest() == entry['patch_sha256'], file
            assert (file.parent / 'LICENSE').is_file(), file
    for path in files(root, '*.json'):
        json.loads(path.read_text())
    tomllib.loads((root / 'themes/parchment/herdr.toml').read_text())
    plistlib.loads((root / 'themes/parchment/codex/parchment.tmTheme').read_bytes())
    for file in files(root, '*.md'):
        source = file.read_text()
        targets = re.findall(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)', source)
        targets += re.findall(r'(?:src|href)="([^"]+)"', source)
        for target in targets:
            target = target.split('#')[0].split('?')[0]
            if not target or ':' in target or target.startswith('//'):
                continue
            assert (file.parent / unquote(target)).exists(), f'{file.relative_to(root)}: missing {target}'
    sums = root / 'SHA256SUMS'
    if sums.exists():
        for line in sums.read_text().splitlines():
            expected, relative = line.split('  ', 1)
            assert (root / relative).resolve().is_relative_to(root.resolve()), relative
            assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == expected, relative
    return len(catalogue['repositories']), len(catalogue['npm_references'])


if __name__ == '__main__':
    try:
        repos, packages = verify()
        print(f'PASS: {repos} pinned repositories, {packages} package references; formats, links and checksums.')
    except (AssertionError, ValueError, OSError) as error:
        sys.exit(f'FAIL: {error}')
