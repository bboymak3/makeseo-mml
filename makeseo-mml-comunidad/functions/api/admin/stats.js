// functions/api/admin/stats.js
// GET: Estadísticas del admin

import { corsResponse, requireAdmin, errorResponse } from '../../_lib/auth.js';

export async function onRequestOptions() {
  return new Response(null, { headers: corsResponse({}, 200).headers });
}

export async function onRequestGet(context) {
  try {
    const { request, env } = context;
    const auth = await requireAdmin(request, env);
    if (auth.error) return auth.error;

    const total = await env.DB.prepare('SELECT COUNT(*) as c FROM mml_users').first();
    const agents = await env.DB.prepare("SELECT COUNT(*) as c FROM mml_users WHERE role = 'user' AND is_active = 1").first();
    const partners = await env.DB.prepare('SELECT COUNT(*) as c FROM mml_agent_profiles WHERE is_partner = 1').first().catch(() => ({ c: 0 }));
    const classes = await env.DB.prepare('SELECT COUNT(*) as c FROM mml_user_class_progress WHERE completed = 1').first().catch(() => ({ c: 0 }));

    return corsResponse({
      total: total?.c || 0,
      agents: agents?.c || 0,
      partners: partners?.c || 0,
      classes_completed: classes?.c || 0,
    });
  } catch (e) {
    return errorResponse('Error: ' + e.message, 500);
  }
}
