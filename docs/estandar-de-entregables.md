# Estándar de calidad por entregable

Qué tiene que cumplir cada tipo de entregable ANTES de declararlo listo.
Escrito 2026-06-12 para que la calidad no dependa del modelo que ejecute:
cada criterio es verificable (se puede chequear con grep, conteo o lectura),
no una intuición.

**Regla general para cualquier modelo:** no entregar nada sin correr el
checklist de su sección. Si un ítem falla, corregir y re-verificar antes
de reportar. Nunca decir "listo" sin haber verificado.

---

## 1 · Guiones de podcast (MPD y BTQ)

Checklist obligatorio antes de entregar (correr greps literales sobre el guion):

- [ ] **Presupuesto de muletillas:** máx 1 "imagínense", máx 1 "me vuela la cabeza"
      (o equivalentes del show). Contar con grep, no de memoria.
- [ ] **Cero réplicas de pura validación** ("Eso es una locura", "Exacto", "Totalmente"
      como turno completo). Cada réplica aporta dato, desacuerdo o pregunta.
- [ ] **Mínimo un desacuerdo real** entre los hosts por episodio.
- [ ] **Léxico firmado por host:** cada host tiene expresiones propias que el otro
      no usa. Verificar que no se cruzan.
- [ ] **No anunciar el hype** ("lo que viene es increíble") — mostrar el dato y dejar
      que golpee solo.
- [ ] **Apertura sin agenda-dump:** el episodio arranca en una escena, no en un índice.
- [ ] **Listas → una escena:** ningún turno enumera 3+ ítems seguidos; se convierte
      el mejor en escena y se descartan los demás.
- [ ] **Turnos cortos:** ningún turno pasa de ~5 oraciones sin interrupción del otro.
- [ ] **Escribir PARA la entrega de cada host.** Juan (MPD): pausado, documental,
      punchlines secas y gravitas — NUNCA exclamaciones de energía ni improv hype.
      El contraste Andrés-energía / Juan-gravitas es el sello del show.
- [ ] **BTQ además:** re-enganche con dato guardado al ~60% del guion + cierre con
      pregunta comentable que interpela AL OYENTE (no al personaje).
- [ ] **Dato climático / payoff verificado:** el dato que se guarda para el final
      (el "re-enganche") debe tener fuente real confirmada ANTES de grabar — no dar
      por buena una cifra/evento sin verificar. Lección EP.017: la gira "Gracias
      Totales" 2020 no tenía fuente; verificarla evitó un error al aire y destapó el
      gancho local (debut El Campín Bogotá, audiencia 70% CO).

## 2 · Títulos y SEO (BTQ)

- [ ] Fórmula exacta: `EP.XX — [Referente]: [frase con keyword BPO / liderazgo / call center]`
- [ ] La keyword buscable está en el título Y en las primeras 2 líneas de la descripción.
- [ ] Numeración `EP.XX` (dos dígitos) — nunca "Ep.X", tres dígitos, ni sufijo
      "| Behind the Queue" en Spotify.
- [ ] Pregunta personal y comentable antes del CTA de la descripción.

## 3 · Planes de redes sociales

- [ ] **Fechas verificadas contra el calendario real** (qué día de la semana es hoy,
      cuándo sale el episodio en vivo). Error típico: asumir el día sin verificar.
- [ ] Secuencia intacta si las fechas se mueven (intriga → lanzamiento → refuerzo);
      el copy post-lanzamiento dice "ya disponible", nunca "mañana".
- [ ] BTQ: LinkedIn se escribe primero (plataforma prioritaria); post del lunes
      7–8 AM incluido; clips salen del episodio que el algoritmo ya empuja.
- [ ] Copy listo para copiar-pegar, separado por plataforma y por día, con quién firma.
- [ ] Quotes marcadas con ⚠️ "confirmar contra el audio grabado antes de publicar".

## 4 · Artwork (prompts de generación)

- [ ] BTQ: principio de nostalgia — estética FIEL a la época del referente,
      no reinterpretación moderna. Brand: fondo #0A0A0A, acentos dorado #C9A84C,
      footer "Behind the Queue" izq · EP.0XX dorado centro · iconos der.
- [ ] MPD: crimson #9B1C1C + plata #A8A8A8, footer con tentáculo/branding del show.
- [ ] El texto dentro de la imagen es consistente con el estado del lanzamiento
      ("MAÑANA" vs "YA DISPONIBLE") y con el copy del plan social.
- [ ] Cada prompt termina con checklist de accuracy de 3 puntos verificables.

## 5 · Análisis de analytics / recomendaciones data-driven

- [ ] Cada recomendación cita su evidencia numérica concreta (ej.: "EP.01 = 193 de
      245 impresiones vía Search"), no impresiones generales.
- [ ] Distinguir correlación de causa; marcar hipótesis como hipótesis.
- [ ] Toda regla nueva que salga del análisis se escribe en el archivo de sistema
      que corresponde (roadmap, skill, CLAUDE.md) — no se queda en el chat.

## 6 · Transcripciones

- [ ] Salida SRT directa (nunca post-procesar TXT — pierde líneas y timestamps).
- [ ] Verificar mapeo de SPEAKER_XX a personas reales antes de usar la diarización.
- [ ] Output en E:\Transcriptor\transcripciones\ (desktop) — nunca en C:.

## 7 · Cambios de entorno / instalaciones

- [ ] Re-ejecutar el comando o test que falló para confirmar el fix — nunca declarar
      "corregido" sin reproducir.
- [ ] Documentar trampas encontradas en el doc de entorno correspondiente
      (ej.: transcriptor/docs/environment.md).
- [ ] Output y cachés a E:\ (desktop) / D:\ (portátil), nunca C:.

## 8 · Propuestas y entregables freelance (skill `freelance-gig`)

- [ ] **Ningún precio inventado:** si el gig matcheó uno de los 7 servicios de
      `services.config.js`, el rango citado es el real de ese archivo — nunca un
      número estimado. Si no matcheó (custom job), no se sugiere precio.
- [ ] **Cada dato factual trazado** a la JD / brief / resultado de web_fetch —
      lo que no se puede verificar va a una sección visible de preguntas
      pendientes, nunca se adivina.
- [ ] **Voz (propuestas):** ningún par de aperturas consecutivas idéntico, cero
      anuncio de hype, cero descuento por debajo del rango (reframe a valor en
      su lugar).
- [ ] **Entregables HTML siguen el output contract `BASE_RULES`** de
      `the-freelancer/freelancer/deliverable.js` cuando se reutiliza esa ruta
      (single-file, brand frame salvo excepción de sitio propio del cliente,
      idioma del cliente).
- [ ] **Sin indicios de IA — visual:** correr la imagen/página/logo contra el
      patrón "esqueleto IA" (hero centrado + 3 cards + carrusel + anillo
      degradado, fuentes Inter/Roboto + gradiente morado). Si aparece, no se
      entrega así — se nombra un ángulo creativo específico del cliente y se
      reconstruye sobre ese ángulo.
- [ ] **Sin indicios de IA — texto:** revisar contra muletillas típicas de IA
      ("no solo es X, es Y", listas de tres, transiciones genéricas tipo "en
      el mundo actual...", acumulación de calificadores, párrafos de largo
      uniforme). Si aparece, corregir antes de entregar.
- [ ] **Self-check explícito antes de declarar listo:** una pasada final
      preguntando "¿algo aquí se ve/lee como plantilla o como IA en automático?"
      — nombrar el indicio específico y corregirlo, no solo anotarlo.
