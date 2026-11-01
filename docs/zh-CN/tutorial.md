# Kimi K3.1 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成 MP4。K3.1 写网页（或 Blender 场景），你来播放并录制。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 Kimi K3.1 Pro。登录后运行，就能拿到 HTML，并带实时预览。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[文本竞技场][arena]里，在 K3.1 旁边再加一两个模型（例如 `anthropic/claude-opus-5.5`、`openai/gpt-6-astra` 或 `deepseek/deepseek-v4.1-flash`），跑一次。所有模型拿到同样的文字，每个结果都显示花费和耗时。这个合集大多就是这样产出的——132 条视频是同题对比，Opus 5.5 是最常见的对手——这也是在你自己任务上验证[对比页](model-comparison.md)结论的最快方式。

## 3. 或者直接调用 API

Kimi K3.1 Pro 在 SandBase 上的模型 ID 是 `moonshotai/kimi-k3.1-pro`，兼容 OpenAI。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "moonshotai/kimi-k3.1-pro",
  max_tokens: 131072,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > kimi.html
jq '.usage' response.json
```

- `max_tokens: 131072`：这个模型的思考始终开启，隐藏的推理 token 也占用同一份额度，而 131072 是 SandBase 对它接受的上限（`sandbase inspect moonshotai/kimi-k3.1-pro`）。额度给小了，你会拿到被截断的页面，而且照样为这些 token 付费。
- `--max-time 900`：长页面要跑好几分钟，创作者报告的 harness 运行从 15 分钟到一个多小时不等。
- `sed '/^```/d'` 去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示计费的 token，包括推理 token。推理按输出价（每百万 $10）计费，输入每百万 $2，缓存命中按 0.1 倍；价格见[模型页][model]。
- 可选：加 `reasoning_effort` —— `low`、`high` 或 `max`（默认 `max`）—— 用思考换速度和成本。
- 图片同理：这个模型是多模态的，可以把参考图放进 `messages[].content`，而不用费劲描述——作者给它喂过概念图来做场景（[@thebuggeddev][fjord]），也给过单张图片让它生成 3D 模型（[@ojigineko_tips][image-to-3d]）。

用浏览器打开 `kimi.html`。如果一片空白，打开开发者工具：常见原因是被截断的文件（加大 `max_tokens`）或 CDN 没加载（要求所有资源内联）。

### 用 SandBase CLI

同一个调用也可以走 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli)，它同样读取 `SANDBASE_API_KEY`：

```bash
npx -y @sandbaseai/cli@latest inspect moonshotai/kimi-k3.1-pro   # 输入字段和价格，免费
jq -n --rawfile prompt prompt.txt '{max_tokens: 131072, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_moonshotai_kimi_k3_1_pro -f input.json --timeout 900 -o result.json
```

`-o result.json` 保存响应；页面在 assistant 消息里，和 API 一样。

## 4. 把页面录成视频

大多数作者是直接录屏。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs kimi.html kimi.mp4 12 1920 1080   # 12 秒，1080p
```

它按你给的尺寸打开页面，录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的效果，就在提示词里要求自动镜头巡游或定长循环（见[提示词写法 §6](prompt-guide.md#6-把交互和状态写进提示词)），让整个画面不依赖鼠标。

想要声音？录制本身只有画面，音频在剪辑里加——也可以像一些作者那样，把无声页面交给视频模型配音乐。这里有些作品直接出自 Kimi 网页版，它的 "3D Make" 流程一次运行就能出模型和成片（[@elvar_official][drone]）。

这个列表里很多视频并非一次 API 调用的产物：Claude Code、OpenCode 和 Blender MCP 贯穿整个[对比页](model-comparison.md)，Kimi 应用自带的 agent 循环也做出了折叠手机页面这类东西（[@chetaslua][iphone]）。

## 安全运行生成的代码

这段 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对于不完全信任的内容，或者要批量运行很多页面，请使用 [SandBase Sandbox][sandbox]：一个有时限、接触不到你的文件和 Key 的隔离环境。

## 分享

把视频发到 X，附上提示词并 @ Kimi K3.1。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-kimi-k3-1/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=moonshotai%2Fkimi-k3.1-pro&utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[model]: https://www.sandbase.ai/model/moonshotai/kimi-k3.1-pro?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[fjord]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113889721185444329?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[image-to-3d]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113933579747209626?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[drone]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113990648646750546?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[iphone]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113694080014356760?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
