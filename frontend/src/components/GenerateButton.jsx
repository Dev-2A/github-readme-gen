export default function GenerateButton({ onClick, loading, disabled }) {
  return (
    <button
      onClick={onClick}
      disabled={loading || disabled}
      className="w-full py-3 rounded-2xl font-bold text-sm transition-all
                 bg-pastel-400 hover:bg-pastel-500 text-white shadow-sm
                 disabled:bg-pastel-200 disabled:cursor-not-allowed
                 active:scale-95"
    >
      {loading
        ? "⏳ README 생성 중..."
        : "✨ README 생성하기"}
    </button>
  );
}