# Kimi K3.1 提示词写法：如何为视频提示 K3.1

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

Kimi K3.1 不直接输出视频。它写代码——用 Three.js、Canvas 或 SVG 的 HTML 页面、一个 Blender 场景、一个可玩的游戏——作者再把结果录下来。这里的很多作品出自 Kimi 网页版自带的 "3D Make" 流程或 agent harness，但效果最好的一次生成作品都遵循同一批提示词形状。下面的写法来自作者随视频公开的提示词，每条都链接到它产出的视频。

有一点会影响所有提示词：这个模型的思考始终开启，推理强度可选 `low`、`high`、`max`（默认 `max`——[`sandbase inspect`](https://www.sandbase.ai/model/moonshotai/kimi-k3.1-pro?utm_source=github&utm_medium=docs&utm_campaign=awesome-kimi-k3-1)）。它先花 token 思考再动笔，这些 token 也算在你的 `max_tokens` 里。

## 1. 点名一个独立的 HTML 文件

这个合集里被重复最多的一句话，就是某种形式的"做成一个 HTML 文件"。它是一段成果能不能被录下来的前提：

- "build 'The Floating Kingdom' as a single HTML file"（把"漂浮王国"做成一个 HTML 文件）——同一句话同时发给了 Opus 5.5、DeepSeek V4.1 Flash、GPT-6 Astra 和 Kimi K3.1 Pro（[@marcthecreatorr][kingdom]）。
- "Build 'Lantern Hour' in a single HTML file: 4 art styles, a full day/night cycle, dynamic lighting and shadows, and interactive controls. Canvas 2D only. No libraries or external assets."（把"灯笼时刻"做成一个 HTML 文件：4 种画风、完整昼夜循环、动态光影和交互控件。只用 Canvas 2D，不要库和外部资源。）（[@adolandev][lantern]）
- "a 12-step Rube Goldberg machine in a single HTML file, running in exactly 30 seconds"（一个 12 步的鲁布·戈德堡机械，单个 HTML 文件，恰好运行 30 秒）（[@adolandev][rube]）——时限也是需求的一部分。

## 2. 指明渲染方式，别只说"3D"

K3.1 会照你点的那一种做，而每种技术栈失败的方式不同：

- **Three.js** 是这里的默认："build a 3d cycle riding a cow using three.js"（用 Three.js 做一头骑自行车的牛）（[@TimJayas][cow]）；"build a 3D BMW M5 using Three.js — full configurator with colors, doors and lights, camera views and a live rev mode"（用 Three.js 做一辆宝马 M5：完整配置器，含颜色、车门、灯光、机位和实时轰油门模式）（[@k2sbhai][bmw]）。作者常会锁版本："recreate Central Park on an autumn morning in Three.js 0.170, pure code, no imported 3D models or textures"（用 Three.js 0.170 还原秋日清晨的中央公园，纯代码，不导入 3D 模型或贴图）（[@yuhasbeentaken][central-park]）。
- **Canvas 2D** 适合完全不依赖库的场景（上面那条 Lantern Hour 提示词明确禁止了所有库）。
- **SVG** 适合文件小、录制干净的画：竞技场时代的 Kibitz 被要求"用 SVG 代码画一只骑自行车的鹈鹕，细节越丰富越好"（[@AndyL5cc][pelican-svg]）。
- **Blender** 是另一条路线：作者通过 Kimi 应用或 MCP harness 驱动它，产出高山湖泊（[@Lummox_eth][alpine]）和樟宜机场（[@crystalsssup][changi]）这类渲染。

## 3. 基准提示词："X 骑自行车"

这个合集里最常出现的提示词是一组骑行测试——社区用来考验模型的荒诞任务，然后给结果打分：

- "Pelican Riding a Bicycle"（骑自行车的鹈鹕）（[@abhinavflac][pelican]）——同一篇帖子里还跑了 Qwen 4。
- "controller riding bycicle riding pelican riding bycicle riding pelican"（手柄骑着自行车骑着鹈鹕骑着自行车骑着鹈鹕）——K3.1 还叫 Kibitz 时接到的套娃版（[@dummerspast39][stacked]）。
- "an infinite zoom of a pelican riding a bicycle, pure JavaScript"（鹈鹕骑自行车的无限缩放，纯 JavaScript）——同一提示词发给三个模型、都开高推理强度（[@techfren][zoom]）。

它能当基准，是因为大家用同一句话、任务不可能完美却容易打分，而且一帧画面就能同时考验渲染、解剖和动画。想跟别的模型公平对比，这就是该抄的提示词。

## 4. 体素与像素场景

K3.1 最有辨识度的产出是体素世界——密集的浮岛场景，缩到 400 px 也好看：

- "3D voxel cherry blossom valley"（3D 体素樱花谷）（[@abhinavflac][cherry]）——八个词，没了。
- "Living Voxel Koi Valley"（活的体素锦鲤谷）（[@abhinavflac][koi-valley]）。
- 体素宝塔岛："intricate pagoda architecture, bridges and floating islands, detailed trees and tiny environmental elements"（精致的宝塔建筑、桥梁和浮岛，细密的树木和微小环境元素）——干活的是这串细节清单（[@adxtyahq][pagoda]）。
- "用three.js做一个可以喷发的像素火山"（[@xueyu1125][volcano]）——提示词一句话，结果是一座定时喷发的火山。

规律：地名 + 体素/像素风格词 + 一两个密度提示。短提示词得到的是模型的选择，不是你的——在意的地方就把数字写下来（见 §6）。

## 5. 浏览器游戏：一次只加一个系统

看起来真能玩的游戏，都不是一口气要出来的。[@slash1sol][galaxy] 公开过配方——"one rule for all three: never ask for 'a space shooter'. One system per prompt, play it, then the next"（三个模型都守同一条规矩：永远不要直接要"一个太空射击游戏"。一次提示词加一个系统，玩一玩，再加下一个）：

1. 一块画布、一片星空、一艘用方向键和触摸移动的飞船。先不要敌人。
2. 自动开火和一种俯冲敌机。玩到闪躲手感对了为止。
3. 波次，一波比一波密，挂出 "WAVE 2" 横幅。
4. 击杀掉落的强化道具。
5. 分数、最高分、命数、暂停键、按空格重新开始的游戏结束画面。
6. 让每个模型检查自己的作品并修复发现的问题。

同样的分步法则产出了 Roadster 发射动画——从空发射台到点火升空共六步，"其中 $2 花给了 Kimi K3.1 Pro，$15 花给了 Opus 5.5"（[@slash1sol][roadster]）。一次成型的游戏确实存在——"Build a Frogger style arcade game in a single self-contained HTML file"（做一个青蛙过河风格的街机游戏，单个自包含 HTML 文件）（[@ivanfioravanti][frogger]）、"build a full minecraft game in the browser"（在浏览器里做一个完整的 Minecraft）（[@starmexxx][minecraft]）——但让人反复玩的都是迭代出来的。

## 6. 把交互和状态写进提示词

如果目标是一段视频，就写清镜头在跑的时候什么东西应该在动——以及停下之后应该有哪些控件：

- "a full interactive Three.js Egyptian temple complex at dawn: sand dunes, dig and brush tools, day and night cycle, burial chamber puzzle, weather, torch, photo mode"（黎明时分的完整可交互 Three.js 埃及神庙群：沙丘、挖掘和毛刷工具、昼夜循环、墓室谜题、天气、火把、拍照模式）（[@sakatayasha][temple]）。
- "an interactive soft-body gummy eyeball in Three.js. Poke it, stretch it, throw it, swing it by the nerve"（Three.js 可交互软糖眼球：戳它、拉它、扔它、拎着视神经晃）（[@daveeyyy_][eyeball]）。
- "build a 3D adult brain, click to isolate cards, assembled, exploded, mid sagittal cut, labels, and auto rotate"（做一个 3D 成人大脑：点击分离部件卡片，有组装、爆炸、正中矢状切面视图，带标签，自动旋转）（[@sakatayasha][brain]）。
- 一座毫无要求的浮空宝塔岛在 Arena 上照样产出了"时间控制、画质开关等好几个控件"（[@ItsmeAjayKV][pagoda-island]）——但别指望每次都有。

要录屏，就在提示词里要求自动镜头运动或定长循环，让整个画面不依赖鼠标——和[教程](tutorial.md#4-把页面录成视频)里的建议一样。

## 7. 拉一个对手一起跑

这个合集一半是提示词加对手。公平的对比长这样：

- 把一模一样的提示词发给两个模型，各跑一次——"Opus 5.5 vs Kimi K3.1, tested on the same prompt: a full real-time Three.js scene of a castle floating above the clouds"（同一提示词：云端漂浮城堡的完整实时 Three.js 场景）（[@sakatayasha][castle]）；"Same prompt: sink the Titanic"（同一提示词：让泰坦尼克号沉没）（[@noclipepe][titanic]）。
- 两边的数字都公布："Kimi K3.1 → 35 分 05 秒 · 198 万 token · 约 $0.88；Opus 5.5 → 28 分 55 秒 · 902 万 token · 约 $8.43"（[@noclipepe][titanic]）。
- 写清每个模型哪里出了问题："a temperature bug prevented Kimi from reviewing its own screenshots, so the comparison isn't entirely fair"（一个温度参数 bug 让 Kimi 看不到自己的截图，所以这个对比并不完全公平）（[@sai0xgen][dragon]）。

## 可以直接用的提示词

```text
把 [主题] 做成一个从磁盘直接打开就能跑的独立 HTML 文件。

画面：[风格，例如 体素 / low-poly / 电影感 PBR / 霓虹]，[氛围、光照、配色]。
运动：[什么在动、怎么动]。加载后自动播放 [10] 秒的镜头巡游，然后循环。
交互：[拖拽 = …，滚轮 = …，点击 = …，按键 = …，开关 = …]。
规则：[必须遵守的数字：房间数、生命、波次、齿轮比、碰撞]。

技术：
- 用 CDN import map 以 ES module 引入 Three.js [版本]，不要其他库。
- 不要外部图片、字体、模型、音频：几何体和贴图全部用代码生成。
- 铺满视口、不出现滚动条、1280x720 下 30 fps 以上。
- 完成前自检：页面加载零 console 错误，每个操作都可用。
- 只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要省略。
```

可以到 [Lab 文本竞技场][arena] 里，把这段同时跑在 K3.1 和其他模型上对比；用 API 的方式见[教程](tutorial.md)。

## 参数设置

- **输出预算。** 思考始终开启（`low`、`high` 或 `max`，默认 `max`），隐藏的推理 token 计入 `max_tokens` 并按输出计费。创作者在 Kimi harness 里报告的构建动辄几十万 token——一辆燃烧的车用了 87.7 万（[@AskClash][burning-car]），泰坦尼克号用了 198 万（[@noclipepe][titanic]）。SandBase API 的 `max_tokens` 上限是 131072，直接给满，别让页面写到一半被截断。
- **推理强度。** 可选 `low`、`high`、`max`。[@SPAC89][kibitz] 当时猜 Arena 上的 Kibitz"默认用了最高推理档位"——而 SandBase 上的默认值确实是 `max`。在意延迟多过打磨时，降到 `high` 或 `low`。
- **一次生成 vs. harness。** Arena 时代的作品大多是 Kimi 应用里的一次生成。更大的作品——折叠手机页面、多人联机游戏、电影感列车——都是连素材一起产出的 harness 运行。同一个模型，不同的循环，不同的账单。

---

引文均为短摘录并注明作者，完整提示词和视频请点链接。中文、日文、西班牙文原文的翻译为我们所做。

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
