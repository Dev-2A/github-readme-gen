from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.github import router as github_router
from app.api.badge import router as badge_router
from app.api.chart import router as chart_router
from app.api.readme import router as readme_router
from app.core.exceptions import GithubAPIError, github_api_error_handler
from app.core.schemas import HealthResponse

app = FastAPI(
    title="GitHub README Generator",
    description="GitHub 활동 데이터로 프로필 README를 자동 생성하는 API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 커스텀 에러 핸들러 등록
app.add_exception_handler(GithubAPIError, github_api_error_handler)

# 라우터 등록
app.include_router(github_router)
app.include_router(badge_router)
app.include_router(chart_router)
app.include_router(readme_router)


@app.get("/")
def root():
    return {"message": "GitHub README Generator API"}


@app.get("/health", response_model=HealthResponse, tags=["health"])
def health_check():
    """서버 상태 확인"""
    return HealthResponse(status="ok", version="0.1.0")