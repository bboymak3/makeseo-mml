# Imagen OG de referencia

Coloca aquí un archivo llamado `og-image.jpg` con dimensiones **1200x630 px**.

Mientras tanto, se referencia `og-image.svg` en el `Layout.astro` como placeholder
(SVG es soportado por WhatsApp y algunas plataformas, pero para máxima compatibilidad
con Facebook/X/LinkedIn se recomienda reemplazarlo por un JPG/PNG).

Puedes generarlo fácilmente desde el SVG incluido con:
```bash
# Requiere ImageMagick o rsvg-convert
rsvg-convert -w 1200 -h 630 og-image.svg -o og-image.jpg
# o
convert -density 144 -background none og-image.svg -resize 1200x630 og-image.png
```
