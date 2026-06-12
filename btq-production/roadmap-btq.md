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
| EP.016 | Pink Floyd / The Wall | publicado — https://open.spotify.com/episode/3CNyTkA6OCLoCrmNEh0LVR |
| EP.017 | Soda Stereo / Cerati | en roadmap |

---

## Estrategia editorial (data-driven — analytics Spotify 2026-06-12)

**Audiencia núcleo (verificada):** hombre 35–44 (43% del total; 56% sumando todo el rango),
Colombia 70% + EE.UU. 20%, escucha en Android y ~15% en desktop Windows (en el trabajo).
Perfil: supervisor/gerente de BPO de ~40 años.

**Reglas para elegir y titular episodios:**

1. **Referentes 80s/90s primero** — rock clásico, rock en español, cine de esa era.
   Evidencia: EP.012 Queen = 40 plays (mejor de la era pop-culture) y el algoritmo lo
   empuja solo (149 impresiones Home); EP.015 Solid Snake = 11 plays (peor del catálogo).
   Gaming/anime nicho: con moderación, no consecutivos.
2. **Un episodio pilar SEO al mes** — título keyword-first estilo EP.01–09 (sin referente
   pop). Razón: la adquisición de oyentes nuevos cayó de ~30/mes (marzo) a ~4/mes (junio);
   EP.01 sigue siendo #1 all-time en consumo gracias a Search (193 de 245 impresiones).
   Los episodios pop-culture ganan el algoritmo pero son invisibles en el buscador.
3. **Fórmula de título pop-culture:** `EP.XX — [Referente]: [frase con keyword BPO /
   liderazgo / call center]`. El gancho emocional se queda, pero el título SIEMPRE lleva
   al menos una keyword buscable.
4. **Numeración consistente:** `EP.XX` (dos dígitos, mayúsculas, guion largo). Nunca
   "Ep.11", "EP.015" ni sufijo "| Behind the Queue" en el título de Spotify.
5. **Cadencia semanal estricta — nunca menos de 7 días entre episodios.** Lección
   EP.015: salió 4 días después del EP.014 y quedó como el episodio más flojo del
   catálogo (11 plays).

**Candidatos sugeridos post-EP.017** (mismo perfil nostalgia 35–44, pendientes de
aprobación de Andres): Metallica, Matrix, Los Simpson, Star Wars, Back to the Future ya
usado — y un pilar SEO entre cada 3–4 pop-culture.

---

**Notas:**
- Seeded desde memoria `btq_production_state` (snapshot 2026-06-02) + corrección de
  estado de EP.016 (recording + script confirmados listos por el usuario, pendiente
  publicar en Spotify — 2026-06-07).
- Mantener esta tabla actualizada manualmente o vía `episode-pipeline` — es la fuente
  que Stage A consulta para decidir cuál episodio sigue.
