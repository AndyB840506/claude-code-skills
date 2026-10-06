# Handoff: Overhaul de andyfreelancer.com y luccatech.com, publicados

**Date:** 2026-10-06 (martes)
**Machine:** laptop (D:\)
**Status:** Complete. Los dos sitios están en producción y verificados; quedan remates menores.

---

## What We Accomplished This Session

- **andyfreelancer.com rehecho y publicado** (concepto "la talla": piedra en bruto que se talla al hacer scroll, campo de facetas esmeralda en WebGL). Tres idiomas estáticos (`/`, `/es/`, `/pt/`), tasación de sitios en vivo (seis pruebas), asistente Esmeralda con guion de entrada antes del modelo, oferta de fundadores (primeros 10 clientes, 30 %, contador y pop-up), certificado de tasación por correo, WhatsApp y Telegram, datos estructurados y `llms.txt`.
- **Correo arreglado**: pasó de Gmail a Resend con el dominio autenticado (SPF, DKIM, DMARC). mail-tester dio 10 de 10. `/health` reporta `mail: ok`, host `smtp.resend.com`.
- **luccatech.com rehecho y publicado** (concepto "el campo": el puntero es una chispa y 72 líneas de campo exactas corren hasta seis terminales). Inglés en `/`, español en `/es/`. Incluye Lucca Tune "en el laboratorio" y HireSignal como "creado por Andrés para Kuma Talent, la empresa que cofundó".
- **Antes y después medido**: luccatech.com pasó de 4 de 6 (41 KB) a 6 de 6 (29 KB) en la tasación. Ambas mediciones en `the-freelancer/site/baselines/`.
- **Lucca Tech sumada como tercera pieza** de la colección de andyfreelancer, con la franja "Medido, antes y después".
- **Kit de LinkedIn con la marca nueva**: banner, 7 tarjetas y dos fotos de perfil (retrato y gema), con y sin texto. En `D:\Freelancer\linkedin-2026-10\` y en `the-freelancer/marketing/linkedin-assets/output/`.
- **Skill `web-page-kit`**: tres aprendizajes agregados (titular dimensionado por su columna en varios idiomas, franjas en vez de fundido para fondos claro y oscuro, vistas previas de Vercel tras SSO y capturas CDP que se cuelgan).

## Where We Paused

**Last action:** commit `99c4bd5` en `master` de the-freelancer (fotos de perfil de LinkedIn), subido.
**Next action:** quitar "The Freelancer" de las plantillas de correo de cotización y contacto y de los 7 informes de muestra. Es lo único que un cliente todavía puede ver con la marca vieja. Andrés no lo ha aprobado aún: preguntar primero.
**Blockers:** ninguno técnico.

### Pendientes de Andrés (NO VERIFICADOS desde aquí)

- Subir a LinkedIn el banner, las tarjetas, la foto de perfil y el titular nuevo. **Atado al portátil o al repo:** los archivos están en `D:\` del portátil; en el escritorio usar la copia del repo.
- Borrar en la hoja de Google las filas de prueba que empiezan por "PRUEBA Claude". Nunca confirmó que llegaron, así que el registro de prospectos en la hoja sigue sin comprobar.
- Repetir la prueba de correo a Hotmail y marcar "no es spam" (el dominio es nuevo y le falta reputación).
- Abrir los dos sitios en un teléfono real. Solo se probaron en emulación.

## Files to Read First

- `C:\Users\andre\.claude\projects\c--Users-andre--claude-skills\memory\project_andyfreelancer_overhaul_2026_10.md` — estado y decisiones del overhaul de andyfreelancer.
- `C:\Users\andre\.claude\projects\c--Users-andre--claude-skills\memory\project_luccatech_overhaul_2026_10.md` — concepto, estructura y receta de deploy de Lucca Tech.
- `C:\Users\andre\repos\the-freelancer\site\` — `index.template.html`, `copy.json`, `chat.json`, `offer.json`, `contact.json`, `build.js`. Se construye con `node site/build.js`.
- `C:\Users\andre\repos\lucca-tech-web\src\` — `page.html` y `copy.json`. Se construye con `node build.js`.

## Notes / Gotchas

- **Repos y commits:** the-freelancer `master` en `99c4bd5`; lucca-tech-web `master` en `db4cb2e`. Ambos subidos.
- **the-freelancer despliega solo al hacer push a `master`** (DigitalOcean, 2 a 4 minutos). **lucca-tech-web NO**: es manual por Vercel con build local (`vercel pull`, `vercel build --prod`, `vercel deploy --prebuilt --prod`, con `NODE_OPTIONS=--use-system-ca`). El `.vercel/project.json` se recrea a mano en cada máquina; los IDs están en la memoria de Lucca Tech.
- **Variables de entorno en DigitalOcean:** las del COMPONENTE ganan a las de la app. Editar en el nivel equivocado costó varias rondas con el SMTP.
- **Oferta de fundadores:** el contador está en 0 de 10. Al cerrar un cliente, subir `taken` a mano en `site/offer.json`, reconstruir y hacer push. Al llegar a 10 la oferta desaparece sola de la página, el pop-up, `llms.txt` y el prompt.
- **Sin commitear a propósito en the-freelancer:** `.env.example`, `concepts/`, `outreach/`. `freelancer/chat/widget.js` quedó en disco sin uso. Andrés no ha decidido qué hacer con ellos.
- **La versión 16-bit de Lucca Tech** sigue en el repo como `index-16bit.html`, fuera del despliegue (`.vercelignore`).
- **Portugués:** toda la versión `/pt/` de andyfreelancer la escribió Claude; no la ha revisado un nativo.
- **Foto de perfil:** la fuente es una selfie de 720×900 con el teléfono en la oreja. Con una foto de frente y más resolución, `marketing/linkedin-assets/avatar-portrait.py` la rehace en un minuto (usa el Python de ComfyUI y un modelo en `D:\AI\models\rembg\`, **solo en el portátil**).
- **Lección de la sesión:** tres veces la primera versión fue "mediocre" (primera página, fotos de perfil) por entregar algo funcional en vez de algo al nivel del sitio. Regla guardada en memoria: una prueba a nivel premium antes de la página completa, y los assets de marca se entregan como juego completo.
- **Prospectos de GEO y Twilight Medical:** en pausa por decisión de Andrés; nadie respondió.

## Questions to Answer

- ¿Se renombra "The Freelancer" en correos e informes de muestra?
- ¿Qué se hace con `.env.example`, `concepts/`, `outreach/` y `widget.js` en the-freelancer?
- ¿Llegaron las filas de prueba a la hoja de Google?
- ¿Hay una foto mejor para el perfil de LinkedIn?
