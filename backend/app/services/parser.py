from dataclasses import dataclass, field


@dataclass
class RepoInfo:
    name: str
    description: str
    stars: int
    language: str
    url: str


@dataclass
class GithubProfile:
    username: str
    name: str
    bio: str
    avatar_url: str
    followers: int
    following: int
    public_repos: int
    lang_ratio: dict[str, float]        # {"Python": 45.0, "TypeScript": 30.0, ...}
    top_repos: list[RepoInfo]
    recent_commit_count: int
    top_languages: list[str] = field(default_factory=list)      # 상위 5개 언어명
    
    def __post_init__(self):
        self.top_languages = list(self.lang_ratio.keys())[:5]


def parse_github_data(raw: dict) -> GithubProfile:
    """collect_github_data() 결과를 GithubProfile 데이터클래스로 변환"""
    top_repos = [
        RepoInfo(
            name=r["name"],
            description=r["description"],
            stars=r["stars"],
            language=r["language"],
            url=r["url"],
        )
        for r in raw.get("top_repos", [])
    ]
    
    return GithubProfile(
        username=raw["username"],
        name=raw["name"],
        bio=raw["bio"],
        avatar_url=raw["avatar_url"],
        followers=raw["followers"],
        following=raw["following"],
        public_repos=raw["public_repos"],
        lang_ratio=raw["lang_ratio"],
        top_repos=top_repos,
        recent_commit_count=raw["recent_commit_count"],
    )