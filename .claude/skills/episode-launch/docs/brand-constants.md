# Brand constants (BTQ)

| Element | Value |
|---------|-------|
| Void (fondo base) | `#0E1113` — **nunca** negro puro `#000000` |
| Panel | `#22262A` — cara alta del degradado, sensación de chapa |
| Acero | `#39434A` — tono medio: reglas, marcos, barras apagadas |
| Cream | `#F4EFE7` — wordmark y títulos |
| Señal | `#FF3D00` — **un solo elemento por imagen** |
| Muted | `#8B9492` — etiquetas mono, metadatos |
| Display | Cabinet Grotesk Extrabold |
| Cuerpo | Supreme (Regular / Medium / Bold) |
| Datos / mono | Martian Mono |
| Headsets | Si aparece uno: contact center boom mic — NEVER music headphones |
| Spotify category | Business → Management (secundaria: Business → Careers) |
| Kicker de marca | `GESTIÓN · CALIDAD · LIDERAZGO` |
| Primary language | Spanish |
| Alcance | **Macro — gestión de equipos y operaciones en cualquier industria** (giro 2026-07-25) |
| Core audience | Hombre 35–44, gerente/supervisor — Colombia 70% + EE.UU. 20% (analytics 2026-06-12) |
| Priority platform | LinkedIn (profesional 35–44; 15% escucha en desktop en el trabajo) |

## Giro de alcance (2026-07-25)

El show deja de estar acotado a call center / BPO y pasa a gestión a nivel empresarial. La
teoría puede venir de donde sea; el aterrizaje es «su equipo / su empresa», ya no «su call
center».

**Lo que NO cambia — la esencia, fijada explícitamente con Andy:**

1. El mundo Sala de Máquinas: grafito, acero, cream, un solo naranja, luz plana de taller.
   Nada de abstracción corporativa — ni rascacielos, ni engranajes, ni apretones de manos.
2. La voz de trinchera: «desde la trinchera, no desde un libro». Macro no significa académico
   ni de consultor.
3. El formato: teórico nombrado + casos reales con consecuencias que escalan + un dato duro +
   el giro al 60 %. **El ORDEN de los segmentos no es parte de la esencia** (precisado
   2026-07-25): lo intocable son esas piezas, no la secuencia en que aparecen. Ver la rotación
   de esqueletos en `btq-production/guion-style-btq.md`.
4. El ritual: «Buenas y santas…», el cierre canónico, las recomendaciones de Andy.
   **Precisión 2026-07-25 (confirmada por Andy):** «las recomendaciones de Andy» se cumple
   aunque vayan **tejidas dentro del cuerpo como citas del argumento** —«esto lo cuenta Mayo en
   su libro», «lo van a ver retratado en tal película», «y lo confirma tal en su charla»— en vez
   de un bloque con encabezado antes del cierre. Lo esencial es que Andy recomiende, no que haya
   una sección llamada así. Motivo: el bloque con nombre funciona como señal de créditos finales
   y le da permiso al oyente para abandonar antes del cierre real (ver § No dar señales de cierre
   falso en `guion-style-btq.md`).
5. La metáfora de la cola: esperar, acumular, el backlog — funciona en cualquier empresa y es
   lo que le da sentido al nombre. **En la marca vive en inglés y no se traduce nunca:**
   «Behind the Queue» se dice y se escribe en inglés incluso a mitad de una frase en español,
   porque `cola` significa «trasero» en buena parte de Latinoamérica. Al bajar al guion se dice
   *fila / espera / backlog*. Regla completa en `btq-production/guion-style-btq.md`.

**Costo aceptado a sabiendas:** se pierde la cola larga SEO de «call center» a cambio de
repertorio. Se le señaló el riesgo a Andy —EP.020 funcionó justamente por esa keyword— y
decidió proceder. Por eso EP.020 **no se retitula**: ver `btq-production/metadata-v4-macro.md`.

**Relación con andyfreelancer:** Void, Cream, Señal y Muted se toman **exactos** del sistema de
`the-freelancer/one-pager/index.html` para que las dos marcas de Andy se lean como familia.
El **Acero** es propio de BTQ y es el diferenciador — andyfreelancer no tiene tono medio. Si el
acero desaparece de una composición, la imagen cae en el cliché de «negro con un acento» y hay
que rehacerla.

---

## Dirección de artwork v4 — "Sala de Máquinas" (2026-07-25)

> **Reemplaza a v3, que queda descongelada y archivada** (ver §Histórico al final). v3 giraba
> alrededor de una regla que dejó de ser aplicable el 2026-07-21, cuando BTQ pasó a 100% pilar
> SEO: *«patrón geométrico del universo del referente»*. Sin cultura pop no hay referente, y la
> dirección se quedó sin su pieza central.

> **Actualización 2026-07-25 (tarde) — las PORTADAS pasan a TIPOGRAFÍA PURA.** Decisión de
> Andy: «prefiero algo sencillo y minimalista». Se abandona la búsqueda de un objeto que
> represente al show. Ninguno de los tres candidatos se explicaba solo, y costaron seis rondas
> y más de veinte generaciones. Lo que sigue vigente de Sala de Máquinas es la **paleta, la
> tipografía y el principio de una sola señal**; lo que se retira es el objeto renderizado.
>
> **Portadas y assets de marca: `comfyui/templates/brand-covers-compose.py`.** No usa ComfyUI
> ni ningún modelo — todo determinista con PIL. Genera portada 1:1, avatar y banner de YouTube
> en una corrida. Se acabaron los sellos alucinados, el veto de anillos y el piso de negro puro.
>
> **Concepto:** el nombre hace el trabajo. El wordmark ocupa el cuadro en tres líneas y
> **`QUEUE` va en Señal `#FF3D00`** — la palabra *es* la señal. No hay objeto que interpretar.
> Verificado legible a 300 y 96 px; avatar legible a 48 px.
>
> ~~Lo de abajo (escena, prompts, upscale) queda como **registro** de la etapa de objeto y sigue
> aplicando a las **quote cards**, que sí llevan escena. Si Andy quiere llevarlas también a
> tipografía pura, es una decisión aparte que no se ha tomado.~~
>
> **CORREGIDO 2026-08-01 — este párrafo era falso y llevaba una semana mandando mal.** Las quote
> cards **también** pasaron a tipografía pura el mismo 2026-07-25. Lo dice el propio generador,
> `comfyui/templates/quote-card-compose.py`: *«antes cada card llevaba una escena renderizada en
> la mitad derecha. Eso era v3 y sobrevivió por descuido al giro a tipografía pura — generaba
> anillos vetados, fondos de estudio blancos y una ronda de iteraciones por card. La cita ES el
> contenido; no necesita ilustración»*. **Gana el código, que es lo que corre.** Detectado al
> proponer artwork con escena para EP.024 apoyándose en este párrafo.
>
> **Estado real: BTQ no tiene hoy ningún asset con escena renderizada.** Portada de episodio,
> portada de show, avatar, banner y quote cards son todos tipografía determinista con PIL. El
> bloque de escena de abajo queda como **registro histórico**, sin destinatario vigente.

> **EXCEPCIÓN PUNTUAL — EP.024, y solo EP.024 (2026-08-01).** Decisión de Andy: la portada de
> ese episodio vuelve a llevar **escena renderizada**, con el concepto de los tres monos
> —«no ver, no oír, no hablar»— torcido para que las manos que los tapan **vengan desde fuera
> del cuadro**, de modo que la imagen diga la tesis del episodio (alguien puso el precio de
> hablar) y no la que el episodio demuele (ignorancia voluntaria).
>
> - **No descongela la dirección.** Se le señaló el costo —la puerta se cerró el 2026-07-25 tras
>   seis rondas y más de veinte generaciones, con un «prefiero algo sencillo y minimalista»— y
>   Andy confirmó que es solo para este episodio. Del EP.025 en adelante sigue la tipografía pura.
> - **Compositor:** `comfyui/templates/portada-compose.py`, que está marcado `MUERTO — NO USAR`.
>   Se revive **únicamente** para esta corrida; la marca no se quita.
> - Aplican íntegras las reglas 1-7 de abajo, en especial el veto de círculos —que con Z-Image a
>   `cfg=1.0` se resuelve construyendo la escena sin motivo redondo, no prohibiéndolo— y el veto
>   de chibi/cartoon, que en este concepto es riesgo alto.

> ⚠️ **TODO LO QUE SIGUE ES REGISTRO HISTÓRICO, NO INSTRUCCIÓN VIGENTE** (marcado 2026-08-01).
> El giro a tipografía pura del 2026-07-25 se corrigió **solo en el encabezado** de esta
> sección; el cuerpo de abajo —las 7 reglas de la dirección, el bloque de escena, el upscale—
> se quedó redactado en presente y lleva una semana leyéndose como vigente.
>
> **Cómo mordió:** el 2026-08-01, al armar el artwork de EP.024, se construyó un prompt desde
> estas reglas y salió una fotografía de cuarto de máquinas —lockers, banco de trabajo,
> luminaria cenital— que no se parece en nada a lo que el show publica. Andy lo detectó de
> inmediato: *«la temática de maquinaria choca mucho con la identidad del programa»*. Tenía
> razón, y la evidencia es la portada publicada de EP.023 (`E:\AI\outputs\BTQ-EP023\`):
> **tipografía sobre vacío, sin escena, sin objeto, sin maquinaria.**
>
> **Lo que de verdad sigue vigente de «Sala de Máquinas» son tres cosas y ninguna es un
> escenario:** la **paleta** (void `#0E1113`, grafito `#22262A`, cream `#F4EFE7`, señal
> `#FF3D00`), la **tipografía** (display grotesca + kicker mono con tracking) y el **principio
> de una sola señal**. El nombre de la dirección sobrevivió a su mundo — es una metáfora de
> paleta, no una locación.
>
> **Antes de escribir cualquier prompt de imagen para BTQ, abrir la última portada publicada**
> y no estas reglas. El generador vigente es `comfyui/templates/portada-ep-compose.py`
> (determinista, sin modelo).

~~**BTQ = el piso de operación como cuarto de máquinas.** Grafito y acero como mundo, luz plana de
taller, y **una sola luz de señal encendida** — el naranja que en una planta significa «mire
esto». Un objeto por episodio, nunca un collage.~~

### Reglas de la dirección — HISTÓRICAS (era de objeto, 2026-07-25 y antes)

1. **Un objeto literal del contenido del episodio**, renderizado con volumen y textura de
   material real (metal, vidrio, baquelita, tela). Nada de personas genéricas. Si una persona es
   indispensable para la escena del hook, **declarar rasgos étnicos explícitos en el prompt** —
   Z-Image Turbo por defecto genera un hombre de rasgos asiáticos sin importar el contexto
   (confirmado 2 veces, 2026-07-21; ver `comfyui/docs/prompting.md`).
2. **Luz plana, cenital, de taller.** El volumen viene del material, no de un halo. *No* usar el
   glow dorado de contorno «como estatua iluminada desde atrás» — eso era v3 y se retiró con el oro.
3. **Un solo elemento en `#FF3D00` por imagen.** Dos acentos matan el efecto de señal.
4. **Fondo: rejilla fina de líneas verticales** tipo panel, en `#1F2428` sobre el degradado. Marca
   de agua, nunca compite con el objeto.
5. **Círculos concéntricos, anillos, halos y dianas: VETADOS** en portadas Y quote cards
   (decisión de Andy 2026-07-10, EP.021). Única excepción: cuando la diana **es** el sujeto central
   de la escena. La línea va en **todo** prompt desde el primer intento:
   `DO NOT render any concentric ring, circle, halo, or archery-target pattern anywhere in this image.`
   ⚠️ **Esa línea va en el prompt POSITIVO, y con Z-Image no basta.** Z-Image Turbo corre a
   `cfg=1.0` y **a CFG 1.0 el prompt negativo no actúa** (ver `comfyui/docs/prompting.md`): meter
   ahí el veto es un no-op. Mordió el 2026-07-28 en MPD T2·01 — tres portadas seguidas con vinilos
   de diana, relojes de pared y calaveras pese al veto completo en el negativo.
   **Con modelos a cfg 1, el veto se resuelve construyendo la escena para que no haya motivo de que
   aparezca lo vetado**, no prohibiéndolo: quitar del concepto todo lo que invoque objetos redondos
   (fotografías → carátulas, sala con pared → reloj, mesa de archivo musical → vinilos) y cerrar el
   fondo en negro. Prohibir es débil; no dar motivo funciona.
   **Pueden colarse disfrazados de textura** — en EP.022 una tela salió cubierta de mini-círculos,
   invisible a tamaño completo y detectada solo al hacer zoom a una esquina. Verificar con zoom a
   las esquinas, no en la vista general.
6. **Cero IP de terceros** en la portada del show: sables, escudos, prismas, logos ajenos. La
   portada 2026 los tenía y es parte de lo que se está corrigiendo.
7. **Sin proporciones chibi. Sin estilo cartoon. Sin circuit boards.**

### Bloque de escena — RETIRADO, no reconstruir de memoria (2026-08-08)

**Este bloque existía acá como texto copiar-y-pegar** ("Bloque de escena (copiar verbatim,
cambia solo el objeto)"), y por eso sobrevivió el retiro de la dirección industrial: la etiqueta
de "histórico" queda arriba de esta sección, pero el texto de abajo se veía igual de listo para
usar que cualquier prompt vigente. Mordió dos veces con el mismo mecanismo — EP.024
(2026-08-01) y EP.025 (2026-08-07, "porque volvimos otra vez al estilo industrial") — las dos
veces alguien escribió un prompt de escena copiando este bloque sin releer que la sección entera
estaba superada. La tercera vez que un episodio necesite una escena-excepción (no tipografía
pura), el prompt se escribe **desde cero**, describiendo el objeto del episodio contra un fondo
void plano — no se reconstruye este bloque de memoria ni se busca en el historial de git.

**El modelo NO escribe texto.** La escena se genera limpia; wordmark, kicker, título y `EP.NN`
se componen después con PIL.

**Lo que sí sigue siendo válido de cualquier escena-excepción** (extraído de los dos episodios
que la usaron, no del bloque retirado): fondo void plano `#0E1113` sin escena/panel/textura
detrás del objeto, un único acento en señal `#FF3D00`, cero anillos o motivos circulares, cero
proporciones chibi/cartoon. Verificar con muestreo de píxel contra los hex canónicos después de
generar — Z-Image aproxima color por palabra, no por valor exacto (ver
`comfyui/docs/prompting.md`).

### Tipografía y footer (composición PIL)

```
Arriba, alineado a la izquierda, margen 6.2% del lado:
- "BEHIND" / "THE QUEUE"  — Cabinet Grotesk Extrabold, cream, 10.8% del lado, dos líneas
- regla de acero de lado a lado
- "OPERACIÓN · CALIDAD · LIDERAZGO" — Martian Mono Regular, muted, 1.75%

Abajo:
- regla de acero
- Título del episodio — Supreme Medium, cream, 3.35%, máximo 2 líneas
- "EP.NN" — Martian Mono Regular, señal #FF3D00, 3.0%, alineado a la derecha
```

**Anclar la regla superior al píxel de tinta más bajo del wordmark** (`font.getbbox(linea)[3]`),
no al avance de línea: la cola de la Q de QUEUE cruza la regla si se calcula por interlineado
(detectado al renderizar, 2026-07-25).

**Las tildes se escriben.** El apaño de quitar acentos venía de que Flow autocorregía palabras
sin tilde; con composición PIL determinista no aplica. Cobertura de glifos verificada vía cmap en
las cinco fuentes: cero faltantes en `áéíóúñÑüÁÉÍÓÚ¿¡—·«»`.

**Retirado de v3:** los cinco puntos dorados superiores y el footer de dos filas con seis íconos
de plataforma. A 300 px eran una mancha gris. Queda solo `EP.NN`.

### Fuentes — instalación

Las tres son gratuitas y están instaladas por usuario en
`%LOCALAPPDATA%\Microsoft\Windows\Fonts` (sin admin), con entradas en
`HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Fonts`:

| Rol | Archivo | Origen |
|-----|---------|--------|
| Display | `CabinetGrotesk-Extrabold.otf` (+ Bold, Medium, Regular) | Fontshare |
| Cuerpo | `Supreme-Bold.otf`, `Supreme-Medium.otf`, `Supreme-Regular.otf` | Fontshare |
| Datos | `MartianMono-Variable.ttf` | Google Fonts (OFL) — Fontshare devuelve 500 |

**Martian Mono es variable y su instancia por defecto es `SemiExpanded Regular`.** En PIL hay que
llamar `font.set_variation_by_name('Regular')` o el mono sale más ancho de lo previsto.

**Aprovisionar una máquina nueva (hecho en el portátil el 2026-07-26).** No hay que copiar
imágenes entre máquinas: los assets de marca se **regeneran**, que para eso son deterministas.
Hacen falta dos cosas, y en el portátil faltaban las dos:

```
python -m pip install Pillow
```

Fuentes, a `%LOCALAPPDATA%\Microsoft\Windows\Fonts` (crear el directorio si no existe):
`https://api.fontshare.com/v2/fonts/download/cabinet-grotesk` y `.../supreme` devuelven ZIP;
Martian Mono sale de `github.com/google/fonts/raw/main/ofl/martianmono/MartianMono[wdth,wght].ttf`
y hay que **renombrarlo a `MartianMono-Variable.ttf`**, que es el nombre que buscan los scripts.
Copiar el archivo basta para PIL; registrarlas en HKCU solo hace falta si se quieren en otras apps.

**Contraprueba de que no hay deriva entre máquinas:** `BTQ-COVER-q92.jpg` tiene que pesar
**235 KB**. Si da otra cosa, falta una fuente o se coló un sustituto.

**Salida:** `E:\AI\outputs\BTQ-brand` en el escritorio, `D:\AI\outputs\BTQ-brand` en el portátil
— el script recibe la carpeta como argumento, nunca a `C:`.

**Dónde van las portadas de EPISODIO — no es la misma carpeta que los assets de marca**
(fijado 2026-07-31; hasta entonces no estaba escrito y se venía derivando de EP.022):

| Qué | Dónde |
|---|---|
| Assets de **marca** (portada del show, avatar y banner de YouTube, og-image) | `E:\AI\outputs\BTQ-brand` |
| Portadas y quote cards de un **episodio** | `E:\Podcast\BTQ\EP NN\BTQ Artwork EP NN\` |

En el portátil, `D:\` en vez de `E:\`. La carpeta del episodio es también donde vive el audio,
así que la compuerta se corre con
`python scripts/verify_assets.py EPNNN --root "E:\Podcast\BTQ\EP NN\BTQ Artwork EP NN"`.

> ⚠️ **Cuando un episodio cambia de tema, hay que barrer la carpeta del EPISODIO, no solo la de
> `E:\AI\outputs`.** El 2026-08-01 EP.024 pasó del Principio de Peter a seguridad psicológica, y
> el barrido de ese día renombró `BTQ-EP024-PETER-OBSOLETO\` en `E:\AI\outputs` — pero
> `E:\Podcast\BTQ\EP 24\` se quedó con **tres trampas**: el WAV y el MP3 de Peter (con el nombre
> corto, que es el que agarra cualquier script por defecto y con una duración a 26 s de la del
> episodio nuevo), y `BTQ Artwork EP 24\` entera con las portadas de Peter — incluido el
> `-1x1-q92.jpg`, que es exactamente el archivo que se sube a Spotify. Ninguna se veía vieja: se
> veían perfectas. **Al reasignar un episodio, renombrar `-OBSOLETO` el audio Y la carpeta de
> artwork del episodio**, y verificar la identidad del audio por las tomas que cita su `.rpp`
> (`FILE "…-<AAMMDD>_<HHMM>…"`), no por la duración ni por el nombre.
Ojo: EP.023 **no** tiene esa carpeta —su artwork v3 murió con el giro— así que no sirve de
patrón; el que manda es EP.022.

Esto retira el sustituto **Impact** que se venía usando desde EP.022 porque Bebas Neue nunca se
instaló. Ya no hace falta.

### Formatos

1. **1:1 — 3000×3000 real** (mínimo de plataforma). Generar nativo a 1024×1024, escalar ×4 con
   `RealESRGAN_x4plus.pth` vía ComfyUI (`UpscaleModelLoader` + `ImageUpscaleWithModel`) y
   remuestrear a 3000. El modelo se instaló el 2026-07-25 en
   `E:\AI\ComfyUI_windows_portable\ComfyUI\models\upscale_models\` — antes de esa fecha la
   documentación lo daba por hecho y la carpeta estaba vacía.
   **Componer la tipografía a 3000 nativo, nunca escalar el texto.**

### Qué generador se usa — mapa vigente (2026-07-25)

Hay generadores muertos en el repo referenciados por handoffs viejos. **Esta tabla manda.**

| Para | Script vigente |
|---|---|
| Portada del show, avatar y banner de YouTube, og-image | `comfyui/templates/brand-covers-compose.py` |
| Portada de un episodio (1:1 · 16:9 · 9:16) | `comfyui/templates/portada-ep-compose.py` |
| Quote cards (tipografía pura, sin ComfyUI) | `comfyui/templates/quote-card-compose.py` |
| Recorte del stinger desde un track largo | `scripts/cortar_jingle.py` |
| Compuerta de assets | `scripts/verify_assets.py` (`--stage-a` si no se ha grabado) |

**Los documentos de workflow también producen assets y también se quedan viejos.** Un script
muerto falla ruidoso; un workflow desactualizado no falla — te hace generar lo incorrecto con
toda confianza. Al congelar una dirección hay que barrer **los dos**:

| Documento | Última verificación contra la realidad |
|---|---|
| `workflows/step2-generate-assets.md` | 2026-07-25 — §A (fórmula de título) y §D (portadas) alineadas a v4 |
| `workflows/post-publish.md` | 2026-07-25 — § 4b reescrita contra el `index.html` real |
| `docs/brand-constants.md` § Quote Cards | 2026-07-25 — pasada a tipografía pura |

> **Cómo se detectó que hacía falta esta tabla** (EP.023, 2026-07-25). El rebrand v4 actualizó
> los *assets* y los *scripts de imagen*, pero dejó **4 productores** apuntando a v3: la sección
> de quote cards de este archivo, `quote-card-compose.py` (Segoe UI + oro + `#0A0A0A`),
> `step2-generate-assets.md` y `post-publish.md`. Ninguno dio error — cada uno se cobró en
> iteraciones o en un asset fuera de marca cuando alguien lo ejecutó días después.
> **Al cerrar un rebrand, listar todo lo que produce un asset y abrirlo uno por uno.**

> ⚠️ **MUERTOS — no usar, aunque aparezcan en handoffs anteriores:**
> `portada-compose.py` (exige una escena renderizada, que ya no existe en esta dirección),
> `show-cover-compose.py` y `youtube-assets-compose.py` (superados por `brand-covers-compose.py`
> el mismo día que nacieron). El concepto de **panel anunciador** para la portada del show —
> seis ventanas apagadas y una encendida— también murió con el giro a tipografía pura:
> ninguna portada lleva ya objeto renderizado.

`portada-ep-compose.py` recibe el **título publicado completo** y lo parsea; aborta si no sigue
la fórmula. Es a propósito: es la única forma de garantizar que la portada y la metadata no
diverjan, y de paso hace de lint del título.

> **Reconciliado con la fórmula invertida (2026-07-31, al componer EP.024).** El script nació el
> 2026-07-25 asumiendo que el ancla era un nombre propio de 2 palabras y la dibujaba **una palabra
> por línea**. La fórmula invertida del 2026-07-28 pone el problema al frente, así que el ancla
> pasó a ser una frase de 10 palabras y el tipo se encogió a **84 px en 16:9** (contra 216 px de
> EP.023) — ilegible en miniatura y una mancha a 96 px. Ahora el ancla **se envuelve por ancho** y
> el paso de línea se calcula sobre **la tinta real**, no con un avance fijo: con `asize * 0.86`
> la tilde de la `É` chocaba con la pata de la `R`.
> **El chequeo de ancho no es redundante con el envoltorio** — una palabra sola más ancha que la
> caja no se puede partir, así que solo bajar el tamaño la mete; sin él, `HAWTHORNE` se sale del
> cuadro. Se detectó porque el arreglo se probó contra un título de la fórmula **vieja**, no solo
> contra el nuevo.
> Un cambio de **fórmula de título** es un cambio de dirección: barrer los productores igual que
> al cerrar un rebrand (ver la nota de la tabla de arriba).
Escena: `E:\AI\outputs\BTQ-v4-annun2-s515202_00001_.png`.

Dos conceptos descartados por el camino, y por qué — sirven de criterio para el próximo:

- **Medidor de panel:** demasiado conceptual. Si una portada necesita explicación, no funciona
  a 300 px, y un VU-meter lee como equipo de audio.
- **Headset de contact center:** legible al instante, pero ancla el show a una sola industria.
  Se cayó con el giro macro del mismo día, ya generado y compuesto pero **nunca publicado**.
- **Calibrador de precisión:** objeto bonito, pero a 300 px lee como un palo gris y su naranja
  desaparece. Falla lo único sobre lo que está construido el sistema.

**Piso de negro de marca:** Z-Image produce algunos píxeles en negro puro `(0,0,0)`, que esta
guía prohíbe y que `verify_assets.py` reprueba. Los composers lo levantan a `#0E1113` por canal
antes de componer — no hace falta corregirlo a mano, pero sí verificarlo en el output.
2. **16:9 — 1920×1080 nativo** (objeto a un lado, resto reservado para texto) +
   `comfyui/templates/cover-16x9-compose.py`.
3. **9:16 — derivado por PIL** de la escena 1:1 ya aprobada: recorte de la porción del objeto +
   relleno con `#0E1113`. No se genera de cero.

### Checklist antes de aprobar

> El ítem «volumen y textura de material real, no silueta plana» se **retiró el 2026-07-31**:
> era de la dirección v3 con escena renderizada y no tiene objeto sobre una portada tipográfica.
> Sigue vivo para MPD y CCC en `scripts/banned-patterns.json` (`flat-silhouette`,
> dirección `escena-renderizada`).

- [ ] Exactamente UN elemento en `#FF3D00`
- [ ] El acero `#39434A` está presente — la imagen no es «negro con un acento»
- [ ] Cero anillos/círculos/dianas — **verificado con zoom a las cuatro esquinas**
- [ ] Fondo negro real `#0E1113`, no `#000000`
- [ ] Texto letra por letra, con tildes
- [ ] Legible a 300×300 y a 96×96 — generar los reescalados y mirarlos

---

## Quote Cards — TIPOGRAFÍA PURA (v4, corregido 2026-07-25)

Formato **16:9 (1920×1080)**, **sin escena renderizada**. Todo determinista con PIL:
`comfyui/templates/quote-card-compose.py`. No usa ComfyUI ni ningún modelo. Citas verbatim
validadas contra el SRT real. Procedimiento compartido para los 3 shows en
`episode-pipeline/workflows/03b-marketing.md`.

- **Composición:** fondo `#0E1113` a sangre completa, rejilla vertical fina en `#1F2428` como
  marca de agua, cita alineada a la izquierda y centrada en vertical, atribución debajo.
- **Tipografía:** cita en **Supreme Bold** cream `#F4EFE7`, atribución en **Martian Mono**
  `#FF3D00` — el único elemento saturado. Cuerpo de la cita dinámico: arranca en 104px y baja
  de 2 en 2 hasta que el bloque envuelto quepa a lo ancho y a lo alto.
- **Cero objetos, cero fotos, cero ilustración.** La cita ES el contenido.
- **Nombre de archivo canónico: `BTQ-EP0NN-QUOTE-N.png`** (fijado 2026-07-28). El gate
  `scripts/verify_assets.py` lo exige por regex; el nombre viejo `-CARDn-16x9.png` (cards
  renderizadas en ComfyUI, EP.021-022) se sigue aceptando solo por los assets de archivo.
  Cualquier otro nombre hace que el gate **omita las cards en silencio** — fue lo que pasó
  desde EP.023 hasta que se detectó el 2026-07-28.

> ⚠️ **Por qué cambió** (decisión de Andy, 2026-07-25). Hasta este día la sección pedía «mitad
> negra con texto / mitad escena» con la escena generada en ComfyUI. Eso era **v3 y sobrevivió
> por descuido al giro a tipografía pura**: mientras portadas, banner y avatar pasaron a
> tipografía, las quote cards se quedaron pidiendo un objeto renderizado. El costo apareció en
> EP.023: de 4 cards generadas, 2 salieron con anillos vetados (una espiral concéntrica en el
> reflejo de un vidrio, tres anillos de bloom alrededor de una lámpara) y una con fondo de
> estudio blanco en vez de `#0E1113`, obligando a rondas de regeneración. Andy lo cortó:
> «mejor dejarlo minimalista como quedó todo el branding nuevo, para que no sigas sacando 20
> iteraciones e imágenes innecesarias».
>
> **La lección general, más allá de las cards:** al congelar una dirección nueva hay que
> **barrer todas las secciones que producen assets**, no solo las que se están rehaciendo en
> ese momento. Un residuo de la dirección vieja no se anuncia — se cobra en iteraciones la
> próxima vez que alguien lo ejecuta.

---

## Histórico — direcciones retiradas

- **v3 «editorial cinemática» (2026-07-04 → 2026-07-25).** Negro `#0A0A0A` + Signal Gold
  `#C9A84C`, Playfair Display / DM Sans / Bebas Neue, figura con volumen y rim light dorado
  «como estatua iluminada desde atrás», fondo con el patrón geométrico del universo del
  referente, footer de 5 puntos + 12 íconos. Murió con el giro a 100% pilar SEO: sin referente
  pop, su regla de fondo era inaplicable. Aplicada en EP.019–EP.023.
- **v2 «cómic pulp ilustrado» (2026-07-04).** Descartada el mismo día.
- **v1 «silueta plana en humo dorado» (2026-06-12 → 2026-07-04).** EP.017–019. Andy la calificó
  de genérica: figura única, de frente, parada, silueta lisa sin volumen.
- **og-image editorial (figura + surcos de vinilo).** Retirada 2026-07-23 — dependía de los aros
  concéntricos vetados. `btq-production/artwork-general-v3.md` queda como registro histórico.
