# -*- coding: utf-8 -*-
"""Deriva los assets de canal de YouTube desde la escena de la portada BTQ v4.

Por que no sirve el cuadrado de Spotify tal cual:
  - el AVATAR se recorta en circulo -> el wordmark de la esquina se pierde
  - el BANNER es una franja muy ancha con "safe area" central

Uso: python youtube-assets-compose.py <escena_4x.png> <carpeta_salida>

Medidas usadas (verificar en la UI de YouTube antes de subir, las specs cambian):
  avatar  800x800,  se muestra recortado en circulo
  banner  2048x1152, safe area central 1235x338 (lo unico visible en todo device)
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

scene_path = sys.argv[1]
out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)

FD = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Fonts")
DISP = os.path.join(FD, "CabinetGrotesk-Extrabold.otf")
MONO = os.path.join(FD, "MartianMono-Variable.ttf")

VOID = (14, 17, 19)
STEEL = (57, 67, 74)
CREAM = (244, 239, 231)
MUTED = (139, 148, 146)
KICKER = "GESTIÓN  ·  CALIDAD  ·  LIDERAZGO"

scene = Image.open(scene_path).convert("RGB")


def floor_brand(img):
    a = np.asarray(img).copy()
    for c, v in enumerate(VOID):
        ch = a[:, :, c]
        ch[ch < v] = v
    return Image.fromarray(a)


scene = floor_brand(scene)
W, H = scene.size


def panel_bbox(img):
    """Caja del objeto: lo que resalta sobre el fondo oscuro."""
    g = np.asarray(img.convert("L")).astype(int)
    mask = g > (int(np.median(g)) + 18)
    ys, xs = np.where(mask)
    return xs.min(), ys.min(), xs.max(), ys.max()


x0, y0, x1, y1 = panel_bbox(scene)
print("objeto detectado en:", (x0, y0, x1, y1), "de", scene.size)

# ---------------- AVATAR 800x800 (recorte circular) ----------------
# El objeto se centra y se deja aire para que el circulo no lo muerda.
cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
half = int(max(x1 - x0, y1 - y0) * 0.78)
crop = scene.crop((max(0, cx - half), max(0, cy - half),
                   min(W, cx + half), min(H, cy + half))).resize((800, 800), Image.LANCZOS)
crop.save(os.path.join(out_dir, "BTQ-yt-avatar-800.png"))

# vista previa con el recorte circular real, para juzgar lo que YouTube va a mostrar
prev = Image.new("RGB", (800, 800), (32, 34, 36))
mask = Image.new("L", (800, 800), 0)
ImageDraw.Draw(mask).ellipse([0, 0, 799, 799], fill=255)
prev.paste(crop, (0, 0), mask)
prev.save(os.path.join(out_dir, "BTQ-yt-avatar-800-PREVIEW-circulo.png"))
print("avatar listo (+ preview del recorte circular)")

# ---------------- BANNER 2048x1152 ----------------
BW, BH = 2048, 1152
SAFE_W, SAFE_H = 1235, 338
sx0, sy0 = (BW - SAFE_W) // 2, (BH - SAFE_H) // 2

banner = Image.new("RGB", (BW, BH), VOID)

# el objeto a la derecha; el fondo de la escena es casi uniforme, asi que
# se funde con un scrim horizontal en vez de dejar costura
obj = scene.resize((BH, BH), Image.LANCZOS)
banner.paste(obj, (BW - BH + 120, 0))
lay = Image.new("RGBA", (int(BH * 0.55), BH))
ld = ImageDraw.Draw(lay)
for i in range(lay.width):
    t = i / max(1, lay.width - 1)
    ld.line([(i, 0), (i, BH)], fill=VOID + (int(255 * (1 - t) ** 1.2),))
px = BW - BH + 120
banner.paste(Image.alpha_composite(
    banner.crop((px, 0, px + lay.width, BH)).convert("RGBA"), lay).convert("RGB"), (px, 0))

d = ImageDraw.Draw(banner)
fm = ImageFont.truetype(MONO, 24)
fm.set_variation_by_name("Regular")


def block_layout(size):
    """Devuelve (font, y de cada linea, y de la regla, y del kicker, alto total).
    Se mide en vez de estimarse: la cola de la Q hace que el alto real no
    coincida con el avance de linea."""
    f = ImageFont.truetype(DISP, size)
    lh = int(size * 0.92)
    ys = [0, lh]
    ink = ys[-1] + f.getbbox("THE QUEUE")[3]
    ry_ = ink + int(size * 0.23)
    ky = ry_ + int(size * 0.20)
    return f, ys, ry_, ky, ky + fm.getbbox(KICKER)[3]


# encoger hasta que TODO el bloque quepa dentro del safe area
size = 132
while size > 60:
    fw, ys, ry_rel, ky_rel, total = block_layout(size)
    if total <= SAFE_H - 24:
        break
    size -= 2
print("wordmark del banner a %d px, bloque de %d px (safe area %d)" % (size, total, SAFE_H))

top = sy0 + (SAFE_H - total) // 2
for line, dy in zip(["BEHIND", "THE QUEUE"], ys):
    d.text((sx0, top + dy), line, font=fw, fill=CREAM)
d.line([(sx0, top + ry_rel), (sx0 + int(size * 4.8), top + ry_rel)], fill=STEEL, width=4)
d.text((sx0, top + ky_rel), KICKER, font=fm, fill=MUTED)

banner.save(os.path.join(out_dir, "BTQ-yt-banner-2048x1152.png"))
banner.save(os.path.join(out_dir, "BTQ-yt-banner-2048x1152.jpg"),
            "JPEG", quality=92, optimize=True, subsampling=0)

# guia visual del safe area, SOLO para revisar -- no se sube
guide = banner.copy()
gd = ImageDraw.Draw(guide)
gd.rectangle([sx0, sy0, sx0 + SAFE_W, sy0 + SAFE_H], outline=(255, 61, 0), width=4)
gd.text((sx0 + 8, sy0 - 34), "SAFE AREA 1235x338 - no subir esta version",
        font=ImageFont.truetype(MONO, 20), fill=(255, 61, 0))
guide.save(os.path.join(out_dir, "BTQ-yt-banner-GUIA-safearea.png"))
print("banner listo (+ guia de safe area)")

for f in sorted(os.listdir(out_dir)):
    p = os.path.join(out_dir, f)
    print("  %-46s %6.0f KB  %s" % (f, os.path.getsize(p) / 1024, Image.open(p).size))
