# 我喜欢的羊皮纸配色

最初我只是想给 Herdr 换一个羊皮纸颜色的主题。后来觉得，既然要调整，要不把常用的 Pi、Codex、Claude Code 和 Kimi Code 也一起考虑进去？这里就是整理出来的这套配色。

羊皮纸的主背景是 `#F3EAD3`，正文是墨棕 `#3F382E`。蓝灰用于链接与函数，橄榄绿用于成功和新增，砖红用于错误和删除。完整语义色在 [palette.json](../themes/parchment/palette.json)。

试的时候要注意，agent 的主题和宿主终端的背景是两回事。只改前者，终端可能还是深色。我建议先开一个独立窗口，把配套的终端颜色也试一下，觉得合适再放进日常配置。

## 各个工具怎么设置

| 工具 | 文件 | 合并／选择方式 |
| --- | --- | --- |
| Kitty | [kitty.conf](../themes/parchment/kitty.conf) | 备份自己的主题文件，在 Kitty 配置中 include 这个文件；保留字体、快捷键和其他配置 |
| Herdr + Radar | [herdr.toml](../themes/parchment/herdr.toml) | 合并同名 theme/sidebar 表，不能重复追加 TOML 表；见下节 |
| Pi | [parchment.json](../themes/parchment/pi/parchment.json) | 放到自己的 agent-dir/themes/parchment.json，通过 `/settings` 选择 |
| Codex CLI | [parchment.tmTheme](../themes/parchment/codex/parchment.tmTheme) | 放到自己的 CODEX_HOME/themes，通过 `/theme` 选择；此文件主要控制语法高亮，整体底色仍依赖终端 |
| Claude Code | [parchment.json](../themes/parchment/claude/parchment.json) | 放到自己的 Claude 配置目录 themes，支持自定义主题的版本可通过 `/theme` 选择 Parchment |
| Kimi Code | [parchment.json](../themes/parchment/kimi/parchment.json) | 放到自己的 Kimi 配置目录 themes，在 TUI 主题设置中选择 parchment |

这些设置对应本次收录的版本，具体测到了哪一步，可以看[验证记录](verification.md)。第一次创建主题目录后，已经打开的客户端可能还没发现它。先保存草稿，再用工具自己的入口重载或选择主题。

Pi 1.3.0 可先做一次临时试用（若已安装同名主题，直接选择它，避免重复资源）：

```sh
pi --theme "$PWD/themes/parchment/pi/parchment.json" --use-theme parchment
```

`themes/parchment/pi/` 也是一个仅包含主题的 Pi package。希望长期引用本地仓库时，可用 Pi 的本地包安装功能；安装后请保留这个目录。[官方主题说明](https://github.com/earendil-works/pi/blob/v1.3.0/packages/coding-agent/docs/themes.md)。

## Herdr 与 Radar

片段包括浅色底版、自定义颜色、Agents 与 Spaces 模板。侧栏模板源自 Radar，原许可保存在 [herdr-radar.txt](../licenses/herdr-radar.txt)。模板包含 Nerd Font 字形；没有对应字体时，图标可能显示为方块，文字状态仍有意义。本包不分发字体。

合并前备份配置。保留原来的插件注册、命令、hook、会话与工作目录字段，只替换片段中的对应展示表。手动维护这些表时，注意 Radar 对用户自定义表的保护，不要再用插件向导覆盖它们。

Herdr 客户端与服务端可能分别保留配色缓存。使用该版本文档中的配置检查与热加载入口，核对侧栏、pane 聚焦边框和当前终端；不要为换色停止正在运行的 server。只在有明确目标的 Herdr 会话内操作。

## Pi 插件搭配

把 [pi-hud.json](../presets/pi/pi-hud.json) 中的 `palette: "theme"` 合并到自己的 HUD 配置，使它读取主题。额度功能在示例中关闭，需要时再按 HUD 文档配置自己的账号。

使用 pi-block-editor、HUD 和 pi-cc-extensions 组合时，把 [pi-cc-extensions.json](../presets/pi/pi-cc-extensions.json) 合并到同名用户配置，由 block editor 负责首页与输入区，HUD 负责状态栏；具体分工见 [Pi 插件说明](pi.md)。HUD 的高档思考等级彩虹与某些插件的独立高亮不完全由主题控制。

## 如果还想保留原来的主题

[Catppuccin Frappé](../themes/catppuccin/catppuccin-frappe.json) 和 [Latte](../themes/catppuccin/catppuccin-latte.json) 保留原调色板署名。可按 Pi 主题说明选择单个主题或明暗配对。

试用前记录原来的主题名称，复制一份将修改的配置。恢复时在原生设置里选回原主题，再恢复自己备份的相关字段。只删除自己新增的主题文件，保留认证、会话与其他偏好。
