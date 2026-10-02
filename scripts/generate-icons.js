// Genera iconos PNG 192 y 512 a partir del favicon SVG
const sharp = require('sharp');
const fs = require('fs');

const svgPath = '/home/z/my-project/globalpro-automotriz/public/favicon.svg';
const iconsDir = '/home/z/my-project/globalpro-automotriz/public/images/icons';
fs.mkdirSync(iconsDir, { recursive: true });

const svgBuffer = fs.readFileSync(svgPath);

(async () => {
  for (const size of [192, 512]) {
    await sharp(svgBuffer, { density: 384 })
      .resize(size, size)
      .png()
      .toFile(`${iconsDir}/icon-${size}.png`);
    console.log(`OK icon-${size}.png`);
  }
  // apple-touch-icon 180
  await sharp(svgBuffer, { density: 384 })
    .resize(180, 180)
    .png()
    .toFile(`${iconsDir}/apple-touch-icon.png`);
  console.log('OK apple-touch-icon.png');
})();
