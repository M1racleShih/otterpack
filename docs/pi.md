# 我在用的 Pi 插件

我目前把这几种功能分给了不同插件：block editor 处理输入区，HUD 显示状态，CC extensions 调整工具输出，模型选择器按供应商分组。它们放在一起，就是截图里这套 Pi。

如果你已经在用 Pi，可以看看自己需要哪一部分。还没配过的话，先从原生 Pi 开始也可以，遇到具体问题再加插件。

## 完整配置，还是只装几个插件？

**想试完整配置的话，**可以从 [cooking-pi](https://github.com/M1racleShih/cooking-pi) 开始。它管理独立配置目录、安装计划、恢复方式和整套固定版本。这里有个版本区别需要说明：cooking-pi 的初始配置基于 Pi 1.2.0，Otterpack 的截图和主题检查用的是 Pi 1.3.0，两边的验证结果不能直接混用。

**已经有自己的 Pi 配置，**就按 [catalog.json](../catalog.json) 选需要的项目。主题和配置示例可以单独用，不需要替换整份 settings.json。

例如，在 Otterpack 根目录还原当前 HUD 源码到一个新目录：

```sh
python3 scripts/materialize.py pi-hud ../otterpack-pi-hud
```

检查生成目录里的源码与说明后，按 Pi 的本地安装方式装入你选定的 agent directory。其余自有插件也可以用同一个还原工具获取固定提交。上游更新继续在各项目维护；Otterpack 的补丁只是当前快照。

## 示例配置与小扩展

| 材料 | 作用 |
| --- | --- |
| [settings.fragment.json](../presets/pi/settings.fragment.json) | 选择 parchment；前提是主题已经加载 |
| [pi-hud.json](../presets/pi/pi-hud.json) | HUD 跟随主题；额度默认关闭 |
| [pi-cc-extensions.json](../presets/pi/pi-cc-extensions.json) | 关闭 CC 的首页、footer、输入框前缀和 aliases，分别交给 block editor、HUD 与本包的 `/clear` |
| [clear.ts](../extensions/pi/clear.ts) | 开新会话时保留模型和思考级别，来源于 cooking-pi |

这份 CC 片段适合上述组合：`showStartupHeader: false`、`enableCustomFooter: false`、`enableEditorPrefix: false`、`enableAliases: false`。如果不安装其他组件，可保留 CC 对应的原生功能。每添加一个插件，检查 `/reload` 是否报告冲突，并实际看看输入框、状态栏与快捷键。

当前 HUD 补丁包含速度统计、NewAPI key 额度和 Kimi Code 额度相关改动。额度查询需要手动启用，默认示例不会发起网络查询。打包时用离线测试数据检查了这些功能，真实账号和供应商还需要你在自己的环境里验证。

网页总结、自动标题、持续目标等扩展可能增加模型调用。相关选择见[工具列表](catalogue.md)，先判断自己是否需要，再安装。

## 读取文档时的样子

![Pi 实际读取示例文档后的终端画面](../assets/pi-workflow.png)

这张图加载了三件基础插件和离线演示 provider，实际读取了示例文件，然后展示固定的演示回复。里面的用量也是示例数值，不能拿来评价模型速度、费用或质量。首页图另外加载了目录中的九个 npm 扩展与 `/clear`，两张图的具体区别写在[截图说明](screenshots.md)里。
