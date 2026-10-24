#!/usr/bin/env python3
"""Local-only conv-docs screenshot fixture; never touches the user's service."""
import argparse
from pathlib import Path
import sys
import tempfile
import shutil

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--source',type=Path,required=True)
p.add_argument('--port',type=int,default=18794)
a=p.parse_args()
sys.path.insert(0,str(a.source.resolve()/'src'))
from conv_docs.store import ConfigStore
from conv_docs.server import DocgateServer, AuditLog

root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='otterpack-docs-demo-') as tmp:
    state=Path(tmp)
    store=ConfigStore(str(state/'config.json'))
    store.set_token('otterpack-local-demo-not-a-secret')
    shutil.copytree(root/'docs/examples',state/'documents')
    store.publish(str(state/'documents'),name='otterpack',project='Otterpack')
    server=DocgateServer(('127.0.0.1',a.port),store,audit=AuditLog(str(state/'audit.log')))
    print(f'Local demo ready: http://127.0.0.1:{server.server_port}',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
