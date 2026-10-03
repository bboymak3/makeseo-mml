"""
Reemplaza las tarjetas de clientes (div) por enlaces (a) con sus URLs de Google Maps.
"""
import re

FILE = '/home/z/my-project/makeseo-mml-comunidad/public/index.html'

# Mapeo: nombre del negocio → URL de Google Maps
CLIENTES = {
    'KLEAR STUDIO': 'https://maps.google.com/?cid=14103349439179398538',
    'OKINNOVATION PE': 'https://maps.google.com/?cid=11375010391976021784',
    'CEMIVAZ': 'https://maps.google.com/?cid=8371222752513105199',
    'Alexandro Refrigeration': 'https://maps.google.com/?cid=6100062695188478151',
    'En Santiago': 'https://maps.google.com/?cid=5770535050404324598',
    'ELECTROMECANICO': 'https://maps.google.com/?cid=5171996969050223756',
    'GRADO33': 'https://maps.google.com/?cid=5048253765322227950',
    'SAMSARA TATTOO STUDIO': 'https://maps.google.com/?cid=13717303125381412891',
    '360 SOLUCIONES': 'https://maps.google.com/?cid=12352573887920262660',
    'CHRISTIAN MOLINA': 'https://maps.google.com/?cid=5991356683179973225',
    'AMYSTUDIO': 'https://maps.google.com/?cid=15635944758478366301',
    'LA CACHAMITA DE ORO': 'https://maps.google.com/?cid=17671237451495645712',
    'LLANOCAR CL': 'https://maps.google.com/?cid=7579209724505328189',
    'HolaX Venezuela': 'https://maps.google.com/?cid=5672959362634915423',
    'Limpieza a Domicilio 24/7': 'https://maps.google.com/?cid=2672323267632148906',
    'EMISOR': 'https://maps.google.com/?cid=2362859520064558930',
    'La Conquista #1': 'https://maps.google.com/?cid=15889830058835674627',
    'Estilosgrado33': 'https://maps.google.com/?cid=1812885396603291624',
    'Alianza 58': 'https://maps.google.com/?cid=621475042026838852',
    'CLARO SERVICIOS': 'https://maps.google.com/?cid=9956249706416433624',
    'Abogados Valencia': 'https://maps.google.com/?cid=6909729685505075331',
    'REGASA': 'https://maps.google.com/?cid=15342271778020583814',
    'JF GOD\'S COMPANY': 'https://maps.google.com/?cid=12203003047723153499',
    'DR.AUTOMOTRIZ': 'https://maps.google.com/?cid=14561742232422258529',
    'GLOBAL PRO Automotriz': 'https://maps.google.com/?cid=3923957367446305732',
    'MUNDONET': 'https://maps.google.com/?cid=7671734058344635530',
    'Dubraskalash.art': 'https://maps.google.com/?cid=6671507534162007091',
    'Optimus Cars SPA': 'https://maps.google.com/?cid=365340981373142326',
    'TAPIZADO DE VOLANTES': 'https://maps.google.com/?cid=12489978171041981369',
}

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for nombre, url in CLIENTES.items():
    # Buscar el div que contiene el nombre del negocio
    # Patrón: <div class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0.5 transition-all">
    #          ...<h3 class="font-bold text-white text-sm">NOMBRE</h3>...
    #          ...</div>

    # Construir el patrón para este negocio específico
    # El nombre puede tener caracteres especiales, escapamos
    nombre_escaped = re.escape(nombre)

    # Patrón: div de apertura + contenido con el nombre + div de cierre
    patron = r'(<div class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0\.5 transition-all">[^<]*<div class="flex items-center gap-2 mb-1"><span class="text-base">[^<]*</span><h3 class="font-bold text-white text-sm">' + nombre_escaped + r'</h3></div>\s*<p class="text-xs text-white/60">[^<]*</p>\s*</div>)'

    replacement = '<a href="' + url + '" target="_blank" rel="noopener noreferrer" class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0.5 transition-all block">'

    match = re.search(patron, content)
    if match:
        old_div = match.group(1)
        # Reemplazar el <div de apertura por <a con href
        new_a = old_div.replace(
            '<div class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0.5 transition-all">',
            '<a href="' + url + '" target="_blank" rel="noopener noreferrer" class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0.5 transition-all block">'
        )
        # Reemplazar el </div> final por </a>
        # El último </div> del bloque
        last_div_idx = new_a.rfind('</div>')
        new_a = new_a[:last_div_idx] + '</a>' + new_a[last_div_idx + 6:]

        content = content.replace(old_div, new_a)
        count += 1
        print(f'  ✓ {nombre} → {url}')
    else:
        print(f'  ✗ {nombre} → NO ENCONTRADO')

print(f'\nTotal: {count}/{len(CLIENTES)} clientes actualizados')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)
