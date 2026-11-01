# Kimi K3.1 对比 Claude Opus 5.5、GPT-6 Astra 和 DeepSeek V4.1 Flash

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 的数据；Lab [Pelican Test][pelican] 用同一份固定提示词跑每个模型并给结果打分。样本不大，但所有人的条件一致。
2. **创作者报告的。** 发在 X 上的同提示词对比，附他们自己的花费和耗时。有参考价值，但我们没有验证。

K3.1 于 2026 年 10 月下旬发布——本合集最早的视频是在它仍以代号 **Kibitz** 隐身出现在 Arena 时做的，全部视频都发布在首次被发现后的约十天内。这决定了怎么读这些数字：实测一侧只有一个快照的厚度，创作者一侧很厚，因为一个神秘的前沿级模型正是所有人都会拿去跑同一套测试的对象。

## 我们测到的：Lab Evals 榜单

Kimi K3.1 Pro **已经上榜**——一行，没有分推理档位。榜单读取的是 2026-10-29 的 Artificial Analysis 快照（智能指数版本 v5，716 个模型），它在本合集最常拿来对比的模型中落在这些位置：

| 模型（榜单上的行） | [智能指数][b-intel] | [输出速度][b-speed] | [单任务成本][b-cost] |
|---|---|---|---|
| Gemini 4 Carbon (High) | 59.4（78 中第 1） | 102 tok/s（373 中第 172） | $7.76（73 中第 67） |
| Claude Opus 5.5 (Max) | 58.4（第 2） | 98 tok/s（第 182） | $10.04（第 71） |
| GPT-6 Astra (Max) | 56.9（第 4） | 76 tok/s（第 245） | $6.24（第 61） |
| GPT-6.1 Sol (Max) | 54.5（第 7） | 81 tok/s（第 231） | $1.27（第 34） |
| **Kimi K3.1 Pro** | **46.0（第 22）** | **37 tok/s（第 353）** | **$3.68（第 53）** |
| Claude Haiku 5.5 (Max) | 36.2（第 32） | 241 tok/s（第 21） | $0.41（第 23） |
| DeepSeek V4.1 Flash 1017 (Max) | 32.5（第 39） | 182 tok/s（第 57） | $0.60（第 28） |
| GLM-5.3 (Max) | 31.7（第 40） | 80 tok/s（第 237） | $5.01（第 56） |

这说明什么、不说明什么：

- **K3.1 Pro 落在廉价快模型和前沿模型之间。** 46.0 分明显高于 DeepSeek V4.1 Flash 1017（32.5）、GLM-5.3（31.7）和 Claude Haiku 5.5（36.2），明显低于 Opus 5.5 Max（58.4）、GPT-6 Astra Max（56.9）和 GPT-6.1 Sol Max（54.5）。创作者反复报告的"Kimi 对 Opus"结果——质量接近、便宜得多——与一个落后榜首约 12 分的模型相符，而不是一个并列的模型。
- **它的单任务成本落在榜中部，不在底部。** $3.68 约为 Opus Max $10.04 的三分之一，不到 Astra Max $6.24 的一半——但绝对值并不便宜：DeepSeek V4.1 Flash 跑同一套评测只要 $0.60，Haiku 5.5 只要 $0.41。创作者晒出的省钱是真实的，只因为对手通常是 Opus 或 Astra。
- **它很慢。** 37 tok/s 排在速度榜接近底部（373 中第 353），比上一代 K3（55 tok/s）还低，远低于 flash 档模型。创作者帖子里 20 到 45 分钟的构建时间，就是这个数字在现实中的样子。
- **还没有编码或智能体行。** Artificial Analysis 尚未发布 K3.1 Pro 的编码或智能体指数（那两个榜单上没有它的行），所以下文每一条"它编码比 X 强"都只是创作者自己的运行。

## 我们测到的：Lab Pelican Test

[Pelican Test][pelican] 让每个模型画一只骑自行车的鹈鹕，一次静态、一次动画（轮子转、腿蹬踏板，只用 CSS/SMIL），渲染成 PNG 后由一个 LLM 裁判按 0–5 分打分。

**榜单上还没有 Kimi K3.1 Pro 这一行**（2026-11-01 读取：22 个模型、146 条结果）。最接近的行是上一代——`moonshotai/kimi-k3`，3.21 分、第 10、每张 $0.089——以及本合集常拿来对比的模型：`anthropic/claude-opus-5.5` 3.46（第 4）、`google/gemini-4-argon` 3.81（第 1）、`openai/gpt-6-astra` 3.08（第 11）、`deepseek/deepseek-v4.1-flash` 3.44（第 5，$0.017）。[自己跑一次][pelican-run]，这个页面缺的数字就补上了。

社区自己早就跑过同类测试——"鹈鹕骑自行车"是本合集里做得最多的题目之一（[@chetaslua][pelican-1]、[@ChrisGPT][pelican-2]、[@AndyL5cc][pelican-svg]），还包括 K3.1 仍叫 Kibitz 时接到的套娃变体（[@dummerspast39][stacked]）。

## 创作者报告的

发在 X 上的同提示词对比。数字按创作者自述：工具不同（Kimi 应用及其 "3D Make" 流程、Claude Code、OpenCode、Blender MCP、裸 API），推理强度不同，订阅套餐的价格不直接可比，往往只跑一次。点进链接可以两边一起看。Claude Opus 5.5 是这里最常见的对手——本合集由 Kimi 对 Opus 的帖子主导。

| 创作者 | 任务 | Kimi K3.1 | 对手 | 创作者结论 |
|---|---|---|---|---|
| [@AI_Screening][screening] | 单文件 Three.js 测试，三个模型 | "完胜 Astra" | Opus 5.5 · GPT-6 Astra | "Kimi 横空出世，现在已经能和前沿模型同场竞技" |
| [@marcusyul][rocket] | 火箭发射场景 | $0.33 | GPT-6.1 Sol $1.15 · Opus 5.5 $2.06 · GPT-6 Astra $2.73 | 比 Opus 便宜约 6 倍、比 Astra 便宜约 8 倍；四家都让火箭飞起来了 |
| [@Bhavani_00007][whale] | 鲸鱼跃出海面场景 | $0.75 | Opus 5.5 $3.01 · Astra $2.00 · Gemini 4 Argon $2.30 | "质量相当，价格只有零头" |
| [@Bhavani_00007][rocket2] | 火箭场景，质量评判 | $1.95，6 分钟 | Opus 5.5 $10.35，24 分钟 | "在这次测试里它的产出质量、成本和速度全面胜过 Opus 5.5" |
| [@noclipepe][titanic] | 让泰坦尼克号沉没 | 35 分 05 秒，198 万 token，约 $0.88 | Opus 5.5：28 分 55 秒，902 万 token，约 $8.43 | "Opus 沉得更好，但 Kimi 用不到一块钱追得吓人地近" |
| [@noclipepe][dino] | 带布娃娃物理的 Chrome 小恐龙 | 19 分 18 秒，$1.25 | Opus 5.5：38 分 55 秒，$8.53 · Gemini 4 Argon：4 分 34 秒，$0.19 | "Opus 赢了，Argon 便宜 45 倍" |
| [@noclipepe][subway] | 地铁跑酷式鹈鹕游戏 | 10 分 01 秒，$0.95 | GPT-6 Astra：19 分 52 秒，$6.53 | "Astra 花 $6.53 做漂亮，Kimi 花不到一块钱做好玩" |
| [@0xRhinoX][jelly] | 可以切、钉、烧的彩虹果冻 | $1.50，17 分钟 | Opus 5.5：$8.00，52 分钟 | "Opus 慢了 3 倍、贵了 5 倍"；更喜欢 Kimi 的结果 |
| [@sakatayasha][castle] | 云端漂浮城堡，实时 Three.js | 44 分钟 | Opus 5.5：35 分钟 | "Opus 仍然无敌，更快、UI 更好"——但"开源模型追到这个程度已经惊人" |
| [@sakatayasha][temple] | 黎明的可交互埃及神庙群 | 41 分钟 | DeepSeek V4.1 Flash：32 分钟 | 问观众哪个更好 |
| [@marcthecreatorr][kingdom] | "漂浮王国"单文件 HTML，四模型 | 25 分钟，约 $3 | Opus：1 小时 15 分，约 $12 · DeepSeek：2 小时，约 $0.9 · Astra：40 分钟，约 $20.76 | "DeepSeek 跑了 2 小时，性价比还是它赢" |
| [@olezhavich][ski] | 带缆车的雪场浮岛 | 41 分 37 秒，$4.16 | DeepSeek：约 1 小时，$1.92 · Astra：19 分 12 秒，$8.72 | "Kimi 造了最舒服的一座"；DeepSeek 最密也最便宜 |
| [@slash1sol][galaxy] | 太空射击游戏，六步增量提示 | $0.31，"我一直玩下去的那个" | Astra：$2.55 · Opus：$1.93 | Kimi 版胜在可玩性；Astra 的散射道具没做出来，Opus 缺暂停和道具 |
| [@slash1sol][roadster] | Roadster 发射动画，六步 | $2，16 万 token | Opus 5.5：$15，60 万 token | "我留下的是那个 $2 的渲染" |
| [@k1rallik][roadster2] | 同一个 Roadster 发射对 Opus | $2，16 万 token | Opus 5.5：$15，60 万 token | "$2 的动画反而更好看，这就尴尬了" |
| [@adxtyahq][pagoda] | 体素宝塔岛动画 | 15 分钟，$5.71 | Opus 5.5：32 分钟，$17.13 | "质量相当的前提下快约 2 倍、便宜约 3 倍" |
| [@vib3coded][airport] | 像素机场 | $0.98 | GPT-6 Astra：$17.61 | "看性价比我选 Kimi" |
| [@vib3coded][bottle] | 体素瓶中信 | $0.21 | GPT-6.1 Sol：$9.81 | Sol 细节更多；"Kimi 用 $0.21 做得够好了" |
| [@daveeyyy_][eyeball] | 软糖眼球软体交互 | 8 分钟，$0.24 | Astra：4 分钟，$1.07 · Opus：19 分钟，约 $6.09 | "只有 Opus 把完整需求做出来了" |
| [@HavisT83099][carousel] | 黄昏的复古旋转木马 | 15 分钟，$0.41 | Opus：13 分钟，约 $2.12 · ChatGPT：19 分钟，约 $0.60 | "Kimi 只花了 Claude 五分之一的钱" |
| [@thehypedotnews][arc] | 日落凯旋门 | $6.06，最快完成 | DeepSeek：$0.78 · GLM-5.3：$7.36 · Qwen 3.8 Max：$8.88 | "Kimi 造出了最好的巴黎"；DeepSeek 便宜 8 倍且"几乎一样好" |
| [@SamgreyAi][pirate] | 日落海盗船 | $4.20 | Opus 5.5：$2.30 | "Opus 追求炫目，Kimi 追求写实" |
| [@elvar_official][sandworm] | 沙虫，与 GPT-6 Astra 同题 | 每一节都带装甲板、嘴能开合 | Astra："灰管子堆叠" | Kimi 保留了对方丢失的细节 |
| [@Lummox_eth][train] | 电影感子弹列车，四种工作流 | $19，5 分钟 | Astra：$54，15 分钟 · Blender MCP：$87，24 分钟 · Claude Code：$131，38 分钟 | 比 Claude Code "便宜 7 倍、快 7.6 倍" |
| [@Lummox_eth][temple-jp] | 日式寺庙渲染，四种工具 | $14，4 分钟 | Astra：$48，14 分钟 · Blender MCP：$79，23 分钟 · Claude Code：$127，34 分钟 | 比 Claude Code "便宜 9 倍、快 8.5 倍" |
| [@Lummox_eth][alpine] | 电影感高山湖泊，Blender | $11，3 分钟 | Astra：$45，12 分钟 · Blender MCP：$74，21 分钟 · Claude Code：$115，30 分钟 | 四种工作流之间近 10 倍的成本和时间差 |
| [@EnvolDev][eiffel] | 埃菲尔铁塔，四模型 | 40 分 30 秒，$3.12 | Terra：5 分 33 秒，$0.44 · Sol：22 分 28 秒，$1.10 · Muse Spark：免费，17 分 01 秒 | Terra "把我惊到了"；Kimi 的"网格塔身最细"但最慢 |
| [@marcthecreatorr][supercar] | 3D 超跑，四模型 | 1 小时 15 分，$3.38 | Terra：5 分钟，$0.26 · Sol：25 分钟，$1.88 · Sonnet 5.5：29 分钟，$5.22 | 四个里最慢；"3D 编码不是这个模型优化的方向"——说的是 Terra 的短板，不是 Kimi |
| [@AskClash][burning] | 程序化燃烧汽车，5–10 秒 | 23 分 50 秒，87.7 万 token，$0.63 | GPT-6.1 Terra：8 分 19 秒，119 万 token，$0.24 | 两个结果都放上来了 |
| [@filicroval][kerr] | 实时克尔黑洞观测站 | "做出来的是坏的，没打磨" | 本地 DGX Spark 上的 Qwen 3.8 Flash-Next | 这一局本地模型碾压了 Kimi |
| [@kenonews][underwater] | 水下科考站场景 | 对 Opus 5.5 | Opus 5.5 | "Kimi K3.1 Pro 这是摆脱不了 API 套壳的嫌疑了……还是我用法不对？" |
| [@LLMJunky][rocketleague] | Rocket League Bench | "我测过最强的开放模型" | Opus 5.5 · Astra · Fable 5.1 | "在 3D 建模上明显落后前沿整整一代——至少在这一个测试上" |
| [@IFITALEX][polaroid] | 宝丽来相机解构版（中文） | 对 DeepSeek V4.1 Flash 1017 | DeepSeek | "Kimi K3.1 Pro 这局被 DeepSeek 完爆"——可能是 harness 的问题 |
| [@atomic_chat_hq][spongebob] | 海绵宝宝任务，各 5 个 agent 组队 | 26 分钟 | Opus 5.5 队：2 小时，"花费高得多" | "Kimi K3.1 在海绵宝宝上比 Opus 5.5 便宜 10 倍" |
| [@Kaggii_][rounds] | 对 Opus 5.5 的四轮记分对比 | 编码 65.7 · 金融 64.4 · 3D 92.7 | Opus：66.4 · 62.2 · 96.2 | 按 Moonshot 自己的图表打成 2:2；"Opus 聪明 3 分，你为这 3 分付 2 倍"（他引的指数是厂商数字，不是 AA 的） |

没有成本数字的单项运行与质量评价：

- [@crystalsssup][hand] 让它把一只机械手拆成 2,317 个零件——"你真的可以想到什么就做什么"。[@LuminaBench][heli] 15 分钟内拿到了带起降、组装和爆炸图的直升机。
- [@chetaslua][oneshot] 15 分钟一次生成了一个演示网站；[@chetaslua][iphone] 花 1 小时 30 分和 $12.50 做了一个 Blender 搭出来的折叠手机页面。
- [@thebuggeddev][tsushima] 做了一个对马岛之魂风格的浏览器游戏——"比 Claude Opus 5.5 便宜 5 倍，比 GPT-6 Astra 便宜 80%"。
- [@noisyb0y1][mp] 10 分钟拿到一个能玩的多人联机浏览器游戏，自称花了 $18（帖子里前后数字不一致，价格仅供参考）。
- [@ItsmeAjayKV][kibitz] 在 Arena 上以 Kibitz 之名遇到它，"提示词只让它生成一座浮空宝塔岛，别的什么都没写"——结果很喜欢它自己加上的控件。
- [@sakatayasha][brain] 49 分钟做了一个可交互大脑解剖浏览器——"第一次有模型做出我真的会发给学生的作品"。
- [@yihui_indie][compilation] 把 157 个 Kimi K3.1 作品剪成混剪——本合集采样的正是这波发布周浪潮。
- [@_MaxBlade][subs] 花 $400 买订阅只为发 4 条提示词，提醒"走 API 的话只要 $29"——重度 harness 用户的价格警示。
- [@ojigineko_tips][img3d]（日文）给它一张图，免费档约 18 分钟拿到可旋转 3D 模型，中途自己修正了一次卡壳。
- [@xueyu1125][volcano]（中文）用一条一句话的像素火山提示词回应了质疑帖。

两类来源合起来的规律：只要对手是 Opus 5.5、GPT-6 Astra 或 Claude Code 工作流，K3.1 在价格上几乎全胜，通常差 3–10 倍。质量上则分裂：创作者认为它在体素/Three.js 场景和可玩构建上打平甚至领先，而 Opus 在提示词遵循和打磨上仍有优势；便宜快速的模型（Terra、DeepSeek、Haiku 档）在质量不是第一优先时能在价格和速度上压过它。没有任何实测基准说它赢过 Opus——包括 Moonshot 自己的图表，创作者引用的那几轮也落后 1–3 分。

## 重跑一次再相信对比

设置一变结果就变。[@sai0xgen][dragon] 指出一次飞龙测试里 harness 的温度 bug 让 K3.1 看不到自己的渲染图；[@IFITALEX][polaroid] 怀疑那次糟糕的解构是 harness 而非模型的问题；[@jurlycat][pelican-3d] 提出了元问题——"你按第一次尝试还是按能推到多远来评判一个编码模型？"——因为 Kimi 的鹈鹕靠"再改好一点"的多轮追问，而 Opus 一次成型。自己跑一遍：把提示词粘到 [Lab 文本竞技场][arena]，选两三个模型；或者按[教程](tutorial.md)用 API。

## 更多实测

- [Lab Evals 榜单][evals]——Artificial Analysis 数据，2026-10-29 快照。K3.1 Pro 的行在智能、速度和成本榜上。
- [Lab Pelican Test][pelican]——同一提示词、同一评分方式，画作直接展示。还没有 K3.1 的成绩。
- [SandBase Lab 上的全部 AI 视频合集][collections]——其他模型的同类列表，包括 [MiniMax M3.1 Flash][minimax-repo] 和 [Gemini 4 Carbon][carbon-repo]。

---

Lab 数据：[Evals 榜单][evals]（Artificial Analysis，2026-10-29 快照）与 [Pelican Test][pelican]（2026-11-01 读取）。创作者数据：他们本人的帖子，已附链接，未经我们独立验证。

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
