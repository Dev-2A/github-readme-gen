from fastapi import Request
from fastapi.responses import JSONResponse


class GithubAPIError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


class UserNotFoundError(GithubAPIError):
    def __init__(self, username: str):
        super().__init__(f"GitHub 유저를 찾을 수 없습니다: '{username}'", status_code=404)


async def github_api_error_handler(request: Request, exc: GithubAPIError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message},
    )