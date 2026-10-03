// functions/api/upload/index.js
// POST: Subir imagen (avatar del usuario) - guarda como base64 en mml_users.avatar
// Recibe multipart/form-data con campo "file"

import { corsResponse, getUserFromRequest, errorResponse } from '../../_lib/auth.js';

export async function onRequestOptions() {
  return new Response(null, { headers: corsResponse({}, 200).headers });
}

export async function onRequestPost(context) {
  try {
    const { request, env } = context;
    const user = await getUserFromRequest(request, env);
    if (!user) return errorResponse('Token requerido o inválido', 401);

    const userId = user.sub || user.id;
    const formData = await request.formData();
    const file = formData.get('file');

    if (!file || !(file instanceof File)) {
      return errorResponse('No se encontró archivo', 400);
    }

    // Validar tipo
    if (!file.type.startsWith('image/')) {
      return errorResponse('Solo se permiten imágenes', 400);
    }

    // Máximo 500KB
    if (file.size > 500 * 1024) {
      return errorResponse('La imagen no puede superar 500KB', 400);
    }

    // Convertir a base64
    const arrayBuffer = await file.arrayBuffer();
    const bytes = new Uint8Array(arrayBuffer);
    let binary = '';
    for (let i = 0; i < bytes.length; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    const base64 = btoa(binary);
    const dataUrl = 'data:' + file.type + ';base64,' + base64;

    // Guardar en mml_users.avatar
    await env.DB.prepare('UPDATE mml_users SET avatar = ?, updated_at = datetime(\'now\') WHERE id = ?')
      .bind(dataUrl, userId).run();

    return corsResponse({
      success: true,
      url: dataUrl,
      message: 'Avatar actualizado',
    });
  } catch (e) {
    return errorResponse('Error: ' + e.message, 500);
  }
}
