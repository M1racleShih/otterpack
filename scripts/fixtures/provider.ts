// Adapted from cooking-pi (M1racleShih), MIT. Synthetic offline demo only.
import { createAssistantMessageEventStream } from '@earendil-works/pi-ai';
import type { ExtensionAPI } from '@earendil-works/pi-coding-agent';

const zeroCost = { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 };
let calls = 0;
function streamFixture(model, context) {
  const stream = createAssistantMessageEventStream();
  const message = context.messages.filter(m => m.role === 'user').at(-1);
  const prompt = typeof message?.content === 'string' ? message.content : (message?.content ?? []).filter(c => c.type === 'text').map(c => c.text).join('');
  const tool = prompt.startsWith('Read the demo notes') ? ['demo', 'read', 'field-notes.md'] : prompt.match(/^TOOL:(read|write|edit):(.+)$/s);
  const afterTool = context.messages.at(-1)?.role === 'toolResult';
  const continuation = JSON.stringify(context.messages.at(-1)).includes('Synthetic custom continuation');
  const output = {
    role: 'assistant', api: 'openai-completions', provider: 'otterpack-fixture', model: model.id,
    content: [], timestamp: Date.now(), stopReason: 'stop',
    usage: { input: 100, output: 20, cacheRead: 0, cacheWrite: 0, totalTokens: 120, cost: { ...zeroCost, total: 0 } },
  };
  queueMicrotask(() => {
    stream.push({ type: 'start', partial: output });
    if (tool && !afterTool && !continuation) {
      const [, name, path] = tool;
      const args = name === 'read' ? { path } : name === 'write' ? { path, content: 'otterpack-pi updated\n' } : { path, oldText: 'updated', newText: 'edited' };
      const call = { type: 'toolCall', id: `otterpack-call-${++calls}`, name, arguments: args };
      output.content.push(call);
      output.stopReason = 'toolUse';
      stream.push({ type: 'toolcall_start', contentIndex: 0, partial: output });
      stream.push({ type: 'toolcall_delta', contentIndex: 0, delta: JSON.stringify(args), partial: output });
      stream.push({ type: 'toolcall_end', contentIndex: 0, toolCall: call, partial: output });
    } else {
      const text = continuation ? 'OTTERPACK_READY' : afterTool ? 'The notes are ready. Keep the scope small, make progress visible, and verify what changed.' : prompt.startsWith('ECHO:') ? prompt.slice(5) : 'OTTERPACK_READY';
      output.content.push({ type: 'text', text });
      stream.push({ type: 'text_start', contentIndex: 0, partial: output });
      stream.push({ type: 'text_delta', contentIndex: 0, delta: text, partial: output });
      stream.push({ type: 'text_end', contentIndex: 0, content: text, partial: output });
    }
    stream.push({ type: 'done', reason: output.stopReason, message: output });
    stream.end(output);
  });
  return stream;
}

export default function fixtureProvider(pi: ExtensionAPI) {
  pi.registerProvider('otterpack-fixture', {
    name: 'Otterpack Fixture', baseUrl: 'http://127.0.0.1:9', apiKey: 'fixture-not-a-secret',
    api: 'openai-completions', streamSimple: streamFixture,
    models: ['fixture-alpha', 'fixture-beta'].map(id => ({ id, name: id === 'fixture-alpha' ? 'Otterpack Alpha' : 'Otterpack Beta', reasoning: true, input: ['text'], cost: zeroCost, contextWindow: 200000, maxTokens: 4096 })),
  });
}
