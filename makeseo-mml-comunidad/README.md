# MakeSEO Academy · Método Malla Local (MML)

Proyecto completo de la marca personal y academia de **Edward Valencia (@makeseo)**, creador del Método Malla Local (MML). Incluye landing principal, academia online con login, dashboard de agente, examen final, certificados PDF y panel de administración.

## 🚀 URLs en producción

| Recurso | URL |
|---------|-----|
| **Landing principal** | https://makeseo.app/ |
| **Clientes** | https://makeseo.app/clientes |
| **Login academia** | https://makeseo.app/academia/login.html |
| **Dashboard agente** | https://makeseo.app/academia/ |
| **Panel admin** | https://makeseo.app/academia/admin.html (no enlazado desde la web, `noindex`) |
| **Master Prompt MML** | https://makeseo.app/master-prompt/ |
| **Archivo .md descargable** | https://makeseo.app/master-prompt.md |
| **PDF plantilla certificado** | https://makeseo.app/partnerdigimon.pdf |

Dominio oficial: **makeseo.app** (el proyecto también responde en `makeseo-mml.pages.dev`, pero todas las
URLs canónicas, el sitemap y `robots.txt` apuntan a makeseo.app).

## 🔐 Cuenta admin

Si la base de datos se creó con la cuenta admin por defecto del seed, entra al panel admin, crea tu
propia cuenta admin y elimina la de por defecto. No escribas contraseñas en este README.

## 📐 Estructura del proyecto

```
makeseo-mml-comunidad/
├── public/                              # Estáticos
│   ├── index.html                       # Landing principal (ver "Landing principal" abajo)
│   ├── clientes.html, servicios.html, quienes-somos.html, blog.html, faq.html, contacto.html
│   ├── css/tailwind.css                 # Tailwind compilado (generado con scripts/tailwind en la raíz del repo)
│   ├── sitemap.xml, robots.txt          # SEO (dominio makeseo.app, URLs sin .html)
│   ├── favicon-32.png
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
├── wrangler.toml                        # Config Cloudflare (D1 + variables públicas). JWT_SECRET va como secreto en el panel
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

Secciones en orden (`public/index.html`). La portada está orientada al **portafolio de clientes**;
el contenido educativo queda dentro de dos botones gigantes desplegables (`<details class="mega">`):

1. **Hero** — H1 "Método Malla Local", botones **Quiero posicionar mi negocio** (WhatsApp), **Ver nuestros clientes**, YouTube y Canal WhatsApp
2. **Nuestros Clientes** (`#clientes`) — 6 destacados con ★ dorada + "Ver los 31 clientes". Cada ficha abre un modal con perfil de Google y "Visitar página web" si tiene `data-web-url`
3. **Servicios 360 Soluciones** (`#contacto`)
4. **Bots IA (BotWA)** (`#bots-ia`)
5. **Directorios comerciales** (`#directorios`) — HolaX y En Santiago
6. **🎓 ACADEMIA** (botón gigante naranja, `#grupo-academia`) — al abrirlo: CTA Academia, Agentes Certificados, ¿Qué es el MML?, 3 Pilares (`#metodo`), Tutoriales YouTube, Comunidad WhatsApp
7. **🤖 MASTER PROMPT** (botón gigante celeste, `#grupo-master-prompt`) — al abrirlo: generador por nicho (`#prompt-generador`) y playbook completo (`#master-prompt`)
8. **FAQ** (`#faq-index`)
9. **Footer** + botones flotantes (WhatsApp derecha, YouTube izquierda)

Los enlaces a una sección que está dentro de un botón gigante (por ejemplo `#metodo` en el menú o `/#comunidad`
desde otra página) abren el desplegable automáticamente (`mmlOpenHash` en el JS de la portada).

**Menú:** enlaces + botones de colores **Clientes** (rojo), **Comunidad** (verde) y **Academia** (naranja).
Entre 1024 y 1279 px los tres botones muestran solo el ícono para que el menú quepa.

### Clientes destacados y webs
Destacados (orden fijo, borde dorado y ★): Optimus Cars SPA, GLOBAL PRO Automotriz, ELECTROMECANICO,
TAPIZADO DE VOLANTES, LLANOCAR CL, DR.AUTOMOTRIZ. 21 clientes tienen web (`data-web-url`); el resto muestra
"Página web (próximamente)". Las tarjetas están duplicadas en `index.html` y `clientes.html`: cambia ambas.

## 🔧 Stack técnico

- **Frontend:** HTML estático + Tailwind CSS compilado (`public/css/tailwind.css`) + Vanilla JS
- **Backend:** Cloudflare Pages Functions (Workers)
- **Base de datos:** Cloudflare D1 (SQLite)
- **Auth:** JWT (HMAC-SHA256) + Google OAuth (opcional)
- **PDF:** pdf-lib + jsPDF + pdf.js
- **Hosting:** Cloudflare Pages ($0)
- **Fonts:** Inter + Poppins (Google Fonts)

## ⚙️ Variables de entorno

| Variable | Dónde | Notas |
|----------|-------|-------|
| `JWT_SECRET` | **Secreto** en Cloudflare (proyecto → Configuración → Variables y secretos) | Obligatoria. Sin ella el login falla (ya no hay clave por defecto en el código). Cambiarla cierra las sesiones abiertas. |
| `APP_URL` | `wrangler.toml` `[vars]` | `https://makeseo.app` |
| `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` | Secretos en Cloudflare | Solo si usas Google OAuth |

### Despliegue en Cloudflare Pages
Directorio raíz del proyecto: `makeseo-mml-comunidad` · comando de compilación vacío · salida `public`
(se lee de `wrangler.toml`). Se despliega solo con cada push a `main`.

### Regenerar el CSS
Si agregas clases de Tailwind que no existían en el HTML:
```bash
cd ../scripts/tailwind && npm install && npm run build
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
# Visita: https://makeseo.app/api/migrate/agent-academy
```

## 🔒 Seguridad

- ✅ Contraseñas hasheadas con SHA-256
- ✅ JWT firmado con HMAC-SHA256
- ✅ Middleware `requireAdmin` en endpoints admin
- ✅ No se pueden eliminar usuarios admin
- ✅ No se puede eliminar la propia cuenta
- ✅ `JWT_SECRET` como secreto de Cloudflare, sin valores por defecto en el código
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
2. **JWT_SECRET** — guárdalo como secreto en Cloudflare y quita la línea de `wrangler.toml`
3. **Google OAuth** (opcional) — configura `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET` como secretos en Cloudflare
4. **Videos de clases 4, 5, 6** — cuando Edward suba los videos a YouTube, actualiza el campo `video_url` en la DB
5. **Personalizar agentes certificados** — los 4 perfiles en la landing son de ejemplo, reemplaza con agentes reales

## 📞 Contacto

- **YouTube:** https://youtube.com/@makeseo
- **WhatsApp:** https://whatsapp.com/channel/0029VbDhWAHLo4hmIWhEhI1w
- **Servicios:** 360 Soluciones · +58 416-777-5771
- **Correo:** correo36000@gmail.com

---

**MakeSEO Academy · Método Malla Local (MML) · Edward Valencia · @makeseo · 360 Soluciones**
