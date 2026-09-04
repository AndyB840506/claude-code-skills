# Estilo Visual — Portadas de Artículo

Calibrado 2026-09-04. Genera portadas con ComfyUI (skill `comfyui`) para cada artículo.

## Estilo (confirmado por el usuario)
**Abstracto/conceptual** — formas, texturas o composiciones geométricas ligadas a la
idea central del artículo. Explícitamente NO fotorrealista: los modelos locales
fotorreales (bigASP) producen el típico "stock photo corporativo de IA" (gente de
traje, luces genéricas) que se lee como generado por IA — contradice el objetivo de
`docs/anti-patrones-ia.md`. NO usar sd_xl_base/bigASP para estas portadas.

## Modelo y formato
- **Z-Image Turbo** (`comfyui/templates/zimage-txt2img-api.json`), natural-language
  prompt (subject + action + setting + lighting + camera/style) — ver
  `comfyui/docs/prompting.md`.
- Sin personas en escena: evita de raíz los problemas de anatomía/etnia/proporciones
  documentados en el prompting guide de comfyui para figuras humanas.
- Tamaño: **1200×630** (ratio de portada de artículo/link preview de LinkedIn),
  generado nativo, sin upscale — no es resolución de impresión.
- Paleta: reusar los tokens del artifact del artículo (`--accent` teal, `--flag`
  ámbar u otro par que se elija ese día) para que portada y página se vean como un
  mismo objeto, no dos piezas sueltas.
- Concepto: derivar la imagen de la tesis/metáfora central del artículo (ej.
  "La Proyección Sin Dueño" → línea de proyección que se rompe y cae en un vacío),
  nunca un ícono genérico de "liderazgo" (apretón de manos, bombilla, engranajes).

## Procedimiento
1. Identificar máquina (`Get-PSDrive` — `E:` existe = desktop, si no = portátil `D:`)
   y sustituir la raíz (`E:\AI` / `D:\AI`) en todo lo siguiente.
2. `curl -s -m 3 http://127.0.0.1:8188/system_stats` — si responde, saltar el paso 3.
3. Si no responde: lanzar el servidor con **PowerShell** (no Bash — mangla backslashes
   en rutas de Windows), comando en `comfyui/docs/stack-reference.md` § Launch,
   sustituyendo la raíz. Esperar con
   `curl -s --retry 40 --retry-delay 3 --retry-connrefused --retry-all-errors .../system_stats`
   y confirmar que `devices[0].name` trae la GPU correcta.
4. Encolar con el template Z-Image (POST `/prompt`), poll `/history/<id>` hasta
   `status.status_str == "success"`.
5. **Verificar visualmente con Read** (regla de la faja) antes de seguir — nunca
   asumir que "success" significa que la imagen sirve.
6. Copiar el PNG final a `C:\Users\andre\repos\linkedin-articulos\` (el archivo real
   que el usuario sube a LinkedIn — un artifact no permite descargar, así que el
   archivo en disco es la entrega real, no solo la vista previa embebida).
7. Embeber la portada en el artifact **sin hacerla pasar por el contexto de la
   conversación**: la codificación base64 de una imagen de ~600 KB son ~800.000
   caracteres — pasarla por un parámetro de tool call es un desperdicio de contexto
   enorme. Construir el HTML final enteramente dentro de un comando de Bash (`head` +
   `base64 -w0` + `tail`, ver ejemplo abajo), nunca imprimiendo el base64.
   `list_types`/`upload_asset` del Artifact tool requiere la capacidad `assets`, que
   **no está disponible para este usuario** (verificado 2026-09-04 vía
   `artifact-capabilities` — lista completa: artifact, db, downloads, mcp, room,
   sample, self) — por eso el método es base64 inline, no `upload_asset`. Si en el
   futuro `assets` aparece disponible, preferirlo sobre base64 (evita el peso del
   archivo publicado).

```bash
F="ruta/al/articulo.html"
IMG="C:/Users/andre/repos/linkedin-articulos/YYYY-MM-DD-slug-cover.png"
LINE=$(grep -n "<h1>" "$F" | head -1 | cut -d: -f1)
head -n $((LINE-1)) "$F" > "$F.new"
{ printf '  <img class="cover" alt="..." src="data:image/png;base64,'; base64 -w0 "$IMG"; printf '">\n'; } >> "$F.new"
tail -n +$LINE "$F" >> "$F.new"
mv "$F.new" "$F"
```

## Nota de infraestructura
El servidor de ComfyUI no queda corriendo entre sesiones — cada invocación de esta
skill que necesite portada debe repetir el check/lanzamiento del paso 2-3. No asumir
que sigue arriba de una sesión anterior.
