# Artwork Composition (post-proceso PIL)

Que hacer DESPUES de generar: componer tipografia, scrims, grading, aprobar en miniatura.
Separado de `prompting.md` el 2026-07-22 — ese archivo es sobre que pedirle al MODELO;
este es sobre lo que el modelo no debe hacer nunca.

**Regla raiz:** el modelo genera escena e iconos aislados. Todo texto que se vaya a leer
se compone con PIL, deterministico. Ver `comfyui/templates/`.

## Reglas heredadas de prompting.md

- **Logos/íconos de marca: SÍ los reconoce, pero solo aislados — texto largo mezclado
  con escena SIEMPRE sale con errores** (aprendido 2026-07-14, BTQ EP.022). Pedir una
  escena completa + wordmark + título + footer con nombres de íconos en un solo prompt
  produjo íconos de la fila 1 (Facebook/Instagram/TikTok) reconocibles y a color, pero
  TODO el texto horneado salió con errores de ortografía ("BEHIND THE QUEUE" → "BEHIND
  THE QEQUE") y faltó la fila 2 de íconos. Aislar los íconos en su propia generación
  (fondo negro puro, "no text, no words, no letters", sin escena) los deja limpios y
  recortables. **Regla:** el modelo nunca genera texto que se vaya a leer en el
  resultado final — solo escena e íconos aislados; todo texto (wordmark, títulos,
  números de episodio) se compone aparte con PIL, igual que ya se hacía con las citas
  de las quote cards. Plantilla: `comfyui/templates/portada-compose.py`.
- **Composiciones verticales extremas (figura confinada a un tercio del frame, el resto
  negro puro) no son controlables de forma confiable solo con prompt** (aprendido
  2026-07-15, BTQ EP.022 9:16): 2 intentos con instrucciones explícitas de proporción
  fallaron — la figura terminó ocupando la mitad o la base del frame ambas veces.
  **Regla:** cuando una composición ya fue resuelta y aprobada en OTRO aspect ratio (ej.
  el 1:1), y el nuevo formato solo necesita una porción de esa misma escena con relleno
  negro alrededor, no seguir iterando el prompt — recortar la escena aprobada con PIL y
  rellenar el resto con el negro de marca exacto (`(10,10,10)` / `#0A0A0A`). Cero riesgo
  de reintroducir errores ya corregidos (género, checkbox, íconos extra) y más rápido
  que seguir apostando con el modelo.
- **El "negro puro" que renderiza el modelo NO es pixel-idéntico al negro de marca
  programático `(10,10,10)`** (aprendido 2026-07-15, BTQ EP.022): una generación aislada
  con fondo "pure black" suele salir en `(0,0,0)` o similar, un valor distinto aunque
  visualmente ambos "se vean negros". Pegar ese asset de forma opaca junto a o sobre un
  bloque negro programático (footer, panel de texto) deja una costura/caja rectangular
  visible. **Regla:** al componer un asset generado por IA sobre un bloque negro PIL,
  usar una máscara de alfa derivada de `ImageChops.difference()` contra negro puro
  (`Image.paste(asset, pos, mask)`), nunca un paste opaco — así solo los píxeles de
  contenido real se componen y el negro programático se ve continuo. Ver el fix aplicado
  en `comfyui/templates/portada-compose.py` (tira de íconos sobre el footer).
- **El envejecido/filtro de foto antigua NO se le pide al modelo: va como post-proceso PIL**
  (aprendido 2026-07-22, MPD T2). Z-Image devuelve foto de producto limpia por más que se pida
  "expired 35mm film, faded, scratches". Script reutilizable: `comfyui/templates/vintage_grade.py`
  (`vintage(img, strength)` importable): desatura, split-tone cálido, levanta negros, viñeta, grano
  por medios tonos, polvo y rayas confinadas a los márgenes laterales para que nunca crucen el
  sujeto. Aplicarlo DESPUÉS del upscale, a la resolución final, para que el grano quede a escala.
- **Crear la herramienta no es aplicarla** (mordió 2026-07-22, MPD T2, dos sesiones
  seguidas). La sesión del 21 detectó que el wordmark blanco se perdía sobre el mármol
  pálido y creó `scrim-overlay.py` para resolverlo — pero la portada se cerró y publicó
  **sin aplicarlo**, así que el defecto siguió vivo y hubo que rehacer el lockup entero al
  día siguiente. **Regla:** cuando un fix se materializa en un script nuevo, el mismo turno
  lo aplica al artefacto que lo motivó y muestra el resultado; un helper recién creado que
  no aparece en el pipeline de la pieza es un fix que no ocurrió.
- **El artwork se aprueba a 150 px, no a 3000** (aprendido 2026-07-22, MPD T2). El tamaño
  real en una lista de Spotify ronda los 150-300 px; a 3000 px cualquier lockup se ve bien.
  Reducir la pieza final con LANCZOS a 150 y **mirarla** antes de declararla lista. En la
  T2 ese test reprobó lo que a tamaño completo parecía correcto: el wordmark sobre mármol
  era un borrón y el subtítulo en rojo desaparecía. **Corolarios:** ningún texto se apoya
  directo sobre una zona clara (mármol) ni sobre el fuego — va sobre scrim o sobre zona
  naturalmente oscura; y el título va en **una sola línea**, porque partirlo en dos empuja
  el bloque hacia arriba, hacia la zona más brillante de la escena.
- **Contraste térmico: una escena cálida en todo lee acogedora, no misteriosa** (aprendido
  2026-07-22, MPD T2). La primera portada tenía fuego, mármol, madera **y sombras** del
  mismo lado del espectro; el resultado leía "club de caballeros", no misterio. El arreglo
  no es cambiar de paleta sino **separar las temperaturas**: sombras, medios tonos y aire
  hacia azul nocturno, y el calor reservado a la única fuente de luz real (la llama). Así
  la escena se vuelve nocturna y el fuego gana fuerza por ser lo único cálido del cuadro.
  Script con parámetros congelados: `comfyui/templates/night_grade.py` (split toning por
  luminancia), después del upscale y de `vintage_grade`, antes de componer el lockup.
  **Precaución contra el reflejo de descartar:** predecir que un tinte fuerte "se va a ver
  como filtro falso" sin generarlo es teorizar — se generan las variantes y se miran. En
  T2 la variante más agresiva (la que yo había descartado en teoría) fue la elegida.
- **La paleta de un sistema visual se muestrea del artwork, no se propone de memoria**
  (aprendido 2026-07-22, MPD T2). Leer el pixel real de la pieza vigente (promedio de un
  parche, más estable que un pixel suelto; y para el acento, el pico de mayor sesgo
  cálido/frío). En T2 eso reveló un color que la propuesta escrita "a ojo" no contemplaba
  y que domina media imagen — la piedra del mármol — y descartó dos que ya no existían en
  la escena. Marcar en el specimen cuáles hex son muestra y cuáles derivados.
- **Al cambiar el sistema visual de una temporada, versionar el compositor, no mutarlo**
  (aprendido 2026-07-22, MPD T2): `mpd-lockup-t2.py` se creó al lado de
  `mpd-portada-compose.py` en vez de editarlo, para que las portadas ya publicadas de la
  temporada anterior sigan reproducibles tal como salieron.
- **Reusar assets de íconos/logos reales entre shows antes de regenerar** (aprendido
  2026-07-17, MPD EP.005): los íconos de plataforma (Spotify, Apple Podcasts, Amazon
  Music, redes sociales) son los mismos logos reales sin importar el show — si otro
  show ya generó y validó una tira de íconos (ej. `E:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\BTQ-icon-strip-source.png`),
  recortar la fila/ícono que se necesita de ahí es más rápido y confiable que pedirle
  al modelo que los regenere desde cero.

## Tipografia sobre escenas simetricas — los scrims de borde no bastan

(aprendido 2026-07-22, kit de redes MPD T2)

En formatos anchos (portada de Facebook, banner de YouTube, cabecera de X) la plataforma
obliga a **centrar** la tipografia, y una escena simetrica pone su zona mas brillante
justo en el centro. Los scrims de arriba/abajo dejan limpia la franja del medio, que es
exactamente donde cae el titulo: en la primera tanda, "Misterios y Leyendas" quedo encima
de la llama.

**Regla:** en formatos anchos, atenuar la escena ENTERA hacia el color de fondo del
sistema (`veil()` en `mpd-social-kit.py`, mezcla 0.44-0.52) y recien despues aplicar los
scrims de borde, mas suaves. El fuego queda como resplandor y el texto recupera contraste.
Los scrims de borde solos sirven cuando el bloque de texto vive en un extremo, no al medio.

**Corolario:** si un elemento del bloque sigue perdiendose despues de atenuar (tipico: la
bajada en color secundario sobre la zona clara), quitarlo de ese formato en vez de seguir
oscureciendo la escena. En el banner de YouTube se elimino la tagline por eso.

## Avatares: la masa oscura es lo que hace legible, no la oscuridad total

(aprendido 2026-07-22, MPD T2)

Un avatar se ve a 40-150 px. El primer encuadre corto a la altura de la repisa y el cuadro
quedo dominado por marmol palido: a 150 px leia como una mancha clara — el mismo defecto
que tumbo la primera portada. **Regla:** encuadrar de modo que entre una masa oscura
grande (una butaca, una silueta) contra el punto de luz. Y la vinneta suave: a 0.62 el
cuadro se lavaba entero hacia el color de fondo y perdia contraste; 0.42 + un toque de
contraste funciono. Generar las miniaturas de 150 y 40 px y **mirarlas**.

## Revelar artwork bajo un objeto: generar el objeto AISLADO

(aprendido 2026-07-22, teaser de la sabana, MPD T2)

Para un teaser de "obra tapada" (sabana, tela, papel) la tentacion es pedirle al modelo la
escena completa: la tela encima de un cuadro. **No hacerlo** — lo que se asome bajo la tela
va a ser una invencion del modelo, no el artwork real.

**Regla:** generar SOLO el objeto que tapa, sobre fondo negro puro. Despues, en PIL:

1. Mascara del objeto por luminancia (umbral ~88 sirvio para tela blanca sobre negro).
2. Borde superior del objeto **columna por columna** — arriba de esa linea va el artwork
   real, debajo manda el objeto.
3. Sombra proyectada sobre lo revelado (gradiente de ~40 px difuminado en el borde). Sin
   esto, las dos capas se leen como recortes pegados, no como una tela apoyada encima.
4. Pasar el compuesto entero por el grading del sistema — una tela blanca cruda seria un
   segundo elemento brillante fuera de paleta.

Asi el que decide cuanto se revela es el compositor, no el modelo. Scripts:
`mpd-teaser-sabana-gen.py` (generacion) y `mpd-teaser-sabana.py` (composicion).

**Ojo con el formato vertical:** al llenar un 9:16 con una portada cuadrada, el titulo
sube hasta una altura donde el objeto ya no cubre todo el ancho y se asoma por el borde.
En vertical, partir de la escena SIN texto y dibujar el wordmark aparte.

