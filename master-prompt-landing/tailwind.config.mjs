/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        'primary-cyan': '#00BCD4',
        'primary-teal': '#00838F',
        'accent-orange': '#ff6b00',
        'accent-orange-light': '#ff8c33',
        'dark-navy': '#0b1020',
        'dark-navy-alt': '#121a33',
        'ink-dark': '#1a1a1a',
        'text-muted': '#5b6475',
        'border-light': '#e6e9f0',
        'bg-alt': '#f5f7fb',
        'whatsapp-green': '#25D366',
      },
      fontFamily: { sans: ['Poppins', 'ui-sans-serif', 'system-ui', 'sans-serif'] },
      borderRadius: { 'xl-card': '18px', '2xl-card': '24px' },
      boxShadow: {
        'card': '0 4px 24px -8px rgba(11, 16, 32, 0.08)',
        'glow-cyan': '0 0 30px rgba(0, 188, 212, 0.45)',
        'glow-orange': '0 10px 30px -6px rgba(255, 107, 0, 0.45)',
      },
      backgroundImage: {
        'hero-radial': 'radial-gradient(circle at 30% 20%, rgba(0, 188, 212, 0.25), transparent 45%), radial-gradient(circle at 80% 0%, rgba(255, 107, 0, 0.18), transparent 35%)',
        'gradient-orange': 'linear-gradient(135deg, #ff6b00 0%, #ff8c33 100%)',
      },
      animation: {
        'pulse-slow': 'pulseSlow 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow-pulse': 'glowPulse 2s ease-in-out infinite alternate',
      },
      keyframes: {
        pulseSlow: { '0%, 100%': { opacity: '1' }, '50%': { opacity: '0.85' } },
        glowPulse: { '0%': { boxShadow: '0 0 20px rgba(0, 188, 212, 0.45)' }, '100%': { boxShadow: '0 0 38px rgba(0, 188, 212, 0.75)' } },
      },
    },
  },
  plugins: [],
};
