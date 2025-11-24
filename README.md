# Chomsky AI - CTTechnologies

고급스럽고 따뜻한 AI 챗봇 서비스

## 🚀 Cloudtype 배포 가이드 (한 번에 배포!)

### 사전 준비
1. [Cloudtype](https://cloudtype.io/) 회원가입 및 로그인
2. GLM API 키 발급 ([Z.ai 플랫폼](https://open.bigmodel.cn/) 또는 [Z.ai Global](https://z.ai/))
3. GitHub 저장소에 코드 푸시 (권장)

---

## 📋 배포 단계 (5분 완성!)

### 1단계: Cloudtype 프로젝트 생성
- Cloudtype 대시보드 → **"새 프로젝트"** 클릭
- GitHub 저장소 연결 또는 파일 직접 업로드

### 2단계: 빌드 설정
- **빌드 경로**: `backend`
- **실행 명령어**: `gunicorn app:app`
- **포트**: `5000`

### 3단계: 환경 변수 설정
```
GLM_API_KEY=your_glm_api_key_here
PORT=5000
```

### 4단계: 배포!
- **"배포"** 버튼 클릭
- 완료! 🎉

### 5단계: 확인
- 배포된 URL로 접속 (예: `https://chomsky.cloudtype.app`)
- 채팅 시작!

---

## ✅ 핵심 포인트

✨ **백엔드와 프론트엔드가 하나의 프로젝트로 배포됩니다!**
- Flask가 프론트엔드 HTML도 함께 서빙
- 별도의 프론트엔드 배포 불필요
- CORS 문제 없음
- 관리 간편

---

## 📁 프로젝트 구조

```
chomsky-ai/
├── backend/
│   ├── app.py              # Flask 서버 (프론트엔드 서빙 포함)
│   ├── requirements.txt    # Python 의존성
│   ├── Procfile           # Cloudtype 실행 명령
│   └── .env.example       # 환경 변수 예시
├── frontend/
│   └── index.html         # React 챗봇 UI
├── README.md
└── .gitignore
```

---

## 🔧 로컬 개발

### 실행 방법
```bash
# 1. 백엔드 디렉토리로 이동
cd backend

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 환경 변수 설정
cp .env.example .env
# .env 파일을 열어서 GLM_API_KEY를 입력하세요

# 5. 서버 실행
python app.py
```

### 접속
- 브라우저에서 `http://localhost:5000` 열기
- 채팅 시작! ✨

---

## 🎨 디자인 특징

- **폰트**: 
  - Cormorant Garamond (로고) - 우아한 세리프
  - Raleway (본문) - 세련된 산세리프
- **색상**: 
  - 따뜻한 베이지 (#f5f1e8)
  - 고급스러운 브라운 (#8b7355)
- **스타일**: 
  - 그라데이션 배경
  - 글라스모피즘 효과
  - 부드러운 애니메이션
- **반응형**: 모바일/태블릿/데스크톱 최적화

---

## 🔑 환경 변수

### 필수
- `GLM_API_KEY`: GLM-4.5-Flash API 키

### 선택
- `PORT`: 서버 포트 (기본값: 5000)

---

## 📝 API 엔드포인트

### GET `/`
프론트엔드 HTML 서빙

### GET `/api/health`
서버 상태 확인
```json
{
  "status": "healthy",
  "service": "Chomsky AI by CTTechnologies"
}
```

### POST `/api/chat`
챗봇 메시지 전송
```json
// Request
{
  "messages": [
    {"role": "user", "content": "안녕하세요"}
  ]
}

// Response
{
  "success": true,
  "message": "안녕하세요! 무엇을 도와드릴까요?"
}
```

---

## 💡 문제 해결

### 1. 배포 후 페이지가 안 보여요
✅ **해결**: 
- Cloudtype에서 빌드 경로가 `backend`로 설정되었는지 확인
- `/` 경로로 접속 (예: `https://your-app.cloudtype.app/`)

### 2. API 키 오류
✅ **해결**:
- Cloudtype 환경 변수에 `GLM_API_KEY` 올바르게 입력했는지 확인
- [Z.ai 콘솔](https://open.bigmodel.cn/)에서 API 키 유효성 확인

### 3. 채팅 응답이 안 와요
✅ **해결**:
- 브라우저 개발자 도구(F12) → Network 탭에서 `/api/chat` 요청 확인
- 응답 에러 메시지 확인
- GLM API 크레딧 잔액 확인

### 4. 로컬에서 실행 안 돼요
✅ **해결**:
- `backend` 디렉토리에서 실행 중인지 확인
- `.env` 파일에 `GLM_API_KEY` 입력했는지 확인
- 가상환경 활성화 확인: `which python` (venv 경로여야 함)

---

## 📌 배포 체크리스트

배포 전 확인:
- [ ] GLM API 키 발급 완료
- [ ] GitHub에 코드 푸시 (권장)
- [ ] Cloudtype 계정 생성

배포 설정:
- [ ] 빌드 경로: `backend`
- [ ] 실행 명령어: `gunicorn app:app`
- [ ] 포트: `5000`
- [ ] 환경 변수: `GLM_API_KEY` 입력

배포 후 확인:
- [ ] URL로 접속 확인
- [ ] 페이지 로딩 확인
- [ ] 메시지 전송 테스트 성공

---

## 🌟 특징

- ✅ **완전 무료 AI**: GLM-4.5-Flash 사용
- ✅ **한 번에 배포**: 백엔드+프론트엔드 통합
- ✅ **고급스러운 UI**: 따뜻하고 세련된 디자인
- ✅ **빠른 응답**: 경량화된 구조
- ✅ **반응형 디자인**: 모든 기기 지원

---

## 📞 지원

**Chomsky AI** by **CTTechnologies**

© 2024 CTTechnologies. All rights reserved.

