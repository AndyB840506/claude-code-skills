# Portadas de EPISODIO de Mr. Putrid's Den - TEMPORADA 2 ("La Guarida"): 1:1, 16:9 y 9:16.
#
# Los tres formatos del episodio salen de aca, de una sola escena y un solo lockup.
# mpd-lockup-t2.py sigue siendo el compositor de las piezas de TEMPORADA (la portada del
# show); no se toca.
#
# Decisiones fijas, cada una motivada:
#   - La escena NO se regenera por formato. Ya fue aprobada en 1:1 (sin aros/relojes/
#     vinilos, verificada con zoom); volver a pedirsela al modelo en otro aspect ratio
#     reabre ese riesgo, y a cfg=1.0 el prompt negativo de Z-Image no actua. Regla en
#     comfyui/docs/artwork-composition.md.
#   - 16:9 recorta una banda de la escena. 9:16 NO recorta a los lados: extiende el
#     lienzo arriba y abajo estirando las filas de borde. Un recorte vertical de una
#     escena cuadrada se come el ancho, y aca el ancho ES el contenido -- son cinco
#     sillas, una por muerto. Con tres sillas y dos cortadas por el borde el concepto
#     se rompe.
#   - La escena pasa por night_grade (variante E, congelada). NO es cosmetico: la primera
#     portada de este episodio se compuso sin grading y quedaba en un casi-negro neutro
#     (sesgo azul B-R = +0.9) mientras la portada de temporada y el fondo de la web viven
#     en +36.7 y el medianoche declarado del sistema es #0B1A39 (+46). O sea: el episodio
#     estaba fuera de la paleta de su propia marca. Medido el 2026-07-30 sobre los cuatro
#     archivos, no estimado.
#   - Ese grading resuelve solo el piso de negro: negro puro con shadow_amt 0.66 hacia
#     (16,38,92) cae en (10.6, 25.1, 60.7), que es exactamente el medianoche del sistema.
#     La 1:1 anterior necesitaba un levantamiento explicito a 11 porque no tenia grading.
#
# Uso: python mpd-portada-ep-t2.py
import importlib.util
import os
import pathlib
from PIL import Image, ImageDraw, ImageFont


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).with_name(filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Los modulos del kit tienen guion en el nombre: se cargan por ruta para no duplicar
# la matematica de los degradados ni la del recorte por aspect.
scrim_bands = _load("scrim_overlay", "scrim-overlay.py").scrim_bands
night_grade = _load("night_grade", "night_grade.py").night_grade
_kit = _load("mpd_social_kit", "mpd-social-kit.py")
crop_aspect = _kit.crop_aspect

# Paleta del lockup de la 1:1 (mpd-lockup-t2.py). POLVO_DIM es el calido, no el azulado
# del kit de redes: la bajada de la portada publicada es esta.
FOOTER_DARK = (20, 17, 16)
POLVO = (231, 221, 201)
POLVO_DIM = (168, 155, 132)
BRASA = (217, 191, 122)
MEDIANOCHE = (11, 26, 57)

F_DISPLAY = "C:/Windows/Fonts/BOOKOSB.TTF"   # Bookman Old Style Bold
F_ITALIC = "C:/Windows/Fonts/BOOKOSI.TTF"    # Bookman Old Style Italic
F_LABEL = "C:/Windows/Fonts/segoeuib.ttf"

WORDMARK = "MR. PUTRID'S DEN"
FOOTER_FRAC = 0.058          # franja de iconos, igual que en la 1:1

SCENE = r"E:\AI\outputs\MPD-T2E01-escenario-3000_00001_.png"
ICONS = r"E:\Podcast\MPD\EP 05\artwork-local\mpd-icon-strip-source.png"
OUT_DIR = r"E:\Podcast\MPD\Temporada 2\EP 01\artwork"

SEASON_LABEL = "Temporada 2 · Episodio 1"
TITLE = "El Club de los 27"
TAGLINE = "Cinco muertes, dos años, la misma edad."
NUMERAL = "27"


def plate(canvas, y0, y1, alpha=118, dark=(6, 12, 26)):
    """Oscurece una banda horizontal con los dos bordes difuminados.

    Existe porque el scrim de borde no alcanza donde vive el bloque de titulo: el charco
    de luz del piso cae justo ahi y la linea de temporada en brasa desaparecia en
    miniatura (comprobado a 300 px sobre la 1:1 anterior). Subir el scrim entero apagaba
    el piso iluminado, que es lo que le da profundidad a la escena; esta placa oscurece
    solo la franja del texto. Los bordes se difuminan sobre un tercio de la altura para
    que no quede una caja rectangular visible.
    """
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


def draw_numeral(canvas, text, center=(0.5, 0.395), height_frac=0.26, style="ghost",
                 fill=POLVO, stroke=BRASA, ghost_alpha=86):
    """Numeral grande compuesto con PIL, centrado por el bounding box real del glifo.

    El numero NO se le pide al modelo: la regla del kit es que el modelo nunca genera
    texto que se vaya a leer (mordio en BTQ EP.022, "BEHIND THE QEQUE"). Aca ademas es
    el elemento principal de la pieza, asi que tiene que ser deterministico.

    Se centra por textbbox y no por textlength porque la caja de la fuente incluye
    ascendente y descendente: centrar por la caja deja el numero visiblemente alto.

    style: "solid" (relleno polvo) | "outline" (solo contorno brasa) | "ghost"
    (relleno tenue + contorno brasa).
    """
    W, H = canvas.size
    font = ImageFont.truetype(F_DISPLAY, int(H * height_frac * 1.35))
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    x0, y0, x1, y1 = probe.textbbox((0, 0), text, font=font)
    x = int(W * center[0] - (x1 - x0) / 2 - x0)
    y = int(H * center[1] - (y1 - y0) / 2 - y0)
    sw = max(2, int(H * 0.0034))

    def stamp(color, draw_fn):
        layer = Image.new("L", (W, H), 0)
        draw_fn(ImageDraw.Draw(layer))
        canvas.paste(Image.new("RGB", (W, H), color), (0, 0), layer)

    if style == "solid":
        stamp(fill, lambda d: d.text((x, y), text, font=font, fill=255))
    elif style == "outline":
        stamp(stroke, lambda d: d.text((x, y), text, font=font, fill=0,
                                       stroke_width=sw, stroke_fill=255))
    else:
        stamp(fill, lambda d: d.text((x, y), text, font=font, fill=ghost_alpha))
        stamp(stroke, lambda d: d.text((x, y), text, font=font, fill=0,
                                       stroke_width=sw, stroke_fill=255))


def tracked(draw, cx, y, text, font, fill, spacing):
    """Dibuja centrado en cx con tracking. Devuelve el ancho ocupado."""
    widths = [draw.textlength(c, font=font) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = cx - total / 2
    for c, cw in zip(text, widths):
        draw.text((x, y), c, font=font, fill=fill)
        x += cw + spacing
    return total


def draw_lockup(canvas, *, wm_top, block_bottom, title_frac, icon_strip_path=None,
                footer_frac=FOOTER_FRAC, label_frac=0.024, wm_frac=0.040, tagline=TAGLINE):
    """Wordmark arriba + bloque de titulo anclado a `block_bottom`, y footer de iconos.

    El bloque crece hacia ARRIBA desde block_bottom en vez de hacia abajo desde un tope:
    lo que hay que respetar es el borde inferior (footer y zona segura de la plataforma),
    no el arranque.
    """
    W, H = canvas.size
    draw = ImageDraw.Draw(canvas)

    wm_font = ImageFont.truetype(F_DISPLAY, int(H * wm_frac))
    tracked(draw, W / 2, wm_top, WORDMARK, wm_font, POLVO, int(H * wm_frac * 0.10))
    rule_w, rule_h = int(W * 0.07), max(2, int(H * 0.0013))
    rule_y = wm_top + int(H * wm_frac * 1.55)
    draw.rectangle([(W - rule_w) / 2, rule_y, (W + rule_w) / 2, rule_y + rule_h], fill=BRASA)

    # Titulo en UNA linea: partirlo lo empuja hacia arriba, sobre las sillas.
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
    # Tracking cerrado (0.003H, no 0.005H): la etiqueta es lo primero que se pierde al
    # reducir, y el tracking abierto separa los glifos hasta que la palabra deja de leerse
    # como bloque. Verificado mirando la miniatura de 300 px, no calculado.
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
    """Guarda con el piso de negro garantizado.

    El clamp va aca y no solo sobre la escena porque los que se cuelan por debajo de 11
    son los bordes de los logos de plataforma: se pegan con mascara de alfa, y donde la
    mascara es parcial sobre un pixel negro del logo el resultado baja de 11. Son unas
    decenas de pixeles dentro de los glifos, pero dejan de cumplir la invariante.
    """
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


# El scrim inferior baja a 0.30/205 (venia de 0.34/238): con la escena del escenario
# vacio, ese scrim apagaba el charco de luz, que es lo unico que hay en el cuadro ademas
# del haz. La legibilidad del bloque de texto la sostiene `plate`, no el scrim.
BOTTOM_SCRIM = dict(bottom_frac=0.30, bottom_alpha=205)


def build_1x1(scene):
    """3000x3000. La pieza que manda: es la portada del episodio en Spotify."""
    im = scrim_bands(scene, top_frac=0.24, top_alpha=215, **BOTTOM_SCRIM)
    draw_numeral(im, NUMERAL, center=(0.5, 0.405), height_frac=0.275)
    draw_lockup(im, wm_top=int(3000 * 0.052),
                block_bottom=3000 - int(3000 * FOOTER_FRAC) - int(3000 * 0.055),
                title_frac=0.075, icon_strip_path=ICONS)
    return save(im, "MPD-T2E01-PORTADA-3000.jpg")


def build_16x9(scene):
    """1920x1080. Banda horizontal: aire oscuro arriba para el wordmark y el numeral,
    el charco de luz del piso abajo para el bloque de titulo."""
    im = crop_aspect(scene, 16 / 9, y_center=0.62).resize((1920, 1080), Image.LANCZOS)
    im = scrim_bands(im, top_frac=0.22, top_alpha=150, **BOTTOM_SCRIM)
    draw_numeral(im, NUMERAL, center=(0.5, 0.375), height_frac=0.30)
    draw_lockup(im, wm_top=int(1080 * 0.055),
                block_bottom=1080 - int(1080 * FOOTER_FRAC) - int(1080 * 0.030),
                title_frac=0.088, icon_strip_path=ICONS)
    return save(im, "MPD-T2E01-16x9-FINAL.png")


def build_9x16(scene):
    """1080x1920. Recorte vertical nativo de la escena.

    No extiende el lienzo: la version de sillas lo hacia para no perder ninguna de las
    cinco, y el escenario vacio no tiene nada que preservar a los lados.
    """
    im = crop_aspect(scene, 1080 / 1920, y_center=0.52).resize((1080, 1920), Image.LANCZOS)
    im = scrim_bands(im, top_frac=0.20, top_alpha=140, **BOTTOM_SCRIM)
    draw_numeral(im, NUMERAL, center=(0.5, 0.40), height_frac=0.20)
    draw_lockup(im, wm_top=int(1920 * 0.075),
                block_bottom=1920 - int(1920 * FOOTER_FRAC) - int(1920 * 0.045),
                title_frac=0.058, label_frac=0.017, wm_frac=0.029, icon_strip_path=ICONS)
    return save(im, "MPD-T2E01-9x16-FINAL.png")


if __name__ == "__main__":
    scene = night_grade(Image.open(SCENE).convert("RGB"))
    print("escena:", SCENE, "| night_grade variante E")
    build_1x1(scene)
    build_16x9(scene)
    build_9x16(scene)
