#!/usr/bin/env python3
"""Render REAL Pi PTY output. Adapted from cooking-pi capture-preview.py (MIT).

Optional tools: pyte 0.8.2 and Pillow. Supply installed Pi 1.3.0 and the three
component directories. This creates a fresh HOME and refuses model traffic.
"""
import argparse
import errno
import fcntl
import json
import os
from pathlib import Path
import pty
import select
import shutil
import signal
import struct
import tempfile
import termios
import time
import pyte
from PIL import Image, ImageDraw, ImageFont

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--pi', type=Path, required=True)
p.add_argument('--hud', type=Path, required=True)
p.add_argument('--editor', type=Path, required=True)
p.add_argument('--picker', type=Path, required=True)
p.add_argument('--font', type=Path, required=True)
p.add_argument('--catalog-packages', type=Path, help='Optional installed npm directory for the fuller welcome frame')
p.add_argument('--welcome-only', action='store_true')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
columns, rows = 96, 44
with tempfile.TemporaryDirectory(prefix='otterpack-pi-') as temporary:
    base = Path(temporary)
    workspace = base/'home/otterpack-demo'
    workspace.mkdir(parents=True)
    agent = base/'agent'
    (agent/'themes').mkdir(parents=True)
    shutil.copyfile(root/'themes/parchment/pi/parchment.json',agent/'themes/parchment.json')
    packages=[]
    for source in [a.hud,a.editor,a.picker]:
        name=json.loads((source/'package.json').read_text())['name']
        destination=base/'home/tools'/name
        destination.mkdir(parents=True)
        for relative in ['package.json','index.ts','src','extensions']:
            item=source/relative
            if item.is_dir():shutil.copytree(item,destination/relative)
            elif item.is_file():shutil.copyfile(item,destination/relative)
        packages.append(str(destination))
    if a.catalog_packages:
        for package in json.loads((root/'catalog.json').read_text())['npm_references']:
            source=a.catalog_packages/package['name']
            installed=json.loads((source/'package.json').read_text())
            assert installed['version']==package['version'],package['name']
            packages.append(str(source.resolve()))
        (agent/'extensions').mkdir()
        shutil.copyfile(root/'extensions/pi/clear.ts',agent/'extensions/clear.ts')
        shutil.copyfile(root/'presets/pi/pi-cc-extensions.json',agent/'pi-cc-extensions.json')
    demo=base/'home/tools/demo-provider.ts'
    shutil.copyfile(root/'scripts/fixtures/provider.ts',demo)
    (agent/'settings.json').write_text(json.dumps({'theme':'parchment','packages':packages}))
    (agent/'pi-hud.json').write_text(json.dumps({'palette':'theme','quota':{'enabled':False}}))
    (workspace/'field-notes.md').write_text('# A small toolkit, a thoughtful workflow\n\n1. Make the goal clear.\n2. Keep the work visible.\n3. Carry the result with you.\n4. Check what actually changed.\n')
    env = {'PATH':os.environ['PATH'],'HOME':str(base/'home'),'PI_CODING_AGENT_DIR':str(agent),
           'TERM':'xterm-256color','COLORTERM':'truecolor','LANG':'C.UTF-8','PI_OFFLINE':'1','PI_TELEMETRY':'0','PI_TITLE_OFF':'1',
           'NODE_OPTIONS':'--import='+json.dumps(str(root/'scripts/fixtures/no-network.mjs')),
           'OTTERPACK_PI_NETWORK_LOG':str(base/'network.log')}
    command = [str(a.pi.resolve()),'--offline','--no-mcp','--no-skills','--no-prompt-templates','--no-context-files',
               '--no-approve','--no-session','--tui-mode','fullscreen','--use-theme','parchment',
               '--provider','otterpack-fixture','--model','fixture-alpha','--thinking','medium',
               '--name','Otterpack demo','-e',str(demo)]
    pid,fd=pty.fork()
    if pid==0:
        os.chdir(workspace)
        os.execvpe(command[0],command,env)
    fcntl.ioctl(fd,termios.TIOCSWINSZ,struct.pack('HHHH',rows,columns,0,0))
    data=bytearray()
    def pump(seconds):
        deadline=time.monotonic()+seconds
        while time.monotonic()<deadline:
            ready,_,_=select.select([fd],[],[],min(.1,max(0,deadline-time.monotonic())))
            if ready:
                try:chunk=os.read(fd,65536)
                except OSError as error:
                    if error.errno==errno.EIO:raise RuntimeError('Pi exited: '+data.decode(errors='replace')[-3000:]) from error
                    raise
                if not chunk:raise RuntimeError('PTY closed')
                data.extend(chunk)
    try:
        pump(3)
        welcome=bytes(data)
        if not a.welcome_only:
            os.write(fd,b'Read the demo notes and summarize the workflow.\r')
            pump(3)
            os.write(fd,b'\x0f')
            pump(.5)
    finally:
        os.kill(pid,signal.SIGTERM)
        for _ in range(40):
            done,_=os.waitpid(pid,os.WNOHANG)
            if done:break
            time.sleep(.05)
        else:
            os.kill(pid,signal.SIGKILL);os.waitpid(pid,0)
        os.close(fd)
    assert not (base/'network.log').exists(),'Unexpected network attempt'

screen=pyte.Screen(columns,rows)
pyte.Stream(screen).feed(data.decode(errors='replace'))
plain='\n'.join(screen.display)
if not a.welcome_only:assert 'The notes are ready.' in plain,plain
assert 'Error loading' not in plain,plain
palette={'black':'#3F382E','red':'#943D35','green':'#3F6040','brown':'#7C5328','blue':'#345F7A',
         'magenta':'#6C4F7A','cyan':'#345F7A','white':'#645949','brightblack':'#645949','brightred':'#943D35',
         'brightgreen':'#3F6040','brightbrown':'#7C5328','brightblue':'#345F7A','brightmagenta':'#6C4F7A',
         'brightcyan':'#345F7A','brightwhite':'#3F382E'}
font=ImageFont.truetype(str(a.font),16)
cw=round(font.getlength('M'));ch=21;pad=18;header=30
def color(value,bg=False):
    if value=='default':return '#F3EAD3' if bg else '#3F382E'
    return palette.get(value,'#'+value if len(value)==6 else '#3F382E')
frames=[('pi-parchment.png',welcome)]
if not a.welcome_only:frames.append(('pi-workflow.png',data))
for filename,frame in frames:
    screen=pyte.Screen(columns,rows)
    pyte.Stream(screen).feed(frame.decode(errors='replace'))
    im=Image.new('RGB',(columns*cw+2*pad,rows*ch+2*pad+header),'#E7DCC2');draw=ImageDraw.Draw(im)
    draw.text((pad,8),'Otterpack / Pi 1.3.0 / Parchment / offline demo',font=font,fill='#645949')
    for y in range(rows):
        for x in range(columns):
            c=screen.buffer[y][x];fg,bg=color(c.fg),color(c.bg,True)
            if c.reverse:fg,bg=bg,fg
            left,top=pad+x*cw,pad+header+y*ch
            draw.rectangle((left,top,left+cw,top+ch),fill=bg)
            # Terminal block characters fill the cell, including its line leading.
            if c.data=='█':draw.rectangle((left,top,left+cw-1,top+ch-1),fill=fg)
            elif c.data=='▀':draw.rectangle((left,top,left+cw-1,top+ch//2-1),fill=fg)
            elif c.data=='▄':draw.rectangle((left,top+ch//2,left+cw-1,top+ch-1),fill=fg)
            elif c.data and c.data!=' ':draw.text((left,top),c.data,font=font,fill=fg)
    im.save(root/'assets'/filename)
(root/'.local').mkdir(exist_ok=True)
(root/'.local/pi-screen.txt').write_text(plain+'\n')
(root/'.local/pi-screen.ansi').write_bytes(data)
print('PASS: real Pi PTY, synthetic provider, '+('welcome only' if a.welcome_only else 'read tool completed')+', zero network attempts; assets/pi-parchment.png')
