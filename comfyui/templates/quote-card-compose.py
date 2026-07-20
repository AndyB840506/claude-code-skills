# Uso CLI: python quote-card-compose.py <escena.png> "<cita>" "<atribucion>" <salida.png>
# Tambien importable: from quote_card_compose import compose_quote_card
# Compone una quote card BTQ 1920x1080: escena a la derecha (960x1080), texto a la
# izquierda sobre negro puro. Requiere PIL (ya viene en python_embeded de ComfyUI).
# Genera la escena directo a 960x1080 (o cualquier alto x 960 de ancho) para evitar
# recorte/deformación al pegarla en la mitad derecha.
# Import directo (no CLI) recomendado para citas con tildes/enies — evita perderlas por
# escaping de shell al invocar vía Bash/PowerShell (ver comfyui/docs/stack-reference.md
# "Compose scripts con texto acentuado").
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
HALF = 960
BLACK = (10, 10, 10)       # #0A0A0A — void black de marca BTQ
OFFWHITE = (245, 242, 236)  # #F5F2EC — cita
GOLD = (201, 168, 76)       # #C9A84C — atribucion

# Segoe UI: tildes/nn correctas de forma determinista (nunca generadas por el modelo)
QUOTE_FONT_PATH = "C:/Windows/Fonts/segoeuib.ttf"
ATTR_FONT_PATH = "C:/Windows/Fonts/segoeui.ttf"


def _wrap_and_measure(text, font_path, size, max_width):
    font = ImageFont.truetype(font_path, size)
    chars_per_line = max(10, int(max_width / (size * 0.52)))
    lines = textwrap.wrap(text, width=chars_per_line, break_long_words=False)
    line_h = int(size * 1.28)
    total_h = line_h * len(lines)
    max_line_w = max((font.getlength(l) for l in lines), default=0)
    return font, lines, line_h, total_h, max_line_w


def compose_quote_card(scene_path, quote, attribution, out_path):
    canvas = Image.new("RGB", (W, H), BLACK)

    scene = Image.open(scene_path).convert("RGB")
    scene = scene.resize((HALF, H), Image.LANCZOS)
    canvas.paste(scene, (HALF, 0))

    draw = ImageDraw.Draw(canvas)

    margin_x = 90
    margin_top = 90
    margin_bottom = 130
    text_width_px = HALF - 2 * margin_x
    avail_height = H - margin_top - margin_bottom

    # Tamano de fuente dinamico: empieza grande y baja hasta que la cita quepa en el
    # alto disponible (citas largas como EP021 CARD2 terminan ~60px, cortas en ~72px)
    size = 72
    while size > 24:
        font, lines, line_h, total_h, max_line_w = _wrap_and_measure(quote, QUOTE_FONT_PATH, size, text_width_px)
        if total_h <= avail_height - 100 and max_line_w <= text_width_px:
            break
        size -= 2

    attr_size = max(22, int(size * 0.34))
    attr_font = ImageFont.truetype(ATTR_FONT_PATH, attr_size)

    block_h = total_h + 40 + int(attr_size * 1.4)
    start_y = margin_top + (avail_height - block_h) // 2

    y = start_y
    for line in lines:
        draw.text((margin_x, y), line, font=font, fill=OFFWHITE)
        y += line_h

    y += 30
    draw.text((margin_x, y), attribution, font=attr_font, fill=GOLD)

    canvas.save(out_path)
    print("saved", out_path, "quote font size", size)


if __name__ == "__main__":
    compose_quote_card(
        scene_path=sys.argv[1],
        quote=sys.argv[2],
        attribution=sys.argv[3],
        out_path=sys.argv[4],
    )
