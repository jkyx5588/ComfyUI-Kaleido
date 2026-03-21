import requests
import json
import time
import os
from server import PromptServer
from aiohttp import web
from PIL import Image
import io
import base64
import torch
import numpy as np

# 导入数据
from .lumina_data import COMMUNICATION_PLATFORMS

class LuminaLinkListenerNode:
    """
    v101.0 Kaleido Neural Link (Listener)
    Acts as a Gateway. It waits for an external signal (via HTTP) to trigger the workflow.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        platforms = sorted(list(COMMUNICATION_PLATFORMS.keys()))
        return {
            "required": {
                "platform": (platforms, {"default": "🌐 Local HTTP API"}),
                "listen_port": ("INT", {"default": 8888, "min": 1000, "max": 9999}),
                "poll_interval": ("FLOAT", {"default": 1.0, "tooltip": "Time in seconds to check for new messages."}),
            }
        }

    # 输出接收到的指令
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("📨 Received_Prompt", "👤 User_ID", "⚙️ Raw_Payload")
    
    FUNCTION = "listen_for_request"
    CATEGORY = "Kaleido/Infrastructure"
    
    # 这是一个特殊的逻辑：实际上 ComfyUI 节点很难做真正的“阻塞监听”而不卡死界面。
    # 这里我们采用一种“伪监听”或者“服务端扩展”的方式。
    # 为了简化实现，我们这里模拟一个“文件监听器”作为最安全的演示。
    # *高级实现需要编写 ComfyUI 的 __init__.py 中的 server.routes 扩展*
    
    def listen_for_request(self, platform, listen_port, poll_interval):
        # ⚠️ 注意：真正的 HTTP 监听需要在 ComfyUI 启动时注册路由。
        # 为了让这个节点即插即用，我们使用“文件桥接”模式作为 OpenClaw 的模拟。
        # 您可以在手机上用捷径写一个 txt 文件到电脑，这个节点读取它。
        
        bridge_file = "kaleido_request.txt"
        print(f"📡 Kaleido Link: Watching {bridge_file} for incoming signals...")
        
        # 简单的轮询逻辑 (模拟守护进程)
        # 在实际 ComfyUI 运行中，这会阻塞队列直到文件出现，适合“自动运行”模式
        timeout = 30 # 最多等30秒，防止死锁
        start_time = time.time()
        
        while (time.time() - start_time) < timeout:
            if os.path.exists(bridge_file):
                try:
                    with open(bridge_file, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                    
                    if content:
                        # 读取后删除文件，防止重复触发
                        os.remove(bridge_file)
                        print(f"📨 Signal Received: {content}")
                        return (content, "User_Local", json.dumps({"source": "file"}))
                except:
                    pass
            
            time.sleep(poll_interval)
            
        return ("No Signal", "None", "{}")

class LuminaLinkSenderNode:
    """
    v101.0 Kaleido Neural Link (Sender)
    Sends the result back to the user (e.g. via Discord Webhook or Telegram API).
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "webhook_url": ("STRING", {"default": "", "placeholder": "https://discord.com/api/webhooks/..."}),
                "message_text": ("STRING", {"default": "Here is your creation!", "multiline": True}),
                "image_input": ("IMAGE",),
            }
        }

    RETURN_TYPES = ()
    OUTPUT_NODE = True # 这是一个输出节点
    FUNCTION = "send_result"
    CATEGORY = "Kaleido/Infrastructure"

    def send_result(self, webhook_url, message_text, image_input):
        if not webhook_url or webhook_url == "":
            print("🚫 No Webhook URL provided.")
            return ()

        # 1. 处理图片
        try:
            i = 255. * image_input[0].cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            
            # 保存到内存
            img_bytes = io.BytesIO()
            img.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            
            # 2. 发送请求 (以 Discord Webhook 为例)
            # Discord 需要 multipart/form-data
            files = {
                'file': ('kaleido_result.png', img_bytes, 'image/png')
            }
            data = {
                'content': f"🌌 **Kaleido Generation**\n{message_text}"
            }
            
            print(f"🚀 Sending result to Webhook...")
            r = requests.post(webhook_url, data=data, files=files)
            
            if r.status_code in [200, 204]:
                print("✅ Delivery Successful!")
            else:
                print(f"❌ Delivery Failed: {r.status_code} - {r.text}")
                
        except Exception as e:
            print(f"❌ Link Error: {e}")

        return ()