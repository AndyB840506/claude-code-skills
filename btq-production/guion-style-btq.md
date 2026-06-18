# Guía de estilo de guion — Behind the Queue (BTQ)

> Consultar SIEMPRE antes de escribir un guion de BTQ (igual que MPD consulta su glosario de tono).
> Nace del feedback de Andy (2026-06-17): los guiones estaban "muy tiesos, les falta chispa".
> Referencia de narrativa con chispa: los guiones de MPD (ej. `mrputridsden-production/scripts/EP005-aterciopelados.html`).

BTQ es **solo host (Andy)**: conecta un referente pop (música, cine, juegos) con una lección de
liderazgo para un supervisor/gerente de BPO de ~40 años. La chispa no viene de banter entre hosts
(no hay co-host) — viene del ritmo hablado, la escena, el dato que sorprende, el humor y la calidez.

---

## Diagnóstico — qué pone "tieso" un guion BTQ (visto en EP.017)

1. **Frases de ensayo escrito, no de habla.** Oraciones largas con subordinadas y cadenas de
   guiones largos que nadie dice en voz alta sin sonar leyendo.
2. **Estructura formulaica.** Casi cada segmento termina en un `REMATE`. Mismo patrón
   hook → explicación → remate, una y otra vez. El oyente lo predice.
3. **Refrán-tesis repetido hasta el cansancio.** En EP.017 "seguir sonando/funcionando cuando ya
   no estés" aparece ~9× casi textual. Mata el impacto.
4. **Mismo conector siempre.** "Llévenlo a su piso", "Tradúzcanlo a su operación", "Piensen en su
   piso" — el puente referente→BPO se hace con la misma frase cada vez.
5. **Tono solemne parejo.** Todo es grave, importante, de TED talk. Cero humor, cero guiño, cero
   autoconciencia, cero sorpresa. Sin contraste, todo suena plano.

---

## Las 9 reglas de chispa (BTQ solo host)

1. **Escribe como Andy habla, no como se escribe.** Frases cortas, declarativas. Rompe las cadenas
   de guiones largos en 2-3 frases. Si una oración no se puede decir de un respiro, pártela.

2. **Varía el ritmo — no todo termina en REMATE.** Máximo ~3-4 remates por episodio, en los
   momentos de verdad. Los demás segmentos pueden cerrar con una pregunta, un dato seco, una
   imagen, o un silencio. La sorpresa vive en romper el patrón.

3. **Una tesis, dicha 2-3 veces máximo — y variada.** Elige el refrán central y ánclalo en 2-3
   momentos clave, cada vez con palabras distintas. Nunca repetir la misma frase textual >3×
   (lint obligatorio, ver abajo).

4. **Varía el puente referente→BPO.** Prohibido repetir "llévenlo a su piso / tradúzcanlo a su
   operación". Alternativas: una pregunta directa, una micro-escena del piso, un "a usted le pasó
   esto el martes", un dato de la operación, un personaje (el supervisor que…). El puente cambia
   cada vez.

5. **Abre con escena, no con anuncio.** En vez de "Hoy quiero arrancar con una pregunta", meter al
   oyente en una imagen: el estadio lleno, el piso a las 6pm un viernes, el chat del cliente
   explotando. Cinematográfico. "Imagínense" se permite, pero con presupuesto (máx 1, igual que MPD).

6. **Carne investigada y verificada — nunca inventada.** El sello es "la tarea hecha": datos
   reales, fechas, cifras, anécdotas poco conocidas pero ciertas. NUNCA inventar fuentes (en una
   versión de EP.017 se había citado un artículo HBR inexistente — se reemplazó por casos reales
   Jobs/Apple y Collins. Investigar en web antes de escribir; marcar lo no confirmado como
   [VERIFICAR]).

7. **Mete humor, guiño y autoconciencia.** Andy solo, una hora — necesita contraste. Un chiste
   seco, admitir lo obvio ("sí, ya sé, otro que les habla de Cerati"), una exageración, un aparte.
   El humor no le quita peso a la lección: le da respiro para que la lección pegue más duro.

8. **Conectores de contenido, no meta-anuncios.** Prohibido "Aquí es donde BTQ deja de ser
   teoría", "ahora vamos a la parte aplicable". La última frase de un segmento ya engancha el
   siguiente. El oyente no necesita el índice.

9. **Concreto > abstracto. Una escena vívida vence a una lista.** En vez de enumerar 5 lecciones
   genéricas, elegir UNA y darle un personaje, un día, un detalle. El resto va más corto.

---

## Regla de 2 partes (igual que MPD)

Si la data y las anécdotas dan para más de ~55-60 min de contenido con chispa (sin relleno),
**partir en 2 episodios** desde el guion. Razón: la investigación profunda + anécdotas ciertas
poco conocidas suelen pasarse de la hora (ver memoria `project-mpd-episodes-two-parts`). Estructurar
el corte natural desde el inicio; cada parte con su propia apertura/cierre y un recap de ~20 seg al
abrir la Parte 2. Ojo: BTQ tiene cadencia semanal estricta (≥7 días entre episodios) — 2 partes =
2 semanas, encaja con el roadmap.

---

## Antes / Después (ejemplo real, estilo BTQ)

**ANTES (tieso — estilo EP.017):**
> "Hay un momento — y la mayoría de los líderes de operaciones lo viven sin darse cuenta — en el
> que un guion de atención, un flujo de escalación, una forma de medir desempeño, deja de estar
> resolviendo el problema para el que se diseñó, y empieza simplemente a funcionar por inercia.
> Nadie lo cuestiona, porque 'así se ha hecho siempre' y los números siguen saliendo en verde."

**DESPUÉS (con chispa):**
> "Piensen en ese guion de atención que llevan tres años usando. El que nadie toca porque 'convierte
> bien'.
> [PAUSA]
> Déjenme adivinar: nadie se acuerda quién lo escribió. Y el día que alguien preguntó por qué se
> hace así, la respuesta fue 'porque siempre se ha hecho así'.
> [PAUSA]
> Eso no está funcionando. Eso está sobreviviendo. Y hay una diferencia enorme."

Qué cambió: frases cortas decibles · un guiño ("déjenme adivinar") · una imagen concreta · un remate
seco por contraste, no por fórmula · cero cadena de guiones largos.

---

## Lint antes de entregar un guion BTQ

- [ ] Refrán-tesis: contar ocurrencias casi textuales del refrán central → **máx 3**.
- [ ] Remates: contar bloques `REMATE` → **máx ~3-4 por episodio**, no uno por segmento.
- [ ] Puente referente→BPO: que NO se repita la misma frase ("llévenlo a su piso") — variar cada vez.
- [ ] Muletillas: máx 1 "imagínense", 0 "me vuela la cabeza" (igual que MPD).
- [ ] Frase larga: ninguna oración que no se pueda decir de un respiro; partir las cadenas de guiones.
- [ ] Al menos 2-3 momentos de humor/guiño/autoconciencia repartidos.
- [ ] Datos verificados (fuentes reales, nada inventado); lo dudoso marcado [VERIFICAR].
- [ ] Aperturas y conectores de contenido (sin meta-anuncios tipo "ahora vamos a…").
- [ ] Duración estimada: si pasa de ~60 min con chispa, evaluar partir en 2.
