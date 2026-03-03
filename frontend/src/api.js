const BASE = "http://localhost:8000";

export async function fetchUserData(username) {
  const res = await fetch(`${BASE}/github/user/${username}`);
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.error || "유저 정보를 불러올 수 없습니다.");
  }
  return res.json();
}

export async function generateReadme(options) {
  const res = await fetch(`${BASE}/readme/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(options),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.error || "README 생성에 실패했습니다.");
  }
  return res.json();
}

export function getChartUrl(username, style = "pie") {
  return `${BASE}/chart/languages/${username}?style=${style}`;
}

export function getProfileBadgeUrl(username) {
  return `${BASE}/badge/profile/${username}`;
}