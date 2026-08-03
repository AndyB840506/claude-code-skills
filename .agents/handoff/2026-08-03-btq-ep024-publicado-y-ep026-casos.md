# Handoff: EP.024 publicado y cerrado, EP.026 con los tres casos verificados

**Date:** 2026-08-03 (lunes)
**Machine:** desktop (E:\) — el audio y el artwork de EP.024/EP.026 viven ahí
**Status:** In progress — EP.024 cerrado; EP.026 listo para escribir guion; EP.027 pendiente de rediseño

---

## What We Accomplished This Session

**EP.024 — publicado y cerrado**
- Andy publicó el episodio. La URL provisional resultó ser la definitiva: verificada con
  **HTTP 200** y `og:title` idéntico al título del episodio.
- Propagada a los 2 CTAs del artículo y a la home; tracklist rotado a 023 · 022 · 021 · 020
  (salió EP.019). Desplegado y **verificado en vivo**, no en local.
- **Artículo nativo de LinkedIn** creado, publicado por Andy y corregido:
  `https://www.linkedin.com/pulse/mi-puerta-siempre-est%C3%A1-abierta-por-qu%C3%A9-nadie-la-cruza-andres-zdtie`

**Tres reglas de estilo pedidas por Andy, ya escritas donde se generan los assets**
- Los posts del plan social van en **bloque de código**, no en cita de bloque: con `>` al
  inicio de cada línea el carácter se arrastra al copiar.
- **Comillas rectas `"…"`, nunca angulares**, y la **raya `—` no se usa como conector ni como
  inciso**. Retrofiteado el artículo del sitio: 24 pares de angulares y 27 de 40 rayas
  reescritas una por una, desplegado y verificado en vivo.
- **Techo de título: 70 caracteres y 9 palabras de ancla.** Medido: todo el catálogo post-giro
  vive entre 46 y 70.

**Roadmap — tres bloques nuevos**
- **Vetas del cliente** (A: el proceso nació torcido · B: la política se cambió para ahorrar),
  con prioridad regional y los reguladores de consumo (SIC, SERNAC, PROFECO, Procon) como
  fuente primaria. **No es carril nuevo:** se espera a que la rotación 3+1 dé una vuelta.
- **Filtro de 5 compuertas** para temas de sugeridor externo, con los sobrevivientes de las dos
  tandas ya evaluados.
- **EP.026 fijado** (carga cognitiva) y **EP.027 pasa a rediseño de guion**.

**EP.026 — los tres casos cerrados contra fuente primaria**
Ver `pipeline-state-ep026.md`. TMI (Kemeny), Avianca 052 (NTSB/AAR-91/04) y Keystone ICU
(NEJM 2006, vía el repositorio de Johns Hopkins), con citas literales.

---

## Where We Paused

**Last action:** auditoría del kit aplicada (la receta de `pymupdf` quedó en un solo sitio).

**Next action:** abrir la fuente primaria de la teoría de carga cognitiva (Sweller) — es el
último pendiente del EP.026 — y arrancar el guion con esqueleto E.

**Blockers:** ninguno. Los tres casos están verificados y el título está fijado.

---

## Files to Read First

- `btq-production/pipeline-state-ep026.md` — **empezar por aquí.** Los tres casos con sus citas
  literales, el título, los aterrizajes obligatorios y la instrucción sobre el caso Avianca.
- `btq-production/roadmap-btq.md` — la tabla de cupos, las vetas del cliente y el filtro de
  temas. Creció ~166 líneas hoy.
- `btq-production/pipeline-state-ep027-peter.md` — para el rediseño del guion de Peter.

---

## Notes / Gotchas

- **⚠️ EP.027 no está listo aunque el roadmap diga «grabado».** Falla la compuerta de contenido
  aplicable: **13,9%** medido contra el **≥25%** que exige `guion-style-btq.md`. Andy decidió
  rediseñar el guion sobre el formato del EP.024 (esqueleto E) y **acepta regrabar completo** —
  reestructurar no son dos parches, son 42 minutos de voz otra vez. El teaser grabado anuncia la
  Ley de Little como «el episodio siguiente», y con Little en EP.031 esa promesa quedó corrida
  cuatro semanas.
- **⚠️ Contradicción sin resolver entre dos documentos.** `pipeline-state-ep027-peter.md` dice
  «NO verificado: los £827 millones exactos» de Barings; el `CLAUDE.md` global dice que el
  2026-07-31 se encontró la cifra en el blog del personal del Banco de Inglaterra, y que la
  fuente dice «twice» donde el guion decía «más del doble». Uno de los dos está viejo. **Abrir
  la fuente al tocar ese guion.**
- **El siguiente cupo de pilar SEO es EP.035, no EP.032.** Se afirmó mal dos veces hoy. La
  rotación se cuenta contra la tabla: 024-026 Oficio → 027 pilar; 028-030 → 031; 032-034 → 035.
- **El informe de la NTSB se equivoca en su propia primera página:** el sumario ejecutivo dice
  «July 19, 1989» y la portada dice el 25 de enero de 1990, que es la fecha real. Si se usa al
  aire como ironía, hay que explicarlo o parece error nuestro.
- **La cifra del 66% de Keystone estaba mal atribuida en el tiempo** en todos los resúmenes de
  búsqueda: el 66% es a los **16-18 meses**; a los 0-3 meses la reducción es del **38%**.
- **Los PDF oficiales vienen escaneados** y ni WebFetch ni `pypdf` sacan nada de ellos. Se
  instaló `pymupdf`. Receta en `skills/CLAUDE.md` § instrumentos que mienten en silencio.
- **`guion-style-btq.md` llegó a 1.046 líneas** — tercera auditoría seguida que lo señala.
  Partirlo sigue aplazado a propósito.

---

## Questions to Answer

- **Pendiente abierto del EP.026:** abrir la fuente primaria de Sweller sobre carga cognitiva.
  Es el único `[ ]` que queda en `pipeline-state-ep026.md`.
- La cifra de «más de 1.500 vidas y ~USD 175 millones» de Keystone **no está en el abstract**.
  Si se quiere decir al aire, hay que encontrar de dónde sale.
- ¿Qué herramienta produjo las sugerencias de temas? Si genera con un modelo en vez de consultar
  datos de búsqueda, no trae señal de demanda y el argumento SEO para adoptarlos se cae.
  Anotado como pendiente en `roadmap-btq.md`.
- El post de LinkedIn del **martes 4 de agosto** sigue sin publicar, ya con la puntuación nueva.
- **Machine-bound:** el audio, el SRT, las portadas y las quote cards de EP.024 y EP.027 están
  en `E:\` — no existen desde el portátil.
