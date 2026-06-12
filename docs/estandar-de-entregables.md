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
