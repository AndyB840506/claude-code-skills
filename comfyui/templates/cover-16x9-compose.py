# Uso: python cover-16x9-compose.py <escena.png> "<TITULO>" "<subtitulo>" <salida.png>
# Compone la portada 16:9 (thumbnail YouTube / web hero) BTQ v3: titulo + subtitulo
# alineados a la izquierda, centrados verticalmente en la mitad negra de la escena.
# Sin footer -- las miniaturas se recortan. Requiere PIL.
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

scene_path = sys.argv[1]
title = sys.argv[2].upper()
subtitle = sys.argv[3]
out_path = sys.argv[4]

canvas = Image.open(scene_path).convert("RGB")
W, H = canvas.size
draw = ImageDraw.Draw(canvas)

OFFWHITE = (245, 242, 236)  # #F5F2EC
GOLD = (201, 168, 76)       # #C9A84C

MARGIN_X = int(W * 0.047)
max_text_w = int(W * 0.42)

title_font_path = "C:/Windows/Fonts/impact.ttf"
sub_font_path = "C:/Windows/Fonts/segoeuib.ttf"


def wrap_and_measure(text, font_path, size, max_width, line_mult):
    font = ImageFont.truetype(font_path, size)
    chars_per_line = max(6, int(max_width / (size * 0.52)))
    lines = textwrap.wrap(text, width=chars_per_line, break_long_words=False)
    line_h = int(size * line_mult)
    total_h = line_h * len(lines)
    max_line_w = max((font.getlength(l) for l in lines), default=0)
    return font, lines, line_h, total_h, max_line_w


title_size = int(H * 0.14)
while title_size > int(H * 0.05):
    t_font, t_lines, t_line_h, t_total_h, t_max_w = wrap_and_measure(title, title_font_path, title_size, max_text_w, 1.05)
    if t_max_w <= max_text_w and len(t_lines) <= 4:
        break
    title_size -= 2

sub_size = int(title_size * 0.30)
s_font, s_lines, s_line_h, s_total_h, s_max_w = wrap_and_measure(subtitle, sub_font_path, sub_size, max_text_w, 1.3)

gap = int(H * 0.035)
block_h = t_total_h + gap + s_total_h
start_y = (H - block_h) // 2

y = start_y
for line in t_lines:
    draw.text((MARGIN_X, y), line, font=t_font, fill=OFFWHITE)
    y += t_line_h

y += gap
for line in s_lines:
    draw.text((MARGIN_X, y), line, font=s_font, fill=GOLD)
    y += s_line_h

canvas.save(out_path)
print("saved", out_path, "title font size", title_size, "lines", len(t_lines))
