# Roadmap — Behind The Queue (BTQ)

Fuente de verdad de "qué episodio sigue". `episode-pipeline` la lee al arrancar
Stage A (`00-roadmap.md`) y la actualiza al cerrar cada macro-stage.

Estados posibles: `en roadmap` → `guion listo` → `grabado` → `en Spotify` → `publicado`

| EP | Título | Estado |
|---|---|---|
| EP.011 | Frieren | publicado |
| EP.012 | Bohemian Rhapsody | publicado |
| EP.013 | Back to the Future | publicado |
| EP.014 | Maomao | publicado |
| EP.015 | Solid Snake (Metal Gear Solid) | publicado — https://open.spotify.com/episode/6fpGqMqaLozmWB4ABOlO3S |
| EP.016 | Pink Floyd / The Wall | grabado — guion listo, pendiente subir a Spotify |
| EP.017 | Soda Stereo / Cerati | en roadmap |

---

**Notas:**
- Seeded desde memoria `btq_production_state` (snapshot 2026-06-02) + corrección de
  estado de EP.016 (recording + script confirmados listos por el usuario, pendiente
  publicar en Spotify — 2026-06-07).
- Mantener esta tabla actualizada manualmente o vía `episode-pipeline` — es la fuente
  que Stage A consulta para decidir cuál episodio sigue.
