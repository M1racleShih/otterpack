#!/usr/bin/env python3
"""Synthetic local WebSocket fixture for the REAL Herdr Remote UI; no Herdr calls.

Run with websockets installed. Serve the reconstructed web/ folder separately.
The fixture ignores all mutating messages and never forwards them anywhere.
"""
import asyncio
import json
import time
from websockets.asyncio.server import serve

now=int(time.time()*1000)
def agent(i,label,status,title,kind='pi'):
    return {'pane_id':f'w1:p{i}','agent':kind,'label':label,'status':status,
            'cwd':'/demo/otterpack','project':'otterpack','host':'local','remote':None,
            'workspace_id':'w1','tab_id':f'w1:t{i}','title':title,'focused':i==1,
            'scrollback':30,'viewport_rows':34,'has_session':False,
            'last_active_at':now-i*1000,'last_seen_at':now-10000,'order':i}
agents=[agent(1,'parchment','working','Checking the theme palette'),
        agent(2,'field-notes','done','Ready for a careful read','claude'),
        agent(3,'resource-pack','idle','A small toolkit, ready to share','codex')]
snapshot={'type':'agents','agents':agents,'panes':[],
          'spaces':{'workspaces':[{'workspace_id':'w1','label':'otterpack','number':1,'focused':True,'tab_count':3,'pane_count':3,'host':'local'}],
                    'tabs':[{'tab_id':f'w1:t{i}','workspace_id':'w1','label':label,'number':i,'focused':i==1,'pane_count':1,'host':'local'} for i,label in enumerate(['parchment','field-notes','resource-pack'],1)]}}
content='\x1b[38;2;63;56;46mOtterpack / parchment demo\n\nA small toolkit for thoughtful work.\n\n\x1b[38;2;52;95;122mRead\x1b[0m field-notes.md\n\n  Make the goal clear.\n  Keep the work visible.\n  Carry the result with you.\n  Check what actually changed.\n\n\x1b[38;2;63;96;64m✓\x1b[0m Theme files checked\n\x1b[38;2;63;96;64m✓\x1b[0m Sources and licenses recorded\n\nSynthetic demo content.\nNo live agent is connected.\n'

async def handle(ws):
    await ws.send(json.dumps(snapshot))
    await ws.send(json.dumps({'type':'sessions','sources':[{'host':'local','active':'demo','sessions':[{'name':'demo','running':True}]}]}))
    async for raw in ws:
        msg=json.loads(raw)
        if msg.get('type')=='read_pane':
            await ws.send(json.dumps({'type':'pane_content','pane_id':msg['pane_id'],'content':content}))
        elif msg.get('type') in ['list','list_agents','agents']:
            await ws.send(json.dumps(snapshot))

async def main():
    async with serve(handle,'127.0.0.1',18796):
        print('Demo WebSocket ready: ws://127.0.0.1:18796; no real agents',flush=True)
        await asyncio.Future()

if __name__=='__main__':
    try:asyncio.run(main())
    except KeyboardInterrupt:pass
