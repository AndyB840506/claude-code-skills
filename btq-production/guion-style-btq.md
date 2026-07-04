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
   **Episodios atados a un momento cultural en curso** (un Mundial, unos premios, una serie del
   momento): anclar el guion en hechos históricos ya verificables y tratar el evento vivo solo como
   telón de fondo. NUNCA afirmar resultados del evento en curso si caen más allá del corte de
   conocimiento — marcarlos `[ACTUALIZAR AL GRABAR]` para que el host meta UN dato fresco y real al
   grabar, sin inventar (visto en EP.018 / Mundial 2026: las anécdotas son de 1950/1993/2014/2019;
   nada del torneo en curso se afirma como resultado).

7. **Mete humor, guiño y autoconciencia.** Andy solo, una hora — necesita contraste. Un chiste
   seco, admitir lo obvio ("sí, ya sé, otro que les habla de Cerati"), una exageración, un aparte.
   El humor no le quita peso a la lección: le da respiro para que la lección pegue más duro.

8. **Conectores de contenido, no meta-anuncios.** Prohibido "Aquí es donde BTQ deja de ser
   teoría", "ahora vamos a la parte aplicable". La última frase de un segmento ya engancha el
   siguiente. El oyente no necesita el índice.

9. **Concreto > abstracto. Una escena vívida vence a una lista.** En vez de enumerar 5 lecciones
   genéricas, elegir UNA y darle un personaje, un día, un detalle. El resto va más corto.

---

## Estructura canónica del episodio (pop-culture) — seguir desde el primer borrador

Derivado de comparar EP.018 (completo) vs. un primer borrador de EP.019 que se quedó corto
(feedback Andy 2026-06-26: "se encasilló en el referente, le faltó el cierre"). Un episodio
BTQ pop-culture lleva, en orden, estos bloques. No omitir ninguno al escribir el borrador:

1. **Apertura** (ritual: "Buenas y santas…") + **Hook** en escena.
2. **El Puente** referente → supervisor BPO (a veces enlaza con el episodio anterior).
3. **Cuerpo** (2-4 segmentos): la tesis desarrollada con el referente. Dentro de estos
   segmentos, meter **datos de interés** puntuales — verificados, poco conocidos, con ángulo
   de "esto no te lo esperabas, cuéntaselo a alguien" (incluye separar mito de realidad del
   referente cuando aplique, ej. qué inventó Hollywood vs. qué pasó de verdad). Van pegados al
   momento de la anécdota, no en un bloque aparte. No forzar uno por segmento — solo donde el
   dato realmente sorprenda (evitar volverlo fórmula, ver regla 2).
   [Cambio 2026-07-04: antes vivía como bloque final "Mito o Realidad"; la curva de retención
   de EP.012 y EP.018 mostraba que ahí es exactamente donde el oyente abandona — se movió al
   cuerpo y se reencuadró de corrección académica a dato compartible.]
4. **Re-enganche al ~60%**: el dato/giro más fuerte va en la segunda mitad, no en el primer
   tercio (completion rates 50-67%).
5. **Referencias Cruzadas — FUERA del referente.** Traer 2 ejemplos reales y verificados del
   MISMO tema pero de otro mundo (otra época, otro oficio, otro país). NO quedarse solo dentro
   de la película/banda del episodio. Ej. EP.018: Zander (director de orquesta) + Ferguson.
   EP.019: Sócrates + John Wooden. Es lo que hace el episodio universal y no un resumen del
   referente.
6. **Aplicable Hoy**: 3 cosas concretas para esta semana.
7. **Recomendaciones de Andy — diversificadas.** Máximo UNA atada al referente (la peli/disco
   del episodio); las otras saltan fuera (un libro de otro mundo, una charla, otra peli). NO
   las tres dentro del mismo tema/época. Mezclar medios: película + libro + charla.
8. **Cierre canónico** (NO omitir nada de esto — es la firma de BTQ):
   - **Pregunta comentable** que interpela al oyente sobre SU situación.
   - **CTA de comentarios:** "escríbanlo en los comentarios del episodio, en Spotify, los leo
     todos" (+ guiño a los comentarios del episodio anterior).
   - **CTA de compartir** ("si esto les hizo pensar en alguien, compártanlo").
   - **Redes:** LinkedIn — "estoy en LinkedIn como Andrés Bermúdez Rodríguez".
   - **Teaser** del próximo episodio (bien armado, no una nota suelta).
   - **Firma + TM canónico:** "Yo soy Andy. Y recuerden: [tesis del episodio en una frase
     memorable]" + nota OUTRO MUSICAL.

## Voz narrativa — "MPD meets TED", no documental BBC (feedback Andy 2026-06-26)

Los tramos históricos/expositivos son los que más fácil caen en modo informe ("esto pasó,
luego esto, esto significa X"). Reescribirlos en voz narrativa de escena:

- **Presente, no pasado.** "Roma. 31 de diciembre del 192. El hombre más poderoso del mundo
  se está alistando…" mete al oyente AHÍ; "el último día del 192 lo mataron" solo lo reporta.
- **Ritmo staccato emocional** en los beats clave: frases cortas, declarativas, encadenadas.
- **"Ubíquense / Métanse en esto"** para poner al oyente en la escena (sin gastar el
  presupuesto de "imagínense").
- **El giro descubierto** ("Y aquí está lo que casi nadie ve…") en vez de explicar la lección.
- Referencia de técnica: los guiones de MPD (`mrputridsden-production/scripts/`).

## Regla de 2 partes (igual que MPD)

Si la data y las anécdotas dan para más de ~55-60 min de contenido con chispa (sin relleno),
**partir en 2 episodios** desde el guion. Razón: la investigación profunda + anécdotas ciertas
poco conocidas suelen pasarse de la hora (ver memoria `project-mpd-episodes-two-parts`). Estructurar
el corte natural desde el inicio; cada parte con su propia apertura/cierre y un recap de ~20 seg al
abrir la Parte 2. Ojo: BTQ tiene cadencia semanal estricta (≥7 días entre episodios) — 2 partes =
2 semanas, encaja con el roadmap.

---

## Calibración de duración — dimensionar en PALABRAS, no en minutos adivinados

Regla medida (no de gusto). El guion se dimensiona contando **palabras habladas** y dividiendo por
el ritmo real de Andy, **no** estimando minutos "a ojo" por segmento. Las marcas de minutos por ojo
salen infladas y hacen que Andy termine ~15 min antes de lo marcado y tenga que estirar.

**Ritmo real de Andy ≈ 143 palabras/min** (medido contra el SRT del EP.17: 6.062 palabras habladas /
42,3 min de audio). Ese número **ya incluye sus pausas** — es ritmo de entrega, no de lectura en seco.
Diagnóstico EP.17: estaba marcado a "57 min" (≈90 wpm imaginario) y cayó en ~42-45. EP.18 v1 tenía
4.213 palabras = ~29 min reales aunque estaba marcado a 52.

**Tabla de dimensionamiento (palabras habladas → minutos a 143 wpm):**

| Objetivo real | Palabras habladas |
|---|---|
| ~45 min | ~6.400 |
| ~50 min | ~7.150 |
| ~55 min | ~7.900 |
| ~60 min (techo → evaluar 2 partes) | ~8.600 |

**Ajuste por expansión en vivo:** Andy suele decir **~15% más** de lo escrito (EP.17: guion 5.265
palabras → habló 6.062). Por eso conviene escribir el guion para que **en seco** caiga ~7-8% por debajo
del objetivo, y dejar que su expansión natural lo lleve al número. Ej.: para ~57 min reales, escribir
~7.000 palabras (≈49 min en seco; con +15% ≈ 57). **Siempre dejar colchón para CORTAR, no para estirar.**

**Cómo medir** (excluir lo que no se lee: bloques `NOTA`, chips `PAUSA`, encabezados de segmento,
tabla de arquitectura): contar palabras de `p.line` + `remate` + `dato` + `mito/realidad` + `sub`,
y dividir por 143. Marcar los tiempos de la arquitectura en consecuencia.

**Recalibrar** el 143 wpm cada pocos episodios contra el SRT más reciente (los SRT viven en
`E:\Transcriptor\transcripciones\`); si su ritmo cambia, actualizar este número y la tabla.

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
- [ ] **Vocabulario accesible:** cero palabras que el host/audiencia no usen al hablar
      (regionalismos raros, cultismos, tecnicismos). Cazar y reemplazar por habla natural —
      ej. rechazados: "galones", "desperdigado", "embestida", "factura final", "telón de
      fondo". Si dudas si una palabra "se entiende", cámbiala.
- [ ] **Estructura canónica completa** (ver sección arriba): ¿están Referencias Cruzadas
      FUERA del referente, recomendaciones diversificadas, y el cierre canónico entero
      (comentarios Spotify · compartir · LinkedIn · teaser · firma + TM · outro)? No omitir.
- [ ] **Sin bloque "Mito o Realidad" al final:** los datos de interés / mito-vs-realidad van
      distribuidos dentro del Cuerpo, no como segmento aparte antes del cierre.
- [ ] **Voz narrativa, no documental:** los tramos históricos en presente/escena, no en
      modo informe.
- [ ] Aperturas y conectores de contenido (sin meta-anuncios tipo "ahora vamos a…").
- [ ] Duración: contar **palabras habladas / 143 wpm** (ver "Calibración de duración"), NO estimar minutos a ojo. Verificar que el guion en seco caiga ~7-8% bajo el objetivo (la expansión en vivo de Andy lo sube ~15%). Si pasa de ~60 min con chispa, evaluar partir en 2.
