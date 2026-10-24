#!/usr/bin/env python3
"""Reconstruct a pinned component in a NEW directory; never install or run it."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_path(root, relative):
    parts = PurePosixPath(relative)
    if parts.is_absolute() or not parts.parts or any(p in ('..', '.git') for p in parts.parts):
        raise ValueError('Unsafe manifest path')
    result = root.joinpath(*parts.parts)
    if not result.resolve().is_relative_to(root.resolve()):
        raise ValueError('Path escapes component directory')
    return result


def run(*args, cwd):
    subprocess.run(args, cwd=cwd, check=True)


def fetch(entry, target):
    url = entry['repository']
    if not re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', url):
        raise ValueError('Expected a public GitHub repository URL')
    if not re.fullmatch(r'[0-9a-f]{40}', entry['commit']):
        raise ValueError('Expected a full commit SHA')
    run('git', 'init', '--quiet', str(target), cwd=target.parent)
    run('git', '-c', 'protocol.file.allow=never', 'fetch', '--quiet', '--depth=1', url, entry['commit'], cwd=target)
    run('git', '-c', 'core.hooksPath=/dev/null', 'checkout', '--quiet', '--detach', 'FETCH_HEAD', cwd=target)
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=target, text=True).strip()
    if head != entry['commit']:
        raise ValueError('Fetched commit does not match the catalogue')


def materialize(entry, destination, root=ROOT):
    destination = Path(destination).expanduser().absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError('Destination must not already exist')
    if not destination.parent.is_dir():
        raise ValueError('Create the destination parent directory first')
    patch = None
    if entry.get('patch'):
        patch = safe_path(root, entry['patch'])
        if digest(patch) != entry['patch_sha256']:
            raise ValueError('Patch checksum mismatch')
    with tempfile.TemporaryDirectory(prefix='.otterpack-', dir=destination.parent) as tmp:
        work = Path(tmp) / 'source'
        fetch(entry, work)
        if patch:
            run('git', 'apply', '--check', str(patch), cwd=work)
            run('git', 'apply', str(patch), cwd=work)
            for relative, expected in entry['patched_files'].items():
                file = safe_path(work, relative)
                actual = digest(file) if file.is_file() else None
                if actual != expected:
                    raise ValueError(f'Patched file checksum mismatch: {relative}')
        # Reserve the destination atomically. A concurrent creator is never overwritten.
        destination.mkdir()
        try:
            for child in work.iterdir():
                shutil.move(str(child), destination / child.name)
        except Exception:
            # Leave partial output for inspection; never delete a caller's directory.
            raise
    return destination


def main():
    entries = {e['id']: e for e in json.loads((ROOT / 'catalog.json').read_text())['repositories']}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('component', choices=sorted(entries))
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    try:
        result = materialize(entries[args.component], args.destination)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'Not prepared: {error}\n')
    print(f'Prepared {args.component} at {result}. Nothing installed or started.')


if __name__ == '__main__':
    main()
