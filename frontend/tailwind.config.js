/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        pastel: {
          50:  "#f0f4ff",
          100: "#dce8ff",
          200: "#c5d5f5",
          300: "#8db0f0",
          400: "#5b8af5",
          500: "#3a5bb8",
          600: "#2d4a9a",
        },
      },
    },
  },
  plugins: [],
}