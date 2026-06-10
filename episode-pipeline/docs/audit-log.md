# Bitácora de auditoría y archivo de estado

Stage A crea ambos archivos por episodio, guardados en la carpeta de producción del
show correspondiente (`btq-production/` o `mrputridsden-production/episodios/`):

- **`pipeline-audit-ep[NNN].md`** — registro auditable; cada stage agrega su entrada
  documentando regla verificada, qué se inspeccionó, resultado (pass/fail) y notas
- **`pipeline-state-ep[NNN].md`** — checkpoint vivo; cada macro-stage lo actualiza al
  cerrar (`stage_a/b/c: complete` + `spotify_url`) — es lo que el Routing — Paso 0 lee
  para saber dónde retomar

Formato de entrada:
```
## Stage N — [nombre]
- Qué se hizo: [resumen]
- Archivos generados/modificados: [rutas]
- Validaciones (si aplica):
  - [regla] → [pass/fail] → [detalle]
- Resultado: [OK / pendiente de aprobación / bloqueado]
```
