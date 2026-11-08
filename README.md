# MakeSEO Academy — Edward Valencia | MML

Plataforma educativa de SEO Local y Marketing Digital. Academia + landing principal del ecosistema **makeseo.app**.

## 🚀 URLs

| Servicio | URL |
|----------|-----|
| **Sitio principal** | https://makeseo.app/ |
| **Clientes** | https://makeseo.app/clientes |
| **Servicios** | https://makeseo.app/servicios |
| **Quiénes somos** | https://makeseo.app/quienes-somos |
| **Blog** | https://makeseo.app/blog |
| **FAQ** | https://makeseo.app/faq |
| **Contacto** | https://makeseo.app/contacto |
| **Master Prompt** | https://makeseo.app/master-prompt/ |
| **Academia (login)** | https://makeseo.app/academia/login.html |
| **Academia (dashboard)** | https://makeseo.app/academia/ |
| **Hosting** | Cloudflare Pages (proyecto `makeseo-mml`) |

> Cloudflare Pages sirve las páginas sin `.html` (`/blog.html` redirige a `/blog`).
> Por eso el sitemap, los `canonical` y los datos estructurados usan las URLs sin extensión.

## 🌐 Ecosistema makeseo.app

| Subdominio | Proyecto | Función |
|------------|----------|---------|
| makeseo.app | MakeSEO Academy (este repo) | Academia + Landing |
| bot.makeseo.app | SGC SaaS | Bot WhatsApp citas |
| botproducto.makeseo.app | SGC Tienda | Bot productos |
| flujos.makeseo.app | SGC Flujos | Motor flujos |

## 📁 Estructura del repo

| Carpeta | Contenido |
|---------|-----------|
| `makeseo-mml-comunidad/` | **El sitio que se publica** (landing, academia, functions, `wrangler.toml`). Ver su [README](makeseo-mml-comunidad/README.md). |
| `scripts/tailwind/` | Generador del CSS de Tailwind (`public/css/tailwind.css`). |
| `scripts/` | Scripts sueltos de mantenimiento (enlaces de clientes, CIDs). |
| `globalpro-automotriz/`, `master-prompt-landing/` | Otros proyectos (no se publican con este sitio). |

## ☁️ Despliegue (Cloudflare Pages)

Se despliega solo con cada push a `main`. Configuración del proyecto en Cloudflare
(**Configuración → Compilaciones**):

| Ajuste | Valor |
|--------|-------|
| Directorio raíz | `makeseo-mml-comunidad` |
| Comando de compilación | *(vacío)* |
| Directorio de salida | `public` (lo lee de `wrangler.toml`) |

> No usar submódulos de git en este repo: Cloudflare falla al clonar si hay un
> submódulo sin `.gitmodules`.

## 🎨 CSS (Tailwind compilado)

Las páginas ya **no** usan el Tailwind de CDN. Usan `/css/tailwind.css`, generado a partir
de las clases que aparecen en el HTML. **Si agregas clases nuevas de Tailwind, regenera el CSS:**

```bash
cd scripts/tailwind
npm install
npm run build   # escribe makeseo-mml-comunidad/public/css/tailwind.css
```

Los colores y animaciones propios (`dark-navy`, `primary-cyan`, `accent-orange`, …) están en
`scripts/tailwind/tailwind.config.js`.

## 📋 Características

### Landing
- Portada: hero con botones **"Quiero posicionar mi negocio"** (WhatsApp) y **"Ver nuestros clientes"** → **Nuestros Clientes** justo después.
- **31 fichas de clientes**: 6 destacadas con estrella dorada (Optimus Cars, Global Pro, Electromecánico,
  Tapizado de Volantes, Llanocar, Dr. Automotriz) y el resto en un desplegable "Ver los 31 clientes".
- Cada ficha abre un modal con **perfil de Google** y, si tiene, **"Visitar página web"** (`data-web-url` en la tarjeta).
- Botón rojo **Clientes** en el menú de todas las páginas.
- Orientada al portafolio: Clientes → Servicios → Bots IA → Directorios. Lo educativo va en dos **botones gigantes desplegables**: **ACADEMIA** (academia, agentes, método, tutoriales, comunidad) y **MASTER PROMPT** (generador + playbook).
- Canal @makeseo, Comunidad WhatsApp, Bots IA (BotWA + Bot de Tienda), directorios HolaX y En Santiago.

#### Agregar o editar un cliente
Las tarjetas están en `public/index.html` (sección `#clientes`) y en `public/clientes.html`. Cada una es un
`<div onclick="openClientModal(...)">` con `data-share-url` (perfil de Google) y, opcional, `data-web-url` (web).
Las destacadas llevan borde dorado y `★`. En la portada solo se ven las 6 primeras; el resto queda en el desplegable.

### Academia
- 6 clases MML + examen (14 preguntas)
- Certificado PDF automático
- Niveles y XP (gamificación)
- Canal YouTube configurable (máx. 3)
- Login con email o Google OAuth

### SEO
- Dominio único `https://makeseo.app/` en canonical, Open Graph, JSON-LD, `robots.txt` y sitemap.
- Geo tags y `lang` orientados a **Chile** (`es-CL`, Santiago).
- `sitemap.xml` con 8 URLs públicas (la academia y el admin no se indexan: `noindex`).
- Schema.org: Person, Organization, EducationalOrganization, Course, FAQPage, VideoObject, Service.
- og-image 1200×630.

## 🔐 Credenciales y secretos

**No escribas contraseñas ni claves en este repo.**

- `JWT_SECRET` (firma las sesiones de la academia) debe estar como **Secreto** en Cloudflare:
  proyecto `makeseo-mml` → **Configuración → Variables y secretos** → Agregar → Tipo *Secreto*.
- La base de datos D1 está declarada en `makeseo-mml-comunidad/wrangler.toml` (`generico_db`).

---
**MakeSEO Academy · makeseo.app · Edward Valencia · @makeseo · MML**
