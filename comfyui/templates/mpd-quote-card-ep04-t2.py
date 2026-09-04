# Quote cards de MPD EP.04 (T2*E4) "Paul is Dead" - 1920x1080, sistema La Guarida.
# Copiado de mpd-quote-card-ep03-t2.py y adaptado: escena/paleta/rutas vienen de
# mpd-portada-ep04-t2.py. No reusar tal cual para el proximo expediente.
#
# Uso: python mpd-quote-card-ep04-t2.py
import importlib.util
import os
import pathlib
from PIL import Image, ImageChops, ImageDraw, ImageFont


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).with_name(filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ep = _load("mpd_portada_ep04_t2", "mpd-portada-ep04-t2.py")
scrim_bands = _load("scrim_overlay", "scrim-overlay.py").scrim_bands
_kit = _load("mpd_social_kit", "mpd-social-kit.py")
crop_aspect, veil = _kit.crop_aspect, _kit.veil

POLVO, POLVO_DIM, BRASA = _ep.POLVO, _ep.POLVO_DIM, _ep.BRASA
FOOTER_DARK, FOOTER_FRAC = _ep.FOOTER_DARK, _ep.FOOTER_FRAC
F_DISPLAY, F_LABEL = _ep.F_DISPLAY, _ep.F_LABEL
SCENE, ICONS = _ep.SCENE, _ep.ICONS
OUT_DIR = _ep.OUT_DIR

EPISODIO = "T2 · E4"
SIZE = (1920, 1080)

# Verbatim del SRT real (E:\Transcriptor\transcripciones\MPD EP 04.srt), no del guion.
# Unica limpieza aplicada: "Fred Labor" -> "Fred LaBour" (error de transcripcion ASR
# del apellido real, no una edicion de contenido). Una por acto + cierre humanizador,
# mismo patron de EP.006/EP.02/EP.03 (4 cards, y_center distinto para no repetir encuadre).
QUOTES = [
    ("Q1", "01:56", 0.30, "A 700 kilómetros de ahí, en una granja de las tierras altas de "
                          "Escocia, Paul McCartney está perfectamente vivo, jugando con sus "
                          "hijas, sin la menor idea de que acaba de morir por segunda vez."),
    ("Q2", "08:01", 0.38, "Fred LaBour no se lo tomó en serio ni un segundo. Él y su editor "
                          "lo consideraban, en sus propias palabras, obviamente un chiste — "
                          "pero nunca esperaron que nadie lo creyera de verdad."),
    ("Q3", "19:07", 0.45, "Ese parche no dice OPD, dice OPP — la insignia real de la Policía "
                          "Provincial de Ontario, en Canadá."),
    ("Q4", "24:52", 0.52, "La maquinaria era exactamente la misma que la de hoy. Lo único "
                          "que cambió después fue la velocidad."),
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
    """Baja el cuerpo hasta que el bloque entero entra en max_w x max_h."""
    size = int(H * start_frac)
    while size > int(H * 0.020):
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
    im = veil(im, 0.38)
    im = scrim_bands(im, top_frac=0.24, top_alpha=150, bottom_frac=0.34, bottom_alpha=210)
    draw = ImageDraw.Draw(im)

    margin_x = int(W * 0.10)
    max_w = W - 2 * margin_x
    footer_h = int(H * FOOTER_FRAC)
    attr_font = ImageFont.truetype(F_LABEL, int(H * 0.021))
    rule_h = max(2, int(H * 0.0035))
    rule_w = int(W * 0.055)

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
    path = os.path.join(OUT_DIR, "MPD-T2E04-%s-1920x1080.png" % tag)
    im.save(path)
    print("  %-34s %2d lineas  cuerpo %3d px  %7.0f KB"
          % (os.path.basename(path), len(lines), font.size, os.path.getsize(path) / 1024))
    return path


if __name__ == "__main__":
    for tag, ts, yc, text in QUOTES:
        compose(tag, ts, yc, text)
