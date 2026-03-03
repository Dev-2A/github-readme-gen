import { useState } from "react";
import UsernameForm    from "./components/UsernameForm";
import OptionsPanel    from "./components/OptionsPanel";
import UserCard        from "./components/UserCard";
import GenerateButton  from "./components/GenerateButton";
import ReadmePreview   from "./components/ReadmePreview";
import { fetchUserData, generateReadme } from "./api";

const DEFAULT_OPTIONS = {
  chart_style:    "pie",
  show_stats:     true,
  show_languages: true,
  show_repos:     true,
  custom_title:   "",
  custom_bio:     "",
};

export default function App() {
  const [profile,      setProfile]      = useState(null);
  const [options,      setOptions]      = useState(DEFAULT_OPTIONS);
  const [fetchLoading, setFetchLoading] = useState(false);
  const [genLoading,   setGenLoading]   = useState(false);
  const [fetchError,   setFetchError]   = useState("");
  const [genError,     setGenError]     = useState("");
  const [markdown,     setMarkdown]     = useState("");

  // 유저 데이터 불러오기
  const handleFetch = async (username) => {
    setFetchLoading(true);
    setFetchError("");
    setProfile(null);
    setMarkdown("");
    try {
      const data = await fetchUserData(username);
      setProfile(data);
    } catch (e) {
      setFetchError(e.message);
    } finally {
      setFetchLoading(false);
    }
  };

  // README 생성
  const handleGenerate = async () => {
    if (!profile) return;
    setGenLoading(true);
    setGenError("");
    setMarkdown("");
    try {
      const result = await generateReadme({
        ...options,
        username: profile.username,
      });
      setMarkdown(result.markdown);
    } catch (e) {
      setGenError(e.message);
    } finally {
      setGenLoading(false);
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

      {/* 메인 레이아웃 — 2단 그리드 */}
      <div className="max-w-5xl mx-auto space-y-5">

        {/* 상단: 입력 + 옵션 + 유저 카드 */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">

          {/* 왼쪽: 입력 + 옵션 */}
          <div className="space-y-4">
            <UsernameForm onSubmit={handleFetch} loading={fetchLoading} />
            <OptionsPanel options={options} onChange={setOptions} />
          </div>

          {/* 오른쪽: 유저 카드 */}
          <div className="space-y-4">
            {fetchError && (
              <div className="bg-red-50 border border-red-200 text-red-500
                              rounded-2xl px-5 py-4 text-sm">
                ⚠️ {fetchError}
              </div>
            )}
            {fetchLoading && (
              <div className="bg-white border border-pastel-200 rounded-2xl
                              px-5 py-10 text-center text-pastel-300 text-sm animate-pulse">
                GitHub 데이터를 불러오는 중...
              </div>
            )}
            {!fetchLoading && !fetchError && !profile && (
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

        {/* README 생성 버튼 */}
        {profile && (
          <GenerateButton
            onClick={handleGenerate}
            loading={genLoading}
            disabled={!profile}
          />
        )}

        {/* 에러 */}
        {genError && (
          <div className="bg-red-50 border border-red-200 text-red-500
                          rounded-2xl px-5 py-4 text-sm">
            ⚠️ {genError}
          </div>
        )}

        {/* 하단: README 미리보기 */}
        {markdown && (
          <ReadmePreview markdown={markdown} username={profile?.username} />
        )}

      </div>
    </div>
  );
}