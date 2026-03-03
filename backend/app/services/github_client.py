import httpx
from app.core.config import GITHUB_TOKEN, GITHUB_API_BASE
from app.core.exceptions import GithubAPIError, UserNotFoundError

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def _handle_response(res: httpx.Response, username: str = "") -> dict | list:
    if res.status_code == 404:
        raise UserNotFoundError(username)
    if res.status_code == 403:
        raise GithubAPIError("GitHub API 요청 한도 초과. 잠시 후 다시 시도해주세요.", 429)
    if res.status_code == 401:
        raise GithubAPIError("GitHub Token이 유효하지 않습니다.", 401)
    if not res.is_success:
        raise GithubAPIError(f"GitHub API 오류 (HTTP {res.status_code})", res.status_code)
    return res.json()


async def get_user(username: str) -> dict:
    async with httpx.AsyncClient(timeout=10.0) as client:
        res = await client.get(f"{GITHUB_API_BASE}/users/{username}", headers=HEADERS)
        return _handle_response(res, username)


async def get_repos(username: str) -> list:
    async with httpx.AsyncClient(timeout=10.0) as client:
        res = await client.get(
            f"{GITHUB_API_BASE}/users/{username}/repos",
            headers=HEADERS,
            params={"per_page": 100, "sort": "updated"},
        )
        return _handle_response(res, username)


async def get_recent_commits(username: str, days: int = 30) -> list:
    async with httpx.AsyncClient(timeout=10.0) as client:
        res = await client.get(
            f"{GITHUB_API_BASE}/users/{username}/events/public",
            headers=HEADERS,
            params={"per_page": 100},
        )
        events = _handle_response(res, username)
        return [e for e in events if e.get("type") == "PushEvent"]