# bot/api.py
import random

async def analyze_message(content: str) -> dict: #백엔드 연결 전 임시 api
    """
    더미 백엔드: 50% 확률로 욕설 판단.
    """
    is_abusive = random.choice([True, False])
    if is_abusive:
        return {
            "is_abusive": True,
            "sanitized": "검열된 메시지",
            "updated_score": random.randint(-10, -1)  # 더미 명예도 점수
        }
    else:
        return {
            "is_abusive": False,
            "sanitized": content,
            "updated_score": 0
        }