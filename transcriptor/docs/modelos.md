# Comparativa de modelos Whisper

## Tabla de referencia

| Modelo | Tamaño descarga | RAM necesaria | Velocidad* | Calidad |
|--------|----------------|---------------|------------|---------|
| tiny   | 39 MB          | ~1 GB         | ~32x       | Básica — errores frecuentes en vocabulario técnico |
| base   | 74 MB          | ~1 GB         | ~16x       | Aceptable — buena para voz clara sin acento |
| small  | 244 MB         | ~2 GB         | ~6x        | Buena — suficiente para reuniones y podcasts |
| **medium** | **769 MB** | **~5 GB**  | **~2x**    | **Muy buena — default recomendado** |
| large  | 1.5 GB         | ~10 GB        | ~1x        | Excelente — máxima precisión, vocabulario técnico |

*Velocidad relativa al tiempo real en CPU. `32x` = 1 hora de audio tarda ~2 minutos.

---

## Cuándo usar cada modelo

**`small`** — Para transcripciones rápidas de audios cortos (<30 min), cuando la precisión exacta no es crítica. Bueno para notas de voz personales.

**`medium`** (default) — Para la mayoría de los casos: reuniones, podcasts, entrevistas, clases. Buen balance velocidad/precisión.

**`large`** — Cuando necesitas máxima precisión: vocabulario técnico, nombres propios, múltiples acentos, audio de baja calidad.

---

## Sobre la velocidad en CPU vs GPU

Los tiempos de la tabla asumen **CPU**. Con una GPU NVIDIA compatible (CUDA):

- Los tiempos se reducen entre 5x y 20x
- Requiere pasar `--device cuda` explícitamente en el comando
- Si `--device cuda` no se pasa, whisper usa CPU por defecto

Si el audio de 1 hora tarda más de 30 minutos con `medium`, considerar `small` o verificar si la GPU está siendo utilizada.

---

## Primera descarga

La primera vez que se usa un modelo, Whisper lo descarga desde Hugging Face y lo guarda en:

```
C:\Users\[usuario]\.cache\whisper\
```

Las descargas posteriores usan el modelo en caché — no se vuelve a descargar.
