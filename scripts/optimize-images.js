// Optimiza las imágenes de la galería usando sharp (ya en node_modules)
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const galleryDir = '/home/z/my-project/globalpro-automotriz/public/images/gallery';

const files = fs.readdirSync(galleryDir).filter(f => f.endsWith('.jpg'));

(async () => {
  for (const file of files) {
    const inputPath = path.join(galleryDir, file);
    const webpPath = path.join(galleryDir, file.replace(/\.jpg$/, '.webp'));

    const meta = await sharp(inputPath).metadata();
    const resizeOpts = meta.width > 1200 || meta.height > 1200
      ? { width: 1200, height: 1200, fit: 'inside', withoutEnlargement: true }
      : null;

    if (resizeOpts) {
      const buf = await sharp(inputPath).resize(resizeOpts).jpeg({ quality: 78, progressive: true, mozjpeg: true }).toBuffer();
      fs.writeFileSync(inputPath, buf);
    }

    const pipeline = sharp(inputPath);
    if (resizeOpts) pipeline.resize(resizeOpts);
    await pipeline.webp({ quality: 75 }).toFile(webpPath);

    const newMeta = await sharp(inputPath).metadata();
    const webpStat = fs.statSync(webpPath);
    const jpgStat = fs.statSync(inputPath);
    console.log(`OK ${file}  ${newMeta.width}x${newMeta.height} | JPG ${(jpgStat.size/1024).toFixed(0)}KB | WebP ${(webpStat.size/1024).toFixed(0)}KB`);
  }
  console.log('Done');
})();
