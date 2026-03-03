from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from app.services.data_collector import collect_and_parse
from app.services.readme_builder import build_readme
from app.core.schemas import ReadmeResponse

router = APIRouter(prefix="/readme", tags=["readme"])


class ReadmeOptions(BaseModel):
    username: str
    chart_style: str = "pie"        # "pie" | "bar"
    show_repos: bool = True
    show_languages: bool = True
    show_stats: bool = True
    custom_title: str = ""
    custom_bio: str = ""


@router.post(
    "/generate",
    response_model=ReadmeResponse,
    summary="README 마크다운 생성",
)
async def generate_readme(options: ReadmeOptions):
    profile = await collect_and_parse(options.username)
    markdown = build_readme(
        profile=profile,
        chart_style=options.chart_style,
        show_repos=options.show_repos,
        show_languages=options.show_languages,
        show_stats=options.show_stats,
        custom_title=options.custom_title,
        custom_bio=options.custom_bio,
    )
    return ReadmeResponse(markdown=markdown, username=options.username)


@router.get(
    "/preview/{username}",
    response_class=PlainTextResponse,
    summary="README 마크다운 빠른 미리보기",
)
async def preview_readme(username: str, chart_style: str = "pie"):
    profile = await collect_and_parse(username)
    return build_readme(profile, chart_style=chart_style)