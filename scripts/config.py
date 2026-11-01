"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'kimi-k3-1'
REPO = 'sandbase-lab/awesome-kimi-k3-1'

CFG = dict(
    slug=SLUG,
    kind='code',  # build_readme.py renders the chat-completions curl writing html_out
    name='Kimi K3.1',
    short='K3.1',  # how the prose refers to the model after the first mention
    vendor='Moonshot AI',
    model_id='moonshotai/kimi-k3.1-pro',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-kimi-k3-1',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/moonshotai/kimi-k3.1-pro',
    arena=f'{SITE}/lab/x/llm-arena?models=moonshotai%2Fkimi-k3.1-pro',
    evals=f'{SITE}/lab/evals',
    pelican=f'{SITE}/lab/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-kimi-k3-1-sync/1.0 (+https://github.com/{REPO})',
    html_out='kimi.html',
    # Output limit for the curl example. Thinking is always on for this model and the hidden
    # reasoning tokens come out of max_tokens. Creators report single builds in the hundreds of
    # thousands of tokens through the Kimi harness (877K for a burning-car scene, 1.98M for the
    # Titanic), and SandBase's API caps max_tokens at 131,072
    # (`sandbase inspect moonshotai/kimi-k3.1-pro --json`), so we ask for the cap.
    max_tokens=131072,
    max_tokens_limit=131072,
    context_length=1048576,
    guide_patterns=7,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome Kimi K3.1',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names. 'kimi' stays
    # because the model's own posters say Kimi.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'sonnet',
                 'haiku', 'gpt', 'gemini', 'deepseek', 'argon', 'qwen', 'glm', 'carbon', 'minimax'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Moonshot AI.', 'zh-CN': '与 Moonshot AI（月之暗面）无隶属或背书关系。'},
    # No SandBase blog post on this model exists (checked 2026-11-01). build_readme.py skips the
    # reading section while this is empty — do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: `sandbase inspect moonshotai/kimi-k3.1-pro`, the Lab collection's
# own posts (linked), the Lab Evals boards (Artificial Analysis snapshot 2026-10-29), and the
# Lab Pelican Test leaderboard (read 2026-11-01), which has no row for this model yet.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **Kimi K3.1 examples**: videos, prompts and demos made with Kimi K3.1 and Kimi K3.1 Pro, Moonshot AI\'s flagship open-weight multimodal reasoning model — first tested in Arena under the codename Kibitz, released in late October 2026. Interactive Three.js scenes, voxel worlds, browser games, motion graphics and an outsized number of head-to-head comparisons against Claude Opus 5.5 and other frontier models, most of them written as one self-contained HTML page from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome Kimi K3.1: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[Kimi K3.1 vs. Claude Opus 5.5, GPT-6 Astra and DeepSeek V4.1 Flash](docs/model-comparison.md)'),
            ('Try it now', '[Run Kimi K3.1 Pro in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible). Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. Thinking is always on for this model, and the hidden reasoning tokens come out of `max_tokens`, so the call above asks for the full 131,072-token cap. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is Kimi K3.1?', 'Kimi K3.1 Pro is Moonshot AI\'s flagship open-weight multimodal reasoning model, a post-trained successor to Kimi K3 with a 1,048,576-token context. It accepts text, image and video input and is built for long-horizon coding, agentic tool use and visual software work. Before release it was tested in Arena under the codename **Kibitz**, and the earliest videos in this list were made there. On SandBase the model id is `{model_id}` (the Pro tier; this collection groups K3.1 and K3.1 Pro together). Source: `sandbase inspect moonshotai/kimi-k3.1-pro`.'),
            ('How are these Kimi K3.1 videos made?', 'The model doesn\'t render video. It writes code — a web page (HTML with Three.js, Canvas or SVG), a Blender scene or a playable game — and the creator records the result. Many posts came out of the Kimi web app\'s own "3D Make" flow or agent harnesses like Claude Code and OpenCode; some creators also fed the generated pages through video models for sound. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good Kimi K3.1 prompt?', 'Name one self-contained HTML file and the renderer you want (Three.js is the default for 3D here), describe the scene, the controls and the state a recording should catch, ban external assets, and give it a finish line — or build a game one system per prompt instead of all at once. Leave a large `max_tokens`: thinking is always on and shares that budget. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the Kimi K3.1 API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint. One key works for every model, and `reasoning_effort` takes `low`, `high` or `max` (default `max`). See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is Kimi K3.1 better than Claude Opus 5.5, GPT-6 Astra or DeepSeek V4.1 Flash?', 'Most of this collection is exactly that comparison — 132 of the videos are head-to-heads, and Opus 5.5 is the most common rival. On measured data, the Lab [Evals boards]({evals}) (Artificial Analysis, snapshot 2026-10-29) place K3.1 Pro at 46.0 on the Intelligence Index, rank 22 of 78 — behind Opus 5.5 Max (58.4) and GPT-6 Astra Max (56.9), ahead of DeepSeek V4.1 Flash 1017 (32.5) — at $3.68 per task against Opus\'s $10.04. On creator runs it regularly matches Opus on Three.js scenes for 5-10x less money, though several creators still prefer Opus on detail and prompt adherence. The Lab [Pelican Test]({pelican}) has no K3.1 row yet. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'Creators report from $0.20-$0.33 for a single Three.js scene (a voxel ship, a rocket launch) up to $12.5-$19 for harness runs that also build assets (a folding-phone page, a bullet-train cinematic). The list price on SandBase is $2 per million input tokens and $10 per million output tokens (cache reads at 0.1x), and reasoning tokens bill as output.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a Kimi K3.1 creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'Kimi K3.1 prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} Kimi K3.1 videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **Kimi K3.1 案例**合集：用 Kimi K3.1 和 Kimi K3.1 Pro（Moonshot AI 月之暗面的旗舰开放权重多模态推理模型，发布前曾以代号 Kibitz 出现在竞技场）做出的视频、提示词和演示。包括可交互 Three.js 场景、体素世界、浏览器游戏、动效，以及大量与 Claude Opus 5.5 等前沿模型的同题对比，大多是模型根据提示词写成的单文件网页，均注明作者并链接原帖。',
        'alt': 'Awesome Kimi K3.1：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[Kimi K3.1 对比 Claude Opus 5.5、GPT-6 Astra 和 DeepSeek V4.1 Flash](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 Kimi K3.1 Pro]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。这个模型的思考始终开启，隐藏的推理 token 也占用 `max_tokens`，所以上面的示例给到 131072 的上限。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('Kimi K3.1 是什么？', 'Kimi K3.1 Pro 是 Moonshot AI（月之暗面）的旗舰开放权重多模态推理模型，是 Kimi K3 的后训练继任者，上下文窗口 1,048,576 token。它接受文本、图片和视频输入，面向长程编码、智能体工具调用和可视化软件工作。发布前它以代号 **Kibitz** 出现在竞技场，本合集最早的一批视频就是在那里做的。在 SandBase 上模型 ID 是 `{model_id}`（Pro 档；本合集把 K3.1 和 K3.1 Pro 合在一起）。来源：`sandbase inspect moonshotai/kimi-k3.1-pro`。'),
            ('这些 Kimi K3.1 视频是怎么做出来的？', '模型并不直接渲染视频。它写代码——一个网页（用 Three.js、Canvas 或 SVG 的 HTML）、一个 Blender 场景或一个可玩的游戏——作者再把结果录下来。很多作品出自 Kimi 网页版自带的 "3D Make" 流程或 Claude Code、OpenCode 这类 agent harness；也有作者把生成的页面再过一遍视频模型来配音。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 Kimi K3.1 提示词？', '指定输出一个独立的 HTML 文件，并说明用哪个渲染方式（这里的 3D 默认是 Three.js）；描述场景、交互，以及录屏需要捕捉的状态；禁止外部素材并给它一条终点线——做游戏则一次只加一个系统。`max_tokens` 要给足：思考始终开启，也占用这个额度。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 Kimi K3.1 API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口，一个 Key 调用所有模型；`reasoning_effort` 可选 `low`、`high`、`max`（默认 `max`）。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('Kimi K3.1 比 Claude Opus 5.5、GPT-6 Astra 或 DeepSeek V4.1 Flash 更强吗？', '这个合集大半就是在回答这个问题：132 条视频是同题对比，Opus 5.5 是最常见的对手。实测数据上，Lab [Evals 榜单]({evals})（Artificial Analysis，2026-10-29 快照）把 K3.1 Pro 排在智能指数 46.0、78 个模型中第 22 位——落后于 Opus 5.5 Max（58.4）和 GPT-6 Astra Max（56.9），领先 DeepSeek V4.1 Flash 1017（32.5）——单任务成本 $3.68，对 Opus 的 $10.04。创作者实测里它常以 5–10 分之一的价格在 Three.js 场景上追平 Opus，但也有不少作者认为 Opus 在细节和提示词遵循上更好。Lab [Pelican Test]({pelican}) 还没有 K3.1 的成绩。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '创作者报告的花费从单个 Three.js 场景的 $0.20–$0.33（一艘体素瓶中信、一次火箭发射）到连素材一起搭的 harness 运行 $12.5–$19（折叠手机页面、子弹列车电影感场景）不等。SandBase 标价为每百万输入 token $2、每百万输出 token $10（缓存命中按 0.1 倍），推理 token 按输出计费。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 Kimi K3.1 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'Kimi K3.1 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 Kimi K3.1 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
