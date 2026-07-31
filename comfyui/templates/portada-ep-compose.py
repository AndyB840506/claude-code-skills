# -*- coding: utf-8 -*-
"""Portada de episodio BTQ — direccion v4 minimalista, TIPOGRAFIA PURA.

No usa ComfyUI ni ningun modelo: todo determinista con PIL. Hermana visual de la
portada del show (brand-covers-compose.py): mismo bloque de display a la
izquierda, ultima linea en Senal, kicker de marca abajo.

Uso:
    python portada-ep-compose.py "EP.23 - Efecto Hawthorne: por que ..." <salida.png>

Recibe el TITULO PUBLICADO COMPLETO y lo parsea. Es a proposito: brand-constants
exige que el titulo de la portada y el publicado sean el mismo string, y la unica
forma de garantizarlo es que la imagen se hornee desde ese string y de ningun otro.
Si el titulo no sigue la formula, el script para -- eso tambien lint del titulo.

Fuente canonica: episode-launch/docs/brand-constants.md
"""
import os
import re
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

if len(sys.argv) < 3:
    sys.exit('Uso: python portada-ep-compose.py "<titulo publicado>" <salida.png>\n'
             '     python portada-ep-compose.py @titulo.txt <salida.png>')
full_title = sys.argv[1]
out_path = sys.argv[2]

# En PowerShell 5.1 los acentos se pierden al pasar por argv, y en espanol el
# titulo SIEMPRE los lleva. Con "@ruta" se lee de un archivo UTF-8 y llega intacto.
if full_title.startswith("@"):
    import io
    full_title = io.open(full_title[1:], encoding="utf-8").read().strip()

FD = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Fonts")
DISP = os.path.join(FD, "CabinetGrotesk-Extrabold.otf")
BODY = os.path.join(FD, "Supreme-Medium.otf")
MONO = os.path.join(FD, "MartianMono-Variable.ttf")
for _p in (DISP, BODY, MONO):
    if not os.path.exists(_p):
        sys.exit("FALTA LA FUENTE: %s\nVer brand-constants.md seccion Fuentes." % _p)

VOID = (14, 17, 19)
STEEL = (57, 67, 74)
CREAM = (244, 239, 231)
SIGNAL = (255, 61, 0)
MUTED = (139, 148, 146)
KICKER = "GESTIÓN  ·  CALIDAD  ·  LIDERAZGO"
BRAND = "BEHIND THE QUEUE"

# --- parseo del titulo: EP.NN <guion> Ancla: aterrizaje ---------------------
m = re.match(r"^\s*(EP\.\d{2})\s*[—\-–]\s*(.+?)\s*:\s*(.+?)\s*$", full_title)
if not m:
    sys.exit(
        'TITULO FUERA DE FORMULA: %r\n'
        'Debe ser "EP.NN — Ancla nombrada: que es, en llano, en usted".\n'
        'Ver guion-style-btq.md seccion Titulo.' % full_title)
ep_label, anchor, landing = m.group(1), m.group(2), m.group(3)
if anchor.lower().startswith(("la ", "el ", "los ", "las ")):
    sys.exit('ANCLA SOSPECHOSA: %r empieza como titulo de libro o eslogan.\n'
             'Debe ser un nombre propio al frente (ej. "Ley de Goodhart",\n'
             '"Efecto Hawthorne", "Philip Crosby"). Ver guion-style-btq.md.' % anchor)

def mono(px):
    f = ImageFont.truetype(MONO, px)
    f.set_variation_by_name("Regular")   # el default de la variable es SemiExpanded
    return f


def envolver(words, font, maxw):
    """Reparte las palabras del ancla en lineas que quepan en maxw.

    Con la formula vieja el ancla era un nombre propio de 2 palabras y una
    palabra por linea funcionaba. Con la formula invertida (2026-07-28) el
    ancla es la frase del problema -- 10 palabras en EP.024 -- y una por linea
    encogia el tipo a 84 px en 16:9. Se envuelve por ancho REAL de la fuente,
    no por conteo de caracteres.
    """
    lineas, actual = [], []
    for w in words:
        tentativa = " ".join(actual + [w])
        if actual and font.getlength(tentativa) > maxw:
            lineas.append(" ".join(actual))
            actual = [w]
        else:
            actual.append(w)
    if actual:
        lineas.append(" ".join(actual))
    return lineas


def render(W, H):
    """Compone la portada a cualquier aspect ratio.

    El cuerpo tipografico se escala contra la dimension MENOR: si se escalara
    contra el ancho, en 16:9 el ancla saldria gigante y en 9:16 minuscula.
    """
    U = min(W, H)
    im = Image.new("RGB", (W, H), VOID)
    d = ImageDraw.Draw(im)
    MX, MY = int(W * 0.06), int(H * 0.06)
    rule_w = max(2, int(U * 0.0022))

    # --- cabecera: marca + EP ---
    fb = mono(int(U * 0.0165))
    d.text((MX, MY), BRAND, font=fb, fill=MUTED)
    ep_w = d.textlength(ep_label, font=fb)
    d.text((W - MX - ep_w, MY), ep_label, font=fb, fill=SIGNAL)
    head_rule = MY + fb.getbbox(BRAND)[3] + int(U * 0.018)
    d.line([(MX, head_rule), (W - MX, head_rule)], fill=STEEL, width=rule_w)

    # --- pie: kicker ---
    fk = mono(int(U * 0.0165))
    kicker_y = H - MY - fk.getbbox(KICKER)[3]
    foot_rule = kicker_y - int(U * 0.026)

    # --- aterrizaje: texto llano, hasta 3 lineas ---
    lsize = int(U * 0.030)
    while lsize > int(U * 0.017):
        fl = ImageFont.truetype(BODY, lsize)
        chars = max(12, int((W - 2 * MX) / (lsize * 0.50)))
        llines = textwrap.wrap(landing, width=chars, break_long_words=False)
        if len(llines) <= 3 and max(fl.getlength(x) for x in llines) <= W - 2 * MX:
            break
        lsize -= 2
    llh = int(lsize * 1.34)
    lblock = llh * (len(llines) - 1) + fl.getbbox(llines[-1])[3]

    # --- ancla: envuelta por ancho, ultima palabra en Senal ---
    # Cabe por ANCHO y por ALTO: en 16:9 el limite real es el alto disponible.
    words = [w.upper() for w in anchor.split()]
    gap = int(U * 0.045)
    room = (foot_rule - int(U * 0.03)) - (head_rule + int(U * 0.03)) - gap - lblock
    asize = int(U * 0.20)
    while asize > 40:
        fa = ImageFont.truetype(DISP, asize)
        alineas = envolver(words, fa, W - 2 * MX)
        # Paso UNIFORME entre lineas base. Todas usan la misma fuente, asi que
        # un mismo origen mas un paso constante ya las deja parejas; el paso
        # solo tiene que dar para que la tinta mas alta (la tilde de la E) no
        # toque la mas baja (la cola de la Q) de la linea de arriba. Con el
        # avance fijo de antes (asize * 0.86) chocaban -- visto en EP.024.
        cajas = [fa.getbbox(t) for t in alineas]
        atop = min(b[1] for b in cajas)
        abot = max(b[3] for b in cajas)
        alh = (abot - atop) + int(asize * 0.10)
        ablock = alh * (len(alineas) - 1) + (abot - atop)
        # El chequeo de ancho NO es redundante con envolver(): una palabra sola
        # mas ancha que la caja no se puede partir, asi que envolver() la deja
        # pasar y solo bajar el tamano la mete. Sin esto, HAWTHORNE se sale.
        if max(fa.getlength(t) for t in alineas) <= W - 2 * MX and ablock <= room:
            break
        asize -= 4

    # --- centrado optico entre las dos reglas ---
    avail_top, avail_bot = head_rule + int(U * 0.03), foot_rule - int(U * 0.03)
    y = avail_top + ((avail_bot - avail_top) - (ablock + gap + lblock)) // 2
    for i, texto in enumerate(alineas):
        if i == len(alineas) - 1 and " " in texto:
            # Ultima linea: solo la ULTIMA PALABRA en Senal, no la linea entera.
            cabeza, cola = texto.rsplit(" ", 1)
            cabeza += " "
            d.text((MX, y - atop + i * alh), cabeza, font=fa, fill=CREAM)
            d.text((MX + fa.getlength(cabeza), y - atop + i * alh), cola,
                   font=fa, fill=SIGNAL)
        else:
            d.text((MX, y - atop + i * alh), texto, font=fa,
                   fill=SIGNAL if i == len(alineas) - 1 else CREAM)
    ly = y + ablock + gap
    for line in llines:
        d.text((MX, ly), line, font=fl, fill=MUTED)
        ly += llh

    d.line([(MX, foot_rule), (W - MX, foot_rule)], fill=STEEL, width=rule_w)
    d.text((MX, kicker_y), KICKER, font=fk, fill=MUTED)
    return im, asize, lsize, len(llines)


# Los tres sufijos y tamanos que exige scripts/verify_assets.py.
VARIANTS = [("COVER-1x1", 3000, 3000), ("COVER-16x9", 1920, 1080),
            ("COVER-9x16", 1080, 1920)]

base, ext = os.path.splitext(out_path)
base = re.sub(r"-(COVER-\w+)$", "", base)   # idempotente si ya trae sufijo
for suffix, W, H in VARIANTS:
    im, asize, lsize, nlines = render(W, H)
    p = "%s-%s%s" % (base, suffix, ext)
    im.save(p)
    print("%-12s %4dx%-4d  ancla %3d px  aterrizaje %2d px en %d linea/s"
          % (suffix, W, H, asize, lsize, nlines))
    if suffix == "COVER-1x1":
        im.save(base + "-COVER-1x1-q92.jpg", "JPEG", quality=92,
                optimize=True, subsampling=0)
        for px in (300, 96):   # contraprueba de legibilidad, brand-constants
            im.resize((px, px), Image.LANCZOS).save("%s-%d%s" % (base, px, ext))

print("\nancla      : %s" % anchor)
print("aterrizaje : %s" % landing)
