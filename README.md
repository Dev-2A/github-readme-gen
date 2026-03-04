# 🤖 GitHub 프로필 README 자동 생성기

GitHub API로 활동 데이터를 수집하고, SVG 배지·차트가 포함된  
프로필 README를 자동으로 생성해주는 웹 서비스입니다.

![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)

---

## ✨ 주요 기능

- **GitHub 활동 데이터 수집:** 언어 비율, 최근 커밋 수, 스타 많은 레포 등
- **SVG 직접 생성:** 외부 라이브러리 없이 배지·파이차트·바차트·레포 카드 생성
- **파스텔 블루 테마:** 커스터마이징 가능한 일관된 디자인 시스템
- **실시간 미리보기:** 생성된 README를 렌더링 미리보기 및 Raw 모드로 확인
- **복사 / 다운로드:** 클립보드 복사 및 `.md` 파일 다운로드 지원
- **커스터마이징 옵션:** 타이틀·바이오 직접 입력, 섹션 표시 여부, 차트 스타일 선택

---

## 🛠 기술 스택

| 영역 | 기술 |
| --- | --- |
| Backend | Python 3.11+, FastAPI, httpx |
| Frontend | React 18, Vite, Tailwind CSS 3 |
| SVG | 직접 생성 (외부 라이브러리 미사용) |
| 데이터 | GitHub REST API v3 |

---

## 📁 프로젝트 구조

```text
github-readme-gen/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI 라우터 (github, badge, chart, readme)
│   │   ├── core/         # 설정, 상수, 예외, 스키마
│   │   ├── services/     # GitHub API 클라이언트, 데이터 수집·파싱, README 조립
│   │   └── svg/          # SVG 배지·차트 생성기
│   ├── main.py
│   └── requirements.txt
└── frontend/
    └── src/
        ├── components/   # React 컴포넌트
        ├── App.jsx
        └── api.js        # 백엔드 API 호출 유틸
```

---

## 🚀 실행 방법

### 사전 준비

1. Python 3.11 이상
2. Node.js 18 이상
3. GitHub Personal Access Token 발급  
   → GitHub Settings → Developer settings → Personal access tokens → `repo`, `read:user` 권한

---

### 백엔드 실행

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate 

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

`.env` 파일 생성:

```env
GITHUB_TOKEN=여기에_토큰_입력
```

서버 시작:

```bash
uvicorn main:app --reload
```

→ `http://localhost:8000/docs` 에서 API 문서 확인 가능

---

### 프론트엔드 실행

```bash
cd frontend
npm install
npm run dev
```

→ `http://localhost:5173` 에서 앱 실행

---

## 🖥 사용 방법

1. GitHub 유저명 입력 후 **🚀 생성** 클릭
2. 오른쪽에서 프로필 카드·언어 차트 미리보기 확인
3. 옵션 패널에서 차트 스타일·섹션·타이틀·바이오 조정
4. **✨ README 생성하기** 클릭
5. 미리보기 탭에서 결과 확인 후 **복사** 또는 **다운로드**
6. 본인 GitHub 프로필 레포 (`username/username`)의 `README.md`에 붙여넣기

---

## 📡 API 엔드포인트

| Method | 경로 | 설명 |
| --- | --- | --- |
| GET | `/github/user/{username}` | 유저 활동 데이터 조회 |
| GET | `/badge/profile/{username}` | 프로필 요약 배지 SVG |
| GET | `/badge/label?text=...` | 단색 라벨 배지 SVG |
| GET | `/chart/languages/{username}` | 언어 비율 차트 SVG |
| GET | `/chart/repos/{username}` | 스타 레포 카드 SVG |
| POST | `/readme/generate` | README 마크다운 생성 |
| GET | `/readme/preview/{username}` | README 빠른 미리보기 |
| GET | `/health` | 서버 상태 확인 |

---

## 📝 License

[MIT] (./LICENSE)
