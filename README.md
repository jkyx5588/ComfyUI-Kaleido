# ComfyUI-Kaleido
Creative Prompt Generator
# 🌌 ComfyUI-Kaleido (万花筒·全能创意引擎)

**ComfyUI-Kaleido** 是一套基于本地大语言模型 (Ollama) 的全流程 AIGC 创意辅助节点组。它内置了 **160+ 美学流派**、**70+ 技术媒介**、**16型人格思维引擎** 以及 **影视/音乐/设计** 领域的专业知识库 (RAG)。

它旨在将简单的灵感转化为 **工业级** 的提示词（Prompt）和设定方案。

---

## 🛠️ 安装与配置 (Setup)

### 1. 核心依赖：Ollama
本插件的大脑是本地运行的 LLM。**必须安装并运行 Ollama 才能使用。**

1.  **下载**: [https://ollama.com/](https://ollama.com/)
2.  **拉取模型**: 在终端运行以下命令：
    *   `ollama pull qwen2.5` (推荐：逻辑推理强)
    *   `ollama pull llama3` (备选：通用性好)
    *   `ollama pull llava` (必选：用于**识图/看视频**功能)
3.  **保持运行**: 使用插件时，请确保 Ollama 服务在后台运行。

### 2. 插件安装
将本插件文件夹放入 `ComfyUI/custom_nodes/` 目录下，并重启 ComfyUI。

---

## 🔌 基础设施 (Infrastructure)

所有 Kaleido 节点都需要连接这个加载器。

### 🔌 Kaleido Link (Ollama)
*   **功能**：连接本地 Ollama 服务，自动获取已安装的模型列表。
*   **输入**：
    *   `ollama_url`: 默认 `http://127.0.0.1:11434/api/generate`。
    *   `model_selector`: 选择模型（识图请选 `llava`/`minicpm`）。
*   **输出**：
    *   `🔌 Ollama_Connection`: **连接到所有其他 Kaleido 节点的对应输入口。**

---

## 🎨 视觉与影像 (Visuals & Film)

### 🎡 Kaleido Visuals (Aesthetic)
**全能美学顾问**。用于生成高质量的单图 Prompt。
*   **核心玩法**：
    *   `Creator Personality`: 选择 **MBTI 人格** (如 INTJ, ENFP)。AI 会模拟该人格的思维方式来构图。
    *   `Aesthetic Style`: **160+ 流派** (赛博朋克, 巴洛克, 梦核...)。
    *   `Technical Medium`: **70+ 媒介** (湿版摄影, UE5, 显微镜...)。
*   **多模态**：连接图片到 `image_input`，可进行**风格迁移**。

### 🎬 Kaleido Director (Storyboard)
**分镜导演**。用于视频生成的前期分镜设计。
*   **核心玩法**：
    *   `Script Content`: 输入一段剧本或动作描述。
    *   `Video Type`: 选择视频类型 (电影正片, TVC广告, MV)。
    *   `Lens & Movement`: 选择焦段 (16mm-200mm) 和运镜方式 (推拉摇移)。
    *   `Video Frames`: **核心功能**。连接 `Load Video` 的图像输出，AI 会生成 **2x2 蒙太奇**，理解剧情后生成后续分镜。
*   **输出**：适合 AnimateDiff 的批量 Prompt。

### 👤 Kaleido Character (Concept)
**概念设计师**。用于角色和资产的标准化设计。
*   **核心玩法**：
    *   `View Type`: 生成 **三视图 (Turnaround)**、**表情集** 或 **拆解图**。
    *   `Art Style`: 赛璐璐、厚涂、3D白模。
    *   `Image Input`: **草图细化**。上传潦草线条，AI 生成精细渲染图。

### 🎨 Kaleido Palette (Color)
**调色师**。用于电影级调色和色彩科学。
*   **核心玩法**：
    *   `Color Harmony`: 互补色、类似色、三等分。
    *   `Cinematic Look`: 青橙色调、银留法、黑客帝国绿。
    *   `Image Input`: **色彩克隆**。吸取参考图的 LUTs 和光影逻辑。

---

## ✒️ 设计与品牌 (Design & Branding)

### 🔠 Kaleido Typo (Design)
**字体炼金术师**。用于文字特效与排版。
*   **核心玩法**：
    *   `Font Family`: 书法 (颜体/狂草) 或 西文 (Helvetica/Gothic)。
    *   `Structure`: 控制 **重心** 和 **中宫** (Micro-surgery)。
    *   `Fusion`: **跨界融合** (如“赛博狂草” = 书法+霓虹)。
    *   `Image Input`: 吸取参考图的材质纹理。

### 🛡️ Kaleido Icon (Logo)
**符号大师**。用于生成极简、矢量、可商用的 Logo。
*   **核心玩法**：
    *   `Geometry`: 黄金圆切、布尔运算、格式塔。
    *   `Archetype`: 品牌原型 (智者、统治者、创造者)。
    *   `Constraints`: 强制生成白底、无阴影、矢量风。

### 📦 Kaleido Packaging (Product)
**包装设计师**。用于生成 CGI 级产品样机。
*   **核心玩法**：
    *   `Package Type`: 滴管瓶、自立袋、马口铁罐。
    *   `Print Finish`: 烫金、激凸、UV、逆向磨砂。
    *   `Image Input`: 将 Logo 贴图贴在包装上。

---

## 📝 故事与策划 (Story & World)

### 📝 Kaleido Story (Script)
**王牌编剧**。故事生成的源头。
*   **核心玩法**：
    *   `Core Idea`: 输入一个简单的点子。
    *   `Structure`: 救猫咪、英雄之旅、起承转合。
    *   `Conflict`: 人与自我、人与科技、人与社会。
    *   `Device`: 叙事诡计 (契诃夫之枪、红鲱鱼)。
*   **输出**：完整剧本、角色小传 (Character Sheet)。

### 🌍 Kaleido World (Lore)
**世界架构师**。IP 孵化与宏观设定。
*   **核心玩法**：
    *   `Civilization`: 文明等级 (前工业 - 星系级)。
    *   `Magic/Tech`: 硬魔法、生物改造、蒸汽朋克。
    *   `Asset Focus`: 生成 **地图**、**怪兽图鉴**、**武器设定**。

---

## 🎵 声音与音乐 (Audio)

### 🎵 Kaleido Music (Vibe)
**音乐制作人**。为 MusicGen/AudioLDM 生成提示词。
*   **核心玩法**：
    *   `Genre`: 80+ 流派 (Synthwave, Epic Trailer, Trap)。
    *   `Production`: Hi-Fi, Lo-Fi, 空间音频。
    *   `Video Frames`: **看视频配乐**。AI 分析画面情绪，生成契合的 BGM。

### 🎤 Kaleido Lyrics (Song)
**金牌作词人**。为 Suno/Udio 生成歌词。
*   **核心玩法**：
    *   `Structure`: Verse-Chorus, Rap Flow。
    *   `Rhyme`: AABB, 双押, 句内押。
    *   `Video Frames`: **看视频写词**。根据剧情发展撰写叙事性歌词。

---

## 🧐 质检与落地 (QC & Deploy)

### 🧐 Kaleido Review (Critic)
**艺术评论家**。闭环优化与评分。
*   **用法**：
    *   连接 KSampler 生成的图片。
    *   (可选) 连接参考图进行 **对比审稿**。
*   **输出**：AI 会指出缺点（构图、光影、崩坏），并输出 **优化后的 Prompt**。

### 🔌 Kaleido Adapter (Export)
**模型适配器**。
*   **功能**：将通用提示词翻译为特定模型的“方言”。
*   **支持**：FLUX.1 (自然语言), Midjourney v6 (--v 6.0), Pony Diffusion (score_9), SDXL。

---

## 💡 常见问题 (FAQ)

1.  **为什么我看不到图形化预览界面？**
    *   请确保 `__init__.py` 中包含了 `WEB_DIRECTORY = "./web"`。
    *   请尝试清除浏览器缓存 (Ctrl+F5) 并重启 ComfyUI。

2.  **节点显示红色边框报错 `Value not in list`？**
    *   这是因为旧节点的默认值与新版代码不匹配。请**删除旧节点**，重新添加即可。

3.  **连接视频时报错？**
    *   请使用标准的 `Load Video` 节点，将其 `IMAGE` 输出口连接到本插件的 `video_frames` 输入口。

4.  **Ollama 连接失败？**
    *   请确保您已安装 Ollama，且在终端运行了 `ollama serve`。默认地址为 `http://127.0.0.1:11434`。
