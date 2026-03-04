import { useState, useRef } from "react";
import Header          from "./components/Header";
import Footer          from "./components/Footer";
import StepIndicator   from "./components/StepIndicator";
import UsernameForm    from "./components/UsernameForm";
import OptionsPanel    from "./components/OptionsPanel";
import UserCard        from "./components/UserCard";
import SkeletonCard    from "./components/SkeletonCard";
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

  const previewRef = useRef(null);

  // 현재 스텝 계산
  const currentStep = markdown ? 3 : profile ? 2 : 1;

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
      // 생성 완료 후 미리보기로 자동 스크롤
      setTimeout(() => {
        previewRef.current?.scrollIntoView({ behavior: "smooth", block: "start" });
      }, 100);
    } catch (e) {
      setGenError(e.message);
    } finally {
      setGenLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-pastel-50 py-10 px-4">
      <div className="max-w-5xl mx-auto">

        <Header />
        <StepIndicator currentStep={currentStep} />

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
                              rounded-2xl px-5 py-4 text-sm fade-in">
                ⚠️ {fetchError}
              </div>
            )}
            {fetchLoading && <SkeletonCard />}
            {!fetchLoading && !fetchError && !profile && (
              <div className="bg-white border-2 border-dashed border-pastel-200
                              rounded-2xl px-5 py-16 text-center text-gray-300 text-sm">
                <p className="text-4xl mb-3">🔍</p>
                <p>유저명을 입력하고</p>
                <p>생성 버튼을 눌러주세요</p>
              </div>
            )}
            {profile && (
              <div className="fade-in">
                <UserCard profile={profile} chartStyle={options.chart_style} />
              </div>
            )}
          </div>

        </div>

        {/* README 생성 버튼 */}
        {profile && (
          <div className="mt-5 fade-in">
            <GenerateButton
              onClick={handleGenerate}
              loading={genLoading}
              disabled={!profile}
            />
          </div>
        )}

        {/* 생성 에러 */}
        {genError && (
          <div className="mt-4 bg-red-50 border border-red-200 text-red-500
                          rounded-2xl px-5 py-4 text-sm fade-in">
            ⚠️ {genError}
          </div>
        )}

        {/* README 미리보기 */}
        {markdown && (
          <div ref={previewRef} className="mt-5 fade-in">
            <h2 className="text-pastel-500 font-bold text-sm mb-3 px-1">
              ✅ README 생성 완료! 아래에서 복사하거나 다운로드하세요.
            </h2>
            <ReadmePreview markdown={markdown} username={profile?.username} />
          </div>
        )}

        <Footer />
      </div>
    </div>
  );
}