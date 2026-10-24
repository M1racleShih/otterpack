# 把文档带走

[conv-docs](https://github.com/M1racleShih/conv-docs) 让电脑上产出的报告、方案和页面在手机上可读。你明确选中文件或目录，再给它一个临时预览或持久发布入口。

“随时随地”需要运行中的服务、可达的网络和自己的访问凭证。电脑休眠或网络断开时，远程读取也会中断；它不自动把所有文件同步到云端。

## 先准备自己的服务

```sh
python3 scripts/materialize.py conv-docs ../otterpack-conv-docs
```

还原后阅读该目录的中文 README 与 `docs/deploy-runbook.zh.md`。本包带来的补丁包括安全阅读模式的样式边界修复，以及被 HTML 引用的伴生 CSS 放行；路径、隐藏文件、排除规则和认证限制仍然有效。

## 从一个文档开始

服务配置好后，在安装了 conv-docs 的环境里运行：

```sh
conv-docs preview /absolute/path/to/report.md --ttl 2h
```

这里的路径是示例，替换成你明确要阅读的文件。`--once` 可用于阅后过期的临时预览。发布目录时用 `--exclude` 排除不想提供的内容；源码与配置默认被过滤，确有需要才开启 `--allow-code`。

可先用本包的[演示报告](examples/field-notes.md)测试手机排版。示例没有私人数据，也不需要模型调用。查看结束后，按 conv-docs 的 `list` 和 `unpublish` 指令管理自己创建的预览。

我常把一份调研结果先写成可独立阅读的文档，离开电脑后检查它的结论和证据。回到桌前时，再把问题交给 agent。这比在终端滚动历史记录更适合认真阅读。
