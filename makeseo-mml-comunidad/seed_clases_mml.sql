-- ============================================================
-- Clases de la Serie MML - Edward Valencia (@makeseo)
-- 6 episodios alineados con la ruta de aprendizaje oficial
-- ============================================================
-- Aplicar con: npx wrangler d1 execute generico_db --remote --file=./seed_clases_mml.sql

-- Limpiar clases existentes (opcional, comentar si no quieres borrar)
-- DELETE FROM mml_class_questions;
-- DELETE FROM mml_agent_classes;

-- ============================================================
-- CLASE 1: Bienvenida y Prueba de Concepto (ya existe, la actualizamos)
-- ============================================================
UPDATE mml_agent_classes SET
  title = 'Episodio 1: De 0 a Clientes Diarios con SEO Local',
  description = 'Prueba de concepto del MML. Cómo captar llamadas diarias con SEO Local y Google Business Profile.',
  content = 'En este episodio Edward Valencia demuestra en vivo cómo el Método Malla Local (MML) permite recibir llamadas reales de clientes solo con Google Maps optimizado. Verás casos reales, los 3 pilares del método y por qué funciona sin WordPress ni hosting pago.',
  xp_reward = 20,
  sort_order = 1,
  module = 'Módulo 1: Fundamentos',
  module_order = 1,
  video_url = 'https://www.youtube.com/watch?v=MGcITnwpgCo',
  teacher = 'Edward Valencia',
  is_active = 1
WHERE id = 1;

-- ============================================================
-- CLASE 2: Ficha Maestra NAP + SAB
-- ============================================================
INSERT INTO mml_agent_classes (title, description, content, xp_reward, sort_order, module, module_order, video_url, teacher, is_active)
VALUES (
  'Episodio 2: Ficha Maestra NAP y Configuración SAB',
  'Google Business Profile blindado para servicios a domicilio sin local físico.',
  'El Pilar 1 del MML: Google Business Profile Semántico. Aprenderás a crear la Ficha Maestra NAP (Nombre, Dirección/Cobertura y Teléfono idénticos en toda la web), configurar SAB (Service Area Business) para operar sin local físico y evitar suspensiones, y seleccionar categorías estratégicas que disparen las impresiones en Google Maps.',
  25, 2, 'Módulo 1: Fundamentos', 2,
  'https://www.youtube.com/watch?v=0Cf8YR0XjWo',
  'Edward Valencia', 1
);

-- Preguntas clase 2
INSERT INTO mml_class_questions (class_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, points, sort_order)
VALUES
  (2, '¿Qué significa NAP en SEO Local?', 'Nombre, Anuncios, Promociones', 'Nombre, Dirección, Teléfono', 'Número de Accesos Programados', 'Navegación y Aplicaciones Privadas', 'b', 'NAP = Name, Address, Phone. Debe ser idéntico en toda la web.', 10, 1),
  (2, '¿Qué es SAB en Google Business Profile?', 'Service Area Business - negocio sin local físico', 'Sistema de Anuncios Básicos', 'Standard Analytics Bundle', 'Social Account Block', 'a', 'SAB permite operar como servicio a domicilio sin mostrar dirección física.', 10, 2),
  (2, '¿Por qué es importante el NAP consistente?', 'Por estética', 'Para evitar suspensiones y mejorar el ranking local', 'Para cobrar más', 'No es importante', 'b', 'Google penaliza la inconsistencia NAP con peor ranking o suspensión.', 10, 3);

-- ============================================================
-- CLASE 3: Web Serverless con IA
-- ============================================================
INSERT INTO mml_agent_classes (title, description, content, xp_reward, sort_order, module, module_order, video_url, teacher, is_active)
VALUES (
  'Episodio 3: Adiós WordPress - Webs con IA, GitHub y Cloudflare Pages',
  'Construcción de web ultrarrápida 100% desde el móvil con $0 hosting.',
  'El Pilar 2 del MML: Web Serverless Ultrarrápida. Edward te enseña a generar landings con IA preparadas para conversión directa, usar repositorios de GitHub para control de versiones gratuito, y desplegar en Cloudflare Pages con SSL automático y CDN perimetral a costo $0. Todo desde el smartphone.',
  30, 3, 'Módulo 2: Infraestructura', 1,
  'https://www.youtube.com/watch?v=PbDUwBGJqm0',
  'Edward Valencia', 1
);

-- Preguntas clase 3
INSERT INTO mml_class_questions (class_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, points, sort_order)
VALUES
  (3, '¿Qué reemplaza el MML al WordPress tradicional?', 'Wix', 'Código estático en GitHub + Cloudflare Pages', 'Shopify', 'Blogger', 'b', 'Astro/HTML plano en GitHub desplegado en Cloudflare Pages a costo $0.', 10, 1),
  (3, '¿Cuánto cuesta el hosting con Cloudflare Pages?', '$10/mes', '$50/mes', '$0 (gratis)', '$100/año', 'c', 'Cloudflare Pages es gratuito para sitios estáticos con CDN global.', 10, 2),
  (3, '¿Desde qué dispositivo se puede desplegar?', 'Solo PC', 'Solo Mac', '100% desde el móvil', 'Solo servidores dedicados', 'c', 'Todo el desarrollo se hace desde el smartphone con IA + GitHub.', 10, 3);

-- ============================================================
-- CLASE 4: Malla Territorial + Cloudflare D1
-- ============================================================
INSERT INTO mml_agent_classes (title, description, content, xp_reward, sort_order, module, module_order, video_url, teacher, is_active)
VALUES (
  'Episodio 4: Malla Territorial - Despliegue masivo por comunas',
  'Landings SEO por comuna/municipio + base de datos Cloudflare D1.',
  'El Pilar 3 del MML: Malla Territorial y Ecosistema de Autoridad. Aprenderás a desplegar landings SEO específicas para cada comuna o municipio que el negocio cubre, todas interconectadas. Usamos Cloudflare D1 como base de datos para gestionar la cobertura territorial completa. Inyección de citaciones consistentes en directorios locales.',
  30, 4, 'Módulo 2: Infraestructura', 2,
  '', -- Próximamente
  'Edward Valencia', 1
);

-- Preguntas clase 4
INSERT INTO mml_class_questions (class_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, points, sort_order)
VALUES
  (4, '¿Qué es la Malla Territorial?', 'Una red WiFi', 'Landings SEO por comuna/municipio interconectadas', 'Un tipo de dominio', 'Un plugin de WordPress', 'b', 'Es el Pilar 3: cubrir todas las comunas con landings dedicadas.', 10, 1),
  (4, '¿Para qué se usa Cloudflare D1?', 'Para editar videos', 'Como base de datos para gestionar cobertura territorial', 'Para enviar emails', 'Para diseño gráfico', 'b', 'D1 almacena las comunas, progreso y datos de los agentes.', 10, 2);

-- ============================================================
-- CLASE 5: Optimización WebP + GTM + Search Console
-- ============================================================
INSERT INTO mml_agent_classes (title, description, content, xp_reward, sort_order, module, module_order, video_url, teacher, is_active)
VALUES (
  'Episodio 5: Optimización WebP con IA, GTM y Search Console',
  'Compresión de imágenes, medición de conversiones y verificación SEO.',
  'Optimización técnica avanzada: compresión de imágenes a WebP con IA para reducir peso sin perder calidad, configuración de Google Tag Manager para medir conversiones (llamadas, WhatsApp, clics), y verificación en Google Search Console para monitorear el indexado y rendimiento en búsqueda.',
  25, 5, 'Módulo 3: Optimización', 1,
  '', -- Próximamente
  'Edward Valencia', 1
);

-- Preguntas clase 5
INSERT INTO mml_class_questions (class_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, points, sort_order)
VALUES
  (5, '¿Qué formato de imagen es mejor para web?', 'BMP', 'WebP', 'TIFF', 'RAW', 'b', 'WebP ofrece ~50% menos peso que JPG con calidad similar.', 10, 1),
  (5, '¿Para qué sirve Google Tag Manager?', 'Para editar fotos', 'Para medir conversiones y eventos sin tocar código', 'Para enviar facturas', 'Para diseñar logos', 'b', 'GTM gestiona tags de analítica sin modificar el código fuente.', 10, 2);

-- ============================================================
-- CLASE 6: Automatización + Circuito de Reseñas
-- ============================================================
INSERT INTO mml_agent_classes (title, description, content, xp_reward, sort_order, module, module_order, video_url, teacher, is_active)
VALUES (
  'Episodio 6: Automatización de Posts + Circuito de Reseñas',
  'Automatización con IA y circuito continuo de reseñas 5 estrellas por WhatsApp.',
  'Cierre del método: automatización de contenido local con IA para mantener fresca la malla territorial, y el circuito continuo de reseñas reales de 5 estrellas gestionado por WhatsApp. Edward te muestra cómo escalar el sistema sin perder calidad y mantener el ranking local en el tiempo.',
  30, 6, 'Módulo 3: Optimización', 2,
  '', -- Próximamente
  'Edward Valencia', 1
);

-- Preguntas clase 6
INSERT INTO mml_class_questions (class_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, points, sort_order)
VALUES
  (6, '¿Cómo se consiguen reseñas 5 estrellas éticamente?', 'Comprándolas', 'Con un circuito por WhatsApp que invita a clientes satisfechos', 'Borrando las malas', 'Creando cuentas falsas', 'b', 'El circuito automatizado pide reseñas a clientes reales satisfechos.', 10, 1),
  (6, '¿Qué se automatiza con IA en el MML?', 'Nada', 'Posts de contenido local para la malla territorial', 'El cobro a clientes', 'El diseño web', 'b', 'La IA genera contenido local para mantener frescas las landings.', 10, 2);

-- ============================================================
-- Actualizar progreso requerido para examen (al menos 4 clases)
-- ============================================================
INSERT OR REPLACE INTO mml_academy_config (key, value) VALUES ('min_classes_for_exam', '4');
INSERT OR REPLACE INTO mml_academy_config (key, value) VALUES ('passing_score', '70');
INSERT OR REPLACE INTO mml_academy_config (key, value) VALUES ('academy_name', 'MakeSEO Academy');
INSERT OR REPLACE INTO mml_academy_config (key, value) VALUES ('academy_description', 'Formación de Agentes Certificados en el Método Malla Local (MML)');
