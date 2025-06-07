# bot/api.py
import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()
BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")

_session: aiohttp.ClientSession | None = None

def get_session() -> aiohttp.ClientSession:
    global _session
    if _session is None or _session.closed:
        _session = aiohttp.ClientSession(json_serialize=lambda x: x)  # 빠른 json
    return _session


async def analyze_message(content: str, server_id: int, user_id: int) -> dict:
    try:
        async with get_session().post(
                f"{BACKEND_BASE_URL}/users/{server_id}/{user_id}",
                params={"message": content}
        ) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    "is_abusive": data["is_toxic"],
                    "sanitized": content,  # 아직 검열된 메시지는 아님
                    "updated_score": data["score"]
                }
            else:
                print(f"[Backend Error] analyze_message() - Status: {response.status}")
                return {
                    "is_abusive": False,
                    "sanitized": content,
                    "updated_score": 0
                }
    except Exception as e:
        print(f"[analyze_message Error] {e}")
        return {
            "is_abusive": False,
            "sanitized": content,
            "updated_score": 0
        }


async def transform_with_openai(content: str) -> str:
    try:
        async with get_session().get(
            f"{BACKEND_BASE_URL}/gpt/",
            params={"content": content}
        ) as response:
            if response.status == 200:
                data = await response.json()
                return data["sanitized"]
            else:
                print(f"[Backend Error] transform_with_openai() - Status: {response.status}")
                return "⚠️ 검열 실패"
    except Exception as e:
        print(f"[transform_with_openai Error] {e}")
        return "⚠️ 검열 실패"