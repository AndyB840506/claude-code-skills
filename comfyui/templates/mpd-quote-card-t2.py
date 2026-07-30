# Quote cards de Mr. Putrid's Den - TEMPORADA 2 ("La Guarida"), 1920x1080.
#
# Reemplaza a mpd-quote-card-compose.py, que es el compositor de TEMPORADA 1 y sigue
# vigente para las cards ya publicadas de T1: ese usa Impact, crimson #9B1C1C, dorado
# #FFD700 y la flor de cinco puntos, todo retirado en T2. No se muta, se versiona.
#
# Diferencias con el de T1, cada una motivada:
#   - Serif de epoca (Bookman Old Style) y paleta La Guarida. La de T1 esta retirada.
#   - Ajuste automatico a N lineas, no a dos fijas. La cita mas larga de este episodio
#     tiene 128 caracteres y no cabe en dos lineas legibles; el compositor de T1 recibia
#     line1/line2 y obligaba a partir el texto a mano.
#   - Sin numeral. El "27" es el elemento de la portada; repetirlo aca le competiria a
#     la cita, que es lo unico que la card tiene que hacer leer.
#   - El texto va en este archivo, no por argumento de consola: un patron con tildes
#     pasado por la linea de comandos se mangla (mordio el 2026-07-28 en un lint).
#
# Uso: python mpd-quote-card-t2.py
import importlib.util
import os
import pathlib
from PIL import Image, ImageChops, ImageDraw, ImageFont


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).with_name(filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ep = _load("mpd_portada_ep_t2", "mpd-portada-ep-t2.py")
scrim_bands = _load("scrim_overlay", "scrim-overlay.py").scrim_bands
_kit = _load("mpd_social_kit", "mpd-social-kit.py")
crop_aspect, veil = _kit.crop_aspect, _kit.veil

# Una sola fuente de verdad para la paleta, las fuentes y las rutas: el compositor de
# portadas. Si el sistema cambia, cambia en un solo archivo.
POLVO, POLVO_DIM, BRASA = _ep.POLVO, _ep.POLVO_DIM, _ep.BRASA
FOOTER_DARK, FOOTER_FRAC = _ep.FOOTER_DARK, _ep.FOOTER_FRAC
F_DISPLAY, F_LABEL = _ep.F_DISPLAY, _ep.F_LABEL
SCENE, ICONS = _ep.SCENE, _ep.ICONS
OUT_DIR = _ep.OUT_DIR

EPISODIO = "T2 · E1"
SIZE = (1920, 1080)

# Verbatim del SRT del master final (ep006-metadata.md), no del guion.
# El y_center distinto por card mueve el encuadre del escenario: las cuatro comparten
# sistema sin ser el mismo fotograma cuatro veces.
QUOTES = [
    ("Q1", "17:23", 0.56, "Estadísticamente, el club de los 27 no existe."),
    ("Q2", "35:01", 0.62, "Los mata la fama que les cae encima a los 20 años antes de que "
                          "nadie sepa cómo cargarla."),
    ("Q3", "36:01", 0.50, "Cuando uno necesita tres teorías místicas distintas para apuntar "
                          "un patrón, casi siempre es porque el patrón no se sostiene solo."),
    ("Q4", "41:21", 0.66, "Cuídense, cuiden a la gente que quieren y no romanticen tanto a "
                          "los que se van temprano."),
]


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        probe = (cur + " " + w).strip()
        if font.getlength(probe) <= max_w or not cur:
            cur = probe
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(text, max_w, max_h, start_frac, H):
    """Baja el cuerpo hasta que el bloque entero entra en max_w x max_h.

    Devuelve (font, lineas, alto_de_linea). Ajusta contra el bloque completo y no contra
    la linea mas larga: una cita de cuatro lineas cabia de ancho y se salia de alto.
    """
    size = int(H * start_frac)
    while size > int(H * 0.030):
        font = ImageFont.truetype(F_DISPLAY, size)
        lines = wrap(text, font, max_w)
        line_h = int(size * 1.26)
        if line_h * len(lines) <= max_h:
            return font, lines, line_h
        size -= 2
    return font, lines, line_h


def compose(tag, timestamp, y_center, text):
    W, H = SIZE
    scene = _ep.night_grade(Image.open(SCENE).convert("RGB"))
    im = crop_aspect(scene, W / H, y_center=y_center).resize(SIZE, Image.LANCZOS)
    # La escena entera se atenua hacia el azul del sistema: aca manda la cita, no el
    # escenario. Con solo scrims de borde el haz quedaba justo detras del texto.
    im = veil(im, 0.38)
    im = scrim_bands(im, top_frac=0.24, top_alpha=150, bottom_frac=0.34, bottom_alpha=210)
    draw = ImageDraw.Draw(im)

    margin_x = int(W * 0.10)
    max_w = W - 2 * margin_x
    footer_h = int(H * FOOTER_FRAC)
    attr_font = ImageFont.truetype(F_LABEL, int(H * 0.021))
    rule_h = max(2, int(H * 0.0035))
    rule_w = int(W * 0.055)

    # Espacio util: entre el filete de arriba y la atribucion de abajo.
    block_top = int(H * 0.24)
    block_bottom = H - footer_h - int(H * 0.115)
    font, lines, line_h = fit(text, max_w, block_bottom - block_top, 0.088, H)

    y = block_top + ((block_bottom - block_top) - line_h * len(lines)) // 2
    draw.rectangle([(W - rule_w) / 2, y - int(H * 0.075),
                    (W + rule_w) / 2, y - int(H * 0.075) + rule_h], fill=BRASA)
    for line in lines:
        draw.text(((W - font.getlength(line)) / 2, y), line, font=font, fill=POLVO)
        y += line_h

    attr = "MR. PUTRID'S DEN  ·  %s  ·  %s" % (EPISODIO, timestamp)
    _ep.tracked(draw, W / 2, H - footer_h - int(H * 0.072), attr, attr_font,
                POLVO_DIM, int(H * 0.004))

    draw.rectangle([0, H - footer_h, W, H], fill=FOOTER_DARK)
    icons = Image.open(ICONS).convert("RGB")
    diff = ImageChops.difference(icons, Image.new("RGB", icons.size, (0, 0, 0)))
    bbox = diff.getbbox()
    if bbox:
        icons, diff = icons.crop(bbox), diff.crop(bbox)
    icon_h = int(footer_h * 0.62)
    icon_w = int(icons.width * (icon_h / icons.height))
    icons = icons.resize((icon_w, icon_h), Image.LANCZOS)
    mask = diff.convert("L").resize((icon_w, icon_h), Image.LANCZOS).point(
        lambda v: min(255, int(v * 1.6)))
    im.paste(icons, (int((W - icon_w) / 2), int(H - footer_h / 2 - icon_h / 2)), mask)

    im = im.point(lambda v: max(v, 11))
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "MPD-T2E01-%s-1920x1080.png" % tag)
    im.save(path)
    print("  %-34s %2d lineas  cuerpo %3d px  %7.0f KB"
          % (os.path.basename(path), len(lines), font.size, os.path.getsize(path) / 1024))
    return path


if __name__ == "__main__":
    for tag, ts, yc, text in QUOTES:
        compose(tag, ts, yc, text)
