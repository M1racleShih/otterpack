# 截图是怎么做的

我希望大家能直接看看这些工具用起来是什么样，所以优先展示真实界面。为了方便公开，图里的任务、文档、模型名、路径和 agent 状态换成了演示数据，没有放入私人会话、访问凭证或账号额度。下面把每张图的来源和拍摄方式说清楚。

| 图片 | 生成方式 | 能证明什么 |
| --- | --- | --- |
| [Pi 首页](../assets/pi-parchment.png) | Pi 1.3.0 实际 PTY 输出 → pyte 0.8.2 解析 → Pillow 排版 | 当前主题和扩展首页的真实终端输出；不是桌面窗口截屏，也不是生成式 UI 示意 |
| [Pi 读取文档](../assets/pi-workflow.png) | 同一方法，真实 read 工具读取演示文件；provider 返回固定文本 | 输入、读取结果与 HUD 的组合；模型用量是夹具数值 |
| [conv-docs 手机阅读](../assets/conv-docs-mobile.png) | 还原源码运行独立 localhost 服务，浏览器真实截屏 | 实际网页渲染了本包演示文档 |
| [Herdr Remote 总览](../assets/herdr-overview.png) / [执行进度](../assets/herdr-remote-mobile.png) / [代码差异](../assets/herdr-diff-mobile.png) | 还原源码的真实网页连接本地 WebSocket 夹具，浏览器真实截屏；终端文本与 ANSI 由夹具构造 | 网页布局与羊皮纸 ANSI 渲染；不代表真实 Pi 输出、agent 执行或远程连接验收 |
| [Herdr Remote 会话历史](../assets/herdr-history-mobile.png) | 同一网页原生 Conversation history 面板，夹具通过 `get_history` 协议提供合成对话 | 实际 Markdown、表格、工具记录和 Tools 开关；不包含真实会话 |
| [小獭 logo](../assets/otterpack.png) | AI 生成透明插画 | 品牌形象；[提示词与许可](brand.md)单独记录 |

Pi 首页参考了我日常工作台的截图：紧凑的等宽字、居中的三色 π、羊皮纸背景和块状输入框。原始参考图没有公开，演示时也使用了不透明的纸色，避免桌面上的私人内容透出来。

v0.1.1 的手机图参考了我实际使用时的三张截图，分别展示执行进度、代码差异和会话回读。重新拍摄时，用了可以公开的短行示例，缩短视口，让内容更集中，同时保留网页自己的导航、输入区和历史面板。原图中的域名、私人路径、项目代码和会话内容没有复制过来，也没有补画手机状态栏或浏览器外框。

v0.1.2 修改了示例文档的表达，conv-docs 图片也按下面的方法重新拍了一张，保持文字和截图一致。其他图片沿用前一版。

## 复现 Pi 图片

准备 Pi 1.3.0、目录中固定版本的 block editor 和模型选择器、按补丁还原的 HUD，以及自己可用的等宽字体。安装 pyte 0.8.2 与 Pillow 后，在仓库根目录运行：

```sh
python3 scripts/capture-pi.py \
  --pi /path/to/pi \
  --hud /path/to/reconstructed-pi-hud \
  --editor /path/to/pi-block-editor \
  --picker /path/to/pi-provider-model-picker \
  --font /path/to/monospaced-font.ttf
```

这会生成基础组合的首页与读取图。首版使用 MesloLGL Nerd Font Mono、16px、96 列 × 44 行、21px 行高；字库本身不随包分发。终端块字符按整格绘制，保留 π 标志的连续形状。

发布的首页额外加载了 [catalog.json](../catalog.json) 中九个 npm 包与 `/clear`，在基础命令后加：

```text
--catalog-packages /path/to/installed/node_modules --welcome-only
```

脚本核对这些包的版本号，读取[组合配置](../presets/pi/pi-cc-extensions.json)，禁用重复的首页、footer、编辑器前缀与 aliases。首页的 14 是扩展入口数量，包含演示 provider；不是声称本包原创了 14 个插件。完整首页没有启用技能、真实供应商或账号额度。

脚本创建临时 HOME 与 agent directory，使用本地演示 provider 和网络阻断夹具，不读取日常模型配置、不写入现有会话。可选第三方扩展仍是可执行代码，复现时使用自己审核过的安装版本。该 PTY 脚本使用 POSIX 接口；本次只在 Linux 运行。

## 复现网页截图

先用 [materialize.py](../scripts/materialize.py) 还原对应组件。在不同终端运行以下命令；路径替换成自己还原的目录：

```sh
python3 scripts/demo-docs.py --source /path/to/reconstructed-conv-docs
python3 -m http.server 18795 --bind 127.0.0.1 --directory /path/to/reconstructed-herdr-remote/web
python3 scripts/demo-remote.py
```

Remote 夹具需要 Python websockets 14+。三个端口都只绑定 localhost，退出命令即可停止；它们不会启动或操作日常 Herdr 与 conv-docs 服务。

- conv-docs：打开 `http://127.0.0.1:18794`，输入脚本内公开的演示 token `otterpack-local-demo-not-a-secret`，切换中文，打开 `otterpack/field-notes.md`。此值仅供本地演示，不能用于真实服务。
- Remote：打开 `http://127.0.0.1:18795`，在设置中连接 `ws://127.0.0.1:18796` 并选择 Light。worker 展示执行进度，reviewer 展示差异；打开 notes 后点击 Conversation history，滚到顶部拍摄完整短会话。夹具忽略所有修改类消息，不转发到任何 agent。
- 当前图片采用独立 Chrome for Testing 153.0.8010.52、**390 × 700 CSS px、3 倍像素密度**，使用 agent-browser 0.38.1 保存为 1170 × 2100 PNG。总览单独采用 390 × 430 视口。v0.1.0 的原图曾使用 430 × 932 视口；旧版本资源仍保留在对应发行版。

网页图未生成或补画界面元素。图中文字和状态来自明确的演示材料，公开时保留对应组件的许可和署名，见 [Third-party notices](../THIRD_PARTY_NOTICES.md)。
