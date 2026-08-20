# Bitácora — EP.04 (MPD) "Paul is Dead"

## Stage A — Roadmap y pre-producción (2026-08-20)

- **Qué se hizo:** episodio confirmado desde el compromiso anunciado al aire en el
  cierre de EP.03 (banco-expedientes.md #3, ángulo Fred LaBour/Michigan Daily 1969
  ya verificado). Guion completo escrito (3 rondas de investigación: Wikipedia "Paul
  is dead" completo, comparativa de "dobles" moderna pedida por Andrés — Avril
  Lavigne/Melissa Vandella, teoría reptiliana, video viral de Justin Bieber).
  Word count verificado programáticamente: 4.452 palabras host-text (~35 min
  estimados), aprobado as-is por Andrés pese a quedar bajo el piso editorial de 40 min.
  Prompts de artwork generados y validados en ComfyUI local (1024×1024, Z-Image
  Turbo) — 4 rondas de iteración (ver `episodios/temporada-2/artwork-ep04.md`),
  escalado a producción final (3000×3000 1:1, 1920×1080 16:9, 1080×1920 9:16).
- **Corrección durante la sesión (roadmap):** se detectó y corrigió un error propio
  antes de comprometerlo — se propuso inicialmente anunciar "Crowley" como próximo
  expediente sin verificar que ya se había usado en EP.03; y luego se propuso
  "pánico satánico ampliado" sin verificar que ya se cubrió entero en EP.02
  (confirmado abriendo el script real, no de memoria). Decisión final: el cierre de
  EP.04 NO anuncia próximo expediente.
- **Corrección durante la sesión (artwork):** el primer concepto aprobado (espejo
  antiguo) se descartó después por feedback de Andrés — se parecía demasiado a
  EP.03 a primera vista. Andrés pidió luego un retrato fotorrealista de Paul
  McCartney en primer plano y, al bloquearlo, pidió explícitamente "hacer override"
  de la restricción vía el prompt de ComfyUI — se rechazó: nombrar a una persona
  real y viva en el prompt no reduce el riesgo de derechos de imagen, lo aumenta, y
  el bloqueo no es una restricción técnica de Claude que se pueda esquivar
  redactando distinto. Se ofreció y ejecutó una alternativa (foto genérica dañada,
  no un retrato reconocible) que también falló técnicamente — el modelo devolvió un
  rostro completo y nítido, repitiendo un patrón de fallo ya documentado en EP.03.
  Concepto final: periódico enmarcado (sin ningún rostro), 2 rondas hasta reducir el
  pseudo-texto del titular a un nivel invisible a tamaño real (150px, verificado).
- **Archivos generados:**
  - `scripts/EP04-paul-is-dead.html` + `.artifact.html` (Artifact publicado)
  - `episodios/temporada-2/artwork-ep04.md`
  - `E:\Podcast\MPD\Temporada 2\EP 04\artwork\MPD-T2E04-PORTADA-3000.jpg` (+16x9, +9x16)
  - `pipeline-state-ep04.md` (este archivo lo acompaña)
- **Resultado:** OK — pausa natural, esperando grabación. Commiteado y pusheado.
