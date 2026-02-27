from app.services.github_client import get_user, get_repos, get_recent_commits


async def collect_github_data(username: str) -> dict:
    """GitHub 활동 데이터를 종합 수집"""
    user = await get_user(username)
    repos = await get_repos(username)
    commits = await get_recent_commits(username)
    
    # 언어 비율 계산
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
    
    # 스타 많은 레포 Top 5
    top_repos = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:5]
    top_repos_data = [
        {
            "name": r["name"],
            "description": r.get("description") or "",
            "stars": r.get("stargazers_count", 0),
            
        }
        for r in top_repos
    ]
    
    # 최근 커밋 수
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