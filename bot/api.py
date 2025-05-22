# bot/api.py
import random

async def analyze_message(content: str) -> dict: #백엔드 연결 전 임시 api
    """
    더미 백엔드: 50% 확률로 욕설 판단.
    """
    is_abusive = random.choice([True, False])
    return {
        "is_abusive": is_abusive,
        "sanitized": "검열된 메시지" if is_abusive else content
    }