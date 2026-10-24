# 一张顺手的 Pi 工作台

我把几种界面职责交给不同插件：block editor 负责输入区，HUD 负责状态，CC extensions 负责工具输出，模型选择器负责按供应商分组。先从原生 Pi 开始，遇到具体需要再加一件。

## 选一条路径

**想要完整配方：** 从 [cooking-pi](https://github.com/M1racleShih/cooking-pi) 开始。它维护独立配置目录、安装计划、恢复逻辑和整套版本锁。其初始配方基于 Pi 1.2.0；Otterpack 的截图和主题检查基于 Pi 1.3.0，两个版本不能直接视为同一验证结果。

**已有自己的 Pi：** 按 [catalog.json](../catalog.json) 选择独立项目。这个包里的主题和示例配置可以分别取用；不需要替换你的整份 settings.json。

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

当前 HUD 补丁包含速度统计、NewAPI key 额度与 Kimi Code 额度相关改动。网络额度功能需要显式启用，默认示例不会发起查询。本次打包测试使用离线夹具；没有替使用者验证真实账号与供应商。

网页总结、自动标题、持续目标等扩展可能增加模型调用。相关选择见[目录](catalogue.md)，先判断自己是否需要，再安装。

## 一次小任务

![Pi 实际读取示例文档后的终端画面](../assets/pi-workflow.png)

这张图使用三件基础插件和离线演示 provider：真实执行读取文件，再展示固定的演示回复。用量是夹具数值，不能用于评价模型速度、费用或质量。首页图额外加载了目录中的九个 npm 扩展与 `/clear`；[截图说明](screenshots.md)记录了两者区别。
