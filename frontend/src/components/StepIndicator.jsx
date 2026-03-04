const STEPS = [
  { id: 1, label: "유저 검색" },
  { id: 2, label: "옵션 설정" },
  { id: 3, label: "README 생성" },
];

export default function StepIndicator({ currentStep }) {
  return (
    <div className="flex items-center justify-center gap-0 mb-8 select-none">
      {STEPS.map((step, idx) => {
        const done   = currentStep > step.id;
        const active = currentStep === step.id;

        return (
          <div key={step.id} className="flex items-center">
            {/* 원 */}
            <div className="flex flex-col items-center gap-1">
              <div
                className={`w-8 h-8 rounded-full flex items-center justify-center
                            text-xs font-bold border-2 transition-all duration-300 ${
                  done
                    ? "bg-pastel-400 border-pastel-400 text-white"
                    : active
                    ? "bg-white border-pastel-400 text-pastel-400"
                    : "bg-white border-pastel-200 text-pastel-200"
                }`}
              >
                {done ? "✓" : step.id}
              </div>
              <span
                className={`text-xs font-medium transition-colors ${
                  active ? "text-pastel-500" : done ? "text-pastel-400" : "text-gray-300"
                }`}
              >
                {step.label}
              </span>
            </div>

            {/* 연결선 */}
            {idx < STEPS.length - 1 && (
              <div
                className={`w-16 h-0.5 mb-5 mx-1 transition-all duration-300 ${
                  currentStep > step.id ? "bg-pastel-400" : "bg-pastel-100"
                }`}
              />
            )}
          </div>
        );
      })}
    </div>
  );
}