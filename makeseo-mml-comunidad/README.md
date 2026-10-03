# MakeSEO Academy · Método Malla Local (MML)

Proyecto completo de la marca personal y academia de **Edward Valencia (@makeseo)**, creador del Método Malla Local (MML). Incluye landing principal, academia online con login, dashboard de agente, examen final, certificados PDF y panel de administración.

## 🚀 URLs en producción

| Recurso | URL |
|---------|-----|
| **Landing principal** | https://makeseo-mml.pages.dev |
| **Login academia** | https://makeseo-mml.pages.dev/academia/login.html |
| **Dashboard agente** | https://makeseo-mml.pages.dev/academia/ |
| **Panel admin** | https://makeseo-mml.pages.dev/academia/admin.html |
| **Master Prompt MML** | https://makeseo-mml.pages.dev/master-prompt |
| **Archivo .md descargable** | https://makeseo-mml.pages.dev/master-prompt.md |
| **PDF plantilla certificado** | https://makeseo-mml.pages.dev/partnerdigimon.pdf |

## 🔐 Credenciales por defecto (CAMBIAR)

- **Email:** `admin@makeseo.local`
- **Contraseña:** `admin123`

⚠️ Entra al panel admin y crea tu propia cuenta admin, luego elimina la default.

## 📐 Estructura del proyecto

```
makeseo-mml-comunidad/
├── public/                              # Estáticos
│   ├── index.html                       # Landing principal (Hero + MML + 3 Pilares + Agentes + Generador Prompt + Comunidad + 360 Soluciones)
│   ├── favicon.svg
│   ├── partnerdigimon.pdf               # Plantilla del certificado PDF (203KB)
│   ├── master-prompt.md                 # Master prompt descargable
│   ├── academia/
│   │   ├── index.html                   # Dashboard del agente (clases, examen, certificado)
│   │   ├── login.html                   # Login (email/password + Google OAuth)
│   │   └── admin.html                   # Panel admin (usuarios, agentes, clases, preguntas, certificados)
│   ├── master-prompt/
│   │   └── index.html                   # Landing del master prompt con botón copiar
│   └── js/
│       ├── academia-admin.js            # JS del dashboard original (adaptado)
│       ├── academy-certificate.js       # Generación de certificados PDF (pdf-lib + jsPDF)
│       └── auth.js                      # Helper de auth
├── functions/                           # Cloudflare Pages Functions
│   ├── _lib/
│   │   ├── auth.js                      # JWT + requireAdmin + cors
│   │   ├── academy-levels.js            # Cálculo de niveles y XP
│   │   ├── academy-path.js              # Ruta de aprendizaje y bloqueos
│   │   └── academy-video.js             # Helper de videos YouTube
│   └── api/
│       ├── auth/                        # Login, register, me, google OAuth
│       │   ├── login.js
│       │   ├── register.js
│       │   ├── me.js
│       │   ├── google.js
│       │   └── google-config.js
│       ├── user-profile/                # GET/PUT perfil del agente
│       ├── upload/                      # POST subir avatar (base64)
│       ├── agent-classes/               # CRUD clases + preguntas
│       ├── agent-exam/                  # Examen final (questions + submit)
│       ├── agent-progress/              # Progreso del agente
│       ├── academy-config/              # Config clave-valor
│       ├── partners/                    # Lista pública de Partners Digitales
│       ├── admin/
│       │   ├── create-user.js           # Crear usuario
│       │   ├── users/                   # Listar, activar, eliminar usuarios
│       │   ├── stats.js                 # Estadísticas
│       │   ├── academy-agents/          # Lista de agentes con progreso
│       │   ├── academy-analytics/       # Analíticas
│       │   └── agent-actions/           # Graduar, revocar, asignar, medallas
│       └── migrate/
│           └── agent-academy.js         # Migración inicial de tablas
├── schema_mml_academia.sql              # Schema D1 (8 tablas con prefijo mml_)
├── seed_clases_mml.sql                  # 6 clases de la serie MML + preguntas
├── seed_complete_classes.sql            # Marcar clases como completadas (test)
├── wrangler.toml                        # Config Cloudflare (D1 + JWT_SECRET)
└── README.md                            # Este archivo
```

## 🗄️ Base de datos D1

Usa la base de datos existente `generico_db` (ID: `38dd85ba-03dc-4937-af19-4d1c41a18f27`).

**Todas las tablas tienen prefijo `mml_`** para evitar conflictos:

| Tabla | Función |
|-------|---------|
| `mml_users` | Usuarios (agentes y admins) |
| `mml_agent_classes` | Clases de la academia |
| `mml_class_questions` | Preguntas de cada clase |
| `mml_user_class_progress` | Progreso de usuarios por clase |
| `mml_agent_profiles` | Perfil de agente (nivel, XP, partner, graduado) |
| `mml_user_badges` | Insignias/medallas |
| `mml_academy_config` | Configuración clave-valor |
| `mml_exam_attempts` | Intentos de examen final |

## 📚 Contenido de la academia

### 6 Clases (Serie MML de Edward Valencia)

| # | Clase | Módulo | Preguntas | Video |
|---|-------|--------|-----------|-------|
| 1 | De 0 a Clientes Diarios con SEO Local | Fundamentos | 2 | MGcITnwpgCo |
| 2 | Ficha Maestra NAP y Configuración SAB | Fundamentos | 3 | 0Cf8YR0XjWo |
| 3 | Adiós WordPress - Webs con IA, GitHub y Cloudflare | Infraestructura | 3 | PbDUwBGJqm0 |
| 4 | Malla Territorial - Despliegue por comunas | Infraestructura | 2 | Próximamente |
| 5 | Optimización WebP con IA, GTM y Search Console | Optimización | 2 | Próximamente |
| 6 | Automatización de Posts + Circuito de Reseñas | Optimización | 2 | Próximamente |

### Examen final
- **Requisito:** Completar las 6 clases
- **Preguntas:** 14 aleatorias de todas las clases
- **Aprobación:** 80% correctas
- **Intentos:** Máximo 3
- **Recompensa:** +150 XP + estado Partner Digital + certificado PDF

### Certificado PDF
- Plantilla: `partnerdigimon.pdf` (A4 horizontal, 203KB)
- Generación: pdf-lib (escribe nombre, fecha y código sobre la plantilla)
- Fallback: jsPDF si la plantilla no carga
- Vista previa: pdf.js en modal

## 🎨 Landing principal

Secciones en orden:
1. **Hero** — Badge, H1, definición MML, 4 diferenciadores clave, botones YouTube + WhatsApp
2. **CTA Academia** — Botón gigante "IR A LA ACADEMIA"
3. **Agentes Certificados** — 4 perfiles (Edward Valencia, Carlos Mendoza, María Fernández, José Rodríguez)
4. **Generador de Master Prompt** — 12 nichos + input custom + botón copiar + link a chat.z.ai
5. **¿Qué es el MML?** — Definición oficial + 4 diferenciadores explicados
6. **3 Pilares (Trinomio de Autoridad)** — Diagrama: Pilar 1 (GBP) arriba, Pilar 2 (Web Serverless) + Pilar 3 (Malla Territorial) abajo
7. **Tutoriales YouTube** — 6 episodios (3 con embed real, 3 placeholder)
8. **Master Prompt card** — Preview tipo terminal + botones ver/descargar
9. **Comunidad WhatsApp** — CTA masivo con borde gradiente
10. **Servicios 360 Soluciones** — Bloque empresarial + contacto +58 416-777-5771
11. **Footer** — Datos fiscales + links + comunas
12. **Botones flotantes** — WhatsApp (derecha) + YouTube (izquierda)

## 🔧 Stack técnico

- **Frontend:** HTML estático + Tailwind CSS (CDN) + Vanilla JS
- **Backend:** Cloudflare Pages Functions (Workers)
- **Base de datos:** Cloudflare D1 (SQLite)
- **Auth:** JWT (HMAC-SHA256) + Google OAuth (opcional)
- **PDF:** pdf-lib + jsPDF + pdf.js
- **Hosting:** Cloudflare Pages ($0)
- **Fonts:** Inter + Poppins (Google Fonts)

## ⚙️ Variables de entorno

Configuradas en `wrangler.toml`:

```toml
[vars]
JWT_SECRET = "mml_academia_secret_2026_super_seguro_..."
APP_URL = "https://makeseo-mml.pages.dev"
# GOOGLE_CLIENT_ID = "configurar-si-usas-google-oauth"
# GOOGLE_CLIENT_SECRET = "configurar-si-usas-google-oauth"
```

## 📊 Endpoints API

### Auth (público)
| Endpoint | Método | Función |
|----------|--------|---------|
| `/api/auth/login` | POST | Login email/password → JWT |
| `/api/auth/register` | POST | Registro público |
| `/api/auth/me` | GET | Datos del usuario autenticado |
| `/api/auth/google` | GET | Callback Google OAuth |
| `/api/auth/google-config` | GET | Config Google OAuth |

### Agente (requiere auth)
| Endpoint | Método | Función |
|----------|--------|---------|
| `/api/user-profile` | GET | Perfil del agente |
| `/api/user-profile` | PUT | Actualizar perfil |
| `/api/upload` | POST | Subir avatar (base64) |
| `/api/agent-classes` | GET | Listar clases |
| `/api/agent-classes/:id` | GET | Detalle de clase |
| `/api/agent-classes/:id/questions` | GET | Preguntas de una clase |
| `/api/agent-progress` | GET | Progreso del agente |
| `/api/agent-progress` | POST | Guardar progreso |
| `/api/agent-exam` | GET | Estado del examen |
| `/api/agent-exam/questions` | GET | Preguntas del examen |
| `/api/agent-exam` | POST | Enviar respuestas |

### Admin (requiere rol admin)
| Endpoint | Método | Función |
|----------|--------|---------|
| `/api/admin/create-user` | POST | Crear usuario |
| `/api/admin/users` | GET | Listar usuarios |
| `/api/admin/users/:id` | PATCH | Activar/desactivar |
| `/api/admin/users/:id` | DELETE | Eliminar (no admins) |
| `/api/admin/stats` | GET | Estadísticas |
| `/api/admin/academy-agents` | GET | Agentes con progreso |
| `/api/admin/agent-actions` | POST | Graduar, revocar, asignar, medallas |

### Público
| Endpoint | Método | Función |
|----------|--------|---------|
| `/api/partners` | GET | Lista de Partners Digitales |
| `/api/academy-config` | GET | Config de la academia |

## 🛠️ Comandos útiles

```bash
# Deploy
npx wrangler pages deploy public --project-name=makeseo-mml --branch=main --commit-dirty=true

# Aplicar schema
npx wrangler d1 execute generico_db --remote --file=./schema_mml_academia.sql

# Cargar clases
npx wrangler d1 execute generico_db --remote --file=./seed_clases_mml.sql

# Ver datos
npx wrangler d1 execute generico_db --remote --command="SELECT * FROM mml_users"
npx wrangler d1 execute generico_db --remote --command="SELECT * FROM mml_agent_classes"
npx wrangler d1 execute generico_db --remote --command="SELECT * FROM mml_agent_profiles"

# Migración (crear tablas faltantes)
# Visita: https://makeseo-mml.pages.dev/api/migrate/agent-academy
```

## 🔒 Seguridad

- ✅ Contraseñas hasheadas con SHA-256
- ✅ JWT firmado con HMAC-SHA256
- ✅ Middleware `requireAdmin` en endpoints admin
- ✅ No se pueden eliminar usuarios admin
- ✅ No se puede eliminar la propia cuenta
- ✅ Variables de entorno en wrangler.toml (no en código)
- ✅ Todas las tablas con prefijo `mml_` (sin conflictos)

## ✅ Bugs corregidos (auditoría final)

| Bug | Estado |
|-----|--------|
| Referencias "AunClick" en agent-actions, agent-exam, google.js, register.js | ✅ Corregido |
| `/perfil.html` en URL de verificación del certificado | ✅ Corregido → `/academia/?user=` |
| `favicon.jpeg` no existe en academia/index.html | ✅ Corregido → `/favicon.svg` |
| Comentario `/academia-admin` en agent-classes | ✅ Corregido |
| `mml_exam_attempts` (columna mal prefijada) | ✅ Corregido → `exam_attempts` |
| Redirección `/login.html` causaba loop en dashboard | ✅ Corregido → `/academia/login.html` |
| `meridaunclick_token` en localStorage | ✅ Corregido → `mml_token` |
| Endpoint `/api/user-profile` no existía (devolvía HTML) | ✅ Creado |
| Endpoint `/api/upload` no existía | ✅ Creado |
| Acción `graduate` requería examen previo | ✅ Corregido (admin puede graduar directo) |

## ⚠️ Configuración pendiente (TÚ)

1. **Cambiar contraseña admin** — crea tu cuenta admin y elimina `admin@makeseo.local`
2. **Google OAuth** (opcional) — configura `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET` en Cloudflare Pages → Settings → Environment variables
3. **Videos de clases 4, 5, 6** — cuando Edward suba los videos a YouTube, actualiza el campo `video_url` en la DB
4. **Personalizar agentes certificados** — los 4 perfiles en la landing son de ejemplo, reemplaza con agentes reales

## 📞 Contacto

- **YouTube:** https://youtube.com/@makeseo
- **WhatsApp:** https://whatsapp.com/channel/0029VbDhWAHLo4hmIWhEhI1w
- **Servicios:** 360 Soluciones · +58 416-777-5771

---

**MakeSEO Academy · Método Malla Local (MML) · Edward Valencia · @makeseo · 360 Soluciones**
