from fastapi import APIRouter
from app.services.data_collector import collect_and_parse
from app.core.schemas import GithubProfileResponse
from app.core.exceptions import GithubAPIError

router = APIRouter(prefix="/github", tags=["github"])


@router.get(
    "/user/{username}",
    response_model=GithubProfileResponse,
    summary="GitHub 유저 활동 데이터 조회",
)
async def get_user_data(username: str):
    profile = await collect_and_parse(username)
    return {
        "username": profile.username,
        "name": profile.name,
        "bio": profile.bio,
        "avatar_url": profile.avatar_url,
        "followers": profile.followers,
        "following": profile.following,
        "public_repos": profile.public_repos,
        "lang_ratio": profile.lang_ratio,
        "top_repos": [
            {
                "name": r.name,
                "description": r.description,
                "stars": r.stars,
                "language": r.language,
                "url": r.url,
            }
            for r in profile.top_repos
        ],
        "recent_commit_count": profile.recent_commit_count,
        "top_languages": profile.top_languages,
    }