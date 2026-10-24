# Herdr 和我的配套插件

我用 [Herdr](https://github.com/herdrdev/herdr) 管理 workspace、tab 和 pane，配上 [Radar](https://github.com/M1racleShih/herdr-radar) 在侧栏看 agent 的状态。离开电脑后，还可以通过 [Remote](https://github.com/M1racleShih/herdr-remote-solution) 在手机上查看和操作。

## 这里收录了哪些内容

- Radar 固定到目录中的提交，保留其 MIT 作者署名。羊皮纸的 Agents／Spaces 模板放在[主题片段](../themes/parchment/herdr.toml)中。
- Remote 使用固定的公开提交，加上当前的 transcript 兼容、羊皮纸终端背景和前端缓存修复。源码与补丁继续采用 AGPL-3.0-or-later。
- 宿主 Herdr、远程隧道、账号认证和插件启用由各自原生流程处理；这里没有会话快照或真实远程地址。

## 怎么开始用

先按 [Herdr 官方文档](https://herdr.dev)安装宿主，再阅读固定版本的 Radar README。保持工作台运行时，只改展示配置并使用该版本的热加载入口。完成主题调整后，分别检查侧栏文字、pane 边框和终端底色。

Remote 可以先还原完整源码：

```sh
python3 scripts/materialize.py herdr-remote-solution ../otterpack-herdr-remote
```

随后阅读生成目录的 `DEPLOY_zh.md`，确认自己的网络与部署方式。它能远程交互和批准操作，权限范围与仅供阅读的 conv-docs 不同；启用前应理解项目的认证和访问边界。部署中的人工决策步骤仍由你决定。

## 我怎样使用状态

<img src="../assets/herdr-overview.png" width="390" alt="真实 Herdr Remote 网页中的演示 agent 状态列表">

我主要用这些状态判断接下来该看哪里：工作中说明 agent 还有活动，等待回复说明需要我处理，完成了就可以去检查结果。最后能不能接受这次改动，还是要看实际文件和验证结果。

## 在手机上看三件事

| 执行进度 | 代码差异 | 会话结论 |
| --- | --- | --- |
| ![工具活动、任务列表与 HUD](../assets/herdr-remote-mobile.png) | ![新增与删除的代码行](../assets/herdr-diff-mobile.png) | ![会话历史中的中文结论、列表与表格](../assets/herdr-history-mobile.png) |

**看进度：** 打开 worker，工具活动、待办与 HUD 放在同一屏，便于判断现在进行到哪一步。

**核对差异：** 打开 reviewer，读新增与删除的代码行。终端镜像保留原有行宽，实际长行可横向滚动；截图选择能在手机上读完的短示例。

**回读结论：** 在 notes 中打开 Conversation history。工具调用与 Markdown 结论共同呈现；Tools 开关可隐藏工具记录，集中阅读对话。

这三张图参考了我实际使用时的手机截图，换成可以公开的演示内容重新拍摄。终端文字和 ANSI 差异由演示脚本生成，会话历史由真实网页渲染。里面的任务、用量和改动都是示例。

拍图时使用的是独立演示环境，没有连接正在工作的 Herdr pane，也没有拍摄日常桌面会话。具体方式见[截图说明](screenshots.md)。
