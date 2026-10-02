import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://globalproautomotriz.cl',
  // output: 'static' es el valor por defecto y el recomendado para SSG / Cloudflare Pages
  output: 'static',
  integrations: [
    tailwind({
      // Aplicamos Tailwind solo a los archivos del proyecto
      applyBaseStyles: true,
    }),
  ],
  build: {
    // Inlinea pequeños CSS para mejorar FCP / LCP
    inlineStylesheets: 'auto',
  },
  compressHTML: true,
});
