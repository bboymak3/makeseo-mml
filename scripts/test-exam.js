// Script para aprobar el examen del admin vía API
const fs = require('fs');

async function main() {
  // Login
  const loginRes = await fetch('https://makeseo-mml.pages.dev/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'admin@makeseo.local', password: 'admin123' }),
  });
  const loginData = await loginRes.json();
  const token = loginData.token;
  console.log('Token:', token.slice(0, 30) + '...');

  // Obtener preguntas del examen
  const examRes = await fetch('https://makeseo-mml.pages.dev/api/agent-exam/questions', {
    headers: { 'Authorization': 'Bearer ' + token },
  });
  const examData = await examRes.json();
  const questions = examData.questions || [];
  console.log('Preguntas del examen:', questions.length);

  // Obtener respuestas correctas de la DB
  const { execSync } = require('child_process');
  const dbResult = execSync(
    'npx wrangler d1 execute generico_db --remote --json --command="SELECT id, correct_answer FROM mml_class_questions"',
    { env: { ...process.env }, encoding: 'utf8' }
  );
  const dbData = JSON.parse(dbResult);
  const answers = {};
  for (const row of dbData[0].results) {
    answers[row.id] = row.correct_answer;
  }
  console.log('Respuestas correctas obtenidas:', Object.keys(answers).length);

  // Construir payload (formato: array de { question_id, answer })
  const payload = { answers: [] };
  for (const q of questions) {
    if (answers[q.id]) {
      payload.answers.push({ question_id: q.id, answer: answers[q.id] });
    }
  }
  console.log('Respuestas a enviar:', payload.answers.length);

  // Enviar examen
  const submitRes = await fetch('https://makeseo-mml.pages.dev/api/agent-exam', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const submitData = await submitRes.json();
  console.log('Resultado del examen:', JSON.stringify(submitData, null, 2));

  // Verificar estado
  const statusRes = await fetch('https://makeseo-mml.pages.dev/api/agent-exam', {
    headers: { 'Authorization': 'Bearer ' + token },
  });
  const statusData = await statusRes.json();
  console.log('Estado después del examen:', JSON.stringify(statusData, null, 2));

  // Verificar progreso
  const progressRes = await fetch('https://makeseo-mml.pages.dev/api/agent-progress', {
    headers: { 'Authorization': 'Bearer ' + token },
  });
  const progressData = await progressRes.json();
  const p = progressData.profile || {};
  console.log('Perfil después del examen:', {
    exam_passed: p.exam_passed,
    is_partner: p.is_partner,
    partner_at: p.partner_at,
    xp: p.xp,
    level: progressData.level,
  });
}

main().catch(console.error);
