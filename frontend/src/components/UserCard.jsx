import { getProfileBadgeUrl, getChartUrl } from "../api";

export default function UserCard({ profile, chartStyle }) {
  if (!profile) return null;

  return (
    <div className="bg-white border border-pastel-200 rounded-2xl p-5 shadow-sm space-y-3">
      <div className="flex items-center gap-3">
        <img
          src={profile.avatar_url}
          alt={profile.username}
          className="w-12 h-12 rounded-full border-2 border-pastel-200"
        />
        <div>
          <p className="font-bold text-pastel-500 text-sm">{profile.name}</p>
          <p className="text-xs text-gray-400">@{profile.username}</p>
        </div>
        <div className="ml-auto flex gap-3 text-xs text-gray-500">
          <span>👥 {profile.followers}</span>
          <span>📁 {profile.public_repos}</span>
        </div>
      </div>

      {profile.bio && (
        <p className="text-sm text-gray-500 italic border-l-2 border-pastel-200 pl-3">
          {profile.bio}
        </p>
      )}

      {/* SVG 프리뷰 (백엔드에서 직접) */}
      <div className="space-y-2">
        <img
          src={getProfileBadgeUrl(profile.username)}
          alt="profile badge"
          className="w-full"
        />
        <img
          src={getChartUrl(profile.username, chartStyle)}
          alt="language chart"
          className="w-full"
        />
      </div>

      {/* 상위 언어 태그 */}
      {profile.top_languages?.length > 0 && (
        <div className="flex flex-wrap gap-1.5 pt-1">
          {profile.top_languages.map((lang) => (
            <span
              key={lang}
              className="bg-pastel-100 text-pastel-500 text-xs font-medium
                         px-2.5 py-0.5 rounded-full border border-pastel-200"
            >
              {lang}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}