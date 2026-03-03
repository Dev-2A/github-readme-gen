import { useState } from "react";
import UsernameForm from "./components/UsernameForm";
import OptionsPanel from "./components/OptionsPanel";
import UserCard from "./components/UserCard";
import { fetchUserData } from "./api";

const DEFAULT_OPTIONS = {
  chart_style:    "pie",
  show_stats:     true,
  show_languages: true,
  show_repos:     true,
  custom_title:   "",
  custom_bio:     "",
};

export default function App() {
  const [profile, setProfile] = useState(null);
  const [options, setOptions] = useState(DEFAULT_OPTIONS);
  const [loading, setLoading] = useState(false);
  const [error,   setError]   = useState("");

  const handleSubmit = async (username) => {
    setLoading(true);
    setError("");
    setProfile(null);
    try {
      const data = await fetchUserData(username);
      setProfile(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-pastel-50 py-10 px-4">
      {/* 헤더 */}
      <div className="text-center mb-8">
        <h1 className="text-2xl font-bold text-pastel-500">
          🤖 GitHub 프로필 README 생성기
        </h1>
        <p className="text-sm text-gray-400 mt-1">
          GitHub 활동 데이터로 예쁜 프로필 README를 자동 생성해드립니다
        </p>
      </div>

      {/* 메인 레이아웃 */}
      <div className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-5">

        {/* 왼쪽: 입력 + 옵션 */}
        <div className="space-y-4">
          <UsernameForm onSubmit={handleSubmit} loading={loading} />
          <OptionsPanel options={options} onChange={setOptions} />
        </div>

        {/* 오른쪽: 유저 카드 미리보기 */}
        <div>
          {error && (
            <div className="bg-red-50 border border-red-200 text-red-500
                            rounded-2xl px-5 py-4 text-sm">
              ⚠️ {error}
            </div>
          )}
          {loading && (
            <div className="bg-white border border-pastel-200 rounded-2xl
                            px-5 py-10 text-center text-pastel-300 text-sm animate-pulse">
              GitHub 데이터를 불러오는 중...
            </div>
          )}
          {!loading && !error && !profile && (
            <div className="bg-white border-2 border-dashed border-pastel-200
                            rounded-2xl px-5 py-10 text-center text-gray-300 text-sm">
              유저명을 입력하고 생성 버튼을 눌러주세요 🚀
            </div>
          )}
          {profile && (
            <UserCard profile={profile} chartStyle={options.chart_style} />
          )}
        </div>

      </div>
    </div>
  );
}