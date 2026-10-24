# conv-docs：在手机上继续看文档

我对文档预览的需求很直接：电脑上生成了报告、方案或者页面，换到手机上，也希望能方便地继续看。[conv-docs](https://github.com/M1racleShih/conv-docs) 就是用来做这个的。选中要看的文件或目录，就可以创建临时预览，也可以长期发布。

当然，这需要服务还在运行、网络能够访问，并且有自己的访问凭证。它不会自动把所有文件同步到云端；如果电脑休眠或者网络断开，手机上也就暂时读不到了。

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

我希望方案写出来之后，还能找个方便的地方认真读一遍。用手机看看结论和依据，有疑问再回来继续跟 agent 讨论，这也是我想把 conv-docs 放进这个项目的原因。
