"""
Reemplaza los enlaces de Google Maps con los CIDs correctos proporcionados por el usuario.
También agrega SOPREVER que es un cliente nuevo.
"""
import re

FILE = '/home/z/my-project/makeseo-mml-comunidad/public/index.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Mapeo correcto: nombre en el HTML → CID correcto de Google Maps
# Los que no tienen CID usan search URL
LINKS = {
    'KLEAR STUDIO': 'https://www.google.com/maps?cid=10302252259696832581',
    'OKINNOVATION PE': 'https://www.google.com/maps?cid=7054057513753858513',
    'CEMIVAZ': 'https://www.google.com/maps?cid=14850903344403349950',
    'Alexandro Refrigeration': 'https://www.google.com/maps?cid=8520059873500355419',
    'En Santiago': 'https://www.google.com/maps?cid=12035751900638388862',
    'ELECTROMECANICO': 'https://www.google.com/maps?cid=16624725704641647391',
    'GRADO33': 'https://www.google.com/maps?cid=859362967230373973',
    'SAMSARA TATTOO STUDIO': 'https://www.google.com/maps?cid=2345303020109286370',
    '360 SOLUCIONES': 'https://www.google.com/maps?cid=11659559614790558360',
    'CHRISTIAN MOLINA': 'https://www.google.com/maps?cid=11236502585630169203',
    'AMYSTUDIO': 'https://www.google.com/maps?cid=14543276487625466281',
    'LA CACHAMITA DE ORO': 'https://www.google.com/maps?cid=16120770826214642504',
    'LLANOCAR CL': 'https://www.google.com/maps?cid=18089055316295178298',
    'HolaX Venezuela': 'https://www.google.com/maps?cid=13751372749775030272',
    'Limpieza a Domicilio 24/7': 'https://www.google.com/maps?cid=5283607825201280931',
    'EMISOR': 'https://www.google.com/maps?cid=14399347615499628388',
    'La Conquista #1': 'https://www.google.com/maps?cid=9149114361687599031',
    'Estilosgrado33': 'https://www.google.com/maps/search/?api=1&query=Estilosgrado33+Rionegro+Antioquia',
    'Alianza 58': 'https://www.google.com/maps?cid=11383929137743782754',
    'CLARO SERVICIOS': 'https://www.google.com/maps?cid=13843202957069347606',
    'Abogados Valencia': 'https://www.google.com/maps/search/?api=1&query=Abogados+Valencia+Barinas',
    'REGASA': 'https://www.google.com/maps?cid=14028756104158749729',
    'JF GOD\'S COMPANY': 'https://www.google.com/maps?cid=656371965001129880',
    'DR.AUTOMOTRIZ': 'https://www.google.com/maps?cid=174397386064510379',
    'GLOBAL PRO Automotriz': 'https://www.google.com/maps?cid=17992774452111210231',
    'MUNDONET': 'https://www.google.com/maps?cid=3556981972697206904',
    'Dubraskalash.art': 'https://www.google.com/maps?cid=2795968791136560999',
    'Optimus Cars SPA': 'https://www.google.com/maps?cid=1705748098673706448',
    'TAPIZADO DE VOLANTES': 'https://www.google.com/maps?cid=17985961294981612041',
}

count = 0
for nombre, url_correcta in LINKS.items():
    # Buscar el <a href="https://maps.google.com/?cid=..." o cualquier URL de maps que contenga el nombre del negocio
    # Patrón: <a href="CUALQUIER_URL" target="_blank" rel="noopener noreferrer" class="bg-dark-navy-alt/60 ..."> ... <h3 ...>NOMBRE</h3>

    nombre_escaped = re.escape(nombre)

    # Buscar el bloque <a> que contiene este negocio
    patron = r'(<a href=")[^"]*(" target="_blank" rel="noopener noreferrer" class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0\.5 transition-all block">[^<]*<div class="flex items-center gap-2 mb-1"><span class="text-base">[^<]*</span><h3 class="font-bold text-white text-sm">' + nombre_escaped + r'</h3>)'

    match = re.search(patron, content)
    if match:
        old_url = match.group(1) + match.group(2)
        new_url = match.group(1) + url_correcta + match.group(2)
        content = content.replace(old_url, new_url, 1)
        count += 1
        print(f'  ✓ {nombre} → cid={url_correcta.split("cid=")[-1] if "cid=" in url_correcta else "search"}')
    else:
        # Intentar sin el "block" class (por si no se aplicó correctamente antes)
        patron2 = r'(<a href=")[^"]*("[^>]*>[^<]*<div class="flex items-center gap-2 mb-1"><span class="text-base">[^<]*</span><h3 class="font-bold text-white text-sm">' + nombre_escaped + r'</h3>)'
        match2 = re.search(patron2, content)
        if match2:
            old_url = match2.group(1) + match2.group(2)
            new_url = match2.group(1) + url_correcta + match2.group(2)
            content = content.replace(old_url, new_url, 1)
            count += 1
            print(f'  ✓ {nombre} → cid={url_correcta.split("cid=")[-1] if "cid=" in url_correcta else "search"} (pattern 2)')
        else:
            print(f'  ✗ {nombre} → NO ENCONTRADO')

print(f'\nTotal: {count}/{len(LINKS)} enlaces corregidos')

# Agregar SOPREVER antes del cierre del grid
soprever_html = '''        <!-- SOPREVER -->
        <a href="https://www.google.com/maps?cid=5111364283195852261" target="_blank" rel="noopener noreferrer" class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0.5 transition-all block">
          <div class="flex items-center gap-2 mb-1"><span class="text-base">🌳</span><h3 class="font-bold text-white text-sm">SOPREVER</h3></div>
          <p class="text-xs text-white/60">Soluciones y Prevenciones Verdes · Tala y poda de árboles · Santiago CL</p>
        </a>
'''

# Insertar antes del cierre del grid de clientes
grid_close = '      </div>\n\n      <div class="mt-12 text-center" data-reveal>\n        <p class="text-white/60 mb-4">¿Quieres que tu negocio aparezca aquí?'
if grid_close in content:
    content = content.replace(grid_close, '      </div>\n\n      <div class="mt-12 text-center" data-reveal>\n        <p class="text-white/60 mb-4">¿Quieres que tu negocio aparezca aquí?')
    # Encontrar el último </a> antes del </div> que cierra el grid
    # y agregar SOPREVER después
    last_client = '</a>\n      </div>'
    if last_client in content:
        content = content.replace(last_client, '</a>\n' + soprever_html + '      </div>', 1)
        print('\n  ✓ SOPREVER agregado como nuevo cliente')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n✓ Archivo guardado')
