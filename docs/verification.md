# 验证记录与兼容范围

日期：**2026-10-24**。对象为 [catalog.json](../catalog.json) 中的固定版本与补丁。实际环境为 Linux x86_64；本页区分源码测试、界面观察和真实服务连接。

## 本次完成

| 对象 | 实际检查 | 结果与边界 |
| --- | --- | --- |
| 三组源码快照 | 从公开 GitHub 提交还原，检查补丁摘要、`git apply --check` 和所有改动文件摘要 | HUD、conv-docs、Herdr Remote 均通过；没有依赖未推送的本地提交 |
| pi-hud | 在还原源码运行 `npm test`、`npm run check` | 382 项测试通过，边界／语法／文档检查通过；额度适配使用测试夹具，没有验证真实账号 |
| conv-docs | 在还原源码运行 `python3 -m unittest discover -s tests -v` | 85 项通过；另启动独立本地服务，实际浏览并截图演示文档 |
| Herdr Remote | 在还原源码运行 `python -m unittest discover -s tests`，提供 Chromium、Playwright、websockets 与 Telegram 依赖 | 631 项通过，含浏览器外观测试；没有连接生产 relay 或真实 Herdr pane |
| Pi 1.3.0 | 严格主题 schema、实际 Theme 加载、HUD 配色与 CC Diff 浅色分支 | parchment 加载为 light；HUD 使用 theme；CC Diff 使用 github-light |
| Pi 基础组合 | 隔离 HOME 与 agent directory，真实 PTY、三件自有插件与演示 provider | 实际读取演示文件并展示固定回复；网络 guard 未记录请求 |
| Pi 完整首页 | 再加载目录中九个 npm 扩展与 `/clear` | 14 个扩展入口成功加载；首页、输入框、HUD 已检查。仅验证加载，不代表九个扩展的所有功能已验收 |
| Otterpack | `python3 scripts/verify.py`、`python3 -m unittest discover -s tests -v` | 资源格式、链接、补丁和资源摘要检查；6 项还原器测试通过 |
| cd-connect | 本机 bridge health | 桥接不可达，未派发 DSH 任务；没有把桌面执行写成通过 |

源码测试合计 **1,098 项**，另有资源包自身 **6 项**。CI 只运行资源包校验与自身测试，不在每次提交中启动所有上游工具。复现组件测试时，按该固定版本的说明准备依赖；本次 Node 为 24.18.0，浏览器测试使用本机 Chromium，截图用 Chrome for Testing 153.0.8010.52。

## 平台承诺

| 材料／组件 | Linux | macOS | Windows |
| --- | --- | --- | --- |
| 主题文件、文档与目录 | 已做格式检查；Pi 实际加载与渲染 | 可取用文件，未实机验证 | 可取用文件，未实机验证 |
| Kitty / Herdr / Radar 配色 | 本包检查格式；未重新操控日常工作台 | 以各宿主支持范围为准，未实测 | 不承诺原生支持；WSL 也未实测 |
| Codex CLI / Claude Code / Kimi Code 配色 | 本包检查 JSON／plist 格式；未逐项重跑所有 Diff、审批与动画状态 | 按客户端版本确认自定义主题入口 | 按客户端版本确认自定义主题入口 |
| Pi 与插件 | 上表所列离线测试、加载及图片检查 | 上游支持情况另查，组合未实测 | 上游支持情况另查，组合未实测 |
| conv-docs / Remote 网页 | 本地服务与手机尺寸 Chromium 视口实测 | 浏览器可能可用，未测 Safari | 浏览器可能可用，未测 Edge；服务端未实测 |
| dynamic-skills / cd-connect / cooking-pi / 青鸟 | 固定公开来源与许可；本次未完整复测工具功能 | 未验证 | 未验证 |
| 资源还原辅助脚本 | Git + Python 3.11+ 已实测 | 预期可用，未实测 | 未实测；不把 Git Bash 或 WSL 等同于原生验证 |

手机尺寸的浏览器截图不等同于 iOS／Android 真机测试。终端字形、透明背景、颜色探测和快捷键也会随宿主变化。首版提供有明确边界的 Linux 验证记录，没有整套跨平台安装承诺。

## v0.1.1 手机展示更新

同日更新，仅改变截图、演示数据与相关说明。组件源码、补丁和固定版本保持首版状态，沿用上面的组件验证；未重新运行全部组件测试。

- 实际浏览 390 × 700 手机视口：worker 进度、reviewer 差异、notes 会话历史和 conv-docs 文档；逐张检查保存图片。
- 会话历史 Tools 关闭后为 2 条对话，重新打开恢复 5 条记录（含 3 条工具调用）。历史面板与文档页面均未产生整页横向溢出。
- 演示源码语法检查、资源格式／链接／摘要检查与原有 6 项还原器测试通过。
- 截图中的终端内容和历史是合成夹具，没有运行示例代码、调用模型或连接真实 Herdr。

## 自己核对资源包

```sh
python3 scripts/verify.py
python3 -m unittest discover -s tests -v
```

发布包带有 `SHA256SUMS`，检查器会核对清单中的文件。还原组件前可先读[快照说明](snapshots.md)；下载源码成功、测试通过、真实账号可用和服务已经上线是不同结果。
