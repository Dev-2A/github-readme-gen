export default function OptionsPanel({ options, onChange }) {
  const toggle = (key) => onChange({ ...options, [key]: !options[key] });
  const set    = (key, val) => onChange({ ...options, [key]: val });

  return (
    <div className="bg-white border border-pastel-200 rounded-2xl p-5 shadow-sm space-y-5">
      <h2 className="text-pastel-500 font-bold text-base">⚙️ 옵션 설정</h2>

      {/* 차트 스타일 */}
      <div>
        <p className="text-sm text-pastel-500 font-semibold mb-2">언어 차트 스타일</p>
        <div className="flex gap-2">
          {["pie", "bar"].map((style) => (
            <button
              key={style}
              onClick={() => set("chart_style", style)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition-all ${
                options.chart_style === style
                  ? "bg-pastel-400 text-white border-pastel-400"
                  : "bg-white text-pastel-400 border-pastel-200 hover:border-pastel-400"
              }`}
            >
              {style === "pie" ? "🥧 파이차트" : "📊 바차트"}
            </button>
          ))}
        </div>
      </div>

      {/* 섹션 표시 토글 */}
      <div>
        <p className="text-sm text-pastel-500 font-semibold mb-2">표시할 섹션</p>
        <div className="space-y-2">
          {[
            { key: "show_stats",     label: "📊 통계 배지" },
            { key: "show_languages", label: "🗂 언어 차트" },
            { key: "show_repos",     label: "⭐ 스타 레포" },
          ].map(({ key, label }) => (
            <label key={key} className="flex items-center gap-2 cursor-pointer select-none">
              <input
                type="checkbox"
                checked={options[key]}
                onChange={() => toggle(key)}
                className="accent-pastel-400 w-4 h-4"
              />
              <span className="text-sm text-gray-600">{label}</span>
            </label>
          ))}
        </div>
      </div>

      {/* 커스텀 타이틀 */}
      <div>
        <p className="text-sm text-pastel-500 font-semibold mb-1">커스텀 타이틀</p>
        <input
          type="text"
          placeholder="예: Hi, I'm 2A 👋 (비워두면 자동)"
          value={options.custom_title}
          onChange={(e) => set("custom_title", e.target.value)}
          className="w-full border border-pastel-200 rounded-lg px-3 py-2 text-sm
                     focus:outline-none focus:ring-2 focus:ring-pastel-300 text-gray-700"
        />
      </div>

      {/* 커스텀 바이오 */}
      <div>
        <p className="text-sm text-pastel-500 font-semibold mb-1">커스텀 바이오</p>
        <textarea
          rows={2}
          placeholder="예: AI/ML 엔지니어 | 전직 사서 (비워두면 GitHub bio 사용)"
          value={options.custom_bio}
          onChange={(e) => set("custom_bio", e.target.value)}
          className="w-full border border-pastel-200 rounded-lg px-3 py-2 text-sm
                     focus:outline-none focus:ring-2 focus:ring-pastel-300 text-gray-700 resize-none"
        />
      </div>
    </div>
  );
}