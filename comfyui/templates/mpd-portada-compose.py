# Uso CLI: python mpd-portada-compose.py <escena.png> <EP.NNN> "<titulo>" "<tagline>" <salida.png> [icon_strip.png]
# Tambien importable: from mpd_portada_compose import compose
# (evita el problema de acentos perdidos al pasar argumentos con tildes por shell --
# invocar compose() desde un script con strings Python literales es mas confiable).
#
# Compone la tipografia de marca MPD (dots + wordmark + MPD + EP/titulo/tagline + footer
# con flor + iconos de plataforma) sobre una escena ya generada (sin texto horneado).
# Alineacion del bloque de titulo se infiere del aspect ratio: ancho/alto > 1.3 => derecha
# (16:9), si no => centrado (1:1, 9:16) -- igual que la direccion visual congelada en
# artwork-ep005.md. icon_strip.png (opcional): PNG con los iconos de plataforma sobre
# fondo negro puro -- se recorta al bounding box y se pega con mascara de diferencia
# contra negro (mismo patron de portada-compose.py de BTQ).
import sys
import math
import textwrap
from PIL import Image, ImageChops, ImageDraw, ImageFont

BLACK = (26, 26, 26)        # #1a1a1a -- footer + brand dark
CRIMSON = (155, 28, 28)     # #9B1C1C
GOLD = (255, 215, 0)        # #FFD700
SILVER = (168, 168, 168)    # #A8A8A8
WHITE = (255, 255, 255)


def compose(scene_path, ep_number, title, tagline, out_path, icon_strip_path=None):
    scene = Image.open(scene_path).convert("RGB")
    W, H = scene.size
    align_right = (W / H) > 1.3

    canvas = scene.copy()
    draw = ImageDraw.Draw(canvas)

    wordmark_font = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", int(H * 0.052))
    mpd_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(H * 0.026))
    ep_label_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(H * 0.022))
    title_font_path = "C:/Windows/Fonts/impact.ttf"
    tagline_font_path = "C:/Windows/Fonts/segoeuii.ttf"  # Segoe UI Italic
    footer_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", int(H * 0.019))
    footer_ep_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(H * 0.019))
    footer_small_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", int(H * 0.015))

    def center_text(y, text, font, fill, letter_spacing=0):
        if letter_spacing:
            widths = [draw.textlength(c, font=font) for c in text]
            total_w = sum(widths) + letter_spacing * (len(text) - 1)
            x = (W - total_w) / 2
            for c, cw in zip(text, widths):
                draw.text((x, y), c, font=font, fill=fill)
                x += cw + letter_spacing
            return total_w
        else:
            w = draw.textlength(text, font=font)
            draw.text(((W - w) / 2, y), text, font=font, fill=fill)
            return w

    # --- top block: 5 silver dots + wordmark + MPD (always top-center) ---
    dot_r = max(3, int(H * 0.005))
    dot_gap = dot_r * 5
    dots_w = dot_r * 2 * 5 + dot_gap * 4
    dot_y = int(H * 0.032)
    start_x = (W - dots_w) / 2
    for i in range(5):
        cx = start_x + i * (dot_r * 2 + dot_gap) + dot_r
        draw.ellipse([cx - dot_r, dot_y - dot_r, cx + dot_r, dot_y + dot_r], fill=SILVER)

    wm_top = int(H * 0.045)
    center_text(wm_top, "MR. PUTRID'S DEN", wordmark_font, WHITE, letter_spacing=1)
    center_text(wm_top + int(H * 0.058), "MPD", mpd_font, CRIMSON, letter_spacing=6)

    # --- title block: EP.NNN / title / tagline, above the footer ---
    FOOTER_H = int(H * 0.085)
    margin_x = int(W * 0.07)
    max_w = W - 2 * margin_x

    size = int(H * 0.062)
    while size > int(H * 0.028):
        font = ImageFont.truetype(title_font_path, size)
        chars_per_line = max(8, int(max_w / (size * 0.52)))
        lines = textwrap.wrap(title, width=chars_per_line, break_long_words=False)
        max_line_w = max((font.getlength(l) for l in lines), default=0)
        if max_line_w <= max_w and len(lines) <= 2:
            break
        size -= 2
    line_h = int(size * 1.15)

    tagline_size = int(size * 0.42)
    tagline_font = ImageFont.truetype(tagline_font_path, tagline_size)
    tag_chars_per_line = max(10, int(max_w / (tagline_size * 0.5)))
    tag_lines = textwrap.wrap(tagline, width=tag_chars_per_line, break_long_words=False)
    tag_line_h = int(tagline_size * 1.3)

    ep_label_h = int(ep_label_font.size * 1.3)
    block_h = ep_label_h + line_h * len(lines) + int(H * 0.012) + tag_line_h * len(tag_lines)
    y = H - FOOTER_H - block_h - int(H * 0.03)

    ep_upper = ep_number.upper()
    if align_right:
        ep_w = ep_label_font.getlength(ep_upper)
        draw.text((W - margin_x - ep_w, y), ep_upper, font=ep_label_font, fill=SILVER)
        y += ep_label_h + int(H * 0.006)
        for line in lines:
            w = font.getlength(line)
            draw.text((W - margin_x - w, y), line, font=font, fill=WHITE)
            y += line_h
        y += int(H * 0.008)
        for tl in tag_lines:
            w = tagline_font.getlength(tl)
            draw.text((W - margin_x - w, y), tl, font=tagline_font, fill=WHITE)
            y += tag_line_h
    else:
        ep_w = ep_label_font.getlength(ep_upper)
        draw.text(((W - ep_w) / 2, y), ep_upper, font=ep_label_font, fill=SILVER)
        y += ep_label_h + int(H * 0.006)
        for line in lines:
            w = font.getlength(line)
            draw.text(((W - w) / 2, y), line, font=font, fill=WHITE)
            y += line_h
        y += int(H * 0.008)
        for tl in tag_lines:
            w = tagline_font.getlength(tl)
            draw.text(((W - w) / 2, y), tl, font=tagline_font, fill=WHITE)
            y += tag_line_h

    # --- footer bar ---
    draw.rectangle([0, H - FOOTER_H, W, H], fill=BLACK)
    footer_pad = int(W * 0.03)
    draw.text((footer_pad, H - FOOTER_H / 2 - footer_font.size / 2), "Mr. Putrid's Den", font=footer_font, fill=WHITE)

    # center: EP number (crimson) + small flower icon drawn with primitives
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
    print("saved", out_path, "align_right" if align_right else "align_center", "title font size", size)
    if not icon_strip_path:
        print("NOTA: footer usa texto placeholder en vez de iconos reales de plataforma.")


if __name__ == "__main__":
    compose(
        scene_path=sys.argv[1],
        ep_number=sys.argv[2],
        title=sys.argv[3],
        tagline=sys.argv[4],
        out_path=sys.argv[5],
        icon_strip_path=sys.argv[6] if len(sys.argv) > 6 else None,
    )
