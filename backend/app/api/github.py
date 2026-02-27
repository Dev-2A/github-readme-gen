from fastapi import APIRouter, HTTPException
from app.services.data_collector import collect_github_data

router = APIRouter(prefix="/github", tags=["github"])


@router.get("/user/{username}")
async def get_user_data(username: str):
    """GitHub 유저 활동 데이터 조회"""
    try:
        data = await collect_github_data(username)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))