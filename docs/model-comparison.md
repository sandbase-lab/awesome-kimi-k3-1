# Kimi K3.1 vs Claude Opus 5.5, GPT-6 Astra and DeepSeek V4.1 Flash

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Head-to-heads posted on X with their own prompts, costs and times. Useful context, not verified by us.

K3.1 shipped in late October 2026 — the earliest videos in this list were made while it was still a stealth model on Arena under the codename **Kibitz**, and every video here was posted within about ten days of first sighting. That matters for reading the numbers: the measured side is one snapshot deep, and the creator side is enormous because a mystery frontier-tier model is exactly what everyone runs the same test on.

## What we measured: Lab Evals boards

Kimi K3.1 Pro **is** on the boards — one row, no effort-tier variants. The boards read the Artificial Analysis snapshot of 2026-10-29 (Intelligence Index v5, 716 models), which places it here among the models this collection compares it against:

| Model (row on the board) | [Intelligence Index][b-intel] | [Output speed][b-speed] | [Cost per task][b-cost] |
|---|---|---|---|
| Gemini 4 Carbon (High) | 59.4 (#1 of 78) | 102 tok/s (#172 of 373) | $7.76 (#67 of 73) |
| Claude Opus 5.5 (Max) | 58.4 (#2) | 98 tok/s (#182) | $10.04 (#71) |
| GPT-6 Astra (Max) | 56.9 (#4) | 76 tok/s (#245) | $6.24 (#61) |
| GPT-6.1 Sol (Max) | 54.5 (#7) | 81 tok/s (#231) | $1.27 (#34) |
| **Kimi K3.1 Pro** | **46.0 (#22)** | **37 tok/s (#353)** | **$3.68 (#53)** |
| Claude Haiku 5.5 (Max) | 36.2 (#32) | 241 tok/s (#21) | $0.41 (#23) |
| DeepSeek V4.1 Flash 1017 (Max) | 32.5 (#39) | 182 tok/s (#57) | $0.60 (#28) |
| GLM-5.3 (Max) | 31.7 (#40) | 80 tok/s (#237) | $5.01 (#56) |

What this says, and what it doesn't:

- **K3.1 Pro sits between the cheap fast models and the frontier.** 46.0 is a clear step above DeepSeek V4.1 Flash 1017 (32.5), GLM-5.3 (31.7) and Claude Haiku 5.5 (36.2), and a clear step below Opus 5.5 Max (58.4), GPT-6 Astra Max (56.9) and GPT-6.1 Sol Max (54.5). The "Kimi vs Opus" result creators keep reporting — close on quality, much cheaper — is consistent with a model that trails the leader by ~12 points, not one that ties it.
- **Its cost-per-task lands mid-board, not at the bottom.** $3.68 is about a third of Opus Max's $10.04 and less than half of Astra Max's $6.24 — but it is not cheap in absolute terms: DeepSeek V4.1 Flash runs the same eval for $0.60 and Haiku 5.5 for $0.41. The savings creators post are real only because the rival is usually Opus or Astra.
- **It is slow.** 37 tok/s puts it near the bottom of the speed board (#353 of 373), well below its own predecessor K3 (55 tok/s) and far below the flash-tier models. The 20-to-45-minute build times in creator posts are what that number looks like in practice.
- **No coding or agentic row yet.** Artificial Analysis has not published a Coding or Agentic Index for K3.1 Pro (those boards show no row), so every "it codes better than X" claim below rests on creator runs only.

## What we measured: Lab Pelican Test

The [Pelican Test][pelican] asks each model for an SVG of a pelican riding a bicycle, once static and once animated (wheels spin, legs pedal, CSS/SMIL only), rendered to PNG and scored 0 to 5 by an LLM judge.

**There is no Kimi K3.1 Pro row on the leaderboard** (read 2026-11-01: 22 models, 146 results). The closest rows are the previous generation — `moonshotai/kimi-k3` at 3.21, rank 10, $0.089 a drawing — and the models this collection compares it against: `anthropic/claude-opus-5.5` at 3.46 (rank 4), `google/gemini-4-argon` at 3.81 (rank 1), `openai/gpt-6-astra` at 3.08 (rank 11), `deepseek/deepseek-v4.1-flash` at 3.44 (rank 5, $0.017). [Run it yourself][pelican-run] and the board gains the number this page is missing.

The community ran its own version of the test anyway — the "pelican riding a bicycle" posts are among the most-made videos in this collection ([@chetaslua][pelican-1], [@ChrisGPT][pelican-2], [@AndyL5cc][pelican-svg]), including a stacked variant K3.1 got while still codenamed Kibitz ([@dummerspast39][stacked]).

## What creators reported

Same-prompt comparisons posted on X. Numbers are as the creator stated them: different tools (the Kimi app and its "3D Make" flow, Claude Code, OpenCode, Blender MCP, raw API), different reasoning settings, subscription plans whose cost is not directly comparable, often one run. Click through to watch both results. Claude Opus 5.5 is the rival in the most comparisons here — this collection is dominated by Kimi-vs-Opus posts.

| Creator | Task | Kimi K3.1 | Rival | Creator's verdict |
|---|---|---|---|---|
| [@AI_Screening][screening] | Single-HTML Three.js test, three models | "cooked Astra" | Opus 5.5 · GPT-6 Astra | "Kimi came out of nowhere and is now competing at the frontier" |
| [@marcusyul][rocket] | Rocket launch scene | $0.33 | GPT-6.1 Sol $1.15 · Opus 5.5 $2.06 · GPT-6 Astra $2.73 | ~6x cheaper than Opus, ~8x cheaper than Astra; all four got the rocket airborne |
| [@Bhavani_00007][whale] | Whale breaching scene | $0.75 | Opus 5.5 $3.01 · Astra $2.00 · Gemini 4 Argon $2.30 | "Comparable quality at a fraction of the cost" |
| [@Bhavani_00007][rocket2] | Rocket scene, quality call | $1.95, 6 min | Opus 5.5 $10.35, 24 min | "It mogged Opus 5.5 in output quality, cost, and speed in this test" |
| [@noclipepe][titanic] | Sink the Titanic | 35m 05s, 1.98M tokens, ~$0.88 | Opus 5.5: 28m 55s, 9.02M tokens, ~$8.43 | "Opus still sank the Titanic better. But Kimi got scary close for under a dollar" |
| [@noclipepe][dino] | Chrome dino with ragdoll physics | 19m 18s, $1.25 | Opus 5.5: 38m 55s, $8.53 · Gemini 4 Argon: 4m 34s, $0.19 | "Opus won. Argon was 45x cheaper" |
| [@noclipepe][subway] | Subway Surfers-style pelican game | 10m 01s, $0.95 | GPT-6 Astra: 19m 52s, $6.53 | "Astra spent $6.53 making it pretty. Kimi spent under a dollar making it work" |
| [@0xRhinoX][jelly] | Rainbow jelly you can cut, nail and torch | $1.50, 17 min | Opus 5.5: $8.00, 52 min | "Opus took 3x longer and cost 5x more"; prefers Kimi's result |
| [@sakatayasha][castle] | Castle floating above clouds, real-time Three.js | 44 min | Opus 5.5: 35 min | "Opus is still unbeatable, it was faster and better ui" — but "impressive how close open models have gotten" |
| [@sakatayasha][temple] | Interactive Egyptian temple at dawn | 41 min | DeepSeek V4.1 Flash: 32 min | Asks viewers which did better |
| [@marcthecreatorr][kingdom] | "The Floating Kingdom" single HTML file, four models | 25 min, ~$3 | Opus: 1h 15m, ~$12 · DeepSeek: 2h, ~$0.9 · Astra: 40m, ~$20.76 | "DeepSeek took 2 hours and still won on value" |
| [@olezhavich][ski] | Snowy floating island with cable car | 41m 37s, $4.16 | DeepSeek: ~1h, $1.92 · Astra: 19m 12s, $8.72 | "Kimi built the coziest one"; DeepSeek densest and cheapest |
| [@slash1sol][galaxy] | Galaxy shooter, six incremental prompts | $0.31, "the one I kept playing" | Astra: $2.55 · Opus: $1.93 | Kimi's build won on playability; Astra never landed spread shot, Opus missed pause and power-ups |
| [@slash1sol][roadster] | Roadster launch animation, six steps | $2, 160K tokens | Opus 5.5: $15, 600K tokens | "The $2 render is the one I kept" |
| [@k1rallik][roadster2] | Same Roadster launch vs Opus | $2, 160K tokens | Opus 5.5: $15, 600K tokens | "The $2 animation looks better. This is embarrassing." |
| [@adxtyahq][pagoda] | Animated voxel pagoda island | 15 min, $5.71 | Opus 5.5: 32 min, $17.13 | "Roughly 2x faster and 3x cheaper for a comparable result" |
| [@vib3coded][airport] | Pixel airport | $0.98 | GPT-6 Astra: $17.61 | "For value, I'm picking Kimi" |
| [@vib3coded][bottle] | Voxel ship in a bottle | $0.21 | GPT-6.1 Sol: $9.81 | Sol has more detail; "Kimi did a damn good job for $0.21" |
| [@daveeyyy_][eyeball] | Soft-body gummy eyeball | 8 min, $0.24 | Astra: 4 min, $1.07 · Opus: 19 min, ~$6.09 | "Opus is the only one that got the whole brief" |
| [@HavisT83099][carousel] | Vintage carousel at dusk | 15 min, $0.41 | Opus: 13 min, ~$2.12 · ChatGPT: 19 min, ~$0.60 | "Kimi did it for 1/5 of the Claude price" |
| [@thehypedotnews][arc] | Arc de Triomphe at sunset | $6.06, fastest build | DeepSeek: $0.78 · GLM-5.3: $7.36 · Qwen 3.8 Max: $8.88 | "Kimi built the best Paris"; DeepSeek 8x cheaper and "almost as good" |
| [@SamgreyAi][pirate] | Pirate ship at sunset | $4.20 | Opus 5.5: $2.30 | "Opus went for spectacle, Kimi went for realism" |
| [@elvar_official][sandworm] | Sandworm, same prompt as GPT-6 Astra | Panels on every ring, working mouth | Astra: "plain grey tubes" | Kimi's carried detail the other missed |
| [@Lummox_eth][train] | Cinematic bullet train, four workflows | $19, 5 min | Astra: $54, 15 min · Blender MCP: $87, 24 min · Claude Code: $131, 38 min | "7x cheaper and 7.6x faster" than Claude Code |
| [@Lummox_eth][temple-jp] | Japanese temple render, four tools | $14, 4 min | Astra: $48, 14 min · Blender MCP: $79, 23 min · Claude Code: $127, 34 min | "9x cheaper and 8.5x faster" than Claude Code |
| [@Lummox_eth][alpine] | Cinematic alpine lake, Blender | $11, 3 min | Astra: $45, 12 min · Blender MCP: $74, 21 min · Claude Code: $115, 30 min | The 10x cost/time gap across workflows |
| [@EnvolDev][eiffel] | Eiffel Tower, four models | 40m 30s, $3.12 | Terra: 5m 33s, $0.44 · Sol: 22m 28s, $1.10 · Muse Spark: free, 17m 01s | Terra "blew me away"; Kimi has "the finest lattice" but is slowest |
| [@marcthecreatorr][supercar] | 3D supercar, four models | 1h 15m, $3.38 | Terra: 5m, $0.26 · Sol: 25m, $1.88 · Sonnet 5.5: 29m, $5.22 | Slowest of the four; "3D coding is the kind of work the model was optimized for" — said of Terra's weakness, not Kimi's |
| [@AskClash][burning] | Procedural burning car, 5-10 s | 23m 50s, 877K tokens, $0.63 | GPT-6.1 Terra: 8m 19s, 1.19M tokens, $0.24 | Watch both |
| [@filicroval][kerr] | Real-time Kerr black hole observatory | "something broken and not polished" | Qwen 3.8 Flash-Next on a local DGX Spark | The local model "mogged" Kimi on this one |
| [@kenonews][underwater] | Underwater research station scene | vs Opus 5.5 | Opus 5.5 | "Kimi K3.1 Pro is not beating the API wrapper allegations… am I doing something wrong?" |
| [@LLMJunky][rocketleague] | Rocket League Bench | "the best open model that I've tested so far" | Opus 5.5 · Astra · Fable 5.1 | "Easily a full generation behind the frontier on 3D modeling — at least on this one single test" |
| [@IFITALEX][polaroid] | Polaroid camera exploded view (zh) | vs DeepSeek V4.1 Flash 1017 | DeepSeek | "Kimi K3.1 Pro got smoked by DeepSeek on this one" — possibly a harness issue |
| [@atomic_chat_hq][spongebob] | SpongeBob task, teams of 5 agents | 26 min | Opus 5.5 team: 2h, "costing much more" | "Kimi K3.1 10x cheaper than Opus 5.5 at Sponge Bob" |
| [@Kaggii_][rounds] | Four scored rounds vs Opus 5.5 | Code 65.7 · Finance 64.4 · 3D 92.7 | Opus: 66.4 · 62.2 · 96.2 | 2:2 on Moonshot's own charts; "Opus is 3 points smarter. You pay 2x for those 3 points" (his index figures are vendor numbers, not AA's) |

Solo runs and quality notes without a cost:

- [@crystalsssup][hand] asked it to pull a robotic hand apart into 2,317 pieces — "You can just build things." [@LuminaBench][heli] got a helicopter with takeoff/land, assembly and exploded views "in under 15 minutes".
- [@chetaslua][oneshot] one-shot a demo website in 15 minutes; [@chetaslua][iphone] spent 1h30m and $12.50 on a Blender-built folding-phone page.
- [@thebuggeddev][tsushima] built a Ghost of Tsushima-style browser game — "5x cheaper than Claude Opus 5.5 and 80% cheaper than GPT-6 Astra".
- [@noisyb0y1][mp] got a working multiplayer browser game in 10 minutes for a claimed $18 (the post's own figures contradict each other — treat the price as approximate).
- [@ItsmeAjayKV][kibitz] hit it on Arena as Kibitz with "a prompt to generate a floating pagoda island, nothing else in prompt" — and liked the extra controls it added on its own.
- [@sakatayasha][brain] built an interactive brain anatomy explorer in 49 minutes — "the first time a model built me something I'd actually send to a student".
- [@yihui_indie][compilation] cut a compilation of 157 Kimi K3.1 works — the launch-week wave this list samples.
- [@_MaxBlade][subs] spent $400 on subscriptions to send 4 prompts, notes "if i just paid via api it would have been $29 total" — a pricing warning for heavy harness use.
- [@ojigineko_tips][img3d] (ja) fed it a single image and got a rotatable 3D model in ~18 minutes on the free plan, with one self-corrected stumble along the way.
- [@xueyu1125][volcano] (zh) answered a critical post with a one-sentence pixel-volcano prompt of their own.

The pattern across both sources: on price K3.1 wins almost every head-to-head where the rival is Opus 5.5, GPT-6 Astra or a Claude Code workflow — usually by 3-10x. On quality the field is split: creators put it level or ahead on voxel/Three.js scenes and playable builds, while Opus keeps edging it on prompt adherence and polish, and cheap fast models (Terra, DeepSeek, Haiku-tier) beat it on price and speed when quality is second priority. Nobody's measured benchmark says it beats Opus — including Moonshot's own charts, which put it 1-3 points behind on the rounds creators quote.

## Rerun before you trust a comparison

Results move a lot with the setup. [@sai0xgen][dragon] flags that a harness temperature bug kept K3.1 from reviewing its own renders in one dragon-flight test; [@IFITALEX][polaroid] suspects the harness, not the model, for a bad exploded view; [@jurlycat][pelican-3d] raises the meta-question — "Do you judge a coding model by its first attempt or how far you can push it?" — since Kimi's pelican needed "enhance it further" follow-ups where Opus one-shot it. Run the prompt yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals] — Artificial Analysis data, snapshot 2026-10-29. K3.1 Pro's rows are on the Intelligence, Speed and Cost boards.
- [Lab Pelican Test][pelican] — same prompt on every model, scored the same way, with the drawings on screen. No K3.1 row yet.
- [All AI video collections on SandBase Lab][collections] — the same list for other models, including [MiniMax M3.1 Flash][minimax-repo] and [Gemini 4 Carbon][carbon-repo].

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-29) and [Pelican Test][pelican] (read 2026-11-01). Creator data: their posts, linked; not independently verified.

[evals]: https://www.sandbase.ai/lab/evals?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[b-intel]: https://www.sandbase.ai/lab/evals/llm-intelligence?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[b-speed]: https://www.sandbase.ai/lab/evals/llm-speed?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[b-cost]: https://www.sandbase.ai/lab/evals/llm-cost?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican-run]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1&utm_content=run
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=moonshotai%2Fkimi-k3.1-pro&utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[minimax-repo]: https://github.com/sandbase-lab/awesome-minimax-m3-1-flash
[carbon-repo]: https://github.com/sandbase-lab/awesome-gemini-4-carbon
[screening]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113688082474221830?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[rocket]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113708763719012400?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[whale]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113727486580449755?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[rocket2]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113699800847929483?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[titanic]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113974830215098859?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[dino]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114438106254299320?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[subway]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114294888523026501?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[jelly]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114059647233495351?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[castle]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113581118339662139?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[temple]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114330266986799169?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[kingdom]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114074078340649183?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[ski]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2116143918890758198?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[galaxy]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113995388189286653?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[roadster]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114333062506930187?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[roadster2]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113716424887661034?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pagoda]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113687234448875770?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[airport]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113849897438834851?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[bottle]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113716730057150479?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[eyeball]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114014158102397168?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[carousel]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114491459206262930?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[arc]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113758485758328945?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pirate]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114821160235885004?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[sandworm]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114325660248281265?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[train]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2116476226894270738?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[temple-jp]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2115460315131400414?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[alpine]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2115164427657904336?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[eiffel]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114811718320996843?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[supercar]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2115444940448702704?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[burning]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2115264932308775115?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[kerr]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114402157872939277?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[underwater]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114313469029748874?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[rocketleague]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113707413006143727?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[polaroid]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113989179382350015?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[spongebob]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113700709506113948?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[rounds]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114371152151781524?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[hand]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113684128734625948?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[heli]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113186973363929470?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[oneshot]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113552063636578445?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[iphone]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113694080014356760?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[tsushima]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113694356939112498?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[mp]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113716426708291882?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[kibitz]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113297716667371646?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[brain]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114705736903307703?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[compilation]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113930055806230636?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[subs]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113750412507406751?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[img3d]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113933579747209626?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[volcano]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114750666736644321?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[dragon]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114571732938080761?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican-1]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113611006039761281?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican-2]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113749533410955458?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican-svg]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113299432485843308?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[stacked]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113297542372798938?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican-3d]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113895768998531583?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
