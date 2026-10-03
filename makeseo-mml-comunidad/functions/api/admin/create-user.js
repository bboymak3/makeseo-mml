// functions/api/admin/create-user.js
// POST: Crear nuevo usuario (solo admin)

import { corsResponse, requireAdmin, errorResponse } from '../../_lib/auth.js';

export async function onRequestOptions() {
  return new Response(null, { headers: corsResponse({}, 200).headers });
}

async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
  return Array.from(new Uint8Array(hashBuffer)).map(b => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequestPost(context) {
  try {
    const { request, env } = context;
    const auth = await requireAdmin(request, env);
    if (auth.error) return auth.error;

    const { name, email, password, role } = await request.json();

    if (!name || !email || !password) {
      return errorResponse('Nombre, email y contraseña son requeridos', 400);
    }
    if (password.length < 6) {
      return errorResponse('La contraseña debe tener al menos 6 caracteres', 400);
    }
    if (!['user', 'admin'].includes(role)) {
      return errorResponse('Rol inválido. Debe ser "user" o "admin"', 400);
    }

    // Verificar email no exista
    const existing = await env.DB.prepare('SELECT id FROM mml_users WHERE email = ?').bind(email.toLowerCase()).first();
    if (existing) {
      return errorResponse('Ya existe un usuario con ese email', 409);
    }

    const passwordHash = await sha256(password);
    const result = await env.DB.prepare(
      'INSERT INTO mml_users (name, email, password_hash, role, user_type, auth_provider, is_active) VALUES (?, ?, ?, ?, ?, ?, 1)'
    ).bind(name, email.toLowerCase(), passwordHash, role, role === 'admin' ? 'admin' : 'agent', 'email').run();

    return corsResponse({
      success: true,
      id: result.meta.last_row_id,
      message: 'Usuario creado correctamente',
    });
  } catch (e) {
    return errorResponse('Error al crear usuario: ' + e.message, 500);
  }
}
