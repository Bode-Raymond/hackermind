/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors: {
        background: '#000029',
        primary: '#e6e6e6',
        secondary: '#595959',
        accent: {
          orange: {
            primary: '#ffc725',
            secondary: '#f44088',
          },
          blue: {
            primary: '#00f0f7',
            secondary: '#00a8f7',
          }
        }
      }
    },
    fontFamily: {
      'sans': 'JetBrains Mono'
    }
  },
  plugins: [],
}

