#!/usr/bin/env python
"""Compuerta MECANICA para un deploy de sitio (BTQ website).

A diferencia de verify_assets.py (portadas/quote cards de un episodio), esto chequea
lo que un deploy de vercel realmente publica: la og-image y el HTML servido. Solo
reglas mecanicas -- exit 0/1, sin juicio, sin modo warnings. Lo visual (typo horneado,
aros, escena) NO se detecta aqui; eso es lectura de imagen (stage 2).

Uso:
    python scripts/verify_web.py <dir_del_sitio>
    python scripts/verify_web.py btq-production/website

Reglas (fuente entre parentesis):
- og-image.png <= 500 KB           (brand-constants: comprimir bajo 500 KB)
- og-image.png == 1600x900         (artwork-general-v3.md linea 3)
- og-image.png esquina != #000000  (negro de marca, no negro puro)
- cada <img> con width en su style lleva height:auto en el MISMO style
  (CLAUDE.md, Limites de lo publicable -- por <img>, NO un grep global)
"""
import glob
import os
import re
import sys

from PIL import Image

OG_MAX_BYTES = 500 * 1024
OG_SIZE = (1600, 900)
PURE_BLACK = (0, 0, 0)
IMG_TAG = re.compile(r"<img\b[^>]*>", re.I | re.S)
STYLE_ATTR = re.compile(r"style\s*=\s*(['\"])(.*?)\1", re.I | re.S)
WIDTH_RULE = re.compile(r"(?<![\w-])width\s*:\s*[\d.]", re.I)
HEIGHT_AUTO = re.compile(r"(?<![\w-])height\s*:\s*auto", re.I)


def check_og(path):
    fails = []
    size = os.path.getsize(path)
    if size > OG_MAX_BYTES:
        fails.append("og-image.png: %d KB, limite 500 KB (sobran %d KB)"
                     % (size // 1024, (size - OG_MAX_BYTES) // 1024))
    with Image.open(path) as im:
        if im.size != OG_SIZE:
            fails.append("og-image.png: %dx%d, se esperaba %dx%d"
                         % (im.size[0], im.size[1], OG_SIZE[0], OG_SIZE[1]))
        if im.convert("RGB").getpixel((0, 0)) == PURE_BLACK:
            fails.append("og-image.png: esquina es negro puro #000000")
    return fails


def check_html(path):
    fails = []
    html = open(path, encoding="utf-8", errors="replace").read()
    for i, tag in enumerate(IMG_TAG.findall(html), 1):
        m = STYLE_ATTR.search(tag)
        style = m.group(2) if m else ""
        if WIDTH_RULE.search(style) and not HEIGHT_AUTO.search(style):
            snippet = re.sub(r"\s+", " ", tag)[:90]
            fails.append("%s: <img> #%d tiene width sin height:auto en el mismo style -> %s"
                         % (os.path.basename(path), i, snippet))
    return fails


def main():
    if len(sys.argv) != 2:
        print("uso: python verify_web.py <dir_del_sitio>")
        return 2
    root = sys.argv[1]
    if not os.path.isdir(root):
        print("FATAL: no existe la carpeta %s" % root)
        return 2

    fails = []
    print("=== deploy web: %s ===" % root)

    og = os.path.join(root, "og-image.png")
    if os.path.exists(og):
        f = check_og(og)
        print("   og-image.png            %s" % ("PASS" if not f else "FAIL"))
        fails.extend(f)
    else:
        fails.append("no existe og-image.png en %s" % root)

    index = os.path.join(root, "index.html")
    if os.path.exists(index):
        f = check_html(index)
        print("   index.html (<img> rules) %s" % ("PASS" if not f else "FAIL"))
        fails.extend(f)
    else:
        fails.append("no existe index.html en %s" % root)

    print()
    if fails:
        print("FALLOS (%d):" % len(fails))
        for f in fails:
            print("  - %s" % f)
        print("\nDEPLOY GATE: FAIL -- no publicar hasta resolver.")
        return 1
    print("DEPLOY GATE MECANICO: PASS")
    print("Recordatorio: esto NO valida el contenido visual de la og-image (typo, aros).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
