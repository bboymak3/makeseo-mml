-- Marcar todas las clases como completadas para el admin (ID 1) y el agente prueba (ID 2)
-- Esto permite tomar el examen final

INSERT OR IGNORE INTO mml_user_class_progress (user_id, class_id, completed, correct_answers, total_questions, total_points, xp_earned, completed_at)
SELECT 1, id, 1, 2, 2, 20, 20, datetime('now') FROM mml_agent_classes WHERE is_active = 1;

INSERT OR IGNORE INTO mml_user_class_progress (user_id, class_id, completed, correct_answers, total_questions, total_points, xp_earned, completed_at)
SELECT 2, id, 1, 2, 2, 20, 20, datetime('now') FROM mml_agent_classes WHERE is_active = 1;

-- Actualizar el perfil del admin con el XP ganado
UPDATE mml_agent_profiles SET 
  total_classes_completed = 6, 
  xp = xp + 120,
  level = 2,
  xp_to_next_level = 200,
  updated_at = datetime('now')
WHERE user_id = 1;

-- Actualizar el perfil del agente prueba
UPDATE mml_agent_profiles SET 
  total_classes_completed = 6, 
  updated_at = datetime('now')
WHERE user_id = 2;
