EPISODE: EP.023 (BTQ)
stage_a: complete — guion aprobado 2026-07-21; título y portadas rehechos 2026-07-25 bajo el sistema v4.
stage_b: pending — requiere la grabación. Las quote cards se componen aquí, contra la TRANSCRIPCIÓN real, nunca contra el guion.
stage_c: pending
spotify_url: pending

TITULO FIJADO (2026-07-25, decisión de Andy):
  EP.23 — Efecto Hawthorne: por qué su equipo rinde distinto cuando lo miran
  73 caracteres. Este string va IDÉNTICO en portada, Spotify y YouTube.
  Gana el término buscable sobre el teórico (Elton Mayo) porque el modelo
  aprobado no es "el teórico a secas" sino [tipo] de [nombre propio] — igual
  que `Ley de Goodhart`. Precedente en guion-style-btq.md § Título.

ARTWORK — REHECHO 2026-07-25. Tipografía pura, sin ComfyUI.
  Generador: comfyui/templates/portada-ep-compose.py (determinista, PIL).
  Salidas en E:\AI\outputs\BTQ-EP023\ — COVER-1x1 / 16x9 / 9x16 + jpg + 300/96.
  Gate: `python scripts/verify_assets.py EP023 --root E:\AI\outputs\BTQ-EP023
  --show btq --stage-a` → PASS en los 3 aspect ratios, negro de marca OK.
  Los tres inspeccionados visualmente. El 9:16 se ve sparse (es inherente a la
  tipografía pura en un lienzo tan alto); pendiente el juicio de Andy.

  ⚠️ MUERTO — no revivir: el concepto v3 (foco incandescente vintage + headset +
  waveform dorado, test E:\AI\outputs\BTQ-EP023-bulb-v1_00001_.png) murió con el
  giro a tipografía pura del 2026-07-25. También muere el archivo de prompts
  `launch-assets/EP023-hawthorne-artwork-v3.md`. El oro ya no es color de marca.

CONTENIDO (sin cambios desde 2026-07-21): efecto Hawthorne (Elton Mayo, fábrica
Hawthorne de Western Electric, 1920s-30s), pilar SEO sin referente pop. 2 casos
nombrados que escalan (fábrica Hawthorne → Volkswagen Dieselgate: 11M autos,
$30.000M en multas, 7 años de cárcel, ~1.260 muertes prematuras estimadas por
MIT/Harvard) + dato duro de industria (1-5% de llamadas auditadas manualmente).
Giro al 60%: reanálisis 2011 de Levitt & List sobre los datos originales.
~41.0 min medidos, 4.542 palabras.

LINTS CORRIDOS 2026-07-25 sobre el guion:
  - Español neutro: 0 hallazgos en las 5 categorías (anclado a un país, doble
    sentido, cola+adjetivo, voseo, tuteo). Limpio.
  - "Andy" en 3ª persona: 7 apariciones, TODAS en metadata/etiquetas de sección
    (permitido). Ninguna en línea hablada.
  - "imagínense": 1 real (presupuesto: máx 1). OK.

PASADA DE ALCANCE MACRO — HECHA 2026-07-25 (criterio "quirúrgico", elegido por Andy):
  Tocado solo el Segmento 7 (Aplicable Hoy), 3 párrafos. La escena de apertura
  (Julián, analista de calidad, escuchando una llamada) se CONSERVA a propósito:
  la regla 9 de chispa exige escena vívida sobre abstracción, y generalizarla
  habría producido el modo "tieso" que el Diagnóstico de la guía ataca.
  - La herramienta 1 pasa de "auditar llamadas" a nombrar cuatro formas del mismo
    animal: la llamada anunciada, la visita del gerente de zona a la tienda, el
    jefe de copiloto en la ruta del vendedor, el código que se entrega sabiendo
    que lo van a leer con lupa.
  - El dato duro de industria (1-5% de llamadas auditadas) se conserva —el ADN de
    pilar SEO lo exige— pero pasa a ser ejemplo y termina en pregunta abierta a
    cualquier industria, no en cierre de call center.
  - "antes de auditar una sola llamada más" → "antes de revisarle el trabajo a una
    sola persona más".

  ⚠️ CORRECCIÓN de medición: el "~36 menciones de call center" que se reportó antes
  se midió sobre el HTML COMPLETO (notas, tabla de arquitectura, metadata), no
  sobre las líneas habladas. Medido solo sobre `<p class="line">`: call center 0,
  BPO 0. El anclaje real y único era la escena de apertura. Medir el guion
  hablado SIEMPRE contra `<p class="line">`, nunca contra el archivo entero.

  Estado tras la pasada (solo líneas habladas): 4.362 palabras · call center 0 ·
  BPO 0 · centros de contacto 1 · agente 9 y llamadas 10 (la escena de apertura,
  conservada) · equipo 14 · operación 11 · empresa 2 · tienda/vendedor/
  desarrollador 1 c/u. Lints de español neutro: 0 en las 4 categorías.

Grabación pendiente de agendar con Andy.
