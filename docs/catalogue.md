# 工具列表

这里把目前收录的工具列在一起，方便你按需要找。每项具体用了哪个提交、哪个版本，记在 [catalog.json](../catalog.json) 里。自研、改造和直接使用的第三方工具，也分别注明了来源。

| 工具 | 用途 | 来源关系 | 在这里拿到什么 |
| --- | --- | --- | --- |
| [Herdr](https://github.com/herdrdev/herdr) | 多终端与 coding agent 工作台 | 第三方宿主，引用官方项目 | 配套主题与使用建议；不分发宿主二进制 |
| [Herdr Radar](https://github.com/M1racleShih/herdr-radar) | 在侧栏识别工作、完成、等待等状态 | 基于 qintmb / herdr-kit 贡献者的项目改造，MIT | 固定提交、羊皮纸侧栏模板 |
| [Herdr Remote](https://github.com/M1racleShih/herdr-remote-solution) | 手机端查看、交互与远程工作 | 基于 [dcolinmorgan/herdr-remote](https://github.com/dcolinmorgan/herdr-remote) 的部署与改造，AGPL | 固定源码与当前补丁、真实网页截图 |
| [pi-hud](https://github.com/M1racleShih/pi-hud) | 上下文、工具活动与可选额度显示 | 自研，信息组织参考 Claude HUD；MIT | 当前源码补丁，主题配置；额度默认关闭 |
| [pi-block-editor](https://github.com/M1racleShih/pi-block-editor) | 无边框块状输入框与欢迎页 | 自研，MIT | 固定源码入口与搭配说明 |
| [pi-provider-model-picker](https://github.com/M1racleShih/pi-provider-model-picker) | 按供应商分组选择模型 | 自研，MIT | 固定源码入口 |
| [pi-catppuccin-theme](https://github.com/M1racleShih/pi-catppuccin-theme) | Pi 的浅色／深色主题 | 对 Catppuccin 调色板的移植，MIT | Latte / Frappé 文件与原始署名 |
| [cooking-pi](https://github.com/M1racleShih/cooking-pi) | 完整、可复现的 Pi 配方 | 自有组合项目，组件分别署名 | 入口与版本边界；原配方仍在原仓库维护 |
| [conv-docs](https://github.com/M1racleShih/conv-docs) | 把明确选中的文档送到手机阅读 | 自研，含保留许可证的网页依赖，MIT | 当前修复补丁、阅读指南与演示文档 |
| [dynamic-skills](https://github.com/M1racleShih/dynamic-skills) | 按项目选择并锁定技能 | 自研，MIT | 固定源码与实践指南 |
| [cd-connect](https://github.com/M1racleShih/cd-connect) | 与 DSH Desktop 交接任务、按证据验收 | 自研，MIT | 固定源码、交接模板与使用边界 |
| [青鸟 Qingniao](https://github.com/M1racleShih/qingniao) | 本地模型网关与实例路由 | 自研，早期项目，MIT | 延伸阅读入口；尚不作为本包的默认安装项 |

## Pi 的其他选择

下面这些也是我当前装着的 Pi 扩展，这里记录版本和用途，不复制它们的源码。想试完整组合，可以先看 cooking-pi；只装其中几个的话，记得逐项核对自己的 Pi 版本。这份清单来自本次整理时的环境，不能保证换一个宿主版本后，所有扩展仍能一起用。

| 包 | 来源版本 | 用途与代价 |
| --- | --- | --- |
| `pi-cc-extensions` | 1.0.8 | 工具输出与 Diff；与 block editor 搭配时关闭重复输入框功能 |
| `pi-web-access` | 0.43.0 | 网页访问；总结可能发起额外模型请求 |
| `pi-undo-redo` | 0.1.4 | 文件改动撤回与重做；不能替代 Git |
| `pi-codex-compaction` | 0.2.3 | 特定模型／服务的上下文压缩；先核对支持范围 |
| `@juicesharp/rpiv-todo` | 2.13.9 | 任务列表 |
| `@juicesharp/rpiv-ask-user-question` | 2.13.9 | 结构化提问 |
| `@narumitw/pi-goal` | 0.54.13 | 持续任务；注意调用与预算 |
| `@ff-labs/pi-fff` | 0.11.0 | 文件搜索；依赖其平台组件 |
| `pi-session-titler` | 0.1.0 | 自有会话标题扩展；会增加模型请求 |

这些包在本次安装的元数据中都声明了 MIT，项目地址、版本和许可字段也记录在 `catalog.json` 里。以后更新时，还需要重新核对上游许可证；要保留哪些原作者署名和许可全文，见 [Third-party notices](../THIRD_PARTY_NOTICES.md)。
