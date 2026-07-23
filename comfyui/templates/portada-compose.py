# Uso: python portada-compose.py <escena.png> <EP.NNN> "<titulo>" <salida.png> [icon_strip.png]
# Formato del label: 3 digitos con cero a la izquierda -- "EP.022", no "EP.22".
# Decidido 2026-07-23: gana brand-constants.md:84 (EP.0XX). Las portadas hasta EP.022
# inclusive salieron con 2 digitos; no se regeneran retroactivamente.
# Compone la tipografia congelada BTQ v3 (dots + wordmark + BTQ + titulo + footer)
# sobre una escena ya generada. Requiere PIL (ya viene en python_embeded de ComfyUI).
# icon_strip.png (opcional): imagen con 2 filas de iconos de plataforma generadas por
# separado (fondo negro puro) -- se recorta automaticamente al bounding box del
# contenido y se pega a la derecha del footer. Sin este argumento, usa texto placeholder.
import sys
import textwrap
from PIL import Image, ImageChops, ImageDraw, ImageFont

scene_path = sys.argv[1]
ep_number = sys.argv[2]
title = sys.argv[3]
out_path = sys.argv[4]
icon_strip_path = sys.argv[5] if len(sys.argv) > 5 else None

scene = Image.open(scene_path).convert("RGB")
W, H = scene.size

BLACK = (10, 10, 10)        # #0A0A0A
OFFWHITE = (245, 242, 236)  # #F5F2EC
GOLD = (201, 168, 76)       # #C9A84C

canvas = scene.copy()
draw = ImageDraw.Draw(canvas)

wordmark_font = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", int(H * 0.062))
btq_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(H * 0.040))
title_font_path = "C:/Windows/Fonts/segoeuib.ttf"
footer_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(H * 0.020))
ep_font = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", int(H * 0.050))
footer_small_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", int(H * 0.016))


def center_text(y, text, font, fill, letter_spacing=0):
    if letter_spacing:
        widths = [draw.textlength(c, font=font) for c in text]
        total_w = sum(widths) + letter_spacing * (len(text) - 1)
        x = (W - total_w) / 2
        for c, cw in zip(text, widths):
            draw.text((x, y), c, font=font, fill=fill)
            x += cw + letter_spacing
    else:
        w = draw.textlength(text, font=font)
        draw.text(((W - w) / 2, y), text, font=font, fill=fill)


# --- top block: 5 gold dots + wordmark + BTQ ---
dot_r = max(3, int(H * 0.006))
dot_gap = dot_r * 5
dots_w = dot_r * 2 * 5 + dot_gap * 4
dot_y = int(H * 0.035)
start_x = (W - dots_w) / 2
for i in range(5):
    cx = start_x + i * (dot_r * 2 + dot_gap) + dot_r
    draw.ellipse([cx - dot_r, dot_y - dot_r, cx + dot_r, dot_y + dot_r], fill=GOLD)

center_text(int(H * 0.05), "BEHIND THE QUEUE", wordmark_font, OFFWHITE, letter_spacing=2)
center_text(int(H * 0.125), "BTQ", btq_font, GOLD, letter_spacing=6)

# --- title block, below the figure, above the footer ---
FOOTER_H = int(H * 0.09)
title_margin_x = int(W * 0.08)
title_max_w = W - 2 * title_margin_x

size = int(H * 0.052)
while size > int(H * 0.024):
    font = ImageFont.truetype(title_font_path, size)
    chars_per_line = max(10, int(title_max_w / (size * 0.55)))
    lines = textwrap.wrap(title, width=chars_per_line, break_long_words=False)
    max_line_w = max((font.getlength(l) for l in lines), default=0)
    line_h = int(size * 1.25)
    total_h = line_h * len(lines)
    if max_line_w <= title_max_w and len(lines) <= 3:
        break
    size -= 2

title_y = H - FOOTER_H - total_h - int(H * 0.035)
y = title_y
for line in lines:
    w = font.getlength(line)
    draw.text(((W - w) / 2, y), line, font=font, fill=OFFWHITE)
    y += line_h

# --- footer bar ---
draw.rectangle([0, H - FOOTER_H, W, H], fill=BLACK)
footer_pad = int(W * 0.035)
draw.text((footer_pad, H - FOOTER_H / 2 - footer_font.size / 2), "Behind the Queue", font=footer_font, fill=OFFWHITE)

ep_w = ep_font.getlength(ep_number)
draw.text(((W - ep_w) / 2, H - FOOTER_H / 2 - ep_font.size / 2), ep_number, font=ep_font, fill=GOLD)

if icon_strip_path:
    icons = Image.open(icon_strip_path).convert("RGB")
    bg = Image.new("RGB", icons.size, (0, 0, 0))
    diff = ImageChops.difference(icons, bg)
    bbox = diff.getbbox()
    if bbox:
        icons = icons.crop(bbox)
        diff = diff.crop(bbox)
    icon_h = int(FOOTER_H * 0.82)
    icon_w = int(icons.width * (icon_h / icons.height))
    icons = icons.resize((icon_w, icon_h), Image.LANCZOS)
    # The icon strip's own background is near-pure black (0,0,0), which does not
    # match the footer bar color (10,10,10) -- pasting it opaquely leaves a visible
    # seam/box. Use the diff-from-black as an alpha mask so only icon pixels
    # composite onto the footer, letting the footer's own black show through the gaps.
    mask = diff.convert("L").resize((icon_w, icon_h), Image.LANCZOS)
    mask = mask.point(lambda v: min(255, int(v * 1.6)))
    icons_x = W - footer_pad - icon_w
    icons_y = int(H - FOOTER_H / 2 - icon_h / 2)
    canvas.paste(icons, (icons_x, icons_y), mask)
else:
    # Placeholder: nombres de plataforma en vez de iconos reales
    row1 = "Facebook . Instagram . TikTok"
    row2 = "Spotify . Apple Podcasts . Amazon Music"
    r1_w = footer_small_font.getlength(row1)
    r2_w = footer_small_font.getlength(row2)
    draw.text((W - footer_pad - r1_w, H - FOOTER_H * 0.68), row1, font=footer_small_font, fill=OFFWHITE)
    draw.text((W - footer_pad - r2_w, H - FOOTER_H * 0.32), row2, font=footer_small_font, fill=GOLD)

canvas.save(out_path)
print("saved", out_path, "title font size", size, "lines", len(lines))
if not icon_strip_path:
    print("NOTA: footer usa texto placeholder en vez de iconos reales de plataforma.")
