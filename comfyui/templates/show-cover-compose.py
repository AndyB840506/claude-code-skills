# -*- coding: utf-8 -*-
# ############################################################################
# MUERTO desde 2026-07-25 -- NO USAR.
# Superado por comfyui/templates/brand-covers-compose.py, que genera portada,
# avatar, banner y og-image en una sola corrida. El concepto de objeto
# renderizado (panel anunciador) murio con el giro a tipografia pura.
# ############################################################################
"""Portada del SHOW de BTQ (no de un episodio) — direccion v4 "Sala de Maquinas".
Fuente canonica de las reglas: episode-launch/docs/brand-constants.md

Diferencia con portada-compose.py: la portada del show NO lleva titulo ni EP.NN.
Solo wordmark + regla + kicker. El objeto representa al programa entero.

Uso: python show-cover-compose.py <escena_4x.png> <salida.png>

Pipeline completo, en orden:
  1. Generar la escena 1024x1024 en Z-Image (ver el prompt en brand-constants.md).
  2. Escalar x4 con RealESRGAN_x4plus via ComfyUI (nodos UpscaleModelLoader +
     ImageUpscaleWithModel) -> 4096x4096.
  3. Correr este script: remuestrea a 3000, pone piso de negro de marca, compone
     la tipografia nativa y escribe las contrapruebas de 300 y 96 px.
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

scene_path = sys.argv[1]
out_path = sys.argv[2]

FD = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Fonts")
DISP = os.path.join(FD, "CabinetGrotesk-Extrabold.otf")
MONO = os.path.join(FD, "MartianMono-Variable.ttf")
for _p in (DISP, MONO):
    if not os.path.exists(_p):
        sys.exit("FALTA LA FUENTE: %s\nVer brand-constants.md seccion Fuentes." % _p)

VOID = (14, 17, 19)
STEEL = (57, 67, 74)
CREAM = (244, 239, 231)
MUTED = (139, 148, 146)

S = 3000
# "GESTIÓN" y no "OPERACIÓN" desde el giro a alcance macro (2026-07-25): el show
# dejo de estar acotado a call center / BPO.
KICKER = "GESTIÓN  ·  CALIDAD  ·  LIDERAZGO"

im = Image.open(scene_path).convert("RGB").resize((S, S), Image.LANCZOS)

# Piso de negro de marca. Z-Image produce algunos pixeles en negro puro (0,0,0),
# que brand-constants prohibe y que verify_assets.py reprueba. Se levanta por canal,
# asi que solo toca lo que ya estaba por debajo del piso.
a = np.asarray(im).copy()
lifted = int((a.astype(int).sum(axis=2) < sum(VOID)).sum())
for c, v in enumerate(VOID):
    ch = a[:, :, c]
    ch[ch < v] = v
im = Image.fromarray(a)
print("pixeles levantados al piso de marca:", lifted)


def scrim(box, top_down):
    """Degradado a negro de marca para que el texto lea sobre cualquier escena."""
    x0, y0, x1, y1 = box
    h = y1 - y0
    lay = Image.new("RGBA", (x1 - x0, h))
    ld = ImageDraw.Draw(lay)
    for i in range(h):
        t = i / max(1, h - 1)
        ld.line([(0, i), (x1 - x0, i)],
                fill=VOID + (int(255 * ((1 - t) if top_down else t) ** 1.3),))
    im.paste(Image.alpha_composite(im.crop(box).convert("RGBA"), lay).convert("RGB"),
             (x0, y0))


scrim((0, 0, S, int(S * 0.27)), True)

d = ImageDraw.Draw(im)
M = int(S * 0.062)

fw = ImageFont.truetype(DISP, int(S * 0.108))
y = int(S * 0.058)
ink = y
for line in ["BEHIND", "THE QUEUE"]:
    d.text((M, y), line, font=fw, fill=CREAM)
    ink = y + fw.getbbox(line)[3]   # anclar al pixel de tinta: la cola de la Q
    y += int(S * 0.098)

ry = ink + int(S * 0.022)
d.line([(M, ry), (S - M, ry)], fill=STEEL, width=max(2, int(S * 0.0035)))

fm = ImageFont.truetype(MONO, int(S * 0.0175))
fm.set_variation_by_name("Regular")    # el default de la variable es SemiExpanded
d.text((M, ry + int(S * 0.024)), KICKER, font=fm, fill=MUTED)

im.save(out_path)
base, _ = os.path.splitext(out_path)
im.save(base + "-q92.jpg", "JPEG", quality=92, optimize=True, subsampling=0)
print("escrito:", out_path, im.size)
print("        ", base + "-q92.jpg",
      "%.2f MB" % (os.path.getsize(base + "-q92.jpg") / 1024 / 1024))

for px in (300, 96):
    p = "%s-%d.png" % (base, px)
    im.resize((px, px), Image.LANCZOS).save(p)
    print("contraprueba:", p)

# Chequeos del checklist de brand-constants
px = im.load()
darkest = min((sum(px[x, y]), px[x, y]) for x in range(0, S, 7) for y in range(0, S, 7))[1]
pure = any(px[x, y] == (0, 0, 0) for x in range(0, S, 5) for y in range(0, S, 5))
print("pixel mas oscuro:", darkest, "(esperado (14,17,19))")
print("negro puro presente:", pure, "(esperado False)")
