# 从哪里开始

这里的东西比较多，不需要一次全装上。你可以先看看自己目前最想改善什么，再选对应的工具。

| 你现在想改善什么 | 可以先看看 |
| --- | --- |
| 屏幕太刺眼，几种工具配色不一致 | [羊皮纸主题](themes.md)，记得一起调整宿主终端的底色 |
| Pi 输入区和状态栏不够顺手 | [Pi 插件](pi.md)，可以先试输入框和 HUD |
| 同时开几个 agent，经常找不到谁在等回复 | [Herdr](herdr.md)，先看 Radar 的侧栏状态 |
| 电脑上生成的报告，离开桌子后还想继续看 | [conv-docs](conv-docs.md)，先用一个演示文件预览 |
| 每个项目都装了很多 skill，不太好管理 | [dynamic-skills](skills-and-handoffs.md#dynamic-skills)，按项目选择需要的部分 |
| 想把一部分任务交给 DSH Desktop | [cd-connect](skills-and-handoffs.md#cd-connect)，先说明允许修改的范围和验收要求 |

下载后，可以在仓库根目录运行 `python3 scripts/verify.py` 检查文件（需要 Python 3.11+）。主题和配置文件都可以直接打开看。这里要注意一下：`presets/` 里放的是**配置片段**，把需要的字段合并进去就好，不能用它替换整份日常配置。

具体版本在 `catalog.json` 里，三项工具的当前改动放在 `patches/`。如果你需要包含这些改动的完整源码，按[还原说明](snapshots.md)操作。账号配置、认证文件、私人端点和真实会话不在资源包中。

使用前也需要准备好对应环境：Pi 需要自己的模型账号，手机阅读需要运行中的服务和可达的网络，cd-connect 需要对应版本的 DSH Desktop。每个工具的页面里会进一步说明。
