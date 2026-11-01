# Kimi K3.1 prompt guide: how to prompt K3.1 for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

Kimi K3.1 doesn't output video. It writes code — an HTML page with Three.js, Canvas or SVG, a Blender scene, a playable game — and the creator records the result. Many of the pieces here came out of the Kimi web app's own "3D Make" flow or an agent harness, but the strongest one-shot results all follow the same prompt shapes. The patterns below come from prompts creators posted with their videos. Each example links to the video it produced.

One thing that shapes every prompt: thinking is always on for this model, with reasoning effort `low`, `high` or `max` (`max` is the default — [`sandbase inspect`](https://www.sandbase.ai/model/moonshotai/kimi-k3.1-pro?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1)). It spends tokens before it writes, and those tokens come out of your `max_tokens`.

## 1. Name one self-contained HTML file

The single most repeated line in this collection is some form of "as a single HTML file". It is what makes a video recordable at all:

- "build 'The Floating Kingdom' as a single HTML file" — the same four words to Opus 5.5, DeepSeek V4.1 Flash, GPT-6 Astra and Kimi K3.1 Pro ([@marcthecreatorr][kingdom]).
- "Build 'Lantern Hour' in a single HTML file: 4 art styles, a full day/night cycle, dynamic lighting and shadows, and interactive controls. Canvas 2D only. No libraries or external assets." ([@adolandev][lantern])
- "a 12-step Rube Goldberg machine in a single HTML file, running in exactly 30 seconds" ([@adolandev][rube]) — the time limit is part of the brief.

## 2. Say the renderer, not just "3D"

K3.1 picks whichever stack you name, and each one fails differently:

- **Three.js** is the default here: "build a 3D cycle riding a cow using three.js" ([@TimJayas][cow]), "build a 3D BMW M5 using Three.js — full configurator with colors, doors and lights, camera views and a live rev mode" ([@k2sbhai][bmw]). Creators often pin the version: "recreate Central Park on an autumn morning in Three.js 0.170, pure code, no imported 3D models or textures" ([@yuhasbeentaken][central-park]).
- **Canvas 2D** when you want no libraries at all (the Lantern Hour prompt above explicitly bans them).
- **SVG** for small, cleanly recording drawings: the arena-era Kibitz was asked to "用 SVG 代码画一只骑自行车的鹈鹕，细节越丰富越好" ("draw a pelican riding a bicycle in SVG, the more detail the better") ([@AndyL5cc][pelican-svg]).
- **Blender** is a separate track: creators drive it through the Kimi app or an MCP harness for renders like the alpine lake ([@Lummox_eth][alpine]) and Changi Airport ([@crystalsssup][changi]).

## 3. The benchmark prompt: "X riding a bicycle"

The single most common prompt in this collection is a riding test — the community benchmark that asks the model for something absurd and judges the result:

- "Pelican Riding a Bicycle" ([@abhinavflac][pelican]) — run against Qwen 4 in the same post.
- "controller riding bycicle riding pelican riding bycicle riding pelican" — the stacked version K3.1 got while it was still codenamed Kibitz ([@dummerspast39][stacked]).
- "an infinite zoom of a pelican riding a bicycle, pure JavaScript" — same prompt to three models at high reasoning effort ([@techfren][zoom]).

It works as a benchmark because everyone uses the same words, the task is unfinishable-but-gradable, and the result compresses rendering, anatomy and animation into one frame. If you want a fair comparison with another model, this is the prompt to copy.

## 4. Voxel and pixel-art scenes

K3.1's signature output is the voxel world — dense, floating-island scenes that read well at 400 px:

- "3D voxel cherry blossom valley" ([@abhinavflac][cherry]) — eight words, no more.
- "Living Voxel Koi Valley" ([@abhinavflac][koi-valley]).
- A voxel pagoda island with "intricate pagoda architecture, bridges and floating islands, detailed trees and tiny environmental elements" — where the detail list is doing the work ([@adxtyahq][pagoda]).
- "用three.js做一个可以喷发的像素火山" ("a pixel volcano that can erupt, in Three.js") ([@xueyu1125][volcano]) — the prompt is one sentence; the result is a timed eruption.

The pattern: a place name + a voxel/pixel style word + one or two density cues. Short prompts give you the model's choices, not yours — when it matters, write the numbers down (see §6).

## 5. A browser game, one system per prompt

The game posts that look playable were not asked for all at once. [@slash1sol][galaxy] wrote the recipe in public — "one rule for all three: never ask for 'a space shooter'. One system per prompt, play it, then the next":

1. A canvas, a starfield, a ship that moves on arrows and touch. No enemies yet.
2. Auto fire and one enemy type that dives. Play it until the dodge feels right.
3. Waves, each one tighter, with a "WAVE 2" banner.
4. Power-ups dropped from kills.
5. Score, best score, lives, a pause key, a game-over screen that restarts.
6. Each model reviews its own build and fixes what it finds.

The same piecewise rule produced the Roadster launch — six steps from empty pad to lift-off, "$2 of it was Kimi K3.1 Pro, $15 was Opus 5.5" ([@slash1sol][roadster]). One-shot games do exist — "Build a Frogger style arcade game in a single self-contained HTML file" ([@ivanfioravanti][frogger]), "build a full minecraft game in the browser" ([@starmexxx][minecraft]) — but the iterated ones are the ones people keep playing.

## 6. Put the controls and the state in the prompt

If the point is a video, say what has to be moving when the camera rolls — and which controls should exist when it stops:

- "a full interactive Three.js Egyptian temple complex at dawn: sand dunes, dig and brush tools, day and night cycle, burial chamber puzzle, weather, torch, photo mode" ([@sakatayasha][temple]).
- "an interactive soft-body gummy eyeball in Three.js. Poke it, stretch it, throw it, swing it by the nerve" ([@daveeyyy_][eyeball]).
- "build a 3D adult brain, click to isolate cards, assembled, exploded, mid sagittal cut, labels, and auto rotate" ([@sakatayasha][brain]).
- A floating pagoda island with no brief at all still produced "time of day control, render quality toggle + few more" on Arena ([@ItsmeAjayKV][pagoda-island]) — but you can't count on that.

For a recording, ask for an autoplay camera move or a loop of known length, so nothing depends on a mouse — the same advice as the [tutorial](tutorial.md#4-turn-the-page-into-a-video).

## 7. Run it against another model

Half this collection is a prompt plus a rival. The shape that makes a comparison fair:

- The exact same prompt to both models, one shot each — "Opus 5.5 vs Kimi K3.1, tested on the same prompt: a full real-time Three.js scene of a castle floating above the clouds" ([@sakatayasha][castle]); "Same prompt: sink the Titanic" ([@noclipepe][titanic]).
- Publish both numbers: "Kimi K3.1 → 35m 05s · 1.98M tokens · ~$0.88; Opus 5.5 → 28m 55s · 9.02M tokens · ~$8.43" ([@noclipepe][titanic]).
- Say what each model got wrong: "a temperature bug prevented Kimi from reviewing its own screenshots, so the comparison isn't entirely fair" ([@sai0xgen][dragon]).

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Look: [style, e.g. voxel / low-poly / cinematic PBR / neon], [mood, lighting, palette].
Motion: [what moves and how]. Autoplay a [10]-second camera tour on load, then loop.
Interaction: [drag = …, scroll = …, click = …, keys = …, toggles = …].
Rules: [the numbers it must respect: rooms, lives, waves, gear ratios, collisions].

Technical:
- Use Three.js [version] as an ES module from a CDN import map. No other libraries.
- No external images, fonts, models or audio: generate geometry and textures in code.
- Fill the viewport, no scrolling, 30+ fps at 1280x720.
- Before you finish, check that the page loads with zero console errors and that every control works.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it on the [Lab text arena][arena] to run it on K3.1 and other models side by side, or with the API in the [tutorial](tutorial.md).

## Settings

- **Output budget.** Thinking is always on (`low`, `high` or `max`, default `max`), and the hidden reasoning tokens count toward `max_tokens` and bill as output. Creator-reported builds through the Kimi harness ran to hundreds of thousands of tokens — 877K for a burning car ([@AskClash][burning-car]), 1.98M for the Titanic ([@noclipepe][titanic]). The SandBase API caps `max_tokens` at 131,072; ask for the cap so the page is not truncated mid-file.
- **Reasoning effort.** `low`, `high` or `max`. [@SPAC89][kibitz] guessed the Arena Kibitz was "using its highest reasoning setting by default" — and the default on SandBase is indeed `max`. Drop to `high` or `low` when latency matters more than polish.
- **One shot vs. the harness.** Arena-era posts were one shot inside the Kimi app. The bigger pieces — the folding-phone page, the multiplayer game, the cinematic train — were harness runs where the model also produced assets. Same model, different loop, different bill.

---

Quotes are short excerpts credited to their authors; follow the links for full prompts and videos. Translations from Chinese and Japanese are ours.

[kingdom]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114074078340649183?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[lantern]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113711071668142142?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[rube]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113869535338000625?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[cow]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113277551980482975?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[bmw]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113283390548164986?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[central-park]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113717949811032357?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican-svg]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113299432485843308?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[alpine]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2115164427657904336?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[changi]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113698280991580577?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pelican]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113218148837257546?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[stacked]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113297542372798938?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[zoom]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2115313771568648585?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[cherry]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113285539998872040?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[koi-valley]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113657922404466862?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pagoda]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113687234448875770?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[volcano]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114750666736644321?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[galaxy]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113995388189286653?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[roadster]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114333062506930187?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[frogger]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113698617353527664?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[minecraft]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113722581610033330?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[temple]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114330266986799169?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[eyeball]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114014158102397168?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[brain]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114705736903307703?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[pagoda-island]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113297716667371646?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[castle]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113581118339662139?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[titanic]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113974830215098859?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[dragon]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2114571732938080761?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[burning-car]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2115264932308775115?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[kibitz]: https://www.sandbase.ai/lab/ai-videos/kimi-k3-1/2113136432936083808?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=moonshotai%2Fkimi-k3.1-pro&utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1
