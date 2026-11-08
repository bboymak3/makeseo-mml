// Configuración de Tailwind para makeseo-mml-comunidad/public.
// Es la misma que antes estaba inline en cada página (tailwind.config = {...}).
// Regenerar el CSS después de cambiar clases en el HTML:
//   cd scripts/tailwind && npm install && npm run build
const pub = '../../makeseo-mml-comunidad/public';
module.exports = {
  content: [
    `${pub}/index.html`, `${pub}/blog.html`, `${pub}/clientes.html`, `${pub}/contacto.html`,
    `${pub}/faq.html`, `${pub}/quienes-somos.html`, `${pub}/servicios.html`,
    `${pub}/master-prompt/index.html`,
  ],
  theme: {
    extend: {
      colors: {
        'dark-navy': '#0b1020',
        'dark-navy-alt': '#121a33',
        'primary-cyan': '#00BCD4',
        'primary-teal': '#00838F',
        'accent-orange': '#ff6b00',
        'accent-orange-light': '#ff8c33',
        'whatsapp-green': '#25D366',
        'youtube-red': '#FF0000',
      },
      fontFamily: { sans: ['Inter', 'Poppins', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] },
      animation: {
        'pulse-slow': 'pulseSlow 2.5s ease-in-out infinite',
        'glow-pulse': 'glowPulse 2s ease-in-out infinite alternate',
      },
      keyframes: {
        pulseSlow: { '0%, 100%': { opacity: '1' }, '50%': { opacity: '0.85' } },
        glowPulse: { '0%': { boxShadow: '0 0 20px rgba(0, 188, 212, 0.45)' }, '100%': { boxShadow: '0 0 38px rgba(0, 188, 212, 0.75)' } },
      },
    },
  },
};
