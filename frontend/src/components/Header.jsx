export default function Header() {
  return (
    <header className="text-center mb-10">
      {/* 로고 영역 */}
      <div className="inline-flex items-center justify-center
                      w-16 h-16 rounded-2xl bg-white border border-pastel-200
                      shadow-sm mb-4 text-3xl">
        🤖
      </div>
      <h1 className="text-2xl font-bold text-pastel-500 tracking-tight">
        GitHub 프로필 README 생성기
      </h1>
      <p className="text-sm text-gray-400 mt-1.5 max-w-sm mx-auto leading-relaxed">
        GitHub 활동 데이터로 SVG 배지·차트가 포함된
        <br className="hidden sm:block" />
        예쁜 프로필 README를 자동으로 만들어드립니다
      </p>
      {/* 기능 태그 */}
      <div className="flex flex-wrap justify-center gap-2 mt-4">
        {["GitHub API", "SVG 생성", "파스텔 블루 테마", "실시간 미리보기"].map((tag) => (
          <span
            key={tag}
            className="bg-pastel-100 text-pastel-500 text-xs font-medium
                       px-3 py-1 rounded-full border border-pastel-200"
          >
            {tag}
          </span>
        ))}
      </div>
    </header>
  );
}