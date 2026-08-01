# Handoff: BTQ EP.024 cambia de tema, nace el carril «Oficio de Jefe»

**Date:** 2026-08-01 (sábado)
**Machine:** desktop (E:\) — ComfyUI corrió aquí, quedó levantado en el puerto 8188
**Status:** In progress — guion v2 completo y artwork cerrado; falta grabar y abrir 2 fuentes

---

## What We Accomplished This Session

**El disparador.** Andy grabó el EP.024 (Principio de Peter) la noche del 07-31 y lo sintió
«demasiado teórico, como una reseña y un análisis, sin nada memorable que rescatar». Se midió
sobre el guion grabado y la sensación tenía número: **38% era montaje** (historia del libro +
metodología del paper) y solo **13,9% era contenido aplicable**, arrancando en el minuto ~38
de 45. Los tres casos eran Barings 1995, Antietam 1862 y *The Office*: ninguno una operación
contemporánea.

**Decisiones de Andy, en orden:**

1. **Cambiar el tema y regrabar.** Peter NO se descarta: se reubicó a **EP.027** como el pilar
   SEO de la primera vuelta. Su audio queda intacto.
2. **Rotación 3+1** — tres episodios del carril nuevo, el cuarto pilar SEO. Reinstaura la
   cadencia de «un pilar SEO al mes» que el giro del 2026-07-21 había reemplazado, pero el
   carril acompañante ya no es pop-culture (que sigue retirado).
3. **El carril se llama «Oficio de Jefe»** — se escogió sobre `Manejo de Personal`,
   `La Operación` y `Frases de Reunión`. Carga «jefe», que es lo que el oyente busca y con lo
   que se identifica.
4. **Menos EE.UU., más regionalidad** en los casos.
5. **Registro «ejecutivo relajado»** + **dichos populares torcidos**.
6. **Artwork:** los tres monos, en excepción puntual solo para EP.024.

**EP.024 nuevo:** `EP.24 — Por qué su equipo no le cuenta los problemas: seguridad psicológica`
(75 car.). Guion v2 en `btq-production/launch-assets/EP024-puerta-abierta-guion.html` —
**5.405 palabras ≈ 41,3 min**, esqueleto E (acción primero, la recomendación cae en el minuto 2),
9 segmentos, aplicable **29,3%**. Artifact:
https://claude.ai/code/artifact/9a5078a8-3388-4582-97b9-48a71bc7851c

**La taxonomía, que fue idea de Andy y es lo que sostiene el episodio.** No son cuatro
ejemplos: son cuatro formas distintas de que una mala noticia no sirva.

| Caso | Qué falló | Costo |
|---|---|---|
| Nokia 2007-2013 | el mensaje **nunca llegó** — filtrado en el camino | un mercado entero |
| Reficar + Hidroituango | **llegó y no importó** | plata pública · 17.000 evacuados |
| Edificio Space, Medellín 2013 | **llegó y lo parchearon** | 12 muertos |
| Grenfell 2017 | era público y **castigaron al mensajero** | 72 muertos |

**EP.025 fijado:** «Llevo cuatro meses sin llenar esa vacante». Idea de Andy de foros de
LinkedIn; se giró el punto de vista del candidato al que contrata.
**Ley de Little → EP.031** como pilar SEO.

**Artwork cerrado.** Seis rondas. `E:\AI\outputs\BTQ-EP024\` tiene las tres proporciones
(1:1 3000², 9:16, 16:9) más contrapruebas de 300 y 96 px. Ilustración de los tres monos con
las manos entrando desde fuera del cuadro —el proverbio torcido para que diga la tesis y no la
que el episodio demuele—, cuantizada a las tres tintas exactas de marca.

**Reglas nuevas escritas:**
- `guion-style-btq.md`: § Dichos (se tuercen, no se citan; techo de 5, uno por segmento),
  § Lo que el oyente DICE ≠ lo que BUSCA, compuerta 3b (aplicable ≥25% y antes del 60%),
  y la regla huérfana del ADN reapuntada («dato duro del mundo del oyente», antes decía
  «específico de call center» — industria que el show abandonó el 07-25 sin que nadie la
  reapuntara).
- `CLAUDE.md` (proyecto): medidores que **sobre**-reportan, y superar una regla marcando el
  bloque superado, no solo anotándolo arriba.
- `brand-constants.md`: el cuerpo de la era de objeto marcado **histórico**.

---

## Where We Paused

**Last action:** vaciado `portada-compose.py` (137 líneas casi idénticas a su reemplazo) a un
redirect de 6 líneas; el cuerpo sigue en `git show 74e71f5:comfyui/templates/portada-compose.py`.

**Next action:** **Andy graba el EP.024.** Al volver con el audio, seguir el pipeline normal
(transcripción → assets → Spotify).

**Blockers:** ninguno para grabar. Dos cosas abiertas que no bloquean:
- Los informes de la Contraloría sobre **Reficar e Hidroituango no se han abierto**. Todo lo de
  esos dos casos sigue corroborado solo entre secundarias.
- El teaser del segmento 8 está genérico; EP.025 ya tiene tema y se puede concretar.

---

## Files to Read First

- `btq-production/pipeline-state-ep024.md` — estado real del episodio, con los pendientes en
  checkboxes. **Empezar por aquí.**
- `btq-production/launch-assets/EP024-puerta-abierta-guion.html` — el guion.
- `btq-production/roadmap-btq.md` § Rotación 3+1 — por qué existe el carril y cómo se cuenta.
- `btq-production/pipeline-state-ep027-peter.md` — Peter, bajo su numeración nueva.

---

## Notes / Gotchas

- **⚠️ `E:\AI\outputs\BTQ-EP024-PETER-OBSOLETO\` tiene 54 archivos trampa.** Son portadas
  **terminadas y en el sistema visual vigente** que solo llevan el título de Peter. No se ven
  viejas: se ven perfectas. Tampoco sirven para EP.027 porque `EP.24` va horneado dentro de la
  imagen — hay que regenerarlas. Su `titulo.txt` se renombró a `titulo-PETER-VIEJO.txt`.
- **De «Sala de Máquinas» sobreviven la paleta, la tipografía y el principio de una sola señal
  — nada más.** No es un escenario. Construir un prompt desde las reglas viejas produjo una
  foto de cuarto de máquinas que no se parece a lo que el show publica. **Antes de escribir
  cualquier prompt de imagen para BTQ, abrir la última portada publicada, no el documento.**
- **Los negativos de Z-Image no actúan** (cfg 1.0). Se probó a cfg 2.5 y tampoco honró
  `cream border`, `text` ni `watermark` — el texto hasta empeoró. Lo que sí funcionó fue quitar
  la palabra «póster» del prompt: el marco y las marcas de impresor salían de ahí.
- **La pasada de fuentes encontró 3 errores reales:** Nokia no tenía «cuatro de cada diez» en
  2007 (37,8% en el año, 40% solo en Q4); el hallazgo de Edmondson es de **1996**, no del paper
  de 1999; y la torre Space colapsó **mientras una cuadrilla reforzaba una columna** — 10 de los
  12 muertos eran esos trabajadores. El tercero mejoró el episodio.
- **ComfyUI quedó corriendo** en el puerto 8188 de la torre. Cerrarlo si no se va a usar.
- Rutas de `E:\` = solo desktop. Desde el portátil no existen.

---

## Questions to Answer

- ¿Se reusa el audio grabado de Peter para EP.027, o se regraba? Si se reusa, hay que regrabar
  **dos tramos**: el segmento 0 dice «episodio 24» y el 7 anuncia la Ley de Little como el
  siguiente. Y queda abierto si el guion se reusa tal cual —13,9% aplicable— o se reestructura.
- La agrupación de temporada en Spotify con el nombre del carril: **propuesta, NO aprobada**. Es
  un cambio en plataforma pública y necesita el sí de Andy.
- `guion-style-btq.md` va en **1.012 líneas**. Señalado en el audit, no tocado: partirlo es una
  refactorización con riesgo de romper referencias y merece su propia sesión.
