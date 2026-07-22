# Lockup tipografico de Mr. Putrid's Den - TEMPORADA 2 ("La Guarida").
#
# Reemplaza al lockup de Temporada 1 (mpd-portada-compose.py, que sigue vigente para
# el archivo de T1). Diferencias, todas motivadas por defectos medidos:
#   - Serif de epoca (Bookman Old Style) en vez de Impact. Impact es una condensada de
#     cartel moderno; no lee victoriana y contradice la direccion serif del specimen.
#   - Scrim en degradado arriba y abajo. El defecto real de la v1 era contraste, no fuente:
#     el wordmark blanco caia sobre marmol claro y desaparecia a 150px (tamano real en
#     Spotify). Ninguna tipografia arregla eso; el scrim si.
#   - Sin los 5 puntos y sin "MPD" en rojo: ambos se vuelven ruido ilegible en miniatura.
#   - Footer reducido a los iconos de plataforma. El texto del nombre y el numero de
#     temporada estaban duplicados con el bloque principal.
#
# Uso: python mpd-lockup-t2.py            (usa los valores de la portada de temporada)
#      from mpd_lockup_t2 import compose  (recomendado: evita perder tildes por shell)
import math
import sys
import textwrap
from PIL import Image, ImageChops, ImageDraw, ImageFont

# Paleta del sistema T2. Deriva de la escena real (marmol, cuero, fuego, whisky),
# no del specimen de carretera que quedo obsoleto con el codename interno.
#
# OJO: esta constante NO es el "Medianoche #0B1A39" de la paleta. Es el casi-negro
# calido de la franja de iconos. Se llamaba MEDIANOCHE y mentia: cualquiera que leyera
# el archivo iba a creer que ese era el color de fondo del sistema.
FOOTER_DARK = (20, 17, 16)
POLVO = (231, 221, 201)
POLVO_DIM = (168, 155, 132)
# Acento unico del sistema: brasa #D9BF7A, el mismo del specimen y de la web.
# Antes era #CE8B3A, un ambar mas naranja que quedo de una version previa: dejaba la
# portada de Spotify como la unica pieza de la marca con otro acento (2026-07-22).
BRASA = (217, 191, 122)

F_DISPLAY = "C:/Windows/Fonts/BOOKOSB.TTF"   # Bookman Old Style Bold
F_ITALIC = "C:/Windows/Fonts/BOOKOSI.TTF"    # Bookman Old Style Italic
F_LABEL = "C:/Windows/Fonts/segoeuib.ttf"


def _scrim(canvas, height_frac, max_alpha, from_top):
    """Degradado negro sobre un borde. Devuelve el canvas modificado."""
    W, H = canvas.size
    h = int(H * height_frac)
    grad = Image.new("L", (1, h))
    for i in range(h):
        t = i / max(1, h - 1)
        grad.putpixel((0, i), int(max_alpha * ((1 - t) if from_top else t)))
    grad = grad.resize((W, h))
    box = (0, 0, W, h) if from_top else (0, H - h, W, H)
    region = canvas.crop(box)
    canvas.paste(Image.composite(Image.new("RGB", (W, h), (0, 0, 0)), region, grad), box)
    return canvas


def _tracked(draw, y, text, font, fill, W, spacing):
    """Dibuja centrado con tracking. Devuelve el ancho total."""
    widths = [draw.textlength(c, font=font) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = (W - total) / 2
    for c, cw in zip(text, widths):
        draw.text((x, y), c, font=font, fill=fill)
        x += cw + spacing
    return total


def compose(scene_path, season_label, title, tagline, out_path, icon_strip_path=None):
    scene = Image.open(scene_path).convert("RGB")
    W, H = scene.size
    canvas = scene.copy()

    _scrim(canvas, 0.24, 215, from_top=True)
    # Mas denso y mas bajo que el de arriba: el bloque inferior compite con el fuego,
    # que es la zona mas brillante de la escena.
    _scrim(canvas, 0.34, 238, from_top=False)
    draw = ImageDraw.Draw(canvas)

    # --- wordmark arriba ---
    wm_font = ImageFont.truetype(F_DISPLAY, int(H * 0.040))
    wm_y = int(H * 0.052)
    _tracked(draw, wm_y, "MR. PUTRID'S DEN", wm_font, POLVO, W, int(H * 0.004))

    rule_w, rule_h = int(W * 0.07), max(2, int(H * 0.0013))
    rule_y = wm_y + int(H * 0.062)
    draw.rectangle([(W - rule_w) / 2, rule_y, (W + rule_w) / 2, rule_y + rule_h], fill=BRASA)

    # --- bloque inferior: temporada / titulo / tagline ---
    FOOTER_H = int(H * 0.058)
    margin_x = int(W * 0.08)
    max_w = W - 2 * margin_x

    # Una sola linea: partir el titulo lo empuja hacia arriba, sobre el fuego, donde
    # ninguna cantidad de scrim lo salva.
    size = int(H * 0.075)
    while size > int(H * 0.030):
        font = ImageFont.truetype(F_DISPLAY, size)
        lines = textwrap.wrap(title, width=max(8, int(max_w / (size * 0.62))), break_long_words=False)
        if max((font.getlength(l) for l in lines), default=0) <= max_w and len(lines) <= 1:
            break
        size -= 2
    line_h = int(size * 1.14)

    label_font = ImageFont.truetype(F_LABEL, int(H * 0.017))
    tag_font = ImageFont.truetype(F_ITALIC, int(size * 0.33))
    tag_lines = textwrap.wrap(tagline, width=max(10, int(max_w / (tag_font.size * 0.48))), break_long_words=False)
    tag_line_h = int(tag_font.size * 1.35)

    block_h = int(label_font.size * 1.9) + line_h * len(lines) + int(H * 0.014) + tag_line_h * len(tag_lines)
    y = H - FOOTER_H - block_h - int(H * 0.055)

    _tracked(draw, y, season_label.upper(), label_font, BRASA, W, int(H * 0.005))
    y += int(label_font.size * 1.9)
    for line in lines:
        draw.text(((W - font.getlength(line)) / 2, y), line, font=font, fill=POLVO)
        y += line_h
    y += int(H * 0.014)
    for tl in tag_lines:
        draw.text(((W - tag_font.getlength(tl)) / 2, y), tl, font=tag_font, fill=POLVO_DIM)
        y += tag_line_h

    # --- footer: solo iconos de plataforma ---
    draw.rectangle([0, H - FOOTER_H, W, H], fill=FOOTER_DARK)
    if icon_strip_path:
        icons = Image.open(icon_strip_path).convert("RGB")
        diff = ImageChops.difference(icons, Image.new("RGB", icons.size, (0, 0, 0)))
        bbox = diff.getbbox()
        if bbox:
            icons, diff = icons.crop(bbox), diff.crop(bbox)
        icon_h = int(FOOTER_H * 0.62)
        icon_w = int(icons.width * (icon_h / icons.height))
        icons = icons.resize((icon_w, icon_h), Image.LANCZOS)
        mask = diff.convert("L").resize((icon_w, icon_h), Image.LANCZOS).point(lambda v: min(255, int(v * 1.6)))
        canvas.paste(icons, (int((W - icon_w) / 2), int(H - FOOTER_H / 2 - icon_h / 2)), mask)

    canvas.save(out_path, quality=95)
    print("saved", out_path, "| titulo", size, "px | lineas", len(lines))


if __name__ == "__main__":
    base = "E:/Podcast/MPD/Temporada 2/artwork"
    # La escena es ESCENA-OFICIAL (grading nocturno E), no PORTADA-FINAL, que es la
    # version calida previa al pivote de temperatura. Verificado comparando una zona sin
    # tipografia contra la portada publicada: delta 0.01 vs 18.33 (2026-07-22). Corriendo
    # esto con la ruta vieja se regeneraba la portada en la paleta equivocada.
    compose(
        scene_path=f"{base}/MPD-T2-ESCENA-OFICIAL-3000.jpg",
        season_label="Temporada 2",
        title="Misterios y Leyendas",
        tagline="Donde la música se encuentra con el mito",
        out_path=f"{base}/MPD-T2-PORTADA-CONTEXTO-3000.jpg",
        icon_strip_path="E:/Podcast/MPD/EP 05/artwork-local/mpd-icon-strip-source.png",
    )
