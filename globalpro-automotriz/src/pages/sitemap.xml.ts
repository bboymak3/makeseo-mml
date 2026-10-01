import type { APIRoute } from 'astro';
import { comunas } from '../data/comunas.ts';

const SITE_URL = 'https://globalproautomotriz.pages.dev';

export const GET: APIRoute = () => {
  const pages = [
    { url: '/', priority: '1.0', changefreq: 'weekly', lastmod: new Date().toISOString().split('T')[0] },
    { url: '/faq', priority: '0.8', changefreq: 'monthly', lastmod: new Date().toISOString().split('T')[0] },
    { url: '/galeria', priority: '0.7', changefreq: 'monthly', lastmod: new Date().toISOString().split('T')[0] },
    { url: '/privacidad', priority: '0.3', changefreq: 'yearly', lastmod: new Date().toISOString().split('T')[0] },
    ...comunas.map(c => ({
      url: `/comuna/${c.slug}`,
      priority: '0.9',
      changefreq: 'monthly',
      lastmod: new Date().toISOString().split('T')[0],
    })),
  ];

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map(p => `  <url>
    <loc>${SITE_URL}${p.url}</loc>
    <lastmod>${p.lastmod}</lastmod>
    <changefreq>${p.changefreq}</changefreq>
    <priority>${p.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};
