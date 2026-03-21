import { app } from "/scripts/app.js";

const VISUAL_PARAMS =[
    "aesthetic_style", "technical_medium", "creator_personality",
    "video_type", "lens_choice", "camera_movement", "shooting_subject", "framing",
    "music_genre", "instrumentation", "mood_vibe", "production_quality", "structure",
    "structure_preset", "rhyme_scheme", "theme_vibe", "language", "bpm_tempo",
    "font_family", "material_fx", "composition", "fusion_mode", "design_context",
    "layout_grid", "construction_logic", "structure_gravity", "structure_counter",
    "proportion_rule", "micro_detail", "logo_type", "design_style", "brand_archetype",
    "brand_industry", "geometry_logic", "color_psychology", "category", "package_type",
    "material_base", "print_finish", "view_angle", "world_type", "element_focus",
    "civilization_level", "geography_biome", "power_system", "political_structure",
    "asset_focus", "narrative_structure", "protagonist_archetype", "dramatic_conflict",
    "dialogue_style", "narrative_device", "story_tone", "ending_type", "script_format",
    "scene_concept", "wuxia_style", "character_role", "martial_art", "weapon",
    "clothing", "environment", "action_dynamic", "color_harmony", "cinematic_look",
    "film_stock", "grain_texture", "view_type", "art_style", "primary_material",
    "critique_mode", "target_model",
    "room_type", "interior_style", "surface_material", "arch_lighting",
    "fashion_style", "fabric_physics", "tailoring_cut", "presentation",
    "hair_cut", "hair_texture", "dye_technique", "presentation",
    "product_format", "cultural_theme", "material_craft", "merch_presentation",
    "id_category", "design_language", "material_cmf", "id_presentation",
    "industry", "core_value", "design_system", "graphic_style", "deliverable",
    "anatomical_system", "imaging_technique", "illustration_style", "scale_focus",
    "divergence_path", "translation_mode", "geometry_law", "biological_base", "environmental_gravity"
];

const style = document.createElement("style");
style.innerHTML = `
.kld-overlay {
    position: fixed !important; top: 0 !important; left: 0 !important; 
    width: 100vw !important; height: 100vh !important;
    background: rgba(10, 10, 12, 0.85) !important; backdrop-filter: blur(12px) !important;
    z-index: 10000 !important; display: flex !important; 
    justify-content: center !important; align-items: center !important;
    opacity: 0; transition: opacity 0.3s ease;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
    box-sizing: border-box !important; margin: 0 !important; padding: 0 !important;
}
.kld-overlay.show { opacity: 1; }

.kld-modal {
    width: 85vw !important; max-width: 1400px !important; 
    height: 85vh !important; max-height: 900px !important;
    background: linear-gradient(145deg, #1e1e24, #121215) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important; border-radius: 16px !important;
    box-shadow: 0 30px 60px rgba(0,0,0,0.8), inset 0 1px 0 rgba(255,255,255,0.05) !important;
    display: flex !important; flex-direction: column !important; 
    overflow: hidden !important; position: relative !important;
    transform: translateY(20px) scale(0.98);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.kld-overlay.show .kld-modal { transform: translateY(0) scale(1); }

.kld-header {
    flex: 0 0 auto !important; height: 80px !important;
    padding: 0 30px !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important;
    display: flex !important; align-items: center !important; gap: 20px !important; 
    background: rgba(0,0,0,0.3) !important; width: 100% !important; box-sizing: border-box !important;
}
.kld-title { color: #fff !important; font-size: 18px !important; font-weight: 600 !important; margin: 0 !important; display: flex !important; align-items: center !important; gap: 10px !important; white-space: nowrap !important; }
.kld-badge { background: #8b5cf6 !important; color: white !important; padding: 4px 10px !important; border-radius: 20px !important; font-size: 12px !important; font-weight: bold !important; letter-spacing: 1px !important;}

.kld-search {
    flex-grow: 1 !important; height: 44px !important;
    background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1) !important;
    padding: 0 20px !important; border-radius: 22px !important; color: #fff !important; 
    font-size: 15px !important; outline: none !important; transition: all 0.3s !important;
    box-sizing: border-box !important;
}
.kld-search:focus { background: rgba(255,255,255,0.08) !important; border-color: #8b5cf6 !important; box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important; }
.kld-close { background: none !important; border: none !important; color: #888 !important; font-size: 32px !important; cursor: pointer !important; transition: 0.2s !important; display: flex !important; align-items: center !important; justify-content: center !important; width: 40px !important; height: 40px !important; padding: 0 !important;}
.kld-close:hover { color: #fff !important; transform: scale(1.1) !important; }

.kld-scene {
    flex: 1 1 auto !important; height: 100% !important; 
    padding: 40px !important; overflow-y: auto !important; overflow-x: hidden !important;
    perspective: 2000px !important; 
    align-content: start !important;
    box-sizing: border-box !important;
}

.kld-grid {
    display: grid !important; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)) !important;
    gap: 30px !important; width: 100% !important;
}

.kld-scene::-webkit-scrollbar { width: 8px !important; }
.kld-scene::-webkit-scrollbar-thumb { background: #333 !important; border-radius: 4px !important; }

.kld-wrapper {
    position: relative !important; width: 100% !important; height: 330px !important;
    cursor: pointer !important; transform-style: preserve-3d !important;
    will-change: transform !important; z-index: 1 !important;
}
.kld-wrapper:hover:not(.expanded) { z-index: 10 !important; }

.kld-cover {
    position: absolute !important; top: 0 !important; left: 0 !important; 
    width: 100% !important; height: 100% !important;
    background: #1a1a1f !important; border-radius: 8px !important; overflow: hidden !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important; z-index: 2 !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    transform-style: preserve-3d !important;
}
.kld-cover img { width: 100% !important; height: 100% !important; object-fit: cover !important; opacity: 0.9 !important; transition: all 0.4s !important; }
.kld-wrapper:hover:not(.expanded) .kld-cover img { transform: scale(1.05) !important; opacity: 1 !important; }

.kld-cover::after {
    content: '' !important; position: absolute !important; bottom: 0 !important; left: 0 !important; 
    width: 100% !important; height: 60% !important;
    background: linear-gradient(to top, rgba(0,0,0,0.95), transparent) !important; 
    pointer-events: none !important; z-index: 3 !important;
}

.kld-title-text {
    position: absolute !important; bottom: 15px !important; left: 15px !important; right: 15px !important; 
    z-index: 5 !important; font-size: 14px !important; font-weight: 600 !important; line-height: 1.3 !important; 
    text-shadow: 0 2px 4px rgba(0,0,0,0.8) !important; color: #fff !important;
    white-space: normal !important; word-wrap: break-word !important;
    transform: translateZ(30px) !important;
}

/* 🔴 核心修复：分离位移(left)和形状(transform)，彻底解决冲突 */
.kld-glare {
    position: absolute !important; top: 0 !important; 
    left: -150%; /* 注意：这里故意去掉了 !important，让动画控制它 */
    width: 150% !important; height: 100% !important;
    background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.4) 50%, rgba(255,255,255,0) 100%) !important;
    transform: skewX(-25deg) !important; /* 维持固定倾斜角度 */
    z-index: 4 !important; 
    pointer-events: none !important; opacity: 0; /* 悬停前透明 */
    transition: opacity 0.3s ease !important;
}
.kld-wrapper:hover:not(.expanded) .kld-glare { 
    opacity: 1 !important; 
    animation: kld-glare-sweep 1.5s ease-in-out infinite !important; /* 增加了一点时长，看起来更高级 */
}
@keyframes kld-glare-sweep { 
    0% { left: -150%; } 
    100% { left: 150%; } 
}

.kld-placeholder {
    width: 100% !important; height: 100% !important; display: flex !important; justify-content: center !important; align-items: center !important;
    background: linear-gradient(135deg, #2a2a35, #111115) !important; color: rgba(255,255,255,0.15) !important; font-size: 48px !important; font-weight: 800 !important;
}

.kld-panel {
    position: absolute !important; top: 10px !important; left: 100% !important; 
    width: 320px !important; height: calc(100% - 20px) !important;
    background: rgba(25, 25, 30, 0.98) !important; backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255,255,255,0.1) !important; border-left: none !important;
    border-radius: 0 12px 12px 0 !important; padding: 25px !important; box-sizing: border-box !important;
    display: flex !important; flex-direction: column !important;
    transform-origin: left center !important; transform: rotateY(-90deg) !important;
    opacity: 0 !important; pointer-events: none !important;
    transition: all 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
    box-shadow: 30px 15px 40px rgba(0,0,0,0.6) !important;
}

.kld-scene.has-expanded .kld-wrapper:not(.expanded) {
    opacity: 0.05 !important; pointer-events: none !important; filter: blur(8px) !important; transform: scale(0.9) !important;
}

.kld-wrapper.expanded { z-index: 1000 !important; cursor: default !important; }
.kld-wrapper.expanded .kld-cover {
    box-shadow: -15px 25px 50px rgba(0,0,0,0.8) !important;
    border-radius: 12px 0 0 12px !important;
    border-color: rgba(139,92,246,0.5) !important;
}
.kld-wrapper.expanded .kld-panel {
    transform: rotateY(0deg) !important; opacity: 1 !important; pointer-events: auto !important;
}

.kld-panel-tag { font-size: 12px !important; color: #a855f7 !important; font-weight: 800 !important; margin-bottom: 12px !important; letter-spacing: 1px !important;}
.kld-panel-name { font-size: 22px !important; font-weight: 700 !important; margin: 0 0 15px 0 !important; line-height: 1.2 !important; color: #fff !important;}
.kld-panel-desc { 
    font-size: 13px !important; color: #bbb !important; line-height: 1.6 !important; 
    flex-grow: 1 !important; overflow-y: auto !important; padding-right: 5px !important; 
}
.kld-panel-desc::-webkit-scrollbar { width: 4px !important; }
.kld-panel-desc::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.2) !important; border-radius: 2px !important; }

.kld-btn {
    width: 100% !important; padding: 14px !important; background: #6366f1 !important; color: white !important; margin-top: 15px !important;
    border: none !important; border-radius: 8px !important; font-size: 15px !important; font-weight: bold !important;
    cursor: pointer !important; transition: all 0.2s !important; box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
}
.kld-btn:hover { background: #4f46e5 !important; transform: translateY(-2px) !important; box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6) !important; }
.kld-btn:active { transform: translateY(0) !important; }
`;
document.head.appendChild(style);

app.registerExtension({
    name: "Kaleido.Holographic3D",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (!nodeData.name.includes("Lumina") && !nodeData.name.includes("Kaleido")) return;
        
        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            if (onNodeCreated) onNodeCreated.apply(this, arguments);
            const node = this;
            if (!node.widgets) return;

            for (let i = 0; i < node.widgets.length; i++) {
                const w = node.widgets[i];
                if (w.type === "combo" && VISUAL_PARAMS.includes(w.name)) {
                    const btnName = `🖼️ Gallery: ${formatLabel(w.name)}`;
                    const nextWidget = node.widgets[i + 1];
                    if (nextWidget && nextWidget.name === btnName) continue; 
                    
                    const btn = node.addWidget("button", btnName, null, () => {
                        open3DGallery(w, node);
                    });
                    btn.serialize = false; 

                    const btnIndex = node.widgets.indexOf(btn);
                    if (btnIndex > -1) {
                        node.widgets.splice(btnIndex, 1); 
                        node.widgets.splice(i + 1, 0, btn); 
                    }
                    i++;
                }
            }
            setTimeout(() => { node.setSize(node.computeSize()); }, 50);
        };
    }
});

function formatLabel(name) {
    return name.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

// ==========================================
// 🌌 画廊逻辑
// ==========================================
function open3DGallery(targetWidget, node) {
    const existing = document.querySelector(".kld-overlay");
    if (existing) existing.remove();

    const overlay = document.createElement("div");
    overlay.className = "kld-overlay";
    
    const modal = document.createElement("div");
    modal.className = "kld-modal";
    
    const header = document.createElement("div");
    header.className = "kld-header";
    header.innerHTML = `
        <h2 class="kld-title"><span class="kld-badge">ASSET</span> ${formatLabel(targetWidget.name)}</h2>
        <input type="text" class="kld-search" placeholder="Search aesthetics, styles, parameters..." autocomplete="off">
        <button class="kld-close">×</button>
    `;
    
    const scene = document.createElement("div");
    scene.className = "kld-scene";
    
    const grid = document.createElement("div");
    grid.className = "kld-grid";
    scene.appendChild(grid);
    
    const options = targetWidget.options.values;
    const currentVal = targetWidget.value;

    let expandedWrapper = null; 
    const EXPAND_SCALE = 1.55; 

    // 自定义说明字典
    const customDescriptions = {
        "global_afrofuturism": "非洲侨民科技。特征：部落图案、振金、霓虹部落风；光照：生物发光；颜色：紫色、金色、黑色。",
        "arch_brutalism": "粗野主义建筑强调原始的混凝土材质与巨型体量感，常用于反乌托邦场景设定。",
        "cinema_wong_kar_wai": "王家卫风格，特点是抽帧(Step-printing)、霓虹色偏、浅景深与极致的孤独暧昧感。",
        "elec_synthwave": "80年代复古合成器波，充满霓虹灯、网格线和复古科技浪漫。"
    };

    options.forEach(opt => {
        let shortName = opt;
        let tag = "PARAMETER";
        const match = opt.match(/\[(.*?)\]/);
        if (match) {
            tag = match[1]; 
            shortName = opt.replace(match[0], "").trim(); 
        }

        let safeName = opt.replace(/[^a-zA-Z0-9 ]/g, "").trim().toLowerCase().replace(/\s+/g, "_").replace(/^_+|_+$/g, ""); 
        const imgSrc = `/extensions/ComfyUI-Kaleido/assets/${safeName}.jpg`;
        
        let dynamicDesc = customDescriptions[safeName] || "Select this to apply these precise semantic weights to your generative workflow.";

        const words = shortName.split(' ').filter(w => w.match(/[a-zA-Z]/));
        let initials = "✨";
        if(words.length >= 2) initials = (words[0][0] + words[1][0]).toUpperCase();
        else if(words.length === 1) initials = words[0].substring(0, 2).toUpperCase();

        const wrapper = document.createElement("div");
        wrapper.className = "kld-wrapper";
        wrapper.dataset.search = opt.toLowerCase(); 
        
        wrapper.innerHTML = `
            <div class="kld-cover">
                <img src="${imgSrc}" loading="lazy" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
                <div class="kld-placeholder" style="display:none">${initials}</div>
                <div class="kld-glare"></div> 
                <div class="kld-title-text">${shortName}</div>
            </div>
            <div class="kld-panel">
                <div class="kld-panel-tag">${tag}</div>
                <h3 class="kld-panel-name">${shortName}</h3>
                <div class="kld-panel-desc">
                    <span style="color:#a855f7; font-weight:bold;">Core Parameters:</span><br>
                    <span style="color:#fff; font-size:12px;">${opt}</span><br><br>
                    <span style="color:#ddd; line-height:1.6;">${dynamicDesc}</span>
                </div>
                <button class="kld-btn">Apply Selection</button>
            </div>
        `;

        wrapper.addEventListener('mousemove', (e) => {
            if (wrapper.classList.contains('expanded')) return;
            const rect = wrapper.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -15; 
            const rotateY = ((x - centerX) / centerX) * 15;
            wrapper.style.transition = 'transform 0.1s ease-out';
            wrapper.style.transform = `perspective(1000px) translateY(-10px) scale(1.05) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        wrapper.addEventListener('mouseleave', () => {
            if (wrapper.classList.contains('expanded')) return;
            wrapper.style.transition = 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1)';
            wrapper.style.transform = `perspective(1000px) translateY(0px) scale(1) rotateX(0deg) rotateY(0deg)`;
        });

        wrapper.querySelector('.kld-cover').onclick = (e) => {
            e.stopPropagation(); 
            if (wrapper.classList.contains('expanded')) {
                closeExpanded(); return;
            }
            if (expandedWrapper) closeExpanded();

            scene.style.overflow = 'hidden';

            const rect = wrapper.getBoundingClientRect();
            const modalRect = modal.getBoundingClientRect();
            
            const visualOffset = 160 * EXPAND_SCALE; 
            const targetX = modalRect.left + (modalRect.width / 2) - visualOffset;
            const targetY = modalRect.top + (modalRect.height / 2);

            const currentX = rect.left + (rect.width / 2);
            const currentY = rect.top + (rect.height / 2);

            const translateX = targetX - currentX;
            const translateY = targetY - currentY;

            wrapper.style.transition = 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1)';
            wrapper.style.transform = `translate(${translateX}px, ${translateY}px) scale(${EXPAND_SCALE}) rotateX(0deg) rotateY(0deg)`;
            
            wrapper.classList.add("expanded");
            scene.classList.add("has-expanded");
            expandedWrapper = wrapper;
        };

        wrapper.querySelector('.kld-btn').onclick = (e) => {
            e.stopPropagation();
            targetWidget.value = opt;
            if (targetWidget.callback) targetWidget.callback(opt);
            node.setDirtyCanvas(true);
            closeAll();
        };

        grid.appendChild(wrapper);
    });

    const closeExpanded = () => {
        if (!expandedWrapper) return;
        expandedWrapper.style.transition = 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1)';
        expandedWrapper.style.transform = `perspective(1000px) translateY(0px) scale(1) rotateX(0deg) rotateY(0deg)`; 
        expandedWrapper.classList.remove("expanded");
        scene.classList.remove("has-expanded");
        scene.style.overflow = 'auto'; 
        expandedWrapper = null;
    };

    modal.appendChild(header);
    modal.appendChild(scene);
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    requestAnimationFrame(() => overlay.classList.add("show"));

    const closeAll = () => {
        overlay.classList.remove("show");
        setTimeout(() => { if (document.body.contains(overlay)) overlay.remove(); }, 300);
    };

    header.querySelector(".kld-close").onclick = closeAll;
    scene.onclick = (e) => {
        if (e.target === scene || e.target === grid) {
            if (expandedWrapper) closeExpanded();
            else closeAll();
        }
    };

    const searchInput = header.querySelector(".kld-search");
    searchInput.oninput = (e) => {
        const keyword = e.target.value.toLowerCase();
        if(expandedWrapper) closeExpanded(); 
        
        const items = grid.querySelectorAll(".kld-wrapper");
        items.forEach(item => {
            const match = item.dataset.search.includes(keyword);
            item.style.display = match ? "block" : "none";
        });
    };
    setTimeout(() => searchInput.focus(), 100);
    
    document.addEventListener("keydown", function escHandler(e) {
        if (e.key === "Escape") { closeAll(); document.removeEventListener("keydown", escHandler); }
    });
}