# Handoff: Causa raíz del reproceso — regla de Procedencia
**Date:** 2026-07-23 (jueves)
**Machine:** desktop (E:\)
**Status:** Complete — investigación cerrada, correcciones aplicadas y respaldadas

> Hermano de `2026-07-23-hiresignal-outreach-pendiente-fulfillment.md`. Ese cubre el estado
> de HireSignal; este cubre el proceso. La investigación nació de un error cometido en esa
> misma sesión: se trató un handoff de 6 días como estado actual y se construyó medio día
> de trabajo sobre una premisa falsa.

---

## Qué se investigó

Andrés señaló un patrón: "estamos asumiendo sin verificar y generando reprocesos". Se pidió
fecha de inicio, qué cambió, causa raíz, corrección definitiva y proceso de detección.

## Hallazgos (con evidencia, no inferidos)

**No hay punto de cambio.** La hipótesis natural —transición Fable 5 → Opus 4.8— se descartó:

- Primer incidente evidenciado: **2026-06-19** (teoría de "dos zonas DNS" sobre un `nslookup`
  con caché vieja). Los docs fechan la llegada de Opus el **2026-06-22**: el patrón es anterior.
- Volumen de trabajo plano: junio W22–W24 = 37/31/78 commits; julio W27–W30 = 30/41/35/34.
- Frecuencia plana: ~2 incidentes/semana del 06-19 al 07-23, sin escalón.

**Piso de visibilidad (importante para no sobre-concluir):** el repo de memoria arranca el
2026-07-06 y claude-continuity importó toda la memoria en bloque el 2026-06-25. Cualquier
fecha "2026-06-25" es artefacto de importación, no de autoría. **No hay visibilidad antes del
06-19** — esa fecha es donde empieza lo observable, no necesariamente el patrón.

**Causa raíz:** los 12 incidentes catalogados tienen la misma forma — *confiar en una
representación del estado en vez de mirar el estado*, teniendo la fuente primaria a un comando
de distancia (DoH vs nslookup, el repo destino vs el "OK" del script, el remoto vs el clon, el
artefacto vs el "PASS" del subagente, el calendario vs la fecha copiada, la portada real vs el
perfil, la memoria vs el handoff, `HEAD` vs el disco).

**Por qué las reglas existentes no lo atajaron:** la teoría de la faja y la regla 17 gobiernan
la **salida** (no declarar hecho sin evidencia). `validate_before_theorizing` y la regla 13 sí
tocan la entrada, pero con gatillo de sospecha ("cuando el resultado es raro", "al retomar un
handoff"). **Nada se disparaba cuando el input se veía normal** — y el handoff se veía perfecto.
Por eso 5 semanas agregando reglas no bajaron la tasa: se apilaron en el borde equivocado.

## Correcciones aplicadas

| Dónde | Qué | Commit |
|---|---|---|
| `~/.claude/CLAUDE.md` | **§Procedencia** (borde de entrada): nombrar fuente y antigüedad antes de usar un dato como hecho; abrir la primaria si decide algo; parar si dos fuentes chocan. Acotada a inputs que DECIDEN, para no chocar con reglas 11 y 15 | sync `b1c9a46` |
| `~/.claude/CLAUDE.md` regla #13 | Comprimida a instancia de §Procedencia (dejó de duplicar) | sync `b1c9a46` |
| `~/.claude/CLAUDE.md` regla #8 | Corregida: afirmaba que la memoria "se carga en cualquier workspace" — es falso, es por workspace-slug | sync `9d1fd9a` |
| `retrospective/workflows/extract-and-apply.md` | Chequeo obligatorio y primero: *"¿qué artefacto reescribí hoy tras darlo por bueno?"* — contar y nombrar el input asumido; reportar aunque sea 0 | `5fd49b3` |
| `feedback_validate_before_theorizing` | Marcada como instancia de §Procedencia | local |

## Métrica de si funciona

El retrospective ahora reporta un número por sesión. Referencias: **2026-07-23 = 4 reprocesos
en una sesión**; ~2/semana entre 06-19 y 07-23. Dos sesiones seguidas en 0 = la regla sirve.

## Notas / Gotchas

- **§Procedencia es de ENTRADA, la faja es de SALIDA.** No fusionarlas ni "simplificar" una
  dentro de la otra: el diagnóstico fue precisamente que sobran reglas de salida.
- **No agregar más reglas de "verificar más"** ante el próximo incidente. Ya hay cinco. Si
  §Procedencia falla, el arreglo es hacerla disparar más temprano, no apilar otra.
- `Measure-Object -Line` en PS 5.1 **no cuenta líneas en blanco** — dio 28 donde `wc -l` daba
  36. Para conteos de líneas usar `wc`, o se reportan truncamientos inexistentes.
- CLAUDE.md carga en cada sesión: §Procedencia se comprimió de 20 a 14 líneas a propósito.
  Archivo hoy en 147 líneas. Al agregar reglas ahí, pesar el costo de contexto permanente.

## Next Steps

1. Nada obligatorio — la investigación está cerrada.
2. Pendiente menor arrastrado: **solapamiento de triggers entre las 28 skills nunca se
   verificó** (el paso 2 del session-close del 07-23 lo declaró explícitamente no revisado).
3. Al cerrar la próxima sesión, mirar el número que reporte el retrospective.
