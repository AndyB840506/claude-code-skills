# BTQ — Paquete de metadata v4 (giro a alcance macro)

**Fecha:** 2026-07-25 · **Estado:** listo para pegar en Spotify for Creators.
Nada de esto está aplicado todavía — Claude no tiene acceso a la consola.

---

## A · Assets de marca — tipografía pura

Todos en `E:\AI\outputs\BTQ-brand\`, generados por `comfyui/templates/brand-covers-compose.py`
(determinista, sin ComfyUI — se rehacen con un comando).

| Archivo | Dónde va |
|---|---|
| `BTQ-COVER-q92.jpg` | **Spotify** — portada del show, 3000×3000, 235 KB |
| `BTQ-yt-avatar-800.png` | **YouTube** — foto de perfil |
| `BTQ-yt-banner-2048x1152.jpg` | **YouTube** — banner del canal |
| `BTQ-COVER.png` | master sin pérdida |
| `BTQ-COVER-300.png` / `-96.png` | contrapruebas de legibilidad |
| `BTQ-yt-avatar-800-PREVIEW-circulo.png` | **no subir** — cómo se ve ya recortado en círculo |
| `BTQ-yt-banner-GUIA-safearea.png` | **no subir** — el banner con el área segura dibujada |

Concepto: **el nombre hace el trabajo.** El wordmark ocupa el cuadro en tres líneas y `QUEUE`
va en Señal `#FF3D00` — la palabra *es* la señal, no hay objeto que interpretar. El avatar es
`BTQ` con la Q en Señal, porque el wordmark de tres líneas no sobrevive el recorte circular.

Verificado mirando: legible a 300 y a 96 px; avatar legible a 48 px; el bloque del banner
completo —kicker incluido— dentro del área segura de 1235×338.

> Se descartó la línea de portadas con objeto renderizado (medidor, headset, calibrador, panel
> anunciador). Ninguna se explicaba sola. Los archivos `BTQ-SHOW-COVER-v4*` y
> `BTQ-v4-*` quedan en `E:\AI\outputs\` como descarte — **no subir ninguno.**

---

## B · Descripción del show

```
Behind the Queue es el pódcast en español para quienes dirigen equipos y operaciones. Cada episodio toma una ley, una teoría o un principio real de gestión —la Ley de Goodhart, el Principio de Peter, el efecto Hawthorne— y lo baja al piso: qué significa el lunes por la mañana en su empresa. Casos documentados, cifras verificables, decisiones aplicables. Sin teoría vacía. Conduce Andrés Bermúdez Rodríguez, 15 años en operaciones y experiencia del cliente. Desde Bogotá, para toda Latinoamérica.
```

**497 caracteres** (límite 600).

La descripción vieja prometía "videojuegos, música, cine y operaciones" — promesa que el show
dejó de cumplir hace cuatro episodios.

---

## C · Campos del show

| Campo | Hoy | Nuevo |
|---|---|---|
| Categoría | Culture / Society | **Business → Management** |
| Secundaria | — | **Business → Careers** |
| Kicker de marca | Experiencia · Cultura · Liderazgo | **GESTIÓN · CALIDAD · LIDERAZGO** |

> El nombre exacto de las categorías hay que confirmarlo en la consola de Spotify — la
> taxonomía es la de Apple Podcasts y no la verifiqué contra la interfaz real.

---

## D · Retitulación de los episodios publicados

Fórmula: `EP.NN — [Ancla nombrada]: [qué es, en llano, en usted]`. Prefijo siempre `EP.NN`
con dos dígitos y `EP` en mayúscula; minúscula después de los dos puntos; sin sufijo de marca.

| EP | Título actual en Spotify | Título nuevo |
|---|---|---|
| 11 | `Ep.11 — Frieren: El costo de perder a tu mejor gente sin haberla valorado` | `EP.11 — Frieren: el costo real de perder a su mejor gente` |
| 12 | `EP.12 — Bohemian Rhapsody: La experiencia que nadie pidió y todos recordaron para siempre` | `EP.12 — Bohemian Rhapsody: la experiencia que nadie pidió y todos recordaron` |
| 13 | `Ep.13 — Back to the Future: Doc Brown y el arte de apostar por el que nadie ve` | `EP.13 — Back to the Future: mentoría y el talento que nadie ve` |
| 14 | `EP.14 — MAOMAO: Cuando el talento no tiene título` | `EP.14 — Maomao: cómo detectar talento sin título en su equipo` |
| 15 | `EP.015: Solid Snake — cuando descubres que todo lo que te dijeron era mentira \| Behind the Queue` | `EP.15 — Solid Snake: cuando la información que baja a su equipo es mentira` |
| 16 | `EP.16 — The Wall: El muro que construiste ladrillo por ladrillo` | `EP.16 — The Wall: el muro que se construye entre usted y su equipo` |
| 17 | `EP.17 — Soda Stereo: el liderazgo que sigue sonando cuando ya no estás` | `EP.17 — Soda Stereo: el liderazgo que sigue sonando cuando usted ya no está` |
| 18 | `EP.18 — El Mundial: liderazgo cuando no puedes tocar el balón` | `EP.18 — El Mundial: liderazgo cuando usted no puede tocar el balón` |
| 19 | `EP.19 — Gladiator: el liderazgo que sobrevive al cargo` | *sin cambio* |
| 20 | `EP.20 — Ley de Goodhart: cuando el número deja de medir su call center` | **NO TOCAR — ver abajo** |
| 21 | `EP.21 — Los Simpson: cómo evitar el burnout de tu equipo a largo plazo` | `EP.21 — Los Simpson: cómo evitar el burnout de su equipo a largo plazo` |
| 22 | `EP.22 — La Calidad Es Gratis: el costo real de la mala calidad en su call center` | `EP.22 — Philip Crosby: el costo real de la mala calidad en su empresa` |

### Por qué EP.20 no se toca

Es el único episodio con desempeño medido y bueno, y la razón por la que existe el carril
pilar SEO. Su título contiene "call center", que bajo el giro macro sería inconsistente — pero
esa keyword específica es lo que probablemente lo hizo rankear. **Cambiarlo por prolijidad es
sacrificar el único resultado verificado que tiene el show a cambio de que una tabla se vea
uniforme.** Se deja como está y se acepta la inconsistencia a propósito.

Esto es criterio, no dato: no tengo acceso a las analíticas de búsqueda de Spotify para
confirmar de dónde vino su tráfico.

---

## E · Pendiente de decidir — título de EP.023

El efecto se conoce por el nombre de la fábrica (Hawthorne), no por el del investigador
(Elton Mayo). La regla de título pide el nombre propio al frente, pero aquí los dos compiten:

- `EP.23 — Efecto Hawthorne: por qué su equipo rinde distinto cuando lo miran` — el término
  buscable, pero el nombre no es de una persona.
- `EP.23 — Elton Mayo: por qué su equipo rinde distinto cuando lo miran` — el teórico al
  frente, coherente con Goodhart y Crosby, pero casi nadie busca "Elton Mayo".

Decisión de Andy, pendiente. Ver `guion-style-btq.md` § Título.
