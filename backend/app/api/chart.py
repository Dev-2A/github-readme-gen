from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response
from app.services.data_collector import collect_and_parse
from app.svg.chart import make_pie_chart, make_bar_chart, make_repo_card

router = APIRouter(prefix="/chart", tags=["chart"])


@router.get("/languages/{username}")
async def language_pie(
    username: str,
    style: str = Query("pie", description="pie 또는 bar"),
):
    """언어 비율 차트 SVG 반환"""
    try:
        p = await collect_and_parse(username)
        if style == "bar":
            svg = make_bar_chart(p.lang_ratio)
        else:
            svg = make_pie_chart(p.lang_ratio)
        return Response(content=svg, media_type="image/svg+xml")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/repos/{username}")
async def repo_cards(username: str):
    """스타 Top 레포 카드 목록 SVG 반환 (JSON 배열)"""
    try:
        p = await collect_and_parse(username)
        cards = [
            make_repo_card(
                name=r.name,
                description=r.description,
                stars=r.stars,
                language=r.language,
                url=r.url,
            )
            for r in p.top_repos
        ]
        # 첫 번째 카드만 SVG로, 나머지는 JSON으로 내려줘도 됨
        # 여기선 첫 번째 카드 SVG 반환 (미리보기용)
        return Response(content=cards[0] if cards else "", media_type="image/svg+xml")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))