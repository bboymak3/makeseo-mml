// functions/api/user-profile/index.js
// GET: Datos del perfil del usuario autenticado (para el dashboard de la academia)
// PUT: Actualizar perfil (nombre, bio, whatsapp, phone, avatar)

import { corsResponse, getUserFromRequest, errorResponse } from '../../_lib/auth.js';

export async function onRequestOptions() {
  return new Response(null, { headers: corsResponse({}, 200).headers });
}

export async function onRequestGet(context) {
  try {
    const { request, env } = context;
    const user = await getUserFromRequest(request, env);
    if (!user) return errorResponse('Token requerido o inválido', 401);

    // Obtener datos completos del usuario desde mml_users
    const row = await env.DB.prepare(`
      SELECT id, name, email, phone, whatsapp, bio, role, avatar, is_active,
             created_at, updated_at, plan_type, plan_expires_at, user_type
      FROM mml_users WHERE id = ?
    `).bind(user.sub || user.id).first();

    if (!row) return errorResponse('Usuario no encontrado', 404);
    if (!row.is_active) return errorResponse('Usuario inactivo', 403);

    // Devolver en formato que espera el dashboard: { user: {...} }
    return corsResponse({
      user: {
        id: row.id,
        name: row.name,
        email: row.email,
        phone: row.phone,
        whatsapp: row.whatsapp,
        bio: row.bio,
        role: row.role,
        avatar: row.avatar,
        user_type: row.user_type,
        plan_type: row.plan_type,
        plan_expires_at: row.plan_expires_at,
        created_at: row.created_at,
      }
    });
  } catch (e) {
    return errorResponse('Error: ' + e.message, 500);
  }
}

export async function onRequestPut(context) {
  try {
    const { request, env } = context;
    const user = await getUserFromRequest(request, env);
    if (!user) return errorResponse('Token requerido o inválido', 401);

    const body = await request.json();
    const userId = user.sub || user.id;

    // Solo permitir actualizar campos seguros
    const updates = {};
    if (body.name !== undefined) updates.name = String(body.name).slice(0, 100);
    if (body.bio !== undefined) updates.bio = String(body.bio).slice(0, 500);
    if (body.whatsapp !== undefined) updates.whatsapp = String(body.whatsapp).slice(0, 30);
    if (body.phone !== undefined) updates.phone = String(body.phone).slice(0, 30);
    if (body.avatar !== undefined) updates.avatar = String(body.avatar).slice(0, 500);

    const fields = Object.keys(updates);
    if (fields.length === 0) {
      return errorResponse('Nada que actualizar', 400);
    }

    const setClause = fields.map(f => f + ' = ?').join(', ');
    const values = fields.map(f => updates[f]);
    values.push(userId);

    await env.DB.prepare(
      'UPDATE mml_users SET ' + setClause + ', updated_at = datetime(\'now\') WHERE id = ?'
    ).bind(...values).run();

    // Devolver usuario actualizado
    const row = await env.DB.prepare(`
      SELECT id, name, email, phone, whatsapp, bio, role, avatar, is_active, created_at, plan_type
      FROM mml_users WHERE id = ?
    `).bind(userId).first();

    return corsResponse({
      success: true,
      user: row,
    });
  } catch (e) {
    return errorResponse('Error: ' + e.message, 500);
  }
}
