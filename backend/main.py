from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.github import router as github_router
from app.api.badge import router as badge_router
from app.api.chart import router as chart_router
from app.api.readme import router as readme_router

app = FastAPI(
    title="GitHub README Generator",
    description="GitHub 활동 데이터로 프로필 README를 자동 생성하는 API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],    # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(github_router)
app.include_router(badge_router)
app.include_router(chart_router)
app.include_router(readme_router)

@app.get("/")
def root():
    return {"message": "GitHub README Generator API"}