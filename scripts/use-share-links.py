"""
Reemplaza todos los enlaces de clientes por share.google links.
También agrega OKINNOVATION Chile (segunda entrada) que falta.
"""
import re

FILE = '/home/z/my-project/makeseo-mml-comunidad/public/index.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Mapeo: nombre del negocio en el HTML → share.google link
# En el orden que el usuario proporcionó (alfabético)
SHARE_LINKS = {
    '360 SOLUCIONES': 'https://share.google/Q8hWPBpKy1LxzCiAa',
    'Abogados Valencia': 'https://share.google/cFiuM0YRfAtEpG7BE',
    'Alexandro Refrigeration': 'https://share.google/WQLzrL87MGzTNMB4t',
    'Alianza 58': 'https://share.google/p5u62sR3JfyXtH97J',
    'AMYSTUDIO': 'https://share.google/v8ankSL3GUTIY9izs',
    'CEMIVAZ': 'https://share.google/eRgELPwSvISGWd9ZB',
    'CHRISTIAN MOLINA': 'https://share.google/G0146W06Y693u2Yde',
    'CLARO SERVICIOS': 'https://share.google/h91rZJWb0s9FVtS0o',
    'DR.AUTOMOTRIZ': 'https://share.google/6CFkPplosaNLfFkOX',
    'Dubraskalash.art': 'https://share.google/QZVACOSo7JTa55lOx',
    'ELECTROMECANICO': 'https://share.google/V0zQRJoLFsdpRAF53',
    'EMISOR': 'https://share.google/HS2d43G9LksOezuBR',
    'En Santiago': 'https://share.google/2mOzXghFssRyQZYVa',
    'GRADO33': 'https://share.google/nQWDxX41oFLPqHRrd',
    'HolaX Venezuela': 'https://share.google/n9YadKi2RtI3QfiBn',
    'JF GOD\'S COMPANY': 'https://share.google/lpbpPplVZu65yoxZb',
    'LA CACHAMITA DE ORO': 'https://share.google/op6snKES6TrmypxE4',
    'La Conquista #1': 'https://share.google/kbobtwYucU3vbaslN',
    'Limpieza a Domicilio 24/7': 'https://share.google/xbO4pTtwCjClt38XA',
    'LLANOCAR CL': 'https://share.google/sucxSUn3fRya6ZmNs',
    'GLOBAL PRO Automotriz': 'https://share.google/zCexQKf5hvZVBMG92',
    'MUNDONET': 'https://share.google/G6AQc0w12UrtVpOVo',
    'Optimus Cars SPA': 'https://share.google/7BhqsrZk1vLjJAVMR',
    'REGASA': 'https://share.google/H7gApIC14AQNacmEc',
    'SAMSARA TATTOO STUDIO': 'https://share.google/t752PmcyBGKRilClj',
    'SOPREVER': 'https://share.google/AfpzW5tvS7FOt4Ug2',
    'Estilosgrado33': 'https://share.google/bFEPv74FsvmNgxt2R',
    'OKINNOVATION PE': 'https://share.google/d60jH6JP5PxiWAqId',
    'KLEAR STUDIO': 'https://share.google/u5uhajp7ysG70Bq6w',
    'TAPIZADO DE VOLANTES': 'https://share.google/1CXpOCbOR8eijO4Yb',
}

count = 0
for nombre, share_url in SHARE_LINKS.items():
    nombre_escaped = re.escape(nombre)
    # Buscar cualquier URL dentro de un <a> que contenga este negocio
    # Patrón: <a href="CUALQUIER_URL" ...> ... <h3 ...>NOMBRE</h3>
    patron = r'(<a href=")[^"]*("[^>]*>[^<]*<div class="flex items-center gap-2 mb-1"><span class="text-base">[^<]*</span><h3 class="font-bold text-white text-sm">' + nombre_escaped + r'</h3>)'
    
    match = re.search(patron, content)
    if match:
        old_full = match.group(0)
        new_full = old_full.replace(match.group(1), '<a href="').replace(match.group(2), '"' + match.group(2).split('"', 1)[1] if '"' in match.group(2) else '')
        # Más simple: reemplazar la URL directamente
        # Encontrar la URL actual
        url_match = re.search(r'<a href="([^"]*)"', old_full)
        if url_match:
            old_url = url_match.group(1)
            content = content.replace('href="' + old_url + '"', 'href="' + share_url + '"', 1)
            count += 1
            print(f'  ✓ {nombre} → {share_url}')
    else:
        print(f'  ✗ {nombre} → NO ENCONTRADO')

print(f'\nTotal: {count}/{len(SHARE_LINKS)} enlaces reemplazados con share.google')

# Agregar OKINNOVATION Chile (segunda entrada) después de OKINNOVATION PE
okinno_cl_html = '''        <!-- OKINNOVATION CL -->
        <a href="https://share.google/BBRNKtZKRIDBgTzAI" target="_blank" rel="noopener noreferrer" class="bg-dark-navy-alt/60 border border-white/10 rounded-xl p-4 hover:border-primary-cyan/40 hover:-translate-y-0.5 transition-all block">
          <div class="flex items-center gap-2 mb-1"><span class="text-base">🚘</span><h3 class="font-bold text-white text-sm">OKINNOVATION CL</h3></div>
          <p class="text-xs text-white/60">Fabricación & Accesorios Off-Road 4x4 · Santiago de Chile</p>
        </a>
'''

# Buscar el OKINNOVATION PE y agregar el CL después
okinno_pe_pattern = r'(<a href="https://share\.google/d60jH6JP5PxiWAqId"[^>]*>.*?</a>)'
match = re.search(okinno_pe_pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), match.group(0) + '\n' + okinno_cl_html)
    print('  ✓ OKINNOVATION CL agregado después de OKINNOVATION PE')
else:
    print('  ✗ OKINNOVATION PE no encontrado para insertar CL después')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)
print('\n✓ Archivo guardado')
