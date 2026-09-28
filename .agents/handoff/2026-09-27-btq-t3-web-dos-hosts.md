# Handoff: BTQ T3, web rediseñada para dos hosts (en vivo)
**Date:** 2026-09-27
**Machine:** escritorio (E:\)
**Status:** Complete. behind-thequeue.com publicado con el rediseño T3 y verificado en vivo.

---

## What We Accomplished This Session

- **Rediseño completo de behind-thequeue.com para la T3** (Andy + Alejandro), concepto "Línea abierta":
  - Paleta del logo EN VIVO aprobado: crema `#FDF9EF`, azul marino `#03053C`, coral `#F65B51` (texto `#D2382E`) = Andrés, azul `#1268FC` = Alejandro.
  - Onda de conversación global (canvas 2D) que reacciona al puntero, al scroll y al clic. El hero queda fijo en escritorio, el título se parte y las fotos se separan.
  - "De qué hablamos": 5 temas de T3 como lista que se abre. EP.01 aparece como "próximamente", seguido del archivo de T2 (020–023).
  - "Quiénes somos" con los dos. La bio de Alejandro es su texto más un párrafo sobre su papel en el show. Su LinkedIn: `https://www.linkedin.com/in/alejandro-aguirre-hernandez/`.
  - La foto de Alejandro es **generada con IA y él la aprobó** (decisión de Andy). Reemplaza la regla "fotos reales" del handoff del 09-26.
  - El embed de Spotify se reemplazó por una tarjeta propia (ver Gotchas).
  - `ep.css` pasó a la paleta T3, así que `/episodios` coincide con la portada. La og-image nueva es `og-image-t3.jpg` (150 KB).
- **Verificado:**
  - Edge headless en 360, 390, 768, 820, 1024, 1180 y 1440: ancho del documento igual al del dispositivo, 0 errores, 0 revelables atascados.
  - Paridad de enlaces contra la versión anterior: el formulario Web3Forms, el mailto, las redes y las anclas siguen iguales.
  - En vivo con `curl -L`: los assets llegan con los mismos bytes que los archivos locales.
- **Deploy a producción** con `vercel --prod`, que quedó aliasado a behind-thequeue.com.
- **Commits:** `fd0c114`, `f92433f`, `c58c962`, más los de la retrospectiva y el cierre.
- **Retrospectiva aplicada:**
  - `web-page-kit/docs/design-guide.md`: 4 guardrails en Rule 18 (from() + transition:all, selectores de pin, overflow del pin, embed de Spotify), matriz de viewports en Rule 10 y paridad por breakpoint en Rule 17.
  - `episode-launch/docs/brand-constants.md`: nueva sección **Identidad T3**; lo de T2 queda marcado como histórico.
  - Memorias actualizadas.

## Where We Paused

**Last action:** cierre de sesión, después del deploy a producción.
**Next action:** esperar el EP.01 de T3. Al publicarlo, volver al embed de Spotify.
**Blockers:** ninguno para la web.

## Next Steps (quién actúa)

1. **Al publicar el EP.01 de T3 (Claude):** en `btq-production/website/index.html`, reemplazar `.player` por el embed que está comentado justo encima, **sin `theme=0`**. Cambiar también la tarjeta "EP.01 próximamente" de la sección Episodios por el episodio real. Después, `vercel --prod` y verificar con `curl -L`.
2. **Pendientes del handoff del 09-26 que esta sesión NO verificó** (NO VERIFICADOS, preguntarle a Andy):
   - Corregir la metadata del RSS en Spotify for Creators: EP.23 S3E1 → S2E23, EP.22 ep 19 → 22, EP.16 sin season → S2E16. Al 2026-09-27 el RSS en vivo **seguía sin corregir**. Hay que hacerlo antes de publicar el EP.01.
   - Subir los 6 transcripts de `E:\Podcast\BTQ\T3-paquete-alejandro\` a la carpeta de Drive y compartirla. Está en el disco del escritorio.
   - Confirmar el roadmap de 8 temas (solo existe en la conversación del 09-26) y elegir el saludo nuevo.
   - Checkpoint antes de la primera grabación: hoja de ruta del EP.01.
3. **Opcional:** el archivo de T2 en la portada muestra 020–023, que eran los que ya tenía; los más recientes son 024–027. Cambiarlo requiere las URLs de Spotify y citas verificadas de cada episodio.
4. **Opcional:** pasar el logo a 3000×3000 o a vector para Spotify y redes (pendiente desde el 09-26).

## Files to Read First

- `btq-production/website/index.html`: la web en vivo; el comentario sobre `.player` explica lo del embed.
- `.claude/skills/episode-launch/docs/brand-constants.md` § Identidad T3.
- Memoria `project_btq_t3_alejandro.md`.

## Notes / Gotchas

- **Embed de Spotify:** no se puede personalizar. `theme=0` sale gris oscuro, y sin él toma el color del arte del último episodio (el EP.27 de T2 salía rojo y con la carátula vieja).
- **Previews de Vercel:** tienen protección de login, así que `curl` no los lee. Solo Andy, logueado, los ve.
- **LinkedIn:** responde 999 a peticiones automáticas. No se pudo verificar que el perfil de Alejandro abra; la URL es la que pegó Andy.
- `start.ps1` sigue avisando de memoria repartida en 3 slugs (`C--Users-andre-repos-kit-skill-creator` tiene 104 archivos). No se tocó.

## Questions to Answer

- ¿Cuándo sale el EP.01 de T3? De eso depende el paso 1.
