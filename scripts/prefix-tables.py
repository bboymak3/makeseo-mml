"""
Reemplaza todas las referencias a tablas sin prefijo por mml_ en todos los .js
de functions/ para que no haya conflicto con otras DBs.
"""
import os
import re
import glob

FUNCTIONS_DIR = '/home/z/my-project/makeseo-mml-comunidad/functions'

# Tablas a prefijar (de la academia + users)
TABLES_TO_PREFIX = [
    'users',
    'agent_classes',
    'class_questions',
    'user_class_progress',
    'agent_profiles',
    'user_badges',
    'academy_config',
    'exam_attempts',
]

# Patrones SQL a buscar y reemplazar
# Ordenados de más largos a más cortos para que 'class_questions' no se afecte antes que 'agent_classes'
PATTERNS = []

for table in TABLES_TO_PREFIX:
    # FROM table, INTO table, UPDATE table, JOIN table, etc.
    # Usar \b para word boundary, pero permitir backticks o comillas
    PATTERNS.append((
        re.compile(r'\b' + table + r'\b', re.IGNORECASE),
        'mml_' + table
    ))

# Procesar todos los .js en functions/
js_files = glob.glob(os.path.join(FUNCTIONS_DIR, '**', '*.js'), recursive=True)

total_changes = 0
for filepath in js_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    modified = original
    file_changes = 0
    for pattern, replacement in PATTERNS:
        new_modified, count = pattern.subn(replacement, modified)
        if count > 0:
            modified = new_modified
            file_changes += count

    if file_changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        total_changes += file_changes
        print(f"  ✓ {os.path.relpath(filepath, FUNCTIONS_DIR)}: {file_changes} reemplazos")

print(f"\nTotal: {total_changes} reemplazos en {len(js_files)} archivos")
