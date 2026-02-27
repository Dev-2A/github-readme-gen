from app.services.github_client import get_user, get_repos, get_recent_commits
from app.services.parser import parse_github_data, GithubProfile


async def collect_github_data(raw: str) -> dict:
    """GitHub 활동 데이터를 종합 수집"""
    username = raw  # 기존 코드와 동일하게 유지
    user = await get_user(username)
    repos = await get_repos(username)
    commits = await get_recent_commits(username)

    lang_count: dict[str, int] = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            lang_count[lang] = lang_count.get(lang, 0) + 1

    total = sum(lang_count.values()) or 1
    lang_ratio = {
        lang: round(count / total * 100, 1)
        for lang, count in sorted(lang_count.items(), key=lambda x: -x[1])
    }

    top_repos = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:5]
    top_repos_data = [
        {
            "name": r["name"],
            "description": r.get("description") or "",
            "stars": r.get("stargazers_count", 0),
            "language": r.get("language") or "",
            "url": r.get("html_url", ""),
        }
        for r in top_repos
    ]

    recent_commit_count = sum(
        len(e.get("payload", {}).get("commits", []))
        for e in commits
    )

    return {
        "username": username,
        "name": user.get("name") or username,
        "bio": user.get("bio") or "",
        "avatar_url": user.get("avatar_url", ""),
        "followers": user.get("followers", 0),
        "following": user.get("following", 0),
        "public_repos": user.get("public_repos", 0),
        "lang_ratio": lang_ratio,
        "top_repos": top_repos_data,
        "recent_commit_count": recent_commit_count,
    }


async def collect_and_parse(username: str) -> GithubProfile:   # ← 추가
    """수집 + 파싱을 한 번에"""
    raw = await collect_github_data(username)
    return parse_github_data(raw)