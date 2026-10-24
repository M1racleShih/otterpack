import { existsSync, readFileSync, unlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

type ThinkingLevel = "off" | "minimal" | "low" | "medium" | "high" | "xhigh" | "max";

interface ClearState {
	provider: string;
	modelId: string;
	thinkingLevel: ThinkingLevel;
}

function safeUnlink(file: string) {
	try {
		unlinkSync(file);
	} catch {
		// ignore
	}
}

/**
 * /clear — like /new, but keeps the current model and thinking level.
 *
 * How it works:
 * - The command captures model + thinking level as plain data into a
 *   pid-keyed temp file (the old `pi`/`ctx` go stale after session
 *   replacement, and extension modules are re-evaluated, so closures
 *   cannot carry the state across).
 * - `ctx.newSession()` runs the exact same path as the built-in /new.
 * - The new session's extension instance restores model + thinking level
 *   in its `session_start` (reason === "new") handler, then removes the
 *   file. Plain /new finds no file, so it stays untouched.
 */
export default function clearCommand(pi: ExtensionAPI) {
	const stateFile = join(tmpdir(), `pi-clear-state-${process.pid}.json`);

	pi.registerCommand("clear", {
		description: "Start a new session (like /new) but keep model and thinking level",
		handler: async (_args, ctx) => {
			const model = ctx.model;
			if (!model) {
				ctx.ui.notify("/clear: no active model to keep", "warning");
				return;
			}

			const state: ClearState = {
				provider: model.provider,
				modelId: model.id,
				thinkingLevel: pi.getThinkingLevel(),
			};

			try {
				writeFileSync(stateFile, JSON.stringify(state));
			} catch (error) {
				ctx.ui.notify(`/clear: failed to save state (${String(error)})`, "error");
				return;
			}

			const result = await ctx.newSession({
				withSession: async (newCtx) => {
					newCtx.ui.notify(
						`Cleared — kept ${state.provider}/${state.modelId} (thinking: ${state.thinkingLevel})`,
						"info",
					);
				},
			});

			if (result.cancelled) {
				safeUnlink(stateFile);
			}
		},
	});

	pi.on("session_start", async (event, ctx) => {
		if (event.reason !== "new") return;
		if (!existsSync(stateFile)) return;

		let saved: ClearState | undefined;
		try {
			saved = JSON.parse(readFileSync(stateFile, "utf8")) as ClearState;
		} catch {
			// corrupted marker; drop it and behave like a normal /new
		}
		safeUnlink(stateFile);
		if (!saved?.provider || !saved.modelId) return;

		// Restore model if the new session's default differs
		if (ctx.model?.provider !== saved.provider || ctx.model?.id !== saved.modelId) {
			const model = ctx.modelRegistry.find(saved.provider, saved.modelId);
			if (!model) {
				ctx.ui.notify(
					`/clear: model ${saved.provider}/${saved.modelId} not found, keeping default`,
					"warning",
				);
				return;
			}
			const ok = await pi.setModel(model);
			if (!ok) {
				ctx.ui.notify(
					`/clear: no auth for ${saved.provider}/${saved.modelId}, keeping default`,
					"warning",
				);
				return;
			}
		}

		// Restore thinking level (clamped to model capabilities)
		if (saved.thinkingLevel && saved.thinkingLevel !== pi.getThinkingLevel()) {
			pi.setThinkingLevel(saved.thinkingLevel);
		}
	});
}
