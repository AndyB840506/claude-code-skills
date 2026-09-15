# Workflow — compuerta de QA

El contrato mecánico no se revisa a ojo. Un lote de 200 filas "se ve bien" incluso
cuando la fila 137 perdió un `</i>`.

## Correr el validador

```powershell
python scripts\qa_localizacion.py <carpeta>\trabajo.json
```

Para escribir además la columna final (solo lo hace si no hay errores):

```powershell
python scripts\qa_localizacion.py <carpeta>\trabajo.json --salida <carpeta>\salida-es.txt
```

**Pegar la salida real del script en la respuesta al usuario.** No parafrasearla, no
resumirla como "corrió limpio". El código de salida es 1 si hay errores.

---

## Qué revisa

| Check | Nivel | Qué detecta |
|---|---|---|
| `vacio` | ERROR | El inglés tiene texto y el español quedó vacío |
| `espacios` | ERROR | Espacio al inicio/final de celda, o espacio doble interno |
| `saltos` | ERROR | Cantidad de saltos de línea distinta a la del inglés, o `\r` |
| `puntuacion` | ERROR | La puntuación final no espeja la del inglés |
| `tags` | ERROR | Los tags `<i>`, `</b>`, etc. no coinciden en cantidad u orden |
| `placeholders` | ERROR | `(GG)`, `{var}`, `[TOK]`, `%s`, `$VAR` perdidos o alterados |
| `espacio-signo` | ERROR | Espacio antes de `!?;:` — norma francesa, no española |
| `consistencia` | ERROR | El mismo string inglés traducido de dos formas distintas |
| `filas-cola` | ERROR | Filas vacías al final del lote |
| `regionalismo` | AVISO | Jerga local que rompe el neutro, **venga del país que venga** — mexicanismos incluidos (`chingar`, `pinche`, `güey`, `pendejo`), españolismos, voseo, colombianismos. Incluye `coger`, ambiguo en todo el continente |
| `signos` | AVISO | `¿` o `¡` sin cerrar — esperable en este proyecto, confirmar |
| `largo` | AVISO | Expansión mayor a +40% — revisar si es string de UI |

Todos los checks de vocabulario son **aviso, nunca error**: el validador no conoce el
contexto de la escena y una palabra marcada puede ser la correcta.

---

## Qué hacer con cada nivel

**ERROR** — corregir en `trabajo.json` y volver a correr. No se entrega con errores
abiertos. Estos son exactamente los fallos que el cliente describió como rompedores
del build.

**AVISO** — decidir caso por caso y **explicar la decisión al usuario**. Un aviso
descartado se menciona ("la fila 12 abre `¿` sin cerrar porque el inglés no cierra —
es la convención del proyecto"), no se omite en silencio.

---

## Límites del validador — lo que NO revisa

Decirlo importa: un "0 errores" cubre el contrato mecánico, no la calidad.

- **No juzga si la traducción es correcta ni natural.** Eso es lectura humana.
- **No detecta un placeholder bien copiado pero mal ubicado** en la frase.
- **No conoce el límite real de caracteres de la UI del juego** — el check de largo
  es una heurística, no la restricción del motor.
- **No valida los nombres propios** contra un glosario del proyecto.
- **No sabe si un chiste funciona.** Eso lo decide la prueba del lector monolingüe
  (`docs/adaptacion-creativa.md`), que es humana y va antes de correr el script.

Para eso está la página (`page/columna-es.html`): pone los pares EN/ES lado a lado y
permite corregir en línea.

**La página corre sus propios checks, escritos en JavaScript — no son estos.** Son dos
implementaciones independientes del mismo contrato, y eso es deliberado: cruzar un
conteo con una segunda herramienta es más fuerte que confiar en una sola. **Si los dos
no coinciden, hay un bug en alguno de los dos — investigar, no elegir el que más
guste.** El riesgo conocido es que se separen en silencio al editar solo uno: al tocar
un check aquí, tocar también el de `page/columna-es.html`, y al revés.

Por eso el bloque de Consultas y el de Adaptaciones son parte del entregable, no un
adorno: son lo que el script no puede cubrir.
