# 打开工具袋

每项的精确提交或安装版本在 [catalog.json](../catalog.json)。下表的“来源关系”说明 Otterpack 收录它的方式，不把组合工作归为所有组件的原创。

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

这些扩展按实际安装清单登记，源码不随本包复制。版本表示本次来源环境，并不承诺整套组合在所有宿主版本上兼容。完整安装组合可先参考 cooking-pi；按需安装请逐项检查自己的 Pi 版本。

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

以上包清单均声明 MIT；项目 URL、版本与许可字段来自实际安装包元数据，见目录文件。更新时重新核对上游许可证，不把这张表当永久授权。原作者与许可证全文的保留范围见 [Third-party notices](../THIRD_PARTY_NOTICES.md)。
