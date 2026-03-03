import { useState } from "react";

export default function UsernameForm({ onSubmit, loading }) {
  const [input, setInput] = useState("");

  const handleSubmit = () => {
    const trimmed = input.trim();
    if (!trimmed) return;
    onSubmit(trimmed);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") handleSubmit();
  };

  return (
    <div className="bg-white border border-pastel-200 rounded-2xl p-5 shadow-sm">
      <h2 className="text-pastel-500 font-bold text-base mb-3">🔍 GitHub 유저명 입력</h2>
      <div className="flex gap-2">
        <input
          type="text"
          placeholder="예: Dev-2A"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
          className="flex-1 border border-pastel-200 rounded-xl px-4 py-2.5 text-sm
                     focus:outline-none focus:ring-2 focus:ring-pastel-300 text-gray-700
                     disabled:bg-gray-50 disabled:text-gray-400"
        />
        <button
          onClick={handleSubmit}
          disabled={loading || !input.trim()}
          className="bg-pastel-400 hover:bg-pastel-500 disabled:bg-pastel-200
                     text-white font-semibold px-5 py-2.5 rounded-xl text-sm
                     transition-all disabled:cursor-not-allowed"
        >
          {loading ? "⏳ 로딩 중..." : "🚀 생성"}
        </button>
      </div>
    </div>
  );
}