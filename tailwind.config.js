/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./static/**/*.{css,js}",
    "./templates/**/*.html",
    "./templates/*.html",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/forms")({
      strategy: 'base', // only generate global styles
    }),
    require('flowbite/plugin')
  ],
}

