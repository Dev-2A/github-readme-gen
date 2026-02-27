from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from app.services.data_collector import collect_and_parse
from app.svg.badge import make_stat_badge, make_label_badge, make_profile_badge

router = APIRouter(prefix="/badge", tags=["badge"])


@router.get("/stat/{username}")
async def stat_badge(username: str, label: str = "Followers", value: str = ""):
    """단순 통계 배지 반환"""
    svg = make_stat_badge(label, value or "N/A")
    return Response(content=svg, media_type="image/svg+xml")


@router.get("/profile/{username}")
async def profile_badge(username: str):
    """프로필 요약 배지 생성"""
    try:
        p = await collect_and_parse(username)
        svg = make_profile_badge(
            name=p.name,
            username=p.username,
            followers=p.followers,
            following=p.following,
            public_repos=p.public_repos,
        )
        return Response(content=svg, media_type="image/svg+xml")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/label")
async def label_badge(text: str, color: str = ""):
    """단색 라벨 배지 반환"""
    svg = make_label_badge(text, color or None)
    return Response(content=svg, media_type="image/svg+xml")