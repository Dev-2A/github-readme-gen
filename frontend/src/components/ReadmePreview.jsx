import { useState } from "react";
import ReactMarkdown from "react-markdown";

export default function ReadmePreview({ markdown, username }) {
  const [tab, setTab] = useState("preview"); // "preview" | "raw"
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(markdown);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
    const url  = URL.createObjectURL(blob);
    const a    = document.createElement("a");
    a.href     = url;
    a.download = `${username}_README.md`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="bg-white border border-pastel-200 rounded-2xl shadow-sm overflow-hidden">

      {/* 헤더 바 */}
      <div className="flex items-center justify-between px-5 py-3
                      border-b border-pastel-100 bg-pastel-50">
        <div className="flex gap-1">
          {["preview", "raw"].map((t) => (
            <button
              key={t}
              onClick={() => setTab(t)}
              className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                tab === t
                  ? "bg-pastel-400 text-white"
                  : "text-pastel-400 hover:bg-pastel-100"
              }`}
            >
              {t === "preview" ? "👁 미리보기" : "📄 Raw"}
            </button>
          ))}
        </div>

        <div className="flex gap-2">
          <button
            onClick={handleCopy}
            className="flex items-center gap-1 px-3 py-1 rounded-lg text-xs
                       font-semibold border border-pastel-200 text-pastel-400
                       hover:bg-pastel-100 transition-all"
          >
            {copied ? "✅ 복사됨!" : "📋 복사"}
          </button>
          <button
            onClick={handleDownload}
            className="flex items-center gap-1 px-3 py-1 rounded-lg text-xs
                       font-semibold bg-pastel-400 text-white
                       hover:bg-pastel-500 transition-all"
          >
            ⬇️ 다운로드
          </button>
        </div>
      </div>

      {/* 탭 콘텐츠 */}
      <div className="p-5 max-h-[600px] overflow-y-auto">
        {tab === "preview" ? (
          <div className="prose prose-sm max-w-none text-gray-700
                          prose-headings:text-pastel-500
                          prose-a:text-pastel-400
                          prose-blockquote:border-pastel-200
                          prose-code:text-pastel-500
                          prose-hr:border-pastel-100">
            <ReactMarkdown
              components={{
                img: ({ src, alt, ...props }) => (
                  <img
                    src={src}
                    alt={alt}
                    className="max-w-full rounded-lg my-1"
                    {...props}
                  />
                ),
              }}
            >
              {markdown}
            </ReactMarkdown>
          </div>
        ) : (
          <pre className="text-xs text-gray-500 whitespace-pre-wrap break-words
                          bg-pastel-50 rounded-xl p-4 font-mono leading-relaxed">
            {markdown}
          </pre>
        )}
      </div>

    </div>
  );
}