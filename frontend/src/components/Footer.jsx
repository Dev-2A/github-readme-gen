export default function Footer() {
  return (
    <footer className="mt-16 pb-8 text-center space-y-1">
      <p className="text-xs text-gray-300">
        Made with 💙 using{" "}
        <a
          href="https://github.com/Dev-2A/github-readme-gen"
          target="_blank"
          rel="noreferrer"
          className="text-pastel-300 hover:text-pastel-400 underline underline-offset-2
                     transition-colors"
        >
          github-readme-gen
        </a>
      </p>
      <p className="text-xs text-gray-300">
        GitHub API 기본 제공 횟수: 인증 시 5,000 req/hr
      </p>
    </footer>
  );
}