# Portada de MPD EP.02 (T2*E2) - composicion nueva, sin el formato "numeral gigante"
# de EP.006 (decision de Andres: la escena integra las 3 historias, no necesita un
# numero central). Reusa los mismos modulos compartidos (scrim, night_grade, crop_aspect)
# y la misma paleta/tipografia del lockup de T2 -- solo cambia que NO hay draw_numeral.
#
# Escena: cruce de caminos + disco de vinilo en primer plano + casona (Boleskine) al
# fondo bajo luna llena. Generada con Z-Image Turbo, upscaleada a 3000x3000 con
# RealESRGAN, y pasada por night_grade variante E (la misma de EP.006) para el filtro
# azul de marca que pidio Andres explicitamente.
#
# Uso: python mpd-portada-ep02-t2.py
import importlib.util
import os
import pathlib
from PIL import Image, ImageDraw, ImageFont


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).with_name(filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


scrim_bands = _load("scrim_overlay", "scrim-overlay.py").scrim_bands
night_grade = _load("night_grade", "night_grade.py").night_grade
_kit = _load("mpd_social_kit", "mpd-social-kit.py")
crop_aspect = _kit.crop_aspect

FOOTER_DARK = (20, 17, 16)
POLVO = (231, 221, 201)
POLVO_DIM = (168, 155, 132)
BRASA = (217, 191, 122)
MEDIANOCHE = (11, 26, 57)

F_DISPLAY = "C:/Windows/Fonts/BOOKOSB.TTF"
F_ITALIC = "C:/Windows/Fonts/BOOKOSI.TTF"
F_LABEL = "C:/Windows/Fonts/segoeuib.ttf"

WORDMARK = "MR. PUTRID'S DEN"
FOOTER_FRAC = 0.058

SCENE = r"E:\AI\outputs\MPD-T2E02-escenario-3000_00001_.png"
ICONS = r"E:\Podcast\MPD\EP 05\artwork-local\mpd-icon-strip-source.png"
OUT_DIR = r"E:\Podcast\MPD\Temporada 2\EP 02\artwork"

SEASON_LABEL = "Temporada 2 · Episodio 2"
TITLE = "El rock y el diablo"
TAGLINE = "Pactos, símbolos y mensajes ocultos."


def plate(canvas, y0, y1, alpha=118, dark=(6, 12, 26)):
    """Oscurece una banda horizontal con los dos bordes difuminados (ver mpd-portada-ep-t2.py)."""
    W, H = canvas.size
    y0, y1 = max(0, int(y0)), min(H, int(y1))
    h = y1 - y0
    if h <= 1:
        return
    feather = max(1, int(h * 0.34))
    grad = Image.new("L", (1, h))
    for i in range(h):
        edge = min(i, h - 1 - i)
        grad.putpixel((0, i), alpha if edge >= feather else int(alpha * edge / feather))
    grad = grad.resize((W, h))
    box = (0, y0, W, y1)
    canvas.paste(Image.composite(Image.new("RGB", (W, h), dark), canvas.crop(box), grad), box)


def tracked(draw, cx, y, text, font, fill, spacing):
    widths = [draw.textlength(c, font=font) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = cx - total / 2
    for c, cw in zip(text, widths):
        draw.text((x, y), c, font=font, fill=fill)
        x += cw + spacing
    return total


def draw_lockup(canvas, *, wm_top, block_bottom, title_frac, icon_strip_path=None,
                footer_frac=FOOTER_FRAC, label_frac=0.024, wm_frac=0.040, tagline=TAGLINE):
    W, H = canvas.size
    draw = ImageDraw.Draw(canvas)

    wm_font = ImageFont.truetype(F_DISPLAY, int(H * wm_frac))
    tracked(draw, W / 2, wm_top, WORDMARK, wm_font, POLVO, int(H * wm_frac * 0.10))
    rule_w, rule_h = int(W * 0.07), max(2, int(H * 0.0013))
    rule_y = wm_top + int(H * wm_frac * 1.55)
    draw.rectangle([(W - rule_w) / 2, rule_y, (W + rule_w) / 2, rule_y + rule_h], fill=BRASA)

    margin_x = int(W * 0.08)
    max_w = W - 2 * margin_x
    size = int(H * title_frac)
    while size > int(H * 0.030):
        font = ImageFont.truetype(F_DISPLAY, size)
        if font.getlength(TITLE) <= max_w:
            break
        size -= 2

    label_font = ImageFont.truetype(F_LABEL, int(H * label_frac))
    tag_font = ImageFont.truetype(F_ITALIC, int(size * 0.33))

    label_h = int(label_font.size * 1.9)
    title_h = int(size * 1.14)
    tag_h = int(tag_font.size * 1.35) if tagline else 0
    y = block_bottom - (label_h + title_h + int(H * 0.014) + tag_h)

    pad = int(H * 0.022)
    plate(canvas, y - pad, block_bottom + pad)
    tracked(draw, W / 2, y, SEASON_LABEL.upper(), label_font, BRASA, int(H * 0.003))
    y += label_h
    draw.text(((W - font.getlength(TITLE)) / 2, y), TITLE, font=font, fill=POLVO)
    y += title_h + int(H * 0.014)
    if tagline:
        draw.text(((W - tag_font.getlength(tagline)) / 2, y), tagline, font=tag_font, fill=POLVO_DIM)

    footer_h = int(H * footer_frac)
    draw.rectangle([0, H - footer_h, W, H], fill=FOOTER_DARK)
    if icon_strip_path:
        from PIL import ImageChops
        icons = Image.open(icon_strip_path).convert("RGB")
        diff = ImageChops.difference(icons, Image.new("RGB", icons.size, (0, 0, 0)))
        bbox = diff.getbbox()
        if bbox:
            icons, diff = icons.crop(bbox), diff.crop(bbox)
        icon_h = int(footer_h * 0.62)
        icon_w = int(icons.width * (icon_h / icons.height))
        icons = icons.resize((icon_w, icon_h), Image.LANCZOS)
        mask = diff.convert("L").resize((icon_w, icon_h), Image.LANCZOS).point(
            lambda v: min(255, int(v * 1.6)))
        canvas.paste(icons, (int((W - icon_w) / 2), int(H - footer_h / 2 - icon_h / 2)),
                     mask)
    return size, footer_h


def save(im, name):
    im = im.point(lambda v: max(v, 11))
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name)
    if name.lower().endswith((".jpg", ".jpeg")):
        im.save(path, "JPEG", quality=95, optimize=True, progressive=True)
    else:
        im.save(path)
    print("  %-34s %-11s %7.0f KB" % (name, "x".join(map(str, im.size)),
                                      os.path.getsize(path) / 1024))
    return path


BOTTOM_SCRIM = dict(bottom_frac=0.30, bottom_alpha=205)


def build_1x1(scene):
    """3000x3000. La pieza que manda: es la portada del episodio en Spotify."""
    im = scrim_bands(scene, top_frac=0.18, top_alpha=170, **BOTTOM_SCRIM)
    draw_lockup(im, wm_top=int(3000 * 0.045),
                block_bottom=3000 - int(3000 * FOOTER_FRAC) - int(3000 * 0.050),
                title_frac=0.080, icon_strip_path=ICONS)
    return save(im, "MPD-T2E02-PORTADA-3000.jpg")


def build_16x9(scene):
    im = crop_aspect(scene, 16 / 9, y_center=0.55).resize((1920, 1080), Image.LANCZOS)
    im = scrim_bands(im, top_frac=0.16, top_alpha=140, **BOTTOM_SCRIM)
    draw_lockup(im, wm_top=int(1080 * 0.050),
                block_bottom=1080 - int(1080 * FOOTER_FRAC) - int(1080 * 0.030),
                title_frac=0.090, icon_strip_path=ICONS)
    return save(im, "MPD-T2E02-16x9-FINAL.png")


def build_9x16(scene):
    im = crop_aspect(scene, 1080 / 1920, y_center=0.46).resize((1080, 1920), Image.LANCZOS)
    im = scrim_bands(im, top_frac=0.16, top_alpha=140, **BOTTOM_SCRIM)
    draw_lockup(im, wm_top=int(1920 * 0.070),
                block_bottom=1920 - int(1920 * FOOTER_FRAC) - int(1920 * 0.045),
                title_frac=0.060, label_frac=0.017, wm_frac=0.029, icon_strip_path=ICONS)
    return save(im, "MPD-T2E02-9x16-FINAL.png")


if __name__ == "__main__":
    scene = night_grade(Image.open(SCENE).convert("RGB"))
    print("escena:", SCENE, "| night_grade variante E")
    build_1x1(scene)
    build_16x9(scene)
    build_9x16(scene)
