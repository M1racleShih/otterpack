#!/usr/bin/env python3
"""Local synthetic scenes for the REAL Herdr Remote UI; no Herdr or model calls.

Requires websockets 14+. Serve the reconstructed web/ folder separately.
All messages that could modify a real session are ignored, never forwarded.
"""
import asyncio
import json
import time
from websockets.asyncio.server import serve

INK = '63;56;46'
MUTED = '100;89;73'
BLUE = '52;95;122'
GREEN = '63;96;64'
RED = '148;61;53'
AMBER = '124;83;40'
PURPLE = '108;79;122'


def color(text, fg=INK, bg=None):
    code = f'38;2;{fg}' + (f';48;2;{bg}' if bg else '')
    return f'\x1b[{code}m{text}\x1b[0m'


def lines(*rows):
    return '\n'.join(rows)


# These are demonstration strings, not a recording of live agent work.
# Keep the ordinary output within a phone's readable width; the real UI still
# owns typography, ANSI rendering, scrolling, buttons and all panel behavior.
PROGRESS = lines(
    color('Otterpack · mobile preview / DEMO', AMBER),
    '',
    color('❯ ', BLUE) + '让羊皮纸主题在手机上也清楚可读。',
    '',
    color('● Multiple Tools: 3 done · 0 failed', GREEN),
    '├ ' + color('✓ Read ', BLUE) + 'themes/parchment/palette.json',
    '├ ' + color('✓ Read ', BLUE) + 'presets/pi/pi-hud.json',
    '└ ' + color('✓ Read ', BLUE) + 'docs/themes.md',
    '',
    color('Checking the mobile palette', MUTED),
    '',
    '保持纸色底、深色字与清晰的状态标记。',
    '接下来核对新增、删除和输入区的对比。',
    '',
    color('✓ Edit ', BLUE) + 'theme-preview.ts',
    color('  12 │ - const surface = "#FFFFFF";', RED, '240;220;209'),
    color('  12 │ + const surface = "#F3EAD3";', GREEN, '223;231;210'),
    color('  13 │ + const ink = "#3F382E";', GREEN, '223;231;210'),
    color('     ↳ diff +2 −1 · demo change', MUTED),
    '',
    color('◌ Working…', AMBER) + color(' · checking readable contrast', MUTED),
    '',
    color('● Todos (1/3)', AMBER),
    '├ ' + color('✓ 核对主题与插件的颜色来源', GREEN),
    '├ ' + color('◐ 检查手机上的代码差异', AMBER),
    '└ ' + color('○ 整理可独立阅读的交付说明', MUTED),
    '',
    color('  ▌                                                   ', INK, '235;223;196'),
    color('                                                      ', INK, '235;223;196'),
    color('[Otterpack Demo]', AMBER) + ' · ' + color('think:med', BLUE),
    color('~/otterpack-demo · fixture · no model requests', MUTED),
    color('● working', PURPLE) + ' · ' + color('read ✓3 · edit ✓1', GREEN),
)

DIFF = lines(
    color('Otterpack · review a change / DEMO', AMBER),
    '',
    color('✓ Edit ', BLUE) + 'theme-preview.ts',
    color('  10 │ export const palette = {', MUTED),
    color('  11 │ -  paper: "#FFFFFF",', RED, '240;220;209'),
    color('  11 │ +  paper: "#F3EAD3",', GREEN, '223;231;210'),
    color('  12 │ -  ink: "#888888",', RED, '240;220;209'),
    color('  12 │ +  ink: "#3F382E",', GREEN, '223;231;210'),
    color('  13 │ +  success: "#3F6040",', GREEN, '223;231;210'),
    color('  14 │ +  error: "#943D35",', GREEN, '223;231;210'),
    color('  15 │ };', MUTED),
    '',
    color('  18 │ export function statusLabel(ok: boolean) {', MUTED),
    color('  19 │ -  return ok ? "green" : "red";', RED, '240;220;209'),
    color('  19 │ +  return ok ? "✓ passed" : "! failed";', GREEN, '223;231;210'),
    color('  20 │ }', MUTED),
    '',
    color('     ↳ diff +5 −3 · demo change', MUTED),
    '',
    color('✓ Read ', BLUE) + 'docs/mobile-review.md',
    color('  ↳ 颜色之外，也保留文字与符号。', MUTED),
    '',
    color('● Todos (2/3)', AMBER),
    '├ ' + color('✓ 纸色与正文保持清晰对比', GREEN),
    '├ ' + color('✓ 新增与删除有独立标记', GREEN),
    '└ ' + color('◐ 回读会话结论与验收边界', AMBER),
    '',
    color('  ▌                                                   ', INK, '235;223;196'),
    color('                                                      ', INK, '235;223;196'),
    color('[Otterpack Demo]', AMBER) + ' · ' + color('think:med', BLUE),
    color('~/otterpack-demo · fixture · no model requests', MUTED),
    color('● reviewing', PURPLE) + ' · ' + color('read ✓1 · edit ✓1', GREEN),
)

SUMMARY = '''主题预览已整理好，可以在手机上回读交付结论。

### 这次改了什么

- **配色**：纸色 `#F3EAD3`，正文 `#3F382E`。
- **差异**：新增、删除同时保留色块与符号。
- **输入区**：块状编辑器与 HUD 各司其职。

### 验收清单

| 项目 | 观察结果 |
| --- | --- |
| 代码差异 | 新增与删除清楚可辨 |
| 任务状态 | 进度与待办同时可见 |
| 会话历史 | 结论、列表与表格可读 |

### 下一步

把这些内容带回桌面，核对实际文件，再决定是否接受改动。

> 本页为演示会话；没有连接真实 agent，也没有执行上面的示例修改。'''

HISTORY = [
    {'uuid': 'demo-user', 'role': 'user', 'text': '请整理这次羊皮纸主题的改动和验收结果。'},
    {'uuid': 'demo-read', 'role': 'tool', 'tool': 'read', 'target': 'themes/parchment/palette.json'},
    {'uuid': 'demo-edit', 'role': 'tool', 'tool': 'edit', 'target': 'theme-preview.ts',
     'added': 2, 'removed': 1, 'diff': '-const paper = "#FFFFFF";\n+const paper = "#F3EAD3";\n+const ink = "#3F382E";'},
    {'uuid': 'demo-docs', 'role': 'tool', 'tool': 'read', 'target': 'docs/mobile-review.md'},
    {'uuid': 'demo-summary', 'role': 'assistant', 'text': SUMMARY},
]


def snapshot():
    now = int(time.time() * 1000)
    items = [('worker', 'working', '核对主题与可读性'),
             ('reviewer', 'working', '检查代码差异'),
             ('notes', 'done', '交付结论已整理')]
    agents = [
        {'pane_id': f'w1:p{i}', 'agent': 'pi', 'label': label, 'status': status,
         'cwd': '/demo/otterpack', 'project': 'otterpack', 'host': 'local', 'remote': None,
         'workspace_id': 'w1', 'tab_id': 'w1:t1', 'title': title, 'focused': i == 1,
         'scrollback': 32, 'viewport_rows': 32, 'has_session': True,
         'last_active_at': now - i * 1000, 'last_seen_at': now - 10000, 'order': i}
        for i, (label, status, title) in enumerate(items, 1)
    ]
    return {'type': 'agents', 'agents': agents, 'panes': [], 'spaces': {
        'workspaces': [{'workspace_id': 'w1', 'label': 'otterpack', 'number': 1,
                        'focused': True, 'tab_count': 1, 'pane_count': 3, 'host': 'local'}],
        'tabs': [{'tab_id': 'w1:t1', 'workspace_id': 'w1', 'label': 'mobile-demo',
                  'number': 1, 'focused': True, 'pane_count': 3, 'host': 'local'}],
    }}


async def handle(ws):
    await ws.send(json.dumps(snapshot()))
    await ws.send(json.dumps({'type': 'sessions', 'sources': [
        {'host': 'local', 'active': 'demo', 'sessions': [{'name': 'demo', 'running': True}]}]}))
    async for raw in ws:
        msg = json.loads(raw)
        pane = msg.get('pane_id')
        if pane not in ('w1:p1', 'w1:p2', 'w1:p3') and msg.get('type') in ('read_pane', 'get_history'):
            continue
        if msg.get('type') == 'read_pane':
            content = DIFF if pane == 'w1:p2' else PROGRESS
            await ws.send(json.dumps({'type': 'pane_content', 'pane_id': pane, 'content': content}))
        elif msg.get('type') == 'get_history':
            turns = [t for t in HISTORY if msg.get('include_tools', True) or t['role'] != 'tool']
            await ws.send(json.dumps({'type': 'history', 'pane_id': pane,
                                     'messages': [] if msg.get('before') else turns,
                                     'total': len(turns), 'has_more': False,
                                     'file_truncated': False}))
        elif msg.get('type') in ('list', 'list_agents', 'agents'):
            await ws.send(json.dumps(snapshot()))


async def main():
    async with serve(handle, '127.0.0.1', 18796):
        print('Demo WebSocket: ws://127.0.0.1:18796; synthetic progress, diff and history', flush=True)
        await asyncio.Future()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
