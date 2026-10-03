// functions/api/admin/users/index.js
// GET: Listar todos los usuarios (solo admin)

import { corsResponse, requireAdmin, errorResponse } from '../../../_lib/auth.js';

export async function onRequestOptions() {
  return new Response(null, { headers: corsResponse({}, 200).headers });
}

export async function onRequestGet(context) {
  try {
    const { request, env } = context;
    const auth = await requireAdmin(request, env);
    if (auth.error) return auth.error;

    const result = await env.DB.prepare(
      'SELECT id, name, email, role, is_active, created_at, avatar FROM mml_users ORDER BY created_at DESC LIMIT 500'
    ).all();

    return corsResponse({ users: result.results || [] });
  } catch (e) {
    return errorResponse('Error al listar usuarios: ' + e.message, 500);
  }
}
