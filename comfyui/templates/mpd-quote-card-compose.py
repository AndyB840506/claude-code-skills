# Uso CLI: python mpd-quote-card-compose.py <escena.png> "<linea1>" "<linea2>" <EP.NNN> <salida.png> [icon_strip.png]
# Tambien importable: from mpd_quote_card_compose import compose_quote_card
# Compone una quote card MPD 1920x1080: escena full-bleed + gradiente oscuro en el
# tercio inferior + cita (2 lineas) + atribucion pequena + footer con flor + iconos.
# Mismo footer/flor/iconos que mpd-portada-compose.py, sin el bloque de wordmark/dots.
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFont
import math

BLACK = (26, 26, 26)        # #1a1a1a
CRIMSON = (155, 28, 28)     # #9B1C1C
GOLD = (255, 215, 0)        # #FFD700
SILVER = (168, 168, 168)    # #A8A8A8
WHITE = (255, 255, 255)


def compose_quote_card(scene_path, line1, line2, ep_number, out_path, icon_strip_path=None):
    scene = Image.open(scene_path).convert("RGB")
    W, H = scene.size

    # dark gradient overlay, bottom 40% of frame, transparent at top to near-opaque at bottom
    grad_h = int(H * 0.42)
    gradient = Image.new("L", (1, grad_h), 0)
    for y in range(grad_h):
        gradient.putpixel((0, y), int(255 * (y / grad_h) ** 1.6 * 0.88))
    gradient = gradient.resize((W, grad_h))
    dark_layer = Image.new("RGB", (W, grad_h), (10, 10, 10))
    canvas = scene.copy()
    canvas.paste(dark_layer, (0, H - grad_h), gradient)

    draw = ImageDraw.Draw(canvas)

    attr_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(H * 0.021))
    quote_font_path = "C:/Windows/Fonts/impact.ttf"
    footer_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", int(H * 0.019))
    footer_ep_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(H * 0.019))
    footer_small_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", int(H * 0.015))

    FOOTER_H = int(H * 0.085)
    margin_x = int(W * 0.09)
    max_w = W - 2 * margin_x

    size = int(H * 0.05)
    q_font = ImageFont.truetype(quote_font_path, size)
    while max(q_font.getlength(line1), q_font.getlength(line2)) > max_w and size > int(H * 0.026):
        size -= 2
        q_font = ImageFont.truetype(quote_font_path, size)
    line_h = int(size * 1.18)

    attr_text = f"MR. PUTRID'S DEN · {ep_number.upper()}"
    attr_h = int(attr_font.size * 1.3)

    block_h = attr_h + int(H * 0.012) + line_h * 2
    y = H - FOOTER_H - block_h - int(H * 0.035)

    aw = attr_font.getlength(attr_text)
    draw.text(((W - aw) / 2, y), attr_text, font=attr_font, fill=SILVER)
    y += attr_h + int(H * 0.014)

    for line in (line1, line2):
        w = q_font.getlength(line)
        draw.text(((W - w) / 2, y), line, font=q_font, fill=WHITE)
        y += line_h

    # --- footer bar (same as covers) ---
    draw.rectangle([0, H - FOOTER_H, W, H], fill=BLACK)
    footer_pad = int(W * 0.03)
    draw.text((footer_pad, H - FOOTER_H / 2 - footer_font.size / 2), "Mr. Putrid's Den", font=footer_font, fill=WHITE)

    ep_upper = ep_number.upper()
    ep_center_w = footer_ep_font.getlength(ep_upper)
    flower_r = max(3, int(FOOTER_H * 0.10))
    gap = int(FOOTER_H * 0.14)
    group_w = ep_center_w + gap + flower_r * 2
    gx = (W - group_w) / 2
    draw.text((gx, H - FOOTER_H / 2 - footer_ep_font.size / 2), ep_upper, font=footer_ep_font, fill=CRIMSON)
    fx = gx + ep_center_w + gap + flower_r
    fy = H - FOOTER_H / 2
    for k in range(5):
        ang = math.pi * 2 * k / 5 - math.pi / 2
        px = fx + math.cos(ang) * flower_r * 0.62
        py = fy + math.sin(ang) * flower_r * 0.62
        draw.ellipse([px - flower_r * 0.55, py - flower_r * 0.55, px + flower_r * 0.55, py + flower_r * 0.55], fill=CRIMSON)
    draw.ellipse([fx - flower_r * 0.32, fy - flower_r * 0.32, fx + flower_r * 0.32, fy + flower_r * 0.32], fill=GOLD)

    if icon_strip_path:
        icons = Image.open(icon_strip_path).convert("RGB")
        bg = Image.new("RGB", icons.size, (0, 0, 0))
        diff = ImageChops.difference(icons, bg)
        bbox = diff.getbbox()
        if bbox:
            icons = icons.crop(bbox)
            diff = diff.crop(bbox)
        icon_h = int(FOOTER_H * 0.78)
        icon_w = int(icons.width * (icon_h / icons.height))
        icons = icons.resize((icon_w, icon_h), Image.LANCZOS)
        mask = diff.convert("L").resize((icon_w, icon_h), Image.LANCZOS)
        mask = mask.point(lambda v: min(255, int(v * 1.6)))
        icons_x = W - footer_pad - icon_w
        icons_y = int(H - FOOTER_H / 2 - icon_h / 2)
        canvas.paste(icons, (icons_x, icons_y), mask)
    else:
        row = "Spotify . Apple Podcasts . Amazon Music"
        rw = footer_small_font.getlength(row)
        draw.text((W - footer_pad - rw, H - FOOTER_H / 2 - footer_small_font.size / 2), row, font=footer_small_font, fill=SILVER)

    canvas.save(out_path)
    print("saved", out_path, "quote font size", size)


if __name__ == "__main__":
    compose_quote_card(
        scene_path=sys.argv[1],
        line1=sys.argv[2],
        line2=sys.argv[3],
        ep_number=sys.argv[4],
        out_path=sys.argv[5],
        icon_strip_path=sys.argv[6] if len(sys.argv) > 6 else None,
    )
