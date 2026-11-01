# Kimi K3.1 tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. K3.1 writes a web page (or a Blender scene); you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and Kimi K3.1 Pro selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to K3.1 (for example `anthropic/claude-opus-5.5`, `openai/gpt-6-astra` or `deepseek/deepseek-v4.1-flash`) and run once. Every model gets the same words, and each result shows its cost and time. That is how most of this collection was made — 132 of the videos here are head-to-heads, and Opus 5.5 is the most common rival — and it is the quickest way to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

Kimi K3.1 Pro is `moonshotai/kimi-k3.1-pro` on SandBase, OpenAI-compatible.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

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

- `max_tokens: 131072`: thinking is always on for this model and the hidden reasoning tokens come out of the same budget, and 131,072 is the most SandBase accepts for it (`sandbase inspect moonshotai/kimi-k3.1-pro`). With a tight limit you get a truncated page and still pay for the tokens.
- `--max-time 900`: one long page can take several minutes, and harness runs reported by creators ran from 15 minutes to over an hour.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for, including reasoning tokens. Reasoning bills at the output rate ($10 per million), input at $2 per million and cache reads at 0.1x; prices are on the [model page][model].
- Optional: add `reasoning_effort` — `low`, `high` or `max` (default `max`) — to trade thinking for speed and cost.
- Images work the same way: the model is multimodal, so you can put a reference frame in `messages[].content` instead of describing it — creators fed it concept art to build scenes from ([@thebuggeddev][fjord]) and a single image to make a 3D model ([@ojigineko_tips][image-to-3d]).

Open `kimi.html` in a browser. If it is blank, open the developer console: the usual causes are a truncated file (raise `max_tokens`) or a CDN that did not load (ask for everything inline).

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect moonshotai/kimi-k3.1-pro   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 131072, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_moonshotai_kimi_k3_1_pro -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API.

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs kimi.html kimi.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera tour or a fixed-length loop (see [prompt guide §6](prompt-guide.md#6-put-the-controls-and-the-state-in-the-prompt)), so nothing depends on a mouse.

Want sound? The recording is picture only, so add audio in the edit — or, as several creators did, feed the silent page to a video model for a score. Some pieces here came out of the Kimi web app itself, whose "3D Make" flow generates the model and a clip in one run ([@elvar_official][drone]).

Many videos in this list came out of a harness rather than a single API call: Claude Code, OpenCode and Blender MCP appear throughout the [comparison page](model-comparison.md), and the Kimi app's own agent loop built things like the folding-phone page ([@chetaslua][iphone]).

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention Kimi K3.1. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-kimi-k3-1/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=moonshotai%2Fkimi-k3.1-pro&utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[model]: https://www.sandbase.ai/model/moonshotai/kimi-k3.1-pro?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[fjord]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113889721185444329?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[image-to-3d]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113933579747209626?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[drone]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113990648646750546?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[iphone]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113694080014356760?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
