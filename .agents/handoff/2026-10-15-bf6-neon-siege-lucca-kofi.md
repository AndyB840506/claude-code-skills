# Handoff: BF6 Meta Ops — Season 5, NEON SIEGE, público en Lucca Tech + Ko-fi
**Date:** 2026-10-15 (jueves)
**Machine:** desktop (E:\)
**Status:** Complete — app pública y verificada en vivo; quedan pruebas que solo Andrés puede hacer

---

## What We Accomplished This Session

- **Meta refrescado a Season 5** (Game Update 2.1.1.0, "Siege of Vegas", 13-oct-2026): armas MP y
  REDSEC con rankings de wzstats (15-oct) + pick rates de Battlefinity (14-oct) + builds de bfhub,
  las 4 armas nuevas (Mk 24, RSPR, Z84M, ELR-40) y los cambios de mando de EA (compensación de
  retroceso 11% → 5%, deadzone 0 ahora es un 0 real).
- **Pestaña VEHICLES nueva:** builds por asiento (BFTactics ago-2026), tier list S/A/B/C, counters
  con Engineer anti-vehículo y ajustes de control. Todas las fuentes de vehículos son PRE-Season 5;
  van con las notas del parche encima.
- **Rediseño "NEON SIEGE"** aprobado por Andrés: paleta MEDIDA en píxeles del key art oficial de S5,
  Tanker + Khand + JetBrains Mono, campo WebGL (bokeh neón + brasas), accesorios que ruedan como
  tragamonedas. Fuentes ocultas (cero nombres de sitios en el texto visible; "Intel" plegables y cajón
  al pie). Animaciones suavizadas a pedido ("no tan bruscas").
- **Publicado en https://www.luccatech.com/bf6/** (lucca-tech-web `cb5d99c`, luego `333cedd`), con
  link "Side project / Proyecto paralelo" en el footer del home EN y ES, y `/bf6/` en sitemap y llms.txt.
  Verificado en vivo: diff byte a byte contra el local = idénticos (124.299 bytes).
- **Ko-fi en lugar de Buy Me a Coffee** (BMC no paga en Colombia): https://ko-fi.com/boogie8405,
  conectado a su PayPal. Botón en el hero y en el footer de /bf6/. Avatar (Z-Image, seed 8405) y bio en
  inglés en `E:\Claude Output\buy-me-a-coffee\`.
- **Skill `bf6-meta-configurator` reestructurada:** la app ya no se escribe a mano. Plantilla en
  `templates/template.html`, `scripts/build.py` inyecta `weapons.json` + `vehicles.json` (en
  `E:\Claude Output\bf6\data\`), y `scripts/verify/verify-all.ps1` verifica 9 corridas con veredicto
  (probado en las dos direcciones: PASS en vivo, FAIL con un bug reintroducido).
- **Retrospectiva aplicada:** trampas de Edge headless en `web-page-kit/docs/mobile-qa-headless.md`,
  guardrail de "estados finales fijados por timer" en design-guide Regla 18, falsa alarma del CLI 54 de
  Vercel en deploy-preflight, trampas de datos de bfhub en run-report.

## Where We Paused
**Last action:** prompt-reviewer quick aplicado (scripts de verificación guardados en la skill, pull
antes del build, ruta completa en SKILL.md).
**Next action:** nada urgente. Al retomar, preguntar si Andrés ya probó Ko-fi y si la página se siente
fluida en su teléfono.
**Blockers:** ninguno técnico.

## Files to Read First
- `C:\Users\andre\.claude\projects\c--Users-andre--claude-skills\memory\project_bf6_meta_ops.md` — estado,
  decisiones de Andrés y pendientes.
- `bf6-meta-configurator/SKILL.md` + `workflows/run-report.md` + `workflows/html-spec.md` — cómo se
  refresca, construye, verifica y publica.

## Notes / Gotchas
- **Atado a máquina:** los datos viven en `E:\Claude Output\bf6\data\` (desktop). En el portátil no
  existen: un refresh allá re-barre todo y no tiene la base anterior para comparar "qué cambió".
- **Deploy de Lucca Tech es manual** (Vercel prebuilt, team `mrputridsden`, `NODE_OPTIONS=--use-system-ca`).
  Confirmar con `vercel inspect https://www.luccatech.com/` y no fiarse del JSON que imprime el CLI.
- `/bf6/` daba 200 ANTES del deploy (el rewrite comodín sirve el home): para verificar, buscar un
  marcador del contenido, no el código HTTP.
- Edge headless miente con páginas animadas: ver `web-page-kit/docs/mobile-qa-headless.md`, sección
  "Animated pages".
- **ComfyUI quedó corriendo** al cierre (ocupa ~12 GB de VRAM). Andrés no respondió si apagarlo.

## Questions to Answer
- ¿Ko-fi recibe pagos? Nadie ha probado una donación real. PayPal Colombia es "solo transfronterizo":
  las donaciones de otros colombianos probablemente fallen (no confirmado).
- ¿Las animaciones se sienten fluidas en su navegador y en su teléfono real? (solo probado en headless)
- ¿Quiere una opción de pago local para donantes colombianos (Nequi / Bre-B)? Haría público un dato suyo.
