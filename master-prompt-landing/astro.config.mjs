import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://master-prompt-globalpro.pages.dev',
  output: 'static',
  integrations: [tailwind({ applyBaseStyles: true })],
  compressHTML: true,
});
