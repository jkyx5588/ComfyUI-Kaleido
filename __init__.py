# 导入所有核心功能模块
from .lumina_core import OllamaConnectionLoader, LuminaAestheticNode, LuminaDirectorNode
from .lumina_typography import LuminaTypographyNode
from .lumina_music import LuminaMusicNode
from .lumina_lyrics import LuminaLyricsNode
from .lumina_screenwriter import LuminaScreenwriterNode
from .lumina_logo import LuminaLogoNode
from .lumina_color import LuminaColorNode
from .lumina_concept import LuminaConceptNode
from .lumina_critic import LuminaCriticNode
from .lumina_world import LuminaWorldNode
from .lumina_adapter import LuminaAdapterNode
from .lumina_packaging import LuminaPackagingNode
from .lumina_wuxia import LuminaWuxiaNode
from .lumina_brand import LuminaBrandNode
from .lumina_agent import LuminaAgentNode
from .lumina_link import LuminaLinkListenerNode, LuminaLinkSenderNode
from .lumina_deconstructor import LuminaDeconstructorNode
from .lumina_verticals import LuminaInteriorNode, LuminaFashionNode, LuminaHairDesignNode, LuminaCulturalDesignNode # <--- 增加 LuminaCulturalDesignNode
from .lumina_ascension import (
    LuminaXenobiologistNode, 
    LuminaSpatialArchitectNode, 
    LuminaSynestheteNode, 
    LuminaQuantumWeaverNode
)
from .lumina_medical import LuminaMedicalNode # <--- 新增导入
from .lumina_industrial import LuminaIndustrialNode # <--- 新增导入

# 节点类映射 (内部逻辑名保持不变，确保稳定性)
NODE_CLASS_MAPPINGS = {
    "OllamaConnectionLoader": OllamaConnectionLoader,
    "LuminaAestheticNode": LuminaAestheticNode,
    "LuminaDirectorNode": LuminaDirectorNode,
    "LuminaTypographyNode": LuminaTypographyNode,
    "LuminaMusicNode": LuminaMusicNode,
    "LuminaLyricsNode": LuminaLyricsNode,
    "LuminaScreenwriterNode": LuminaScreenwriterNode,
    "LuminaLogoNode": LuminaLogoNode,
    "LuminaColorNode": LuminaColorNode,
    "LuminaConceptNode": LuminaConceptNode,
    "LuminaCriticNode": LuminaCriticNode,
    "LuminaWorldNode": LuminaWorldNode,
    "LuminaAdapterNode": LuminaAdapterNode,
    "LuminaPackagingNode": LuminaPackagingNode,
    "LuminaWuxiaNode": LuminaWuxiaNode,
    "LuminaBrandNode": LuminaBrandNode,
    "LuminaAgentNode": LuminaAgentNode,
    "LuminaLinkListenerNode": LuminaLinkListenerNode,
    "LuminaLinkSenderNode": LuminaLinkSenderNode,
    "LuminaDeconstructorNode": LuminaDeconstructorNode,
    "LuminaInteriorNode": LuminaInteriorNode,
    "LuminaFashionNode": LuminaFashionNode,
    "LuminaHairDesignNode": LuminaHairDesignNode,
    "LuminaCulturalDesignNode": LuminaCulturalDesignNode,
    "LuminaXenobiologistNode": LuminaXenobiologistNode,
    "LuminaSpatialArchitectNode": LuminaSpatialArchitectNode,
    "LuminaSynestheteNode": LuminaSynestheteNode,
    "LuminaQuantumWeaverNode": LuminaQuantumWeaverNode,
    "LuminaMedicalNode": LuminaMedicalNode,
    "LuminaIndustrialNode": LuminaIndustrialNode,
}

# 节点显示名称映射 (UI 呈现名 - 全面升级为 Kaleido)
NODE_DISPLAY_NAME_MAPPINGS = {
    # 基础设施
    "OllamaConnectionLoader": "🔌 Kaleido Link (Ollama)",
    
    # 视觉与影像
    "LuminaAestheticNode": "🎡 Kaleido Visuals (Aesthetic)",
    "LuminaDirectorNode": "🎬 Kaleido Director (Storyboard)",
    "LuminaConceptNode": "👤 Kaleido Character (Concept)",
    "LuminaColorNode": "🎨 Kaleido Palette (Color)",
    "LuminaDeconstructorNode": "👁️ Kaleido Deconstructor (Reverse Eng)",
    
    # 设计与品牌
    "LuminaLogoNode": "🛡️ Kaleido Icon (Logo)",
    "LuminaTypographyNode": "🔠 Kaleido Typo (Design)",
    "LuminaPackagingNode": "📦 Kaleido Packaging (Product)",
    "LuminaBrandNode": "💼 Kaleido Brand Director (Full Case)",
    
    # 声音与音乐
    "LuminaMusicNode": "🎵 Kaleido Music (Vibe)",
    "LuminaLyricsNode": "🎤 Kaleido Lyrics (Song)",
    
    # 策划与剧作
    "LuminaScreenwriterNode": "📝 Kaleido Story (Script)",
    "LuminaWorldNode": "🌍 Kaleido World (Lore)",
    "LuminaWuxiaNode": "⚔️ Kaleido Wuxia Master",
    
    # 质检与落地
    "LuminaCriticNode": "🧐 Kaleido Review (Critic)",
    "LuminaAdapterNode": "🔌 Kaleido Adapter (Export)",
    
    # 智能体
    "LuminaAgentNode": "🤖 Kaleido Archon (Auto-Agent)",
    
    # 神经链路
    "LuminaLinkListenerNode": "📡 Kaleido Link (Receiver)", # <--- 接收端
    "LuminaLinkSenderNode": "🚀 Kaleido Link (Sender)", # <--- 发送端
    
    # 垂直专业领域
    "LuminaInteriorNode": "🏛️ Kaleido Interior Architect",
    "LuminaFashionNode": "👗 Kaleido Fashion Designer",
    "LuminaHairDesignNode": "✂️ Kaleido Hair Stylist",
    "LuminaCulturalDesignNode": "🎁 Kaleido Cultural Merch (Design)",
    "LuminaMedicalNode": "🧬 Kaleido Medical & Anatomy",
    "LuminaIndustrialNode": "🛠️ Kaleido Industrial Design",
    
    # 探求真理
    "LuminaXenobiologistNode": "🧬 Kaleido Xenobiologist (Life)",
    "LuminaSpatialArchitectNode": "🌀 Kaleido Spatial Architect (XR)",
    "LuminaSynestheteNode": "👁️‍🗨️ Kaleido Synesthete (Neuro-Art)",
    "LuminaQuantumWeaverNode": "⏳ Kaleido Quantum Weaver (Time)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

WEB_DIRECTORY = "./web" 

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]