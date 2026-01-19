import sys
import os
import re
import base64
import google.generativeai as genai

# Gemini API 設定
genai.configure(
    api_key=os.environ["GEMINI_API_KEY_FOR_AI_SCREENSHOT_RENAMING_SYSTEM"]
)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def sanitize(name: str, max_len: int = 80) -> str:
    name = re.sub(r'[\/:*?"<>|]', '_', name)
    name = re.sub(r'\s+', '_', name)
    return name[:max_len]

# 対象画像パス
image_path = sys.argv[1]
dir_path = os.path.dirname(image_path)
ext = os.path.splitext(image_path)[1]

# 画像を base64 に変換
with open(image_path, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

prompt = (
    "This is a screenshot.\n"
    "Understand its content and generate a concise Japanese file name.\n"
    "Format: <Category>_<Summary>\n"
    "Categories: Slack, Notion, Browser, Code, Settings, Other\n"
    "Do not include file extension."
)

try:
    response = model.generate_content(
        [
            prompt,
            {
                "mime_type": "image/png",
                "data": image_b64
            }
        ]
    )

    title = sanitize(response.text.strip())
    new_path = os.path.join(dir_path, f"{title}{ext}")

    if not os.path.exists(new_path):
        os.rename(image_path, new_path)

except Exception as e:
    # 失敗時は何もしない（安全設計）
    pass


