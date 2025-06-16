# 🤝 Contributing to discord_bot

이 문서는 `discord_bot`에 기여하기 위해 필요한 가이드라인을 안내합니다.

기여자라면 아래 내용을 숙지한 후 Pull Request를 올려 주세요.

---

## 📦 프로젝트 개요

- 이 봇은 Discord 채널의 메시지를 실시간으로 감지하여, 악성 발언을 필터링하고 순화된 메시지로 대체하는 시스템입니다.
- 프론트엔드는 Python 기반의 Discord Client로 구현되어 있으며, 백엔드 서버와 REST API를 통해 연동됩니다.

---

## 📋 기여 전에

- 먼저 [Issues](https://github.com/ROOM1ghouls/discord_bot/issues) 탭에서 **중복된 이슈가 없는지 확인**해주세요.
- 개선 제안이나 버그 신고는 자유롭게 **이슈로 등록**해 주세요.
- 코드 변경 전에는 반드시 **해당 기능의 책임 영역을 확인**해야 합니다. 예:
    - `main.py`: 전체 메시지 처리 흐름 (수정 시 리뷰 필요)
    - `bot/api.py`: 백엔드 API 통신 관련 기능
    - `bot/webhook.py`: 메시지 전송 로직

---

## 🛠️ 로컬 개발 환경 설정

1. 프로젝트 클론 후 의존성 설치:

```bash
pip install -r requirements.txt
```

2. `.env` 파일 생성:

```
DISCORD_TOKEN=your_token_here
BACKEND_BASE_URL=https://agaricleaner.onrender.com
```

3. 실행:

```bash
python main.py
```

---

## ✅ PR 전 체크리스트

- [ ] 기존 기능을 **깨뜨리지 않았는지 확인**했나요?
- [ ] 커밋 메시지는 **명확한 동사와 함께 작성**했나요? (`Fix`, `Add`, `Refactor` 등)
- [ ] 문서 또는 주석을 **필요한 곳에 추가**했나요?

---

## 💬 커밋 메시지 규칙

### 기본 형식:

```
[type]: [변경 요약]

[선택 사항: 상세 설명]
```

### 타입 예시:

- `Add`: 새로운 기능 추가
- `Fix`: 버그 수정
- `Refactor`: 코드 구조 개선
- `Docs`: 문서 수정
- `Test`: 테스트 추가/수정

---

## 🧷 코드 컨벤션

- 변수명: `snake_case`
- 함수/클래스에는 가능한 한 `docstring` 작성
- 하나의 함수에 너무 많은 논리를 몰아넣지 말고 **역할에 따라 분리**

---

## 🚫 금지사항

- 외부 패키지 추가 시 반드시 **이슈/PR로 논의 후 결정**
- 백엔드 API 명세를 수정할 경우, **사전 공유 필수**
- `main.py`의 **비동기 큐/세마포어 워커 구조는 무단 수정 금지**

---

## 🙌 기여자 목록에 이름을 추가하고 싶다면?

Pull Request가 머지되면, **관리자가 `CONTRIBUTORS.md` 및 `README.md`에 기여자 이름을 수동으로 추가**합니다.

고마운 마음을 담아, 모든 기여자는 기록됩니다!
