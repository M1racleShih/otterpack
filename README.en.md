<p align="center"><img src="assets/otterpack.png" width="200" alt="A little otter holding a tool satchel with parchment and a pencil"></p>

# Otterpack

**Becoming a better programmer in the AI era.**

[简体中文](README.md) · [Tool list](docs/catalogue.md) · [Verification & compatibility](docs/verification.md)

Hi, this is Otterpack. I wanted to collect the Herdr plugins, Pi extensions, themes and other tools I use day to day, and share them in one place. Some are my own projects, some are changes to existing open-source tools, and others are third-party tools I use as they are. I like what they do together, even though I didn't create every part.

I've always thought I had a good eye—this parchment theme, for example 😉 Haha~

Independent tools still live in their own repositories. Otterpack keeps the theme files, configuration examples, exact versions, selected patches and notes on using them together. You can try just one or two things that interest you. The detailed guides are currently in Chinese.

![Actual offline Pi terminal output rendered with the parchment theme; synthetic demo data](assets/pi-parchment.png)

## Want to try it?

```sh
git clone https://github.com/M1racleShih/otterpack.git
cd otterpack
python3 scripts/verify.py
```

The offline verification helper needs Python 3.11+. It checks formats, local links and checksums without installing anything. You can also download a pack from [Releases](https://github.com/M1racleShih/otterpack/releases).

- **Themes:** `themes/parchment/` covers Kitty, Herdr/Radar, Pi, Codex CLI, Claude Code and Kimi Code. `themes/catppuccin/` contains the existing Latte and Frappé Pi ports. See [theme instructions](docs/themes.md) before merging configuration.
- **Pi:** [pi-hud](https://github.com/M1racleShih/pi-hud), [pi-block-editor](https://github.com/M1racleShih/pi-block-editor), [pi-provider-model-picker](https://github.com/M1racleShih/pi-provider-model-picker), a small `/clear` extension and selected third-party packages. I already have [cooking-pi](https://github.com/M1racleShih/cooking-pi) for the full Pi setup; this project includes Pi alongside my other tools.
- **Herdr:** [Radar](https://github.com/M1racleShih/herdr-radar) and [Remote](https://github.com/M1racleShih/herdr-remote-solution), with the original authors and licenses credited.
- **Documents on your phone:** [conv-docs](https://github.com/M1racleShih/conv-docs) serves the files you choose to share. Remote access needs your own running service and reachable network.
- **Skills and task handoffs:** [dynamic-skills](https://github.com/M1racleShih/dynamic-skills) and [cd-connect](https://github.com/M1racleShih/cd-connect).

The early-stage [Qingniao](https://github.com/M1racleShih/qingniao) project is also included as a local model gateway reference. Sources and licenses are listed in the [catalogue](docs/catalogue.md).

To get a component's source with the selected changes, use a new directory:

```sh
python3 scripts/materialize.py conv-docs /path/to/new-conv-docs-directory
```

The helper fetches the recorded GitHub commit, checks the patch hash, applies the patch and verifies the changed files. It never installs packages, starts services or writes to an existing destination. Read the resulting source and the component's installation guide before setting it up. See [versions and patches](docs/snapshots.md).

The first pack records my setup on **October 24, 2026**. Linux is the tested platform; the [verification record](docs/verification.md) explains what has and hasn't been checked on each platform.

The [mobile gallery](docs/herdr.md#在手机上看三件事) shows progress, code changes and conversation history in the actual Herdr Remote interface, captured at 390 × 700. The terminal text and conversations are synthetic examples, not live agent runs. The Pi image above comes from actual offline terminal output. See [how the images were made](docs/screenshots.md).

## Why I put this together

On October 24, Programmer's Day, I asked AI for a gift: help me turn these everyday tools into a project I could share, with a cute, nimble mascot. That's how the little otter with a tool bag came about.

I hope this collection helps me, and people with similar needs, become better programmers in the AI era. I also want to explain [how I use these tools](docs/workflows.md): discussing a problem with AI, understanding the proposed approach, and checking the result. If you think something could work better, I'd be happy to discuss it.

## Author and licenses

Put together by [M1racleShih](https://github.com/M1racleShih). New Otterpack material is offered under [MIT](LICENSE), to the extent applicable. Components retain their own licenses and authors. In particular, **the Herdr Remote patch and its source remain AGPL-3.0-or-later**. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

The mascot was created with an AI image-generation tool; its prompt and source are recorded in [the logo notes](docs/brand.md). This repository is unaffiliated with other projects called Otterpack.
