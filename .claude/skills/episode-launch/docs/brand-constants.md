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
   el giro al 60 %.
4. El ritual: «Buenas y santas…», el cierre canónico, las recomendaciones de Andy.
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
> Lo de abajo (escena, prompts, upscale) queda como **registro** de la etapa de objeto y sigue
> aplicando a las **quote cards**, que sí llevan escena. Si Andy quiere llevarlas también a
> tipografía pura, es una decisión aparte que no se ha tomado.

**BTQ = el piso de operación como cuarto de máquinas.** Grafito y acero como mundo, luz plana de
taller, y **una sola luz de señal encendida** — el naranja que en una planta significa «mire
esto». Un objeto por episodio, nunca un collage.

### Reglas de la dirección

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
   **Pueden colarse disfrazados de textura** — en EP.022 una tela salió cubierta de mini-círculos,
   invisible a tamaño completo y detectada solo al hacer zoom a una esquina. Verificar con zoom a
   las esquinas, no en la vista general.
6. **Cero IP de terceros** en la portada del show: sables, escudos, prismas, logos ajenos. La
   portada 2026 los tenía y es parte de lo que se está corrigiendo.
7. **Sin proporciones chibi. Sin estilo cartoon. Sin circuit boards.**

### Bloque de escena (copiar verbatim, cambia solo el objeto)

```
Dark industrial editorial image, rendered with real volume and material
texture (steel, glass, bakelite, worn enamel) — NOT a flat silhouette
cutout, NOT a glossy 3D render. Background #0E1113, graphite panel tone
#22262A.

Center composition: [OBJETO LITERAL DEL EPISODIO], shot straight on,
lit by flat overhead workshop light. Cool steel greys, matte surfaces,
honest wear. Exactly ONE element glows in signal orange #FF3D00 —
[cuál elemento]. No other warm light anywhere.

Background: a fine vertical line grid, like the ventilation slots of an
equipment panel, in #1F2428 — subtle, engraved, never competing with
the object.

DO NOT render any concentric ring, circle, halo, or archery-target
pattern anywhere in this image.

No circuit boards. No cartoon style. No golden rim light. No text.
```

**El modelo NO escribe texto.** La escena se genera limpia; wordmark, kicker, título y `EP.NN`
se componen después con PIL.

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

Esto retira el sustituto **Impact** que se venía usando desde EP.022 porque Bebas Neue nunca se
instaló. Ya no hace falta.

### Formatos

1. **1:1 — 3000×3000 real** (mínimo de plataforma). Generar nativo a 1024×1024, escalar ×4 con
   `RealESRGAN_x4plus.pth` vía ComfyUI (`UpscaleModelLoader` + `ImageUpscaleWithModel`) y
   remuestrear a 3000. El modelo se instaló el 2026-07-25 en
   `E:\AI\ComfyUI_windows_portable\ComfyUI\models\upscale_models\` — antes de esa fecha la
   documentación lo daba por hecho y la carpeta estaba vacía.
   **Componer la tipografía a 3000 nativo, nunca escalar el texto.**

**Portada del SHOW** (no de un episodio): `comfyui/templates/show-cover-compose.py`. No lleva
título ni `EP.NN` — solo wordmark, regla y kicker; el objeto representa al programa entero.
**Versión vigente (aprobada 2026-07-25): panel anunciador** — la rejilla con la que se vigila
una planta entera. Seis ventanas rectangulares apagadas, una encendida en `#FF3D00`. Muchos
indicadores, uno que importa: gestión a cualquier escala, sin pertenecer a una industria.
Ventaja adicional: **cero geometría circular**, así que el veto de anillos no queda en zona gris.
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

- [ ] Volumen y textura de material real, no silueta plana ni render 3D brillante
- [ ] Exactamente UN elemento en `#FF3D00`
- [ ] El acero `#39434A` está presente — la imagen no es «negro con un acento»
- [ ] Cero anillos/círculos/dianas — **verificado con zoom a las cuatro esquinas**
- [ ] Fondo negro real `#0E1113`, no `#000000`
- [ ] Texto letra por letra, con tildes
- [ ] Legible a 300×300 y a 96×96 — generar los reescalados y mirarlos

---

## Quote Cards — mismo mundo, split 50/50

Formato **16:9 (1920×1080)**, mitad negra con texto / mitad escena. Escena vía ComfyUI, texto
compuesto determinista con PIL (`comfyui/templates/quote-card-compose.py`). Citas verbatim
validadas contra el SRT real. Procedimiento compartido para los 3 shows en
`episode-pipeline/workflows/03b-marketing.md`.

- **Escena:** mismo bloque industrial de arriba — luz plana de taller, un objeto que ilustre la
  cita, un solo elemento en señal. *No* el render cinematográfico con glow de v3.
- **Tipografía:** cita en Supreme Bold cream, atribución en Martian Mono `#FF3D00`. Tamaño de la
  cita dinámico: arranca en 72px y baja de 2 en 2 hasta que el bloque envuelto quepa en el alto
  disponible; la atribución es ~34% del tamaño final de la cita.
- **Fondo propio por card**, desenfocado y distinto en cada una, coherente con el mundo del
  episodio — sin repetir elemento entre las 4 cards.
- **Sin anillos.** Aplica el mismo veto y la misma verificación con zoom.

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
