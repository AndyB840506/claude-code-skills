# Kit de redes de Mr. Putrid's Den - TEMPORADA 2 ("La Guarida").
#
# Genera de una pasada las piezas de perfil y portada para todas las plataformas, a
# partir de la escena oficial de T2 (sin texto) + tipografia deterministica. El texto
# NUNCA se genera con IA.
#
# Reglas del sistema que este script hace cumplir (ver rebrand/identidad-la-guarida.html):
#   - Un solo acento calido. Nada compite con la brasa.
#   - Ninguna tipografia clara se apoya directo sobre el marmol ni sobre el fuego:
#     todo bloque de texto va sobre scrim o sobre panel solido.
#   - Serif de epoca con peso (Bookman Old Style Bold). Nunca una condensada moderna.
#   - Todo lockup se aprueba en miniatura, no a tamano completo: el script escupe las
#     pruebas de 150px y 40px del avatar para mirarlas antes de dar nada por bueno.
#
# Uso: python mpd-social-kit.py [--accent brasa|ambar]
import argparse
import importlib.util
import os
import pathlib
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

# El modulo compartido de scrims tiene guion en el nombre, asi que no se puede
# importar por nombre. Se carga por ruta para no duplicar la matematica del degradado.
_spec = importlib.util.spec_from_file_location(
    "scrim_overlay", pathlib.Path(__file__).with_name("scrim-overlay.py"))
_so = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_so)
scrim_bands = _so.scrim_bands

SCENE = r"E:\Podcast\MPD\Temporada 2\artwork\MPD-T2-ESCENA-OFICIAL-3000.jpg"
OUT_DIR = r"E:\Podcast\MPD\Temporada 2\redes"

# Paleta T2 muestreada del artwork.
MEDIANOCHE = (11, 26, 57)
POLVO = (231, 221, 201)
POLVO_DIM = (154, 163, 184)
ACCENTS = {
    "brasa": (217, 191, 122),   # #D9BF7A - specimen + web (mrputridsden.com)
    "ambar": (206, 139, 58),    # #CE8B3A - el que quedo en la portada de Spotify
}

F_DISPLAY = "C:/Windows/Fonts/BOOKOSB.TTF"
F_ITALIC = "C:/Windows/Fonts/BOOKOSI.TTF"
F_LABEL = "C:/Windows/Fonts/segoeuib.ttf"

WORDMARK = "MR. PUTRID'S DEN"
SEASON = "TEMPORADA 2"
CLAIM = "Misterios y Leyendas"
TAGLINE = "Donde la música se encuentra con el mito"


def crop_frac(im, l, t, r, b):
    """Recorta por fracciones (0-1) del original."""
    W, H = im.size
    return im.crop((int(W * l), int(H * t), int(W * r), int(H * b)))


def crop_aspect(im, aspect, y_center=0.52):
    """Recorta la banda mas ancha posible con el aspect pedido, centrada en y_center.

    y_center por defecto queda un pelo bajo el centro: es donde vive el fuego, que es
    el unico punto calido de la escena y lo que hace reconocible la imagen en chico.
    """
    W, H = im.size
    if W / H > aspect:          # sobra ancho -> recortar a los lados
        w = int(H * aspect)
        x0 = (W - w) // 2
        return im.crop((x0, 0, x0 + w, H))
    h = int(W / aspect)         # sobra alto -> recortar arriba/abajo
    y0 = max(0, min(H - h, int(H * y_center - h / 2)))
    return im.crop((0, y0, W, y0 + h))


def veil(im, amount, color=MEDIANOCHE):
    """Mezcla la imagen entera hacia el azul del sistema.

    Los scrims de borde no sirven en los formatos anchos: la chimenea queda SIEMPRE al
    centro (la escena es simetrica) y las plataformas obligan a centrar la tipografia
    ahi mismo, o sea justo sobre el fuego. Bajar la escena entera deja el fuego como
    resplandor y le devuelve el contraste al texto.
    """
    return Image.blend(im, Image.new("RGB", im.size, color), amount)


def vignette(im, strength=0.55):
    """Oscurece las esquinas. Sube la brasa central sin tocarle el color."""
    W, H = im.size
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)
    steps = 64
    for i in range(steps):
        t = i / steps
        d.ellipse([-W * 0.30 + W * 0.80 * t, -H * 0.30 + H * 0.80 * t,
                   W * 1.30 - W * 0.80 * t, H * 1.30 - H * 0.80 * t],
                  fill=int(255 * (t ** 1.6) * strength))
    return Image.composite(im, Image.new("RGB", (W, H), MEDIANOCHE), mask)


def tracked(draw, cx, y, text, font, fill, spacing):
    """Dibuja con tracking, centrado en cx. Devuelve el ancho ocupado."""
    widths = [draw.textlength(c, font=font) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = cx - total / 2
    for c, cw in zip(text, widths):
        draw.text((x, y), c, font=font, fill=fill)
        x += cw + spacing
    return total


ALL_PARTS = ("wordmark", "rule", "season", "claim", "tagline")


def lockup(canvas, accent, cx, top, block_w, scale=1.0, parts=ALL_PARTS):
    """Bloque tipografico centrado. `parts` elige que elementos se dibujan.

    `block_w` es el ancho util (la zona segura de la plataforma, no el lienzo): la
    tipografia se dimensiona contra el, no contra la imagen, para que nunca caiga en la
    franja que la plataforma recorta.

    El control por `parts` existe porque varios formatos parten el lockup en dos bloques
    (wordmark arriba, titulo abajo); sin el, el wordmark salia duplicado.
    """
    d = ImageDraw.Draw(canvas)
    y = top
    wm_size = max(11, int(block_w * 0.049 * scale))

    if "wordmark" in parts:
        wm_font = ImageFont.truetype(F_DISPLAY, wm_size)
        tracked(d, cx, y, WORDMARK, wm_font, POLVO, max(1, int(wm_size * 0.10)))
        y += int(wm_size * 1.72)

    if "rule" in parts:
        rule_w = int(block_w * 0.085)
        rule_h = max(2, int(wm_size * 0.10))
        d.rectangle([cx - rule_w / 2, y, cx + rule_w / 2, y + rule_h], fill=accent)
        y += int(rule_h + wm_size * 1.30)

    if "season" in parts:
        season_size = max(9, int(block_w * 0.026 * scale))
        season_font = ImageFont.truetype(F_LABEL, season_size)
        tracked(d, cx, y, SEASON, season_font, accent, max(1, int(season_size * 0.30)))
        y += int(season_size * 2.15)

    if "claim" in parts:
        claim_size = max(14, int(block_w * 0.098 * scale))
        while claim_size > 12:
            claim_font = ImageFont.truetype(F_DISPLAY, claim_size)
            if claim_font.getlength(CLAIM) <= block_w:
                break
            claim_size -= 2
        d.text((cx - claim_font.getlength(CLAIM) / 2, y), CLAIM, font=claim_font, fill=POLVO)
        y += int(claim_size * 1.34)

    if "tagline" in parts:
        tag_size = max(10, int(block_w * 0.032 * scale))
        tag_font = ImageFont.truetype(F_ITALIC, tag_size)
        d.text((cx - tag_font.getlength(TAGLINE) / 2, y), TAGLINE, font=tag_font, fill=POLVO_DIM)
        y += int(tag_size * 1.5)
    return y


def save(im, name, quality=92):
    path = os.path.join(OUT_DIR, name)
    im.convert("RGB").save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print("  %-38s %s  %6.1f KB" % (name, "x".join(map(str, im.size)), os.path.getsize(path) / 1024))
    return path


def build(accent_name):
    accent = ACCENTS[accent_name]
    sfx = "" if accent_name == "brasa" else "-ambar"
    os.makedirs(OUT_DIR, exist_ok=True)
    scene = Image.open(SCENE).convert("RGB")
    print("acento:", accent_name, "#%02X%02X%02X" % accent)

    # --- 1. Avatar 1:1 --------------------------------------------------------
    # Sin tipografia: a 40 px cualquier texto es una mancha, y lo que si sobrevive es la
    # silueta y la brasa. El wordmark ya lo pone la plataforma al lado del avatar.
    # El encuadre baja a proposito: la primera version cortaba a la altura de la repisa
    # y el cuadro quedaba dominado por marmol palido -> a 150 px leia como una mancha
    # clara, el mismo defecto que tumbo la primera portada. Este encuadre mete la butaca
    # (masa oscura abajo) y deja el fuego como unico punto claro.
    av = crop_frac(scene, 0.27, 0.41, 0.73, 0.87).resize((1500, 1500), Image.LANCZOS)
    # Vinneta suave, no fuerte: a 0.62 el cuadro entero se lavaba hacia azul y a 40 px
    # quedaba una mancha sin contraste. Lo que hace legible el avatar en chico es el
    # contraste entre la masa oscura de la butaca y la llama, no la oscuridad total.
    av = vignette(av, strength=0.42)
    av = ImageEnhance.Contrast(av).enhance(1.14)
    save(av, f"MPD-T2-avatar-1500{sfx}.jpg", quality=94)
    for px in (150, 40):
        save(av.resize((px, px), Image.LANCZOS), f"pruebas/avatar-{px}px{sfx}.jpg", quality=95)

    # --- 2. Portada de Facebook ----------------------------------------------
    # 820x312 es el tamano de escritorio; se entrega a 2x. Movil recorta a los lados,
    # asi que la tipografia vive dentro de la franja central segura.
    fb = crop_aspect(scene, 1640 / 624, y_center=0.56).resize((1640, 624), Image.LANCZOS)
    fb = veil(fb, 0.46)
    fb = scrim_bands(fb, top_frac=0.42, top_alpha=170, bottom_frac=0.46, bottom_alpha=190)
    lockup(fb, accent, cx=820, top=86, block_w=1000, scale=0.92,
           parts=("wordmark", "rule", "season", "claim"))
    save(fb, f"MPD-T2-facebook-cover-1640x624{sfx}.jpg")

    # --- 3. Instagram post 1:1 -----------------------------------------------
    ig = crop_aspect(scene, 1.0).resize((1080, 1080), Image.LANCZOS)
    ig = veil(ig, 0.20)
    ig = scrim_bands(ig, top_frac=0.30, top_alpha=195, bottom_frac=0.44, bottom_alpha=238)
    lockup(ig, accent, cx=540, top=74, block_w=880, parts=("wordmark", "rule"))
    lockup(ig, accent, cx=540, top=760, block_w=880, parts=("season", "claim", "tagline"))
    save(ig, f"MPD-T2-ig-post-1080{sfx}.jpg")

    # --- 4. Instagram story 9:16 ---------------------------------------------
    # El bloque va en el tercio central: arriba lo tapa el nombre de usuario y abajo
    # la barra de responder.
    st = crop_aspect(scene, 1080 / 1920, y_center=0.46).resize((1080, 1920), Image.LANCZOS)
    st = scrim_bands(st, top_frac=0.26, top_alpha=195, bottom_frac=0.54, bottom_alpha=246)
    lockup(st, accent, cx=540, top=1330, block_w=860)
    save(st, f"MPD-T2-ig-story-1080x1920{sfx}.jpg")

    # --- 5. Banner de YouTube -------------------------------------------------
    # 2560x1440 con zona segura de 1546x423 al centro: es lo unico que se ve en TV y
    # movil. Todo el texto va ahi dentro.
    yt = crop_aspect(scene, 2560 / 1440, y_center=0.55).resize((2560, 1440), Image.LANCZOS)
    # Sin tagline: la zona segura es una franja angosta al centro y la escena tiene el
    # fuego justo ahi. La bajada en POLVO_DIM sobre la llama era el elemento que primero
    # se perdia; el claim en POLVO si aguanta.
    yt = veil(yt, 0.52)
    yt = scrim_bands(yt, top_frac=0.44, top_alpha=160, bottom_frac=0.44, bottom_alpha=175)
    safe_top = (1440 - 423) // 2
    lockup(yt, accent, cx=1280, top=safe_top + 54, block_w=1240, scale=0.86,
           parts=("wordmark", "rule", "season", "claim"))
    save(yt, f"MPD-T2-youtube-2560x1440{sfx}.jpg")

    # --- 6. Cabecera de X -----------------------------------------------------
    xh = crop_aspect(scene, 3.0, y_center=0.56).resize((1500, 500), Image.LANCZOS)
    xh = veil(xh, 0.46)
    xh = scrim_bands(xh, top_frac=0.46, top_alpha=170, bottom_frac=0.42, bottom_alpha=185)
    lockup(xh, accent, cx=750, top=74, block_w=900, scale=0.88,
           parts=("wordmark", "rule", "season", "claim"))
    save(xh, f"MPD-T2-x-header-1500x500{sfx}.jpg")


EP005_COVER = r"E:\Podcast\MPD\EP 05\artwork-local\EP005-1x1-FINAL-FOR-UPLOAD.jpg"
TEASER_DIR = os.path.join(OUT_DIR, "teasers")

ROLL = [
    ("Brian Jones", "1969"),
    ("Alan Wilson", "1970"),
    ("Jimi Hendrix", "1970"),
    ("Janis Joplin", "1970"),
    ("Jim Morrison", "1971"),
    ("Kurt Cobain", "1994"),
    ("Amy Winehouse", "2011"),
]


def wrap_to(text, font, max_w):
    """Parte el texto en lineas que quepan en max_w."""
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


def teaser_base(size, veil_amt, top_a, bot_a, y_center=0.52):
    """Lienzo comun de los teasers: escena recortada, atenuada y con scrims."""
    scene = Image.open(SCENE).convert("RGB")
    im = crop_aspect(scene, size[0] / size[1], y_center=y_center).resize(size, Image.LANCZOS)
    im = veil(im, veil_amt)
    return scrim_bands(im, top_frac=0.34, top_alpha=top_a, bottom_frac=0.46, bottom_alpha=bot_a)


def teaser_expediente(accent, size, name):
    W, H = size
    im = teaser_base(size, 0.46, 190, 232)
    d = ImageDraw.Draw(im)
    block_w = int(W * 0.82)
    cx = W // 2

    lockup(im, accent, cx=cx, top=int(H * 0.07), block_w=block_w, scale=0.86,
           parts=("wordmark", "rule"))

    y = int(H * 0.58)
    tag_font = ImageFont.truetype(F_LABEL, int(block_w * 0.036))
    tracked(d, cx, y, "EXPEDIENTE 01", tag_font, accent, int(tag_font.size * 0.28))
    y += int(tag_font.size * 2.4)

    t_size = int(block_w * 0.135)
    while t_size > 16:
        t_font = ImageFont.truetype(F_DISPLAY, t_size)
        if t_font.getlength("El Club de los 27") <= block_w:
            break
        t_size -= 2
    d.text((cx - t_font.getlength("El Club de los 27") / 2, y), "El Club de los 27",
           font=t_font, fill=POLVO)
    y += int(t_size * 1.5)

    # Cortes explicitos: el wrap automatico partia en "Mismo / día", separando una
    # frase de tres palabras. Las dos fechas van juntas en una linea y el remate en otra.
    hook = ["3 de julio de 1969. 3 de julio de 1971.", "Mismo día. Misma edad."]
    h_size = int(block_w * 0.046)
    while h_size > 12:
        h_font = ImageFont.truetype(F_ITALIC, h_size)
        if max(h_font.getlength(l) for l in hook) <= block_w:
            break
        h_size -= 1
    for line in hook:
        d.text((cx - h_font.getlength(line) / 2, y), line, font=h_font, fill=POLVO_DIM)
        y += int(h_font.size * 1.42)
    save(im, name)


def teaser_nomina(accent, size, name):
    """La nomina. Mas atenuada que las demas: acá manda la lista, no la escena."""
    W, H = size
    im = teaser_base(size, 0.66, 210, 238)
    d = ImageDraw.Draw(im)
    cx, block_w = W // 2, int(W * 0.80)

    lockup(im, accent, cx=cx, top=int(H * 0.06), block_w=block_w, scale=0.86,
           parts=("wordmark", "rule"))

    y = int(H * 0.215)
    lab = ImageFont.truetype(F_LABEL, int(block_w * 0.037))
    tracked(d, cx, y, "TODOS TENÍAN 27", lab, accent, int(lab.size * 0.28))
    y += int(lab.size * 2.8)

    # La lista se dimensiona contra el espacio que QUEDA hasta el margen inferior.
    # Con tamanos fijos, la septima entrada (Amy Winehouse) se salia del lienzo en el
    # formato 1:1 — el ano quedaba cortado por el borde.
    bottom = int(H * 0.94)
    slot = (bottom - y) / len(ROLL)
    n_size = int(min(block_w * 0.072, slot * 0.50))
    n_font = ImageFont.truetype(F_DISPLAY, n_size)
    y_font = ImageFont.truetype(F_LABEL, max(11, int(n_size * 0.40)))
    for nombre, anio in ROLL:
        d.text((cx - n_font.getlength(nombre) / 2, y), nombre, font=n_font, fill=POLVO)
        tracked(d, cx, y + int(n_size * 1.08), anio, y_font, accent, int(y_font.size * 0.24))
        y += slot
    save(im, name)


def build_teasers(accent_name):
    accent = ACCENTS[accent_name]
    os.makedirs(TEASER_DIR, exist_ok=True)
    print("teasers · acento:", accent_name)

    # Beat 1 — el contraste. La primera lamina es la portada REAL de EP.005, sin
    # retocar: decir "esto era el show" con el artwork que la gente ya vio pega mas
    # que un degradado inventado.
    antes = Image.open(EP005_COVER).convert("RGB").resize((1080, 1080), Image.LANCZOS)
    save(antes, "teasers/teaser-1a-antes-1080.jpg")

    teaser_expediente(accent, (1080, 1080), "teasers/teaser-3a-expediente-1080.jpg")
    teaser_expediente(accent, (1080, 1920), "teasers/teaser-3a-expediente-story.jpg")
    teaser_nomina(accent, (1080, 1080), "teasers/teaser-3b-nomina-1080.jpg")
    teaser_nomina(accent, (1080, 1920), "teasers/teaser-3b-nomina-story.jpg")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--accent", choices=list(ACCENTS) + ["both"], default="both")
    ap.add_argument("--teasers", action="store_true", help="solo las piezas de la revelacion de T2")
    args = ap.parse_args()
    if args.teasers:
        build_teasers("brasa" if args.accent in ("both", "brasa") else args.accent)
        raise SystemExit
    os.makedirs(os.path.join(OUT_DIR, "pruebas"), exist_ok=True)
    for name in (list(ACCENTS) if args.accent == "both" else [args.accent]):
        build(name)
