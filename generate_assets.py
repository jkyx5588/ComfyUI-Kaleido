import sys
import os
import re
import random

# 🔴 终极修复：强制将当前脚本所在目录加入 Python 环境变量
# 这样无论你从哪里运行，都能 100% 找到同目录下的 lumina_data.py
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ 找不到 PIL 库。请使用 ComfyUI 的 python_embeded 运行！")
    sys.exit(1)

# 尝试导入我们庞大的数据仓库
try:
    from lumina_data import (
        MBTI_AESTHETICS, PROFESSIONAL_KNOWLEDGE_BASE, TECHNICAL_MEDIA,
        VIDEO_TYPES, CAMERA_MOVEMENTS, LENS_CHOICES, SHOOTING_SUBJECTS, FRAMING_OPTIONS,
        TYPO_FONT_FAMILIES, TYPO_CONSTRUCTION, TYPO_GRAVITY, TYPO_COUNTER,
        TYPO_PROPORTIONS, TYPO_MATERIALS, TYPO_CONTEXTS, TYPO_FUSIONS,
        LYRIC_STRUCTURES, RHYME_SCHEMES, LYRIC_THEMES, LYRIC_LANGUAGES,
        MUSIC_GENRES, MUSIC_INSTRUMENTS, MUSIC_STRUCTURES, MUSIC_PRODUCTION, MUSIC_MOODS,
        STORY_STRUCTURES, CHARACTER_ARCHETYPES, DRAMATIC_CONFLICTS, DIALOGUE_STYLES,
        NARRATIVE_DEVICES, ENDING_TYPES, SCRIPT_FORMATS, STORY_TONES,
        CIVILIZATION_LEVELS, MAGIC_SYSTEMS, WORLD_GEOGRAPHY, WORLD_POLITICS,
        WORLD_ELEMENTS, WORLD_TYPES,
        LOGO_TYPES, LOGO_STYLES, LOGO_GEOMETRY, LOGO_COLORS, LOGO_INDUSTRIES, BRAND_ARCHETYPES,
        COLOR_HARMONIES, CINEMATIC_LOOKS, COLOR_SPACES, FILM_GRAIN_TYPES,
        CONCEPT_VIEWS, CONCEPT_STYLES, CONCEPT_MATERIALS, CRITIC_CRITERIA,
        CRITIC_MODES, TARGET_MODELS, PACK_TYPES, PACK_MATERIALS, PACK_FINISHES,
        PACK_CATEGORIES, PACK_VIEWS, WUXIA_STYLES, WUXIA_ROLES, WUXIA_MOVES,
        WUXIA_WEAPONS, WUXIA_CLOTHING, WUXIA_SCENES, BRAND_VALUES, BRAND_SYSTEMS,
        BRAND_DELIVERABLES, BRAND_GRAPHICS, COMMUNICATION_PLATFORMS, INTERIOR_STYLES, ROOM_TYPES,
        SURFACE_MATERIALS, ARCH_LIGHTING, FASHION_STYLES, FABRIC_PROPERTIES, GARMENT_CUTS,
        FASHION_PRESENTATION, HAIR_STYLES, HAIR_TEXTURES, HAIR_COLORS, HAIR_PRESENTATION,
        CULTURAL_PRODUCTS, CULTURAL_THEMES, CULTURAL_CRAFTS, MERCH_PRESENTATION,
        MED_SYSTEMS, MED_IMAGING, MED_STYLES, MED_SCALES,
        ID_CATEGORIES, ID_DESIGN_LANGUAGES, ID_MATERIALS_CMF, ID_PRESENTATION
    )
except ImportError as e:
    print(f"❌ 导入失败: {e}")
    print(f"请确保 'lumina_data.py' 文件确实存在于此目录下：\n{current_dir}")
    sys.exit(1)

# 聚合所有的选项 Keys
all_options = set()

# 将所有字典的 keys 和列表的 items 加入大集合
data_sources =[
    MBTI_AESTHETICS, PROFESSIONAL_KNOWLEDGE_BASE, TECHNICAL_MEDIA,
    VIDEO_TYPES, CAMERA_MOVEMENTS, LENS_CHOICES, SHOOTING_SUBJECTS, FRAMING_OPTIONS,
    TYPO_FONT_FAMILIES, TYPO_CONSTRUCTION, TYPO_GRAVITY, TYPO_COUNTER,
    TYPO_PROPORTIONS, TYPO_MATERIALS, TYPO_CONTEXTS, TYPO_FUSIONS,
    LYRIC_STRUCTURES, RHYME_SCHEMES, LYRIC_THEMES, LYRIC_LANGUAGES,
    MUSIC_GENRES, MUSIC_INSTRUMENTS, MUSIC_STRUCTURES, MUSIC_PRODUCTION, MUSIC_MOODS,
    STORY_STRUCTURES, CHARACTER_ARCHETYPES, DRAMATIC_CONFLICTS, DIALOGUE_STYLES,
    NARRATIVE_DEVICES, ENDING_TYPES, SCRIPT_FORMATS, STORY_TONES,
    CIVILIZATION_LEVELS, MAGIC_SYSTEMS, WORLD_GEOGRAPHY, WORLD_POLITICS,
    WORLD_ELEMENTS, WORLD_TYPES,
    LOGO_TYPES, LOGO_STYLES, LOGO_GEOMETRY, LOGO_COLORS, LOGO_INDUSTRIES, BRAND_ARCHETYPES,
    COLOR_HARMONIES, CINEMATIC_LOOKS, COLOR_SPACES, FILM_GRAIN_TYPES,
    CONCEPT_VIEWS, CONCEPT_STYLES, CONCEPT_MATERIALS, CRITIC_CRITERIA,
    CRITIC_MODES, TARGET_MODELS, PACK_TYPES, PACK_MATERIALS, PACK_FINISHES,
    PACK_CATEGORIES, PACK_VIEWS, WUXIA_STYLES, WUXIA_ROLES, WUXIA_MOVES,
    WUXIA_WEAPONS, WUXIA_CLOTHING, WUXIA_SCENES, BRAND_VALUES, BRAND_SYSTEMS,
    BRAND_DELIVERABLES, BRAND_GRAPHICS, COMMUNICATION_PLATFORMS, INTERIOR_STYLES, ROOM_TYPES,
    SURFACE_MATERIALS, ARCH_LIGHTING, FASHION_STYLES, FABRIC_PROPERTIES, GARMENT_CUTS,
    FASHION_PRESENTATION, HAIR_STYLES, HAIR_TEXTURES, HAIR_COLORS, HAIR_PRESENTATION,
    CULTURAL_PRODUCTS, CULTURAL_THEMES, CULTURAL_CRAFTS, MERCH_PRESENTATION,
    MED_SYSTEMS, MED_IMAGING, MED_STYLES, MED_SCALES,
    ID_CATEGORIES, ID_DESIGN_LANGUAGES, ID_MATERIALS_CMF, ID_PRESENTATION
]

for source in data_sources:
    if isinstance(source, dict):
        all_options.update(source.keys())
    elif isinstance(source, list):
        all_options.update(source)

# 确保输出目录存在
output_dir = os.path.join(current_dir, "web", "assets")
os.makedirs(output_dir, exist_ok=True)

# 模拟 JS 前端的安全文件名转换逻辑
def get_safe_name(opt):
    safe_name = re.sub(r'[^a-zA-Z0-9 ]', '', opt)
    safe_name = safe_name.strip().lower()
    safe_name = re.sub(r'\s+', '_', safe_name)
    safe_name = safe_name.strip('_')
    return safe_name

def generate_gradient_image(width, height, color1, color2):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data =[]
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

colors =[
    ("#1a2a6c", "#b21f1f"), ("#0f2027", "#203a43"), ("#2c3e50", "#3498db"),
    ("#232526", "#414345"), ("#141e30", "#243b55"), ("#000000", "#434343"),
    ("#4b1248", "#f0c27b"), ("#0f0c29", "#302b63"), ("#240b36", "#c31432")
]

print(f"🚀 开始为 {len(all_options)} 个选项生成高级占位图...")

count = 0
for opt in all_options:
    safe_name = get_safe_name(opt)
    if not safe_name: continue
        
    file_path = os.path.join(output_dir, f"{safe_name}.jpg")
    
    if os.path.exists(file_path):
        continue

    c1, c2 = random.choice(colors)
    img = generate_gradient_image(512, 768, c1, c2)
    draw = ImageDraw.Draw(img)
    
    short_text = opt.split('[')[0].strip()
    if len(short_text) > 20: short_text = short_text[:17] + "..."
    
    words = [w for w in re.split(r'[^a-zA-Z]', short_text) if w]
    initials = "✨"
    if len(words) >= 2: initials = (words[0][0] + words[1][0]).upper()
    elif len(words) == 1: initials = words[0][:2].upper()

    try:
        font_large = ImageFont.truetype("arial.ttf", 250)
        font_small = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # 绘制
    try:
        left, top, right, bottom = draw.textbbox((0, 0), initials, font=font_large)
        w, h = right - left, bottom - top
        draw.text(((512-w)/2, (768-h)/2 - 50), initials, fill=(255,255,255, 30), font=font_large)
        
        left, top, right, bottom = draw.textbbox((0, 0), short_text, font=font_small)
        w, h = right - left, bottom - top
        draw.text(((512-w)/2, 600), short_text, fill=(255,255,255, 200), font=font_small)
    except Exception:
        pass # 兼容极老版本的 Pillow

    img.save(file_path, "JPEG", quality=85)
    count += 1

print(f"✅ 生成完毕！共生成 {count} 张匹配的占位图。")
print(f"📁 图像已保存至: {output_dir}")