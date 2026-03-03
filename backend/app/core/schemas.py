from pydantic import BaseModel


class RepoInfo(BaseModel):
    name: str
    description: str
    stars: int
    language: str
    url: str


class GithubProfileResponse(BaseModel):
    username: str
    name: str
    bio: str
    avatar_url: str
    followers: int
    following: int
    public_repos: int
    lang_ratio: dict[str, float]
    top_repos: list[RepoInfo]
    recent_commit_count: int
    top_languages: list[str]


class ReadmeResponse(BaseModel):
    username: str
    markdown: str


class HealthResponse(BaseModel):
    status: str
    version: str