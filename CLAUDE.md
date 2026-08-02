# Creador de Skills para Claude Code

Este proyecto crea skills personalizadas para Claude Code. Una skill es un archivo que le enseña a Claude a hacer una tarea específica de forma repetible.

## Verify Before Claiming

Los principios viven en `~/.claude/CLAUDE.md`: **§ Verification** (la faja — gobierna la SALIDA, no declarar hecho sin evidencia) y **§ Procedencia** (gobierna la ENTRADA, no usar un artefacto guardado como hecho). El **procedimiento** operativo — tabla de evidencia, recibos, las dos secciones de cierre — vive en la skill `verify`.

**No re-declarar esas reglas aquí.** Estaban escritas en 4 sitios el 2026-07-23 y el fallo siguió ocurriendo: el problema no es que falte la regla, es que falta el enforcement. Agregar una quinta copia diluye, no refuerza.

## Environment

Windows con PowerShell 5.1. Usar PowerShell (no Bash/xcopy) para operaciones de archivos. Evitar backtick-quotes, caracteres Unicode y expresiones if inline en scripts — PS 5.1 no los maneja correctamente.

**Excepción (escrituras byte-exactas):** para contenido que otras herramientas parsean (frontmatter de skills, JSON, restaurar archivos desde git), usar Bash con redirección (`git show X > file`) — `Set-Content -Encoding UTF8` en PS 5.1 escribe BOM y corrompe el archivo (mordió el 2026-07-06: el harness cargó una skill restaurada con el frontmatter ilegible). Y `-Encoding ASCII` destruye tildes/ñ/flechas (mordió el 2026-07-11: MODELS.md con `??`) — para editar archivos con contenido UTF-8, usar la herramienta Write o python, no Set-Content.

Config y reglas operativas en `~/.claude/`; proyectos y archivos de producción en `C:\Users\andre\repos\`. No proponer junctions para `~/.claude/`. Output de producción (imágenes, audios, transcripciones, cachés) va a `E:\` en el desktop y `D:\` en el portátil — nunca a `C:\`.

### Windows — shell

- El shell por defecto es PowerShell. **NO** usar heredocs de bash ni here-strings de PowerShell para contenido multilínea — escribir archivos con la herramienta Write. (No contradice la excepción de arriba: eso es redirección `>`, no heredoc.)
- **En un `.ps1`, `2>&1` sobre un ejecutable nativo aborta el script si `$ErrorActionPreference = "Stop"`.** PS 5.1 envuelve cada línea de stderr en un ErrorRecord (`NativeCommandError`), así que la PRIMERA línea que el proceso escriba a stderr mata el script aunque termine con código 0. Mordió el 2026-07-28: `masterizar-mpd.ps1` (hoy `masterizar-podcast.ps1`) reventó al medir con ffmpeg, que escribe todas sus mediciones a stderr por diseño. Solución: bajar a `Continue` solo alrededor de la llamada y verificar el resultado a mano (`Test-Path`, parsear la salida), en vez de confiar en que la excepción avise.

```powershell
# OJO: el parametro NO se puede llamar $args -- es variable automatica de PowerShell.
function Invocar-Nativo([string[]]$argumentos) {
    $previo = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try { return & ffmpeg @argumentos 2>&1 | ForEach-Object { "$_" } }
    finally { $ErrorActionPreference = $previo }
}
```
- Git Bash mangla rutas absolutas de Windows; usar PowerShell para cualquier cosa que pase rutas a ComfyUI u otros binarios de Windows.

## Comportamiento al iniciar

**Antes de responder nada**, sigue este orden:

1. **Sincroniza con GitHub:** ejecuta `git pull origin main` Y TAMBIÉN `git -C "$env:USERPROFILE\.claude\skills" pull origin main` — son 2 clones del mismo repo y el global se desactualiza solo (mordió 2026-07-08: 1 mes stale en el portátil, una skill "no existía")
   - **Repos externos:** antes del primer edit **o de lanzar cualquier agente (Explore/executor) sobre otro repo** (hiresignal, kuma-talent-web, etc.): `git -C <repo> fetch origin` y verificar si está detrás — pull ANTES de editar o explorar, no al pushear (mordió 2026-07-08: clon de hiresignal 40 commits stale → merge de 4 conflictos; mordió 2026-07-10: exploradores lanzados pre-pull mapearon el árbol viejo y reportaron que un feature existente "no existía").
   - **Trazabilidad del SHA (antes de lanzar subagentes):** correr `git pull --rebase --autostash` en CADA repo que los agentes vayan a leer (`--autostash` porque un working tree sucio aborta el rebase), e **imprimir el HEAD sha resultante de cada uno**. Pasarle ese sha a cada agente en su prompt y exigir que lo **cite en su reporte** — un sha que no coincide delata una lectura stale. **Un agente por workstream** — un *workstream* es un entregable independiente que no comparte archivos de salida con otro (ej.: metadata de Spotify vs rotación del grid). Si dos tareas escriben el mismo archivo, son UN solo workstream.
   - **En plan mode (no se puede hacer pull):** verificar staleness read-only con `git ls-remote origin` vs HEAD local, y poner el pull como primer paso de ejecución del plan (funcionó 2026-07-16 con hiresignal desactualizado).
2. **Busca un handoff reciente:** revisa `.agents/handoff/` — abre el archivo con la fecha más reciente.
3. **Decide cómo continuar:**
   - **Antes de resumirlo, verificarlo.** Producir una tabla `afirmación del handoff | estado real | discrepancia`, con evidencia real por fila: `Get-Date` para cualquier afirmación temporal (nunca inferir la fecha), `git log --oneline -10` + `git status` de cada repo tocado, y listado del directorio de assets del episodio. Lo que no se pueda comprobar se marca **NO VERIFICADA** en vez de omitirse. Nunca presentar lo que dice el handoff como estado actual — el 2026-07-23 un handoff de 27 minutos de antigüedad ya traía una ruta equivocada (`mrputridsden/` cuando el real era `.claude/skills/mrputridsden/`), y el `skill-kit-auditor` llevaba 45 días roto detrás de un handoff que se declaraba "verified across all 11 repos".
   - Si existe uno: resúmelo en 2-3 líneas (qué se hizo, dónde pausó, qué sigue) y pregunta si quiere continuar desde ahí. No asumas que sí.
   - Si no hay ninguno: sigue con el mensaje de bienvenida normal.

Cuando el usuario abra esta carpeta y escriba cualquier cosa (y no hay handoff), responde:

> **Bienvenido al creador de skills**
>
> Voy a ayudarte a crear una skill personalizada para Claude Code. Una skill es como un "modo experto" que le enseña a Claude a hacer algo específico.
>
> **¿Qué proceso quieres automatizar?**
>
> Puede ser cualquier cosa: generar informes, analizar datos, crear documentos, auditar webs, procesar archivos... Si lo haces de forma repetitiva, puede ser una skill.

Después usa la skill `crear-skill` automáticamente.

## Auto-compactación de contexto

**IMPORTANTE:** Cuando el contexto llegue al **50%**, compacta automáticamente:

```
/compact
```

Esto:
- ✓ Resume el contexto anterior
- ✓ Mantiene el historial importante
- ✓ Continúa la sesión sin desconexión
- ✓ Prepara espacio para nueva conversación

**Configuración:** manual — el auto-compact del harness está **desactivado** (`"autoCompactEnabled": false` en `~/.claude/settings.json`) y este proyecto no tiene `.claude/settings.json`. Compactar al 50% es responsabilidad del modelo, nadie lo dispara solo (verificado 2026-07-23).

## Qué genera

- Un archivo `.md` con las instrucciones completas de la skill
- Opcionalmente: un kit completo con CLAUDE.md e INSTRUCCIONES.md para compartir

## Los 10 principios de una buena skill

1. No inventa datos — pregunta lo que necesita
2. Obtiene datos automáticamente cuando puede
3. Auto-instala dependencias si las necesita
4. Libertad creativa en diseño (no CSS rígido)
5. Se adapta al contexto del usuario
6. Flujo conversacional (no interrogatorio)
7. Fallbacks amigables si algo falla
8. Mensaje de bienvenida claro
9. Sin precios sugeridos ni consejos de venta
10. Resumen claro de lo generado al terminar

## Debugging

Para cualquier ID, API key o valor de env var (ej. Google Drive/Sheet IDs), pedir al usuario que los pegue directamente desde la URL del browser o la fuente original — no retipear. Verificar el string exacto antes de depurar.

No declarar un bug como corregido hasta haberlo verificado (re-ejecutar/reproducir). Para JSON parse errors, revisar específicamente BOM y respuestas API vacías. Si una API LLM devuelve 400 "not valid JSON / zero-length document", sospechar de `json_encode` devolviendo `false` por UTF-8 inválido en el input (típico: texto extraído de PDF) — en PHP usar `JSON_INVALID_UTF8_SUBSTITUTE` y loguear `json_last_error_msg()` (mordió el 2026-07-07 en HireSignal).

Con `curl -L` no forzar `-X POST`: tras un redirect 302 curl reenvía el POST sin body (Google responde 411). Omitir `-X` y dejar que curl convierta a GET después del redirect (mordió 2 veces el 2026-07-06 probando el Apps Script de Kuma).

**Instrumentos que mienten en silencio** — no dan error, así que su salida se toma por buena. Fallan en dos direcciones y las dos están cubiertas aquí: la mayoría **sub-reporta** (devuelve de menos y produce «sin hallazgos» falsos), y al final de la sección está el caso inverso —un medidor que **sobre-reporta** y aprueba una compuerta que no pasó—, que es más peligroso porque cierra el paso en vez de abrirlo.

**El principio, antes de la lista de culpables** (generalizado 2026-07-25, tras caer 3 veces en una sesión con instrumentos que NO estaban en la lista): un «cero hallazgos» solo vale si la búsqueda cubrió **todas las formas que el dato puede tomar**. Antes de reportarlo, preguntarse las tres:

1. **¿Otra representación del mismo valor?** Un color vive como `#C9A84C` **y** como `rgba(201,168,76)`; una fecha como `2026-07-25` y como `25 de julio`; una ruta con `\` y con `/`; **un número como `827` y como «ochocientos veintisiete»**. Buscar el hex y no el rgb dejó oro vivo en un CSS que yo había declarado limpio.
   **Corolario, cuando el instrumento es un extractor propio y no un grep:** el filtro que lo vuelve manejable define lo que la auditoría **nunca va a mirar** — no es que el patrón falle sobre el candidato, es que el candidato no entró al conjunto. Mordió **tres veces en cadena** el 2026-07-31 sobre un mismo guion: un extractor filtró por `\d` y no vio las 16 cifras escritas en palabras (dentro había un error real, «cincuenta y seis años» por 57); el que se escribió para arreglarlo exigía que la cifra fuera seguida de `años|millones|mil|por ciento|libras` y no vio «veintidós mil setecientas diecisiete **bajas**» ni «cinco **personas**»; y un tercero dio falso negativo porque el PDF traía un espacio Unicode donde el patrón esperaba uno normal. **La salida no es un filtro más fino: es recorrer el corpus entero por otro eje** (ahí, leer las líneas habladas completas en vez de extraer cifras). Al reportar, decir **contra qué filtro** se buscó, no solo el resultado.
2. **¿Busqué el término o la idea?** Buscar `Kratos` y `cultura pop` no encuentra «los personajes que más amamos», que ES la tesis de cultura pop. Cuando lo que se caza es un concepto, el grep de palabras no basta: hay que leer.
3. **¿El corpus incluye al propio objeto evaluado?** Un guion comparado contra una carpeta que contiene su propia copia `.artifact.html` matchea consigo mismo — 19.000 falsos positivos. Excluir siempre el target y sus derivados.

Y una cuarta, para conteos: **¿estoy midiendo la región relevante o el archivo entero?** «36 menciones de call center» era el HTML completo con notas y metadata; en las líneas habladas eran **0**.

Instancias concretas ya documentadas (las dos primeras mordieron el 2026-07-23):
- `Get-Content X | Measure-Object -Line` **no cuenta líneas en blanco** (dio 28 donde `wc -l` daba 36). Para contar líneas usar `wc -l`.
- `glob.glob('**/x', recursive=True)` de Python **omite directorios que empiezan con punto** — leyó 18 de 28 `SKILL.md` porque se saltó todo `.claude/`. Usar `os.walk`.
- **Patrones con tildes pasados por la línea de comandos se manglan y devuelven ceros falsos.** El 2026-07-28 un lint de muletillas reportó `imagínense = 0` con el patrón roto en la consola. Escribir el script a disco con escapes unicode (`imagín`) y correrlo desde ahí, no pasarlo inline.
- **Un umbral absoluto sub-reporta en los tramos fuertes de la señal.** Mismo día: `silencedetect -40dB` contó **1 pausa** en el último minuto de un audio porque ese tramo estaba 10 LU más alto y los silencios no cruzaban el umbral. Parecía música. El espectrograma mostró voz con pausas normales. Con umbrales fijos, verificar los extremos con un instrumento distinto.
- **Ningún buscador de texto ve el `\r`: `awk`, `grep` y `Select-String` devuelven CERO sobre un archivo CRLF.** Medido el 2026-07-28 sobre un archivo con 3 bytes `0x0D` reales: `awk '/\r$/'` → 0, `grep -c $'\r'` → 0, `Select-String "\r$"` → 0, y `[IO.File]::ReadAllBytes` → 3. Los tres tratan el `\r` como parte del terminador de línea y lo descartan antes de que el patrón lo vea. Mordió ese día: tras editar un `.rpp` de Reaper el chequeo con `awk` dio vacío y parecía que la escritura había convertido los finales de línea; a nivel de bytes los 463 CRLF estaban intactos. **Para verificar finales de línea o cualquier byte de control, contar bytes con python (`open(p,'rb').read().count(b'\r\n')`) o `od -c`** — nunca con un buscador de patrones.
- **Un lint que nombra lo que busca se encuentra a sí mismo** — es el principio 3 («¿el corpus incluye al propio objeto evaluado?») a escala de línea, no de carpeta: la nota que decía «marcadores `[VERIFICAR]` abiertos: 0» hacía que el grep de `[VERIFICAR` reportara 1. Redactar las notas de lint sin escribir el patrón literal.
- **La herramienta de lectura de imágenes cachea por ruta: releer un archivo que acabo de sobrescribir devuelve la versión ANTERIOR.** Mordió el 2026-07-30: tras regenerar `MPD-T2E01-16x9-FINAL.png` con el grading azul, releer esa misma ruta devolvió la miniatura vieja —neutra, sin grading— y estuve a un paso de reportar que el fix no había entrado. Lo que decide es el archivo en disco: medirlo con PIL/python, o escribir la prueba con un **nombre nuevo**. Nunca tomar una segunda lectura de la misma ruta como evidencia de un cambio.

- **Grepear solo el REPO para saber si un asset existe da un «no existe» falso.** Los assets renderizados están repartidos en dos sitios y hay que mirar los dos:
  - **`E:\` (portátil: `D:\`)** — artwork de episodio, quote cards, audio, banners de redes. Ej.: `E:\Podcast\MPD\Temporada 2\redes\`.
  - **El repo, en `*/website/`** — los assets del sitio web, que viven versionados porque se despliegan desde ahí (`den-bg.jpg`, `og-image.jpg`, `t2-cover.jpg`, `bar-bg.png`…).

  Mordió el 2026-07-30: se reportó que no había nada de perfil de YouTube para MPD después de grepear el repo por `banner|2560|channel`, y un minuto después `E:\Podcast\MPD\Temporada 2\redes\` tenía el kit completo — banner 2560×1440, avatar, cover de Facebook y header de X. La regla de que el output va a `E:\` ya existía, pero escrita como regla de **escritura**; muerde como regla de **búsqueda**. **Antes de afirmar que un asset no existe, listar el directorio de producción del show en el disco Y `*/website/` en el repo** — no grepear uno solo. (Ojo con la simplificación inversa: «el repo solo guarda instrucciones» también es falsa, y haría saltarse los 12 assets del sitio.)

**Y el reverso, que es peor: un medidor que hardcodea QUÉ mide da aprobados falsos.** Los casos de arriba sub-reportan y producen «cero hallazgos» falsos; este **sobre**-reporta y cierra una compuerta que en realidad no pasó. Mordió el 2026-08-01: el script que verifica la compuerta de contenido aplicable de un guion tenía los segmentos objetivo fijos como `('1','6')`. Al renumerar el guion —se insertó un segmento nuevo— el 6 pasó a ser otra cosa, y el script reportó **32,3% OK** midiendo el segmento equivocado. Al arreglarlo dio un **fallo igualmente falso**, porque el segmento correcto no llevaba la marca. Solo la tercera medición era real.

- **Un script de compuerta deriva del artefacto qué mide** — lee una marca dentro del propio bloque (`APLICABLE` en su nota, un atributo, un id), nunca un índice o un nombre posicional.
- **Al renumerar, reordenar o insertar algo, re-verificar que el medidor siga apuntando ahí.** El renumerado es silencioso para el script.
- **Un resultado que cruza el umbral por poco merece una segunda mirada al instrumento, no solo al dato.** El PASS falso venía con un margen cómodo, y eso fue justo lo que lo hizo creíble.

Antes de reportar un conteo o un "cero hallazgos", cruzar el total con una segunda herramienta. Ver §Procedencia en `~/.claude/CLAUDE.md`.

**Antes de SUMAR un instrumento a esta lista, reproducir el fallo.** La lista de arriba es larga y buena, y por eso mismo genera falsos diagnósticos: cuando una salida rara se parece a un patrón ya documentado, el parecido hace que un dato suelto **se sienta confirmado**. El 2026-08-01 se reportó que `Get-ChildItem -Recurse -Filter "*.mp3" -File` devolvía cero teniendo 10 archivos; al intentar reproducirlo con cuatro variantes (`-Filter` antes y después de `-File`, `Where-Object Extension`, `-Include`) **las cuatro dieron 10**. No había tal instrumento mentiroso: era una anomalía de una corrida. Un cero que no se reproduce es una anomalía, no una regla — y escribirla habría hecho que la próxima sesión evitara una herramienta que funciona. Esto NO relaja el cruce de conteos de arriba: seguir cruzando siempre, pero **atribuir la causa solo después de reproducirla**.

**Al modificar cualquier productor —compositor de imágenes, formateador, exportador, plantilla—, correrlo contra el caso que YA funcionaba antes de darlo por bueno.** Probar solo el caso nuevo —el que motivó el cambio— esconde las regresiones, porque el caso nuevo es justamente el único que se está mirando. Mordió el 2026-07-31: el arreglo de `portada-ep-compose.py` para títulos largos perdió el chequeo de ancho y hacía que `HAWTHORNE` se saliera del cuadro; con el título de EP.024 se veía perfecto y solo apareció al renderizar un título de la fórmula vieja. **El diff se hace sobre la salida, no sobre lo que el script reporta de sí mismo:** ahí los tamaños de fuente volvían idénticos (420/216/152 px) mientras 220.013 píxeles habían cambiado. Para imágenes deterministas eso es `ImageChops.difference`; para texto, `git diff` o `fc`.

**Al actualizar una regla, separar lo histórico de lo normativo.** Un documento mezcla enunciados que *describen lo que pasó* con enunciados que *mandan lo que se hace*. Solo los segundos se actualizan. El 2026-07-25, al retirar la música de intro/outro, la frase «el ritmo se midió sobre EP.20 sin contar intro/outro musical» **se conservó**: ese episodio sí llevaba música y reescribirla habría falsificado el registro de cómo se calibró la cifra.

**Y al RETIRAR una regla, grepear el documento entero por su nombre antes de darla por retirada.** Un documento largo guarda la misma regla en varios sitios —la sección que la define, el checklist que la exige, la nota que explica por qué existe— y retirarla solo donde se definió deja copias vivas que siguen mandando. El 2026-07-28, en `guion-style-btq.md`, «línea de enganche» vivía en **5 sitios**: se había declarado «maquillaje» y eliminada en uno, y otros dos la seguían exigiendo, incluido el checklist previo a entregar. El resultado no fue teórico: la muletilla entró a EP.022, EP.023 y EP.024. La regla vale para cualquier documento de reglas, no solo para las guías de guion. **Ojo con el párrafo de arriba:** el grep saca *todas* las ocurrencias, pero no todas se borran — las que **mandan** se retiran, y las que **narran** («el lint la encontró en EP.022 y EP.023») se conservan, pasadas a tiempo pasado y marcadas como retiradas. Borrarlas también sería falsificar el registro; dejarlas en presente sería seguir mandando.

**Y el barrido incluye los ENTREGABLES producidos bajo la regla vieja, no solo los documentos de reglas.** Esto es lo que falló el 2026-07-28: una auditoría barrió el kit de MPD, declaró 27 mandatos muertos retirados y se dio por completa — pero el corpus fueron los archivos de reglas. El guion de EP.006, escrito bajo las reglas viejas, seguía cargando en su cabecera el codename retirado («The Crossroads») y la dirección visual descartada («whisky & carretera»), muertos desde hacía 4 y 6 días; y todo su CSS seguía en la paleta de Temporada 1, incluido un ámbar que se había retirado explícitamente. Nada de eso aparecía en los documentos de reglas: vivía en el producto. **Al retirar una regla, grepear el repo, no el documento** — guiones, plantillas, HTML publicado, prompts guardados. Y ojo con dónde se esconde: en ese caso dos colores retirados sobrevivieron al reemplazo completo de la hoja de estilos porque estaban como `style="…#9B1C1C"` **inline en el body**. Para cambios de paleta, el grep obligatorio es `style="[^"]*#`. **Esto NO choca con la regla 11 (NO SOBRE-LEER) ni con «solo inputs que DECIDEN»:** grepear no es leer. El barrido devuelve una lista de coincidencias, y solo se abren los archivos que aparecen — igual que etiquetar un pendiente es barato frente a releerlo todo.

**Y no basta con anotar la superación ARRIBA: hay que marcar el bloque superado en sí mismo.** Una nota de encabezado la ve quien lee el documento de principio a fin; nadie lee así un documento de reglas. Se entra por un grep, por un enlace o por la mitad — y ahí solo se ve el texto viejo, en presente, con toda la autoridad intacta. Mordió el 2026-08-01: el giro de BTQ a portadas de tipografía pura (2026-07-25) se escribió como nota al inicio de la sección de `brand-constants.md`, y **el cuerpo de abajo se quedó describiendo la era de objeto en presente** — las 7 reglas de la dirección, el bloque de escena, el upscale. Una semana después se construyó un prompt de artwork desde ese cuerpo y salió una fotografía de cuarto de máquinas que no se parecía en nada a lo que el show publica; lo detectó Andy, no el documento. En la misma sección, otro párrafo afirmaba que las quote cards seguían llevando escena cuando el generador ya decía lo contrario.

- **Marcar el bloque superado donde vive:** tachado, `HISTÓRICO`, `SUPERADO por X el YYYY-MM-DD`, o moverlo a un anexo al final. Que sea imposible leerlo sin ver que ya no manda.
- **Cuando el documento y el código se contradicen, gana el código** — es lo que corre. Y la contradicción se reporta, no se resuelve en silencio.
- **Al escribir un prompt, un guion o una config desde un documento de reglas, abrir primero el último ENTREGABLE publicado** de esa familia. El entregable es el estado real; el documento es la intención. *(Es el espejo del párrafo anterior: allá los entregables se barren al RETIRAR una regla; acá se leen ANTES de escribir bajo ella. Misma palabra, momentos opuestos.)*

## Una cifra compuesta no es una constante

Cuando una medición mezcla dos variables independientes, el número resultante **solo vale para
la muestra de la que salió** — y escribirlo como constante produce una regla falsa que después
manda sobre decisiones reales.

Mordió el 2026-07-28: el piloto de MPD duró 45:55 contra ~40,5 estimados. Se concluyó «el guion
está 13% largo», se recortaron ~500 palabras y se escribió en la guía de estilo un ritmo de
«113,9 palabras escritas por minuto» como si fuera el ritmo del host. Falso. Al separarlo:

- **Articulación: ~168 wpm.** Medida sobre 13 SRT de dos shows distintos, rango ±6%.
- **Densidad de pausa: 32,5%** en ese episodio contra 9-14% en los anteriores.

**Y la cifra "corregida" salió mal a su vez** — se escribió ~175 wpm ese mismo día. El medidor
contaba la etiqueta `[SPEAKER_00]:` como palabra hablada (infla 3,6-8,6% según cuántos segmentos
tenga el archivo), así que la constante "real" era artefacto del instrumento. Detectado el
2026-07-28 al recalcular sobre la regrabación. **Corolario: separar las variables no basta si el
instrumento que las mide está sesgado — cruzar cada cifra nueva contra un segundo método ANTES de
escribirla como constante.** Lo que la destapó fue que un número (186 wpm) no cuadraba con el resto
de la serie.

El guion no estaba largo; **un tercio de la grabación era silencio**, puesto a propósito por el
registro del formato. La «constante» compuesta mezclaba una propiedad del host con una decisión
de dirección.

**Antes de escribir un ratio como regla, preguntar: ¿qué dos cosas estoy multiplicando aquí, y
puede una moverse sin la otra?** Si puede, medirlas por separado y dejar la fórmula, no el
producto. Y nombrar cuál de las dos es decisión humana — esa es la que hay que fijar primero.

## Límites de lo publicable (medir, no estimar)

- Descripción del show en Spotify: límite duro de **600 caracteres** — contarlos antes de enviar.
- Cualquier copy publicado con límite de plataforma: **imprimir el conteo de caracteres** en la respuesta.
- Imágenes embebidas en HTML: toda `<img>` con regla de `width` debe llevar `height: auto` en la MISMA regla. **Verificación:** revisar cada `<img>` una por una — NO un grep del archivo: `width:\s*\d` también matchea divs, y un solo `height: auto` en cualquier parte enmascara al resto (comprobado 2026-07-23).
- Negro de marca: **no lo redeclares aquí** — la fuente es `.claude/skills/episode-launch/docs/brand-constants.md`. Lo único que se afirma acá: un asset generado que renderiza negro puro `#000000` está mal y se corrige antes de componer.

## Artwork (reglas de generación — persisten entre sesiones)

**Fuente canónica de las reglas de artwork BTQ:** `.claude/skills/episode-launch/docs/brand-constants.md` § "Dirección de artwork" (**CONGELADA v3**, 2026-07-04). Esta sección NO la reemplaza — agrega lo que no está allí. Si chocan, gana el archivo congelado.

- **Motivos vetados:**
  - **Círculos concéntricos / anillos / diana: VETADOS en TODAS las imágenes** — portadas **Y** quote cards. Decisión de Andy del **2026-07-10 (EP.021)**; antes el motivo estaba "reservado para la portada" y por eso reaparecía. Única excepción: cuando la diana **ES el sujeto central** de la escena (ej. Q2 de EP.020). La línea `DO NOT render any concentric ring, circle, halo, or archery-target pattern anywhere in this image.` va en **todo** prompt desde el primer intento: el modelo los reinserta solo (Flow en EP.020; Z-Image local en EP.022) y **pueden colarse disfrazados de textura** — en EP.022 una tela salió cubierta de mini-círculos, invisible a tamaño completo y detectada solo al hacer zoom a una esquina.
  - *cualquier asset:* proporciones chibi; personas en cards marcadas "sin personas".
  - ⚠️ **La og-image editorial (figura + surcos de vinilo) está RETIRADA** — concepto muerto desde 2026-07-23 porque dependía de los aros vetados. `btq-production/artwork-general-v3.md` quedó como registro histórico; su reemplazo será un concepto nuevo, no una corrección. La og-image en vivo sigue con el typo "PREMIUM KEY EDITOIAL" y ~2 MB (límite 500 KB).
- Confirmar el aspect ratio destino por tipo de asset (portada vs quote card vs tile de grid) ANTES de generar.
- Renderizar e inspeccionar visualmente **todas** las variantes de aspect ratio antes de declarar un set completo.

## Long-running jobs (descargas y renders > 2 min)

Antes de arrancar cualquier descarga o render que se espere que pase de 2 minutos:

- **Estimar y decirlo primero:** duración estimada y, si es descarga, bytes totales. Para un render los bytes no dicen nada — la estimación es `steps x it/s` **nombrando la máquina** (3080 Ti 12GB en el desktop vs 3060 6GB en el portátil dan números distintos).
- **Baseline más simple primero:** proponer el workflow mínimo que podría funcionar, **correrlo y mostrar su output** antes de agregar nodos o etapas. Instancia de las reglas #14/#15 globales.
- **Progreso:** lanzar en background escribiendo a un log; reportar en cada frontera de etapa y al terminar, con tiempo transcurrido. El log se puede leer a demanda. **No prometer una cadencia fija de 60s** — el harness no da un timer propio durante una tarea: un comando en foreground bloquea hasta que retorna y uno en background solo avisa al completarse.

## Principios de tooling — lean y reactivo

- No agregar hooks de `SessionStart` ni ningún costo fijo de arranque. Los hooks deben ser dirigidos por evento (`PreToolUse`/`PostToolUse`) y dispararse solo cuando ocurre el evento relevante.
- **`PostToolUse` corre DESPUÉS de la herramienta — no puede bloquear nada.** Para impedir que algo se ejecute hay que usar `PreToolUse` con `hookSpecificOutput.permissionDecision: "deny"` (verificado 2026-07-23 contra el schema de settings).

## Workflows

Ritual de cierre de sesión: `/session-close` lo automatiza completo (retrospective → skill-management → handoff). Equivale a ejecutar `/retrospective`, luego `skill-management`, luego `/handoff` en ese orden. Aplicar los fixes aprobados del audit antes de generar el handoff.

## Regla de transición de modelo (vigente desde 2026-06-12)

Este proyecto fue calibrado con Fable 5, que infiere mucho desde contexto. Cualquier modelo que ejecute aquí (en especial Opus 4.8 después del 2026-06-22) debe compensar siguiendo lo escrito de forma literal:

1. **Seguir los checklists al pie de la letra.** El estándar de calidad por entregable vive en `docs/estandar-de-entregables.md` — correr el checklist de la sección que aplique ANTES de declarar algo listo. Si un ítem falla, corregir y re-verificar.
2. **Correr los lints de las skills antes de entregar** (greps de muletillas, conteos, fórmulas de título). Los criterios son verificables a propósito: verificarlos, no estimarlos.
3. **Consultar MEMORY.md y el handoff más reciente antes de actuar.** Las decisiones de juicio ya tomadas están escritas ahí y en `docs/roadmap-future-proofing.md`; no re-derivarlas ni contradecirlas sin preguntar.
4. **Si una tarea requiere juicio que no está escrito, preguntar al usuario** en vez de improvisar — y al resolverla, escribir la regla nueva donde corresponde.
5. **Al cambiar de objeto dentro de la sesión, re-confirmar el eje de la revisión.** Regla completa en `~/.claude/CLAUDE.md` regla #14 — no re-declararla acá.
