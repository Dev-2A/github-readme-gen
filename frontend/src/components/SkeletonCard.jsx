function SkeletonBlock({ className }) {
  return (
    <div className={`bg-pastel-100 rounded-lg animate-pulse ${className}`} />
  );
}

export default function SkeletonCard() {
  return (
    <div className="bg-white border border-pastel-200 rounded-2xl p-5 shadow-sm space-y-4">
      {/* 아바타 + 이름 */}
      <div className="flex items-center gap-3">
        <SkeletonBlock className="w-12 h-12 rounded-full" />
        <div className="space-y-2 flex-1">
          <SkeletonBlock className="h-3.5 w-28" />
          <SkeletonBlock className="h-3 w-20" />
        </div>
        <div className="flex gap-3">
          <SkeletonBlock className="h-3 w-10" />
          <SkeletonBlock className="h-3 w-10" />
        </div>
      </div>
      {/* bio */}
      <SkeletonBlock className="h-3 w-3/4" />
      {/* 프로필 배지 */}
      <SkeletonBlock className="h-24 w-full rounded-xl" />
      {/* 차트 */}
      <SkeletonBlock className="h-48 w-full rounded-xl" />
      {/* 언어 태그 */}
      <div className="flex gap-2">
        {[60, 72, 56, 80, 64].map((w, i) => (
          <SkeletonBlock key={i} className={`h-5 rounded-full`} style={{ width: w }} />
        ))}
      </div>
    </div>
  );
}