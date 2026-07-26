EPISODE: EP.023 (BTQ)
stage_a: complete — reescrito y verificado 2026-07-25. Listo para grabar.
stage_b: in_progress — grabado y transcrito 2026-07-25. Las quote cards se componen aquí, contra la TRANSCRIPCIÓN real, nunca contra el guion.

## Grabación — 2026-07-25

- Audio: `E:\Podcast\BTQ\EP 23\BTQ EP 23.mp3` (33,5 MB, 34:56 totales) + sesión Reaper `.rpp`.
- Transcripción: `E:\Transcriptor\transcripciones\BTQ EP 23.srt` — WhisperX large-v2, es,
  diarización, exit 0. 336 cues, UTF-8 sin BOM, un solo speaker.
- **Duración real: 33,77 min de habla efectiva** (5.017 palabras a 148,6 wpm), contra los
  40,0 min proyectados. **Andy aceptó publicar así** — el estándar 40-45 queda roto una vez.
- Causa (diagnóstico de Andy): al fusionar dentro del cuerpo los segmentos que antes iban
  sueltos, se asumió que el guion conservaba las palabras del original. Las costuras entre
  segmentos separados eran donde ocurría la expansión en vivo. Expansión real **+13,4%**
  contra el +35,5% asumido. Recalibrado en `guion-style-btq.md` § Calibración de duración.
- Hueco de 18,1 s entre 0:15 y 0:33 → slot del jingle de entrada, limpio.
- **Solo 0,59 s de silencio en cabeza** (el checklist pedía 3 s). Se resuelve insertando el
  silencio en Reaper al montar el stinger; no requiere regrabar.
- Teaser de EP.024: improvisado sobre el `[PENDIENTE DEFINIR]` — quedó genérico a propósito
  («todavía no le puedo decir cuál porque ni yo la tengo cerrada»). El tema sigue sin definir.
- WhisperX transcribe el nombre del show como «Behind the Cue» / «Behind the Cube» (3 veces).
  Es artefacto de transcripción —*Queue* es homófono de *cue*—, no un error de pronunciación:
  corregir solo si el SRT se publica como subtítulos.
stage_c: pending
spotify_url: pending

## Título — FIJADO 2026-07-25 (decisión de Andy)

```
EP.23 — Efecto Hawthorne: por qué su equipo rinde distinto cuando lo miran
```

73 caracteres. Va IDÉNTICO en portada, Spotify y YouTube. Gana el término buscable sobre
el teórico (Elton Mayo) porque el modelo aprobado no es «el teórico a secas» sino
*[tipo] de [nombre propio]* — igual que `Ley de Goodhart`. Precedente en
`guion-style-btq.md` § Título.

## Guion — REESCRITO 2026-07-25, esqueleto INVERTIDO

**Motivo.** EP.020/021/022/023 salieron con el MISMO esqueleto de 9 segmentos. Andy:
«ya en 3 episodios con los mismos chistes pedorros tampoco» y «las recomendaciones se
pueden tornar como el aviso de cierre y no se termine de consumir el episodio».

- **Abre con el desmentido** de Levitt & List (2011), que antes estaba enterrado en el
  segmento 5 como «re-enganche». El mejor material del episodio dejó de ser relleno
  estructural y pasó a ser la premisa.
- **ELIMINADA la escena de apertura compuesta** («Julián, analista de calidad»).
  Contradecía en el primer minuto la promesa del show —«casos documentados, cifras
  verificables»—. La sustituye el reconocimiento del fenómeno con señales operativas
  reales, verificables en el tablero del propio oyente.
- **Recomendaciones TEJIDAS, sin bloque:** Cuddy en el segmento 1 (su «power posing»
  tuvo la misma crisis de replicación), el libro de Mayo en el 3, The Truman Show en el 5.
- Segmentos nombrados por su contenido; cero `Cuerpo N`, cero `Re-enganche`.
- Remates recortados de 10 a 4 (regla 2 de chispa: máx 3-4).
- **Cierre autoconsciente nuevo:** el episodio se aplica a sí mismo la desconfianza con
  la que abre. Amarra el esqueleto invertido.

**Contenido y fuentes:** sin cambios de fondo — efecto Hawthorne (Hawthorne Works de
Western Electric, iluminación 1924-27, cuarto de relés 1927-32, cuarto de cableado y el
«bogey»), término acuñado por Landsberger en 1958, reanálisis de Levitt & List (2011),
Volkswagen Dieselgate, panóptico de Bentham (1785), higiene de manos observada vs
encubierta. Todo en el bloque «Fuentes verificadas» del propio guion. La reescritura
**incorporó cifras que ya estaban verificadas pero se estaban usando en vago**: 40× el
límite de NOx, ~60 muertes prematuras en EE.UU. además de las ~1.200 en Europa, y el
78-87% vs 45-55% del lavado de manos.

**LINTS — todos corridos DESPUÉS de la reescritura:**

| | |
|---|---|
| `lint_guion_repeticion.py` | **PASS** — cero 6-gramas compartidos (antes: FAIL con 28) |
| Español neutro | 0 en las 5 categorías · tuteo 0 |
| Muletillas | `imagínense` 0 · disclaimer de cajón 0 · «Andy» 3ª persona solo en la firma |
| Cierre canónico | las 7 piezas presentes |
| Duración | 4.425 palabras escritas → **40,0 min** (rango 40-45) |
| Alcance | call center 0 · BPO 0 · equipo 8 · operación 7 · empresa 4 |

**Artifact para revisión:** https://claude.ai/code/artifact/96f22190-affa-4f54-854c-5e05135ba1e4

## Artwork — REHECHO 2026-07-25, tipografía pura

Generador: `comfyui/templates/portada-ep-compose.py` (determinista con PIL, sin ComfyUI).
Salidas en `E:\AI\outputs\BTQ-EP023\` — COVER-1x1 / 16x9 / 9x16 + jpg + contrapruebas
300/96.

```
python scripts/verify_assets.py EP023 --root E:\AI\outputs\BTQ-EP023 --show btq --stage-a
   → PASS en los 3 aspect ratios, negro de marca OK
```

Los tres inspeccionados visualmente. El 9:16 se ve sparse —inherente a la tipografía pura
en un lienzo tan alto—; pendiente el juicio de Andy.

> ⚠️ **MUERTO, no revivir:** el concepto v3 (foco incandescente vintage + headset +
> waveform dorado, test `E:\AI\outputs\BTQ-EP023-bulb-v1_00001_.png`) murió con el giro a
> tipografía pura. También muere `launch-assets/EP023-hawthorne-artwork-v3.md`.
> El oro ya no es color de marca.

## Audio

Se retiró la música de intro/outro: va un jingle corto, el mismo al abrir y al cerrar
(`btq-production/jingle-brief.md`). **No bloquea la grabación** — se monta en post.
Andy debe dejar 3 s de silencio en cabeza y cola, y grabar 30 s de room tone.

## Pendiente

- Grabación (Andy).
- Tema de EP.024 sin definir: el teaser del cierre queda genérico a propósito.
