// functions/api/admin/mml_users/[id].js
// PATCH: Activar/desactivar usuario
// DELETE: Eliminar usuario

import { corsResponse, requireAdmin, errorResponse } from '../../../_lib/auth.js';

export async function onRequestOptions() {
  return new Response(null, { headers: corsResponse({}, 200).headers });
}

export async function onRequestPatch(context) {
  try {
    const { request, env, params } = context;
    const auth = await requireAdmin(request, env);
    if (auth.error) return auth.error;

    const userId = params.id;
    const body = await request.json();

    // Solo permitir actualizar is_active por ahora
    if (body.is_active !== undefined) {
      await env.DB.prepare('UPDATE mml_users SET is_active = ?, updated_at = datetime(\'now\') WHERE id = ?')
        .bind(body.is_active ? 1 : 0, userId).run();
      return corsResponse({ success: true, message: 'Usuario actualizado' });
    }

    return errorResponse('Nada que actualizar', 400);
  } catch (e) {
    return errorResponse('Error: ' + e.message, 500);
  }
}

export async function onRequestDelete(context) {
  try {
    const { request, env, params } = context;
    const auth = await requireAdmin(request, env);
    if (auth.error) return auth.error;

    const userId = params.id;

    // No permitir eliminarse a sí mismo
    const authHeader = request.headers.get('Authorization');
    const token = authHeader.slice(7);
    // Decode JWT payload para obtener user id
    const payloadB64 = token.split('.')[1];
    const payload = JSON.parse(atob(payloadB64.replace(/-/g, '+').replace(/_/g, '/')));
    if (String(payload.sub) === String(userId)) {
      return errorResponse('No puedes eliminar tu propia cuenta', 400);
    }

    // No eliminar admins
    const user = await env.DB.prepare('SELECT role FROM mml_users WHERE id = ?').bind(userId).first();
    if (!user) return errorResponse('Usuario no encontrado', 404);
    if (user.role === 'admin') {
      return errorResponse('No se pueden eliminar cuentas admin', 400);
    }

    await env.DB.prepare('DELETE FROM mml_users WHERE id = ?').bind(userId).run();
    return corsResponse({ success: true, message: 'Usuario eliminado' });
  } catch (e) {
    return errorResponse('Error: ' + e.message, 500);
  }
}
