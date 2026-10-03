-- ============================================================
-- Schema MML Academia - Edward Valencia / @makeseo
-- Todas las tablas con prefijo mml_ para evitar conflictos
-- ============================================================
-- Aplicar con: wrangler d1 execute makeseo-mml-db --file=./schema_mml_academia.sql

-- 1. Usuarios (con prefijo mml_)
CREATE TABLE IF NOT EXISTS mml_users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  phone TEXT,
  whatsapp TEXT,
  password_hash TEXT NOT NULL,
  role TEXT DEFAULT 'user',  -- 'user' | 'agent' | 'admin'
  avatar TEXT,
  bio TEXT,
  is_active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now')),
  account_type TEXT DEFAULT 'free',
  user_type TEXT DEFAULT 'agent',
  whatsapp_enabled INTEGER DEFAULT 1,
  google_id TEXT,
  auth_provider TEXT DEFAULT 'email',  -- 'email' | 'google'
  plan TEXT,
  plan_starts_at TEXT,
  plan_expires_at TEXT,
  seller_owner_id INTEGER
);

-- Índice para búsquedas por email y google_id
CREATE INDEX IF NOT EXISTS idx_mml_users_email ON mml_users(email);
CREATE INDEX IF NOT EXISTS idx_mml_users_google_id ON mml_users(google_id);
CREATE INDEX IF NOT EXISTS idx_mml_users_role ON mml_users(role);

-- 2. Clases creadas por admin (academia)
CREATE TABLE IF NOT EXISTS mml_agent_classes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT,
  content TEXT DEFAULT '',
  xp_reward INTEGER DEFAULT 10,
  sort_order INTEGER DEFAULT 0,
  is_active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

-- 3. Preguntas por clase
CREATE TABLE IF NOT EXISTS mml_class_questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id INTEGER NOT NULL,
  question TEXT NOT NULL,
  option_a TEXT NOT NULL,
  option_b TEXT NOT NULL,
  option_c TEXT NOT NULL,
  option_d TEXT NOT NULL,
  correct_answer TEXT NOT NULL CHECK(correct_answer IN ('a', 'b', 'c', 'd')),
  explanation TEXT DEFAULT '',
  points INTEGER DEFAULT 10,
  sort_order INTEGER DEFAULT 0,
  created_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (class_id) REFERENCES mml_agent_classes(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_mml_class_questions_class ON mml_class_questions(class_id);

-- 4. Progreso de usuario por clase
CREATE TABLE IF NOT EXISTS mml_user_class_progress (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  class_id INTEGER NOT NULL,
  completed INTEGER DEFAULT 0,
  correct_answers INTEGER DEFAULT 0,
  total_questions INTEGER DEFAULT 0,
  total_points INTEGER DEFAULT 0,
  xp_earned INTEGER DEFAULT 0,
  completed_at TEXT,
  UNIQUE(user_id, class_id),
  FOREIGN KEY (user_id) REFERENCES mml_users(id),
  FOREIGN KEY (class_id) REFERENCES mml_agent_classes(id)
);
CREATE INDEX IF NOT EXISTS idx_mml_user_class_progress_user ON mml_user_class_progress(user_id);

-- 5. Perfil de agente (nivel/XP)
CREATE TABLE IF NOT EXISTS mml_agent_profiles (
  user_id INTEGER PRIMARY KEY,
  level INTEGER DEFAULT 1,
  xp INTEGER DEFAULT 0,
  xp_to_next_level INTEGER DEFAULT 100,
  total_classes_completed INTEGER DEFAULT 0,
  exam_passed INTEGER DEFAULT 0,
  exam_passed_at TEXT,
  exam_attempts INTEGER DEFAULT 0,
  last_exam_at TEXT,
  is_partner INTEGER DEFAULT 0,
  partner_at TEXT,
  graduated INTEGER DEFAULT 0,
  graduated_at TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (user_id) REFERENCES mml_users(id)
);

-- 6. Insignias / medallas
CREATE TABLE IF NOT EXISTS mml_user_badges (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  badge_type TEXT NOT NULL,
  badge_name TEXT NOT NULL,
  badge_description TEXT DEFAULT '',
  badge_icon TEXT DEFAULT 'fas fa-medal',
  earned_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (user_id) REFERENCES mml_users(id)
);
CREATE INDEX IF NOT EXISTS idx_mml_user_badges_user ON mml_user_badges(user_id);

-- 7. Configuración de la academia (clave-valor)
CREATE TABLE IF NOT EXISTS mml_academy_config (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  updated_at TEXT DEFAULT (datetime('now'))
);

-- 8. Intentos de examen final
CREATE TABLE IF NOT EXISTS mml_exam_attempts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  started_at TEXT DEFAULT (datetime('now')),
  finished_at TEXT,
  score INTEGER DEFAULT 0,
  total_questions INTEGER DEFAULT 0,
  correct_answers INTEGER DEFAULT 0,
  passed INTEGER DEFAULT 0,
  answers_json TEXT,
  FOREIGN KEY (user_id) REFERENCES mml_users(id)
);
CREATE INDEX IF NOT EXISTS idx_mml_exam_attempts_user ON mml_exam_attempts(user_id);

-- ============================================================
-- INSERTS INICIALES
-- ============================================================

-- Usuario admin por defecto (contraseña: "admin123" - cámbiala después)
-- Hash SHA-256 de "admin123": 240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9
INSERT OR IGNORE INTO mml_users (name, email, password_hash, role, user_type, auth_provider)
VALUES ('Admin MML', 'admin@makeseo.local', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'admin', 'admin', 'email');

-- Configuración inicial de la academia
INSERT OR IGNORE INTO mml_academy_config (key, value) VALUES ('academy_name', 'Academia MML · Edward Valencia');
INSERT OR IGNORE INTO mml_academy_config (key, value) VALUES ('academy_description', 'Método Malla Local - Formación de Agentes Certificados');
INSERT OR IGNORE INTO mml_academy_config (key, value) VALUES ('passing_score', '70');
INSERT OR IGNORE INTO mml_academy_config (key, value) VALUES ('xp_per_level', '100');

-- Clase de bienvenida (ejemplo)
INSERT OR IGNORE INTO mml_agent_classes (id, title, description, content, xp_reward, sort_order, is_active)
VALUES (1, 'Bienvenida al Método MML', 'Introducción al Método Malla Local y sus 3 pilares.', 'El Método Malla Local (MML) es una metodología práctica de posicionamiento digital desarrollada por Edward Valencia (@makeseo). En esta clase aprenderás los fundamentos antes de avanzar a la configuración de Google Business Profile, la web serverless y la malla territorial.', 10, 1, 1);

-- Pregunta de ejemplo para la clase 1
INSERT OR IGNORE INTO mml_class_questions (class_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation, points, sort_order)
VALUES
  (1, '¿Qué significa MML?', 'Método de Marketing Local', 'Método Malla Local', 'Módulo de Mantenimiento Local', 'Mapa de Mercados Locales', 'b', 'MML = Método Malla Local, creado por Edward Valencia.', 10, 1),
  (1, '¿Cuál es uno de los 3 pilares del MML?', 'Publicidad pagada en Facebook', 'WordPress con Elementor', 'Google Business Profile Semántico', 'Email marketing masivo', 'c', 'El Pilar 1 es Google Business Profile Semántico (Ficha Maestra NAP + SAB).', 10, 2);

-- ============================================================
-- FIN DEL SCHEMA
-- ============================================================
