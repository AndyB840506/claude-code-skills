# -*- coding: utf-8 -*-
"""Assets de marca de BTQ — direccion v4 minimalista, TIPOGRAFIA PURA.

No usa ComfyUI ni ningun modelo: todo es determinista con PIL. Se acabaron los
sellos alucinados, el veto de anillos y las 6 rondas por objeto.

Genera, en una corrida:
  - portada del show 3000x3000 (+ JPEG y contrapruebas 300 / 96)
  - avatar de YouTube 800x800, seguro para recorte circular (+ preview)
  - banner de YouTube 2048x1152 con el texto dentro del safe area 1235x338

Uso: python brand-covers-compose.py <carpeta_salida>

Concepto: el nombre hace el trabajo. "QUEUE" en Señal es el unico elemento
saturado -- la palabra ES la señal, no hay objeto que interpretar.
Fuente canonica: episode-launch/docs/brand-constants.md
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

out_dir = sys.argv[1] if len(sys.argv) > 1 else r"E:\AI\outputs\BTQ-brand"
os.makedirs(out_dir, exist_ok=True)

FD = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Fonts")
DISP = os.path.join(FD, "CabinetGrotesk-Extrabold.otf")
MONO = os.path.join(FD, "MartianMono-Variable.ttf")
for _p in (DISP, MONO):
    if not os.path.exists(_p):
        sys.exit("FALTA LA FUENTE: %s\nVer brand-constants.md seccion Fuentes." % _p)

VOID = (14, 17, 19)
CREAM = (244, 239, 231)
SIGNAL = (255, 61, 0)
MUTED = (139, 148, 146)
KICKER = "GESTIÓN  ·  CALIDAD  ·  LIDERAZGO"
LINES = [("BEHIND", CREAM), ("THE", CREAM), ("QUEUE", SIGNAL)]


def mono(px):
    f = ImageFont.truetype(MONO, px)
    f.set_variation_by_name("Regular")   # el default de la variable es SemiExpanded
    return f


def block_metrics(font, lines, lh):
    """Alto real del bloque: el avance de linea NO sirve porque la cola de la Q
    de QUEUE baja por debajo de la ultima linea."""
    top = font.getbbox(lines[0][0])[1]
    bottom = lh * (len(lines) - 1) + font.getbbox(lines[-1][0])[3]
    return top, bottom, bottom - top


def draw_block(d, x, y_top, font, lines, lh):
    top = font.getbbox(lines[0][0])[1]
    for i, (txt, color) in enumerate(lines):
        d.text((x, y_top - top + i * lh), txt, font=font, fill=color)


# ---------------------------------------------------------------- portada 1:1
S = 3000
im = Image.new("RGB", (S, S), VOID)
d = ImageDraw.Draw(im)
M = int(S * 0.06)

size = int(S * 0.188)
fw = ImageFont.truetype(DISP, size)
lh = int(size * 0.86)
_, _, h = block_metrics(fw, LINES, lh)

fk = mono(int(S * 0.019))
kicker_y = S - M - fk.getbbox(KICKER)[3]
# centrado optico dentro del espacio util (arriba el margen, abajo el kicker)
y_top = M + ((kicker_y - int(S * 0.03)) - M - h) // 2
draw_block(d, M, y_top, fw, LINES, lh)
d.text((M, kicker_y), KICKER, font=fk, fill=MUTED)

cover = os.path.join(out_dir, "BTQ-COVER.png")
im.save(cover)
im.save(cover.replace(".png", "-q92.jpg"), "JPEG", quality=92, optimize=True, subsampling=0)
for px in (300, 96):
    im.resize((px, px), Image.LANCZOS).save(cover.replace(".png", "-%d.png" % px))
print("portada 1:1 lista — wordmark %d px, bloque %d px" % (size, h))

# ------------------------------------------------------- avatar YouTube 800x800
# Se recorta en circulo: el wordmark de 3 lineas se perderia por los lados.
# Marca corta centrada, con la Q en Señal para mantener el codigo de color.
A = 800
av = Image.new("RGB", (A, A), VOID)
d = ImageDraw.Draw(av)
fa = ImageFont.truetype(DISP, int(A * 0.34))
parts = [("BT", CREAM), ("Q", SIGNAL)]
widths = [d.textlength(t, font=fa) for t, _ in parts]
bb = fa.getbbox("BTQ")
x = (A - sum(widths)) / 2
y = (A - (bb[3] - bb[1])) / 2 - bb[1]
for (t, c), w in zip(parts, widths):
    d.text((x, y), t, font=fa, fill=c)
    x += w
av.save(os.path.join(out_dir, "BTQ-yt-avatar-800.png"))

prev = Image.new("RGB", (A, A), (32, 34, 36))
mask = Image.new("L", (A, A), 0)
ImageDraw.Draw(mask).ellipse([0, 0, A - 1, A - 1], fill=255)
prev.paste(av, (0, 0), mask)
prev.save(os.path.join(out_dir, "BTQ-yt-avatar-800-PREVIEW-circulo.png"))
print("avatar listo (+ preview del recorte circular)")

# ------------------------------------------------------ banner YouTube 2048x1152
BW, BH, SAFE_W, SAFE_H = 2048, 1152, 1235, 338
sx0, sy0 = (BW - SAFE_W) // 2, (BH - SAFE_H) // 2
bn = Image.new("RGB", (BW, BH), VOID)
d = ImageDraw.Draw(bn)

BLINES = [("BEHIND THE", CREAM), ("QUEUE", SIGNAL)]
fk2 = mono(24)
bsize = 150
while bsize > 50:
    fb = ImageFont.truetype(DISP, bsize)
    blh = int(bsize * 0.86)
    _, _, bh = block_metrics(fb, BLINES, blh)
    total = bh + 34 + fk2.getbbox(KICKER)[3]
    if total <= SAFE_H - 20:
        break
    bsize -= 2
ytop = sy0 + (SAFE_H - total) // 2
draw_block(d, sx0, ytop, fb, BLINES, blh)
d.text((sx0, ytop + bh + 34), KICKER, font=fk2, fill=MUTED)
bn.save(os.path.join(out_dir, "BTQ-yt-banner-2048x1152.png"))
bn.save(os.path.join(out_dir, "BTQ-yt-banner-2048x1152.jpg"),
        "JPEG", quality=92, optimize=True, subsampling=0)

guide = bn.copy()
gd = ImageDraw.Draw(guide)
gd.rectangle([sx0, sy0, sx0 + SAFE_W, sy0 + SAFE_H], outline=SIGNAL, width=4)
gd.text((sx0 + 8, sy0 - 34), "SAFE AREA 1235x338 - no subir esta version",
        font=mono(20), fill=SIGNAL)
guide.save(os.path.join(out_dir, "BTQ-yt-banner-GUIA-safearea.png"))
print("banner listo — wordmark %d px, bloque %d px (safe area %d)" % (bsize, total, SAFE_H))

print()
for f in sorted(os.listdir(out_dir)):
    p = os.path.join(out_dir, f)
    print("  %-44s %6.0f KB  %s" % (f, os.path.getsize(p) / 1024, Image.open(p).size))
