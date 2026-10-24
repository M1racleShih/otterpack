<p align="center"><img src="assets/otterpack.png" width="220" alt="小水獭抱着装有卷纸与铅笔的工具袋"></p>

<h1 align="center">Otterpack · 小獭工具包</h1>

<p align="center"><strong>把工具用顺手，把判断留给自己。</strong></p>
<p align="center">主题、插件与工作方法，来自一个程序员与 AI 并肩工作的日常。</p>
<p align="center"><a href="README.en.md">English</a> · <a href="docs/start.md">从这里开始</a> · <a href="docs/catalogue.md">打开工具袋</a> · <a href="docs/workflows.md">实践指南</a> · <a href="docs/verification.md">验证与兼容</a></p>

---

有些工具解决大问题，有些改动只是让每天面对的输入框舒服一点。Otterpack 把我正在用、自己做过或认真改过的这些东西放在一起：一套羊皮纸配色，一张能看清 agent 状态的工作台，几个顺手的 Pi 插件，以及离开电脑后仍能读到成果的方法。

你可以只带走一张主题，也可以沿着指南搭起自己的工作环境。每个独立项目仍在自己的仓库发展；这里保存组合方式、明确版本和必要的补丁。

## 先看看它们

![羊皮纸 Pi：真实离线终端输出，模型与任务数据为演示夹具](assets/pi-parchment.png)

*Pi 1.3.0 的真实离线终端输出，经终端渲染器保存成图；演示模型没有调用上游服务。下方指南记录主题与插件的搭配。*

| 读一份完整的报告 | 看工具执行与任务进度 |
| --- | --- |
| ![conv-docs 的真实浏览器截图，内容为演示文档](assets/conv-docs-mobile.png) | ![Herdr Remote 执行进度：真实网页与合成终端内容](assets/herdr-remote-mobile.png) |

| 核对代码差异 | 回读会话结论 |
| --- | --- |
| ![Herdr Remote 代码差异：真实网页与合成 ANSI 演示](assets/herdr-diff-mobile.png) | ![Herdr Remote 会话历史：真实网页渲染演示对话](assets/herdr-history-mobile.png) |

*手机图在 390 × 700 的浏览器视口中拍摄，展示实际网页。文档、终端内容与会话历史均为演示数据；没有连接真实 agent。图源与复现方式见[截图说明](docs/screenshots.md)，使用场景见 [Herdr 手机工作台](docs/herdr.md#在手机上看三件事)。*

## 工具袋里有什么

| 一件事 | 带走什么 | 从哪里开始 |
| --- | --- | --- |
| 让屏幕舒服一点 | 羊皮纸主题：Kitty、Herdr/Radar、Pi、Codex CLI、Claude Code、Kimi Code；另附 Catppuccin Latte / Frappé | [主题指南](docs/themes.md) |
| 看清多个 agent 的状态 | Herdr Radar 与 Herdr Remote 的版本、配置和本地改造 | [Herdr 工作台](docs/herdr.md) |
| 让 Pi 更顺手 | HUD、块状输入框、供应商分组选择器、`/clear` 与扩展选择 | [Pi 配方](docs/pi.md) |
| 随时读到成果 | conv-docs：指定文件预览、临时链接、手机阅读 | [把文档带走](docs/conv-docs.md) |
| 让技能跟着项目走 | dynamic-skills：共用技能库，按项目选择与固定版本 | [技能与交接](docs/skills-and-handoffs.md) |
| 把任务交出去，再认真验收 | cd-connect：明确范围、原生执行、证据审查 | [技能与交接](docs/skills-and-handoffs.md) |

另外保留 [cooking-pi](https://github.com/M1racleShih/cooking-pi) 的完整 Pi 配方入口，以及早期项目[青鸟](https://github.com/M1racleShih/qingniao)的模型网关参考。工具目录会说明原创、改造和第三方选择之间的区别。

## 挑一件开始

```sh
git clone https://github.com/M1racleShih/otterpack.git
cd otterpack
python3 scripts/verify.py
```

检查脚本需要 Python 3.11+，只读取资源文件。想先试主题，打开[主题指南](docs/themes.md)；想复现当前工具改动，打开[版本快照](docs/snapshots.md)。也可以从 [Releases](https://github.com/M1racleShih/otterpack/releases) 下载资源包。

首版以 **2026-10-24** 的日常环境为来源。Linux 是实际验证平台；macOS、Windows 的范围逐项标在[兼容说明](docs/verification.md)。这份资源包提供按需取用的材料，各工具的安装与认证仍由使用者选择。

## 为什么把它们放在一起

成为 AI 时代更好的 programmer，需要知道自己要做什么，也需要看清工具实际上做了什么。我的习惯是：把目标说清楚，让工作有可见的状态，把结果带到方便阅读的地方，再回到代码和证据里做判断。

这些习惯和工具还会变化。欢迎带着具体场景、截图和版本来交流，让小獭的工具袋继续变得好用。

## 作者与许可

由 [M1racleShih](https://github.com/M1racleShih) 整理与维护。Otterpack 的新增代码、配置、文档和 logo 按 [MIT](LICENSE) 提供；已有组件保留自己的作者与许可，详见 [Third-party notices](THIRD_PARTY_NOTICES.md)。**Herdr Remote 的补丁与对应源码沿用 AGPL-3.0-or-later**，不被根目录的 MIT 重新授权。

Logo 使用 AI 图像工具生成，创作说明与提示词见[品牌说明](docs/brand.md)。名称仅标识本仓库，与其他同名项目无关联。

*2026 · 1024 程序员节。愿这只小獭陪你把每天的工作过得顺手一点。*
