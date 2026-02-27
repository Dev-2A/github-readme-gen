import httpx
from app.core.config import GITHUB_TOKEN, GITHUB_API_BASE

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


async def get_user(username: str) -> dict:
    """유저 기본 정보 조회"""
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{GITHUB_API_BASE}/users/{username}", headers=HEADERS)
        res.raise_for_status()
        return res.json()


async def get_repos(username: str) -> list:
    """퍼블릭 레포 전체 조회 (최대 100개)"""
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{GITHUB_API_BASE}/users/{username}/repos",
            headers=HEADERS,
            params={"per_page": 100, "sort": "updated"},
        )
        res.raise_for_status()
        return res.json()


async def get_recent_commits(username: str, days: int = 30) -> list:
    """최근 커밋 이벤트 조회"""
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{GITHUB_API_BASE}/users/{username}/events/public",
            headers=HEADERS,
            params={"per_page": 100},
        )
        res.raise_for_status()
        events = res.json()
        # PushEvent만 필터링
        return [e for e in events if e.get("type") == "PushEvent"]