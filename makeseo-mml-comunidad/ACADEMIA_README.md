# Academia MML — Edward Valencia / @makeseo

Sistema completo de academia online para el Método Malla Local (MML), con login de agentes, dashboard, certificados y panel de administración.

## 🚀 URLs

| Recurso | URL |
|---------|-----|
| **Login agentes** | https://makeseo.app/academia/login.html |
| **Panel admin** | https://makeseo.app/academia/admin.html |
| **Dashboard academia** | https://makeseo.app/academia/ |
| **Sitio principal** | https://makeseo.app/ |

## 🔐 Cuenta admin

Si la base de datos se creó con la cuenta admin por defecto del seed, entra al panel admin, crea un
usuario con rol admin y tu email real, y elimina la cuenta por defecto. No escribas contraseñas en este archivo.

## 🗄️ Base de datos D1

Se usa la base de datos existente `generico_db` (ID: `38dd85ba-03dc-4937-af19-4d1c41a18f27`).

**Todas las tablas de la academia tienen el prefijo `mml_`** para evitar conflictos:
- `mml_users` — usuarios (agentes y admins)
- `mml_agent_classes` — clases de la academia
- `mml_class_questions` — preguntas de cada clase
- `mml_user_class_progress` — progreso de usuarios por clase
- `mml_agent_profiles` — perfil de agente (nivel, XP, partner)
- `mml_user_badges` — insignias/medallas
- `mml_academy_config` — configuración clave-valor
- `mml_exam_attempts` — intentos de examen final

## 🔑 Inicio de sesión

La academia usa solo **email y contraseña**. El login con Google se quitó (botón y endpoints `/api/auth/google*`).

## 📂 Estructura del proyecto

```
makeseo-mml-comunidad/
├── public/                          # Estáticos
│   ├── index.html                   # Landing principal MML
│   ├── academia/
│   │   ├── index.html               # Dashboard del agente (de meridaunclick)
│   │   ├── login.html               # Login (email/password)
│   │   └── admin.html               # Panel admin para crear usuarios
│   ├── js/
│   │   ├── academia-admin.js        # JS del dashboard
│   │   ├── academy-certificate.js   # Generación de certificados
│   │   └── auth.js                  # Auth helper
│   └── ...
├── functions/                       # Cloudflare Pages Functions
│   ├── _lib/
│   │   ├── auth.js                  # JWT + requireAdmin + cors
│   │   ├── academy-levels.js
│   │   ├── academy-path.js
│   │   └── academy-video.js
│   └── api/
│       ├── auth/
│       │   ├── login.js             # POST /api/auth/login
│       │   ├── register.js          # POST /api/auth/register
│       │   ├── me.js                # GET /api/auth/me
│       ├── admin/
│       │   ├── create-user.js       # POST /api/admin/create-user
│       │   ├── users/index.js       # GET /api/admin/users
│       │   ├── users/[id].js        # PATCH/DELETE /api/admin/users/:id
│       │   └── stats.js             # GET /api/admin/stats
│       ├── agent-classes/           # CRUD de clases
│       ├── agent-exam/              # Examen final
│       ├── agent-progress/          # Progreso
│       ├── academy-config/          # Config
│       └── migrate/agent-academy.js # Migración inicial
├── schema_mml_academia.sql          # Schema D1 con prefijos mml_
└── wrangler.toml                    # Config Cloudflare (D1 + vars)
```

## 🛠️ Comandos útiles

```bash
# Aplicar schema (ya hecho)
npx wrangler d1 execute generico_db --remote --file=./schema_mml_academia.sql

# Ver datos de una tabla
npx wrangler d1 execute generico_db --remote --command="SELECT * FROM mml_users"

# Deploy
npx wrangler pages deploy public --project-name=makeseo-mml --branch=main --commit-dirty=true

# Ejecutar migración de academia (crear tablas faltantes)
# Visita: https://makeseo.app/api/migrate/agent-academy
```

## 🔧 Variables de entorno

- `JWT_SECRET` — **secreto** en Cloudflare (proyecto → Configuración → Variables y secretos). Obligatorio: el código ya no tiene clave por defecto. Cambiarlo cierra las sesiones abiertas.
- `APP_URL` — `https://makeseo.app` (en `wrangler.toml`)

## 📊 Endpoints API

### Auth
- `POST /api/auth/login` — login con email/password
- `POST /api/auth/register` — registro público (si está habilitado)
- `GET /api/auth/me` — datos del usuario autenticado

### Admin (requiere rol admin)
- `POST /api/admin/create-user` — crear usuario
- `GET /api/admin/users` — listar usuarios
- `PATCH /api/admin/users/:id` — activar/desactivar
- `DELETE /api/admin/users/:id` — eliminar (no admins)
- `GET /api/admin/stats` — estadísticas

### Academia (requiere auth)
- `GET /api/agent-classes` — listar clases
- `GET /api/agent-classes/:id` — detalle de clase
- `GET /api/agent-classes/:id/questions` — preguntas
- `POST /api/agent-progress` — guardar progreso
- `GET /api/agent-exam` — examen final
- `POST /api/agent-exam` — enviar respuestas

## ⚠️ Lo que falta configurar TÚ

1. **Cambiar contraseña del admin default** — entra al panel admin y crea tu propia cuenta admin, luego elimina `admin@makeseo.local`
3. **Crear clases y preguntas** — desde el panel admin o vía API
4. **Personalizar el dashboard** — `public/academia/index.html` tiene el branding de AunClick, adaptarlo a MML

## 🔒 Seguridad

- ✅ Contraseñas hasheadas con SHA-256
- ✅ JWT firmado con HMAC-SHA256
- ✅ Middleware `requireAdmin` en endpoints admin
- ✅ No se pueden eliminar usuarios admin
- ✅ No se puede eliminar la propia cuenta
- ✅ Variables de entorno en Cloudflare (no en código)
