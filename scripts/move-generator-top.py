"""
Mueve la sección #prompt-generador al principio (justo después del Hero).
También actualiza el orden del navbar.
"""
import re

FILE = '/home/z/my-project/makeseo-mml-comunidad/public/index.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extraer la sección #prompt-generador completa
# Va desde "<!-- ==================== MASTER PROMPT DISEÑADO PARA TU NICHO ==================== -->"
# hasta el cierre de la sección (antes del próximo "<!-- ==================== COMUNIDAD WHATSAPP ==================== -->")

start_marker = "  <!-- ==================== MASTER PROMPT DISEÑADO PARA TU NICHO ==================== -->"
end_marker = "  <!-- ==================== COMUNIDAD WHATSAPP ==================== -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("ERROR: No se encontraron los marcadores")
    exit(1)

# La sección a mover es desde start_idx hasta end_idx (no incluido)
generador_section = content[start_idx:end_idx]
print(f"Sección generador: {len(generador_section)} chars")

# Eliminar la sección de su posición actual
content_without_generador = content[:start_idx] + content[end_idx:]

# 2. Insertar la sección justo después del Hero (antes de "¿Qué ES EL MML?")
# El Hero termina con "</section>" seguido de un comentario "<!-- ==================== ¿QUÉ ES EL MML? ==================== -->"
hero_end_marker = "  <!-- ==================== ¿QUÉ ES EL MML? ==================== -->"
hero_end_idx = content_without_generador.find(hero_end_marker)

if hero_end_idx == -1:
    print("ERROR: No se encontró el marcador del Hero end")
    exit(1)

# Insertar la sección del generador justo antes del "¿Qué es el MML?"
new_content = content_without_generador[:hero_end_idx] + generador_section + "\n" + content_without_generador[hero_end_idx:]

# 3. Actualizar el orden de los enlaces del navbar
# Buscar los enlaces desktop y reordenar
old_nav = """<a href="#inicio" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Inicio</a>
          <a href="#metodo" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Método MML</a>
          <a href="#tutoriales" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Tutoriales YouTube</a>
          <a href="#comunidad" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Comunidad</a>
          <a href="#contacto" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Contacto</a>"""

new_nav = """<a href="#inicio" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Inicio</a>
          <a href="#prompt-generador" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Generar Prompt</a>
          <a href="#metodo" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Método MML</a>
          <a href="#tutoriales" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Tutoriales YouTube</a>
          <a href="#comunidad" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Comunidad</a>
          <a href="#contacto" class="px-4 py-2 text-sm font-medium text-white/80 hover:text-white hover:bg-white/5 rounded-lg transition-colors">Contacto</a>"""

new_content = new_content.replace(old_nav, new_nav)

# 4. Actualizar también el menú mobile
old_mobile_nav = """<a href="#inicio" class="block px-3 py-2.5 rounded-lg text-white/80 hover:text-white hover:bg-white/5 font-medium text-sm transition-colors mobile-link">Inicio</a>
        <a href="#metodo" class="block px-3 py-2.5 rounded-lg text-white/80 hover:text-white hover:bg-white/5 font-medium text-sm transition-colors mobile-link">Método MML</a>"""

new_mobile_nav = """<a href="#inicio" class="block px-3 py-2.5 rounded-lg text-white/80 hover:text-white hover:bg-white/5 font-medium text-sm transition-colors mobile-link">Inicio</a>
        <a href="#prompt-generador" class="block px-3 py-2.5 rounded-lg text-white/80 hover:text-white hover:bg-white/5 font-medium text-sm transition-colors mobile-link">Generar Prompt</a>
        <a href="#metodo" class="block px-3 py-2.5 rounded-lg text-white/80 hover:text-white hover:bg-white/5 font-medium text-sm transition-colors mobile-link">Método MML</a>"""

new_content = new_content.replace(old_mobile_nav, new_mobile_nav)

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Sección movida al principio")
print("✓ Navbar actualizado con 'Generar Prompt' como segundo enlace")
print(f"  Tamaño final: {len(new_content)} chars")
