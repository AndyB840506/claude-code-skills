#!/usr/bin/env python
"""Compuerta mecanica de assets para un episodio.

Solo hace lo que una maquina puede afirmar sin juicio: existencia de variantes,
dimensiones, aspect ratio, negro de marca y limites de caracteres. Los motivos
visuales (anillos, typos, silueta plana) NO se detectan aqui -- van al stage 2,
la lectura directa de la imagen contra scripts/banned-patterns.json.

Uso:
    python scripts/verify_assets.py EP022
    python scripts/verify_assets.py EP022 --root "E:\\Podcast\\BTQ\\EP 22"

Sale con codigo != 0 si algo falla. No hay modo warnings-only.
"""
import argparse
import json
import os
import re
import sys

from PIL import Image

PURE_BLACK = (0, 0, 0)

# El negro de marca cambia por show -- un tope global reprobaria MPD y CCC enteros.
# TOLERANCIA calibrada contra el set aprobado de BTQ EP.022, que da (7,6,6),
# (10,10,10) y (14,14,15): por eso NO se puede exigir igualdad exacta al valor
# nominal, solo que el pixel caiga dentro de la banda oscura de ese show.
TOLERANCE = 14
SHOWS = {
    "btq": {"brand_black": (10, 10, 10), "hex": "#0A0A0A",
            "source": "episode-launch/docs/brand-constants.md"},
    "mpd": {"brand_black": (26, 26, 26), "hex": "#1A1A1A",
            "source": "comfyui/templates/mpd-portada-compose.py"},
    "ccc": {"brand_black": (20, 20, 20), "hex": "#141414",
            "source": "corporate-crime-confidential-production/artwork-general.md"},
}

# (sufijo de archivo, ancho, alto). El aspect se deriva, no se declara dos veces.
VARIANTS = {
    "COVER-1x1": (3000, 3000),
    "COVER-16x9": (1920, 1080),
    "COVER-9x16": (1080, 1920),
}
CARD_RE = re.compile(r"-CARD\d+-16x9\.png$", re.I)
CARD_SIZE = (1920, 1080)

# Archivos que estan en la carpeta pero NO son entregables.
EXCLUDE_RE = re.compile(r"\(|source|scene-only", re.I)

LIMITS = {"spotify_show_description": 600, "youtube_title": 100, "youtube_description": 5000}


def sample_points(im):
    """4 esquinas + 4 puntos medios de borde.

    OJO: NO todas tienen que ser negras. Las 16:9 son split 50/50 (mitad texto
    sobre negro, mitad escena) y la 16:9 de portada lleva la figura a un lado,
    asi que las esquinas del lado de la escena estan iluminadas a proposito.
    Reprobar por eso tumbaba EP.022 aprobado (verificado 2026-07-23).
    """
    w, h = im.size
    pts = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1),
           (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]
    rgb = im.convert("RGB")
    return [(p, rgb.getpixel(p)) for p in pts]


def is_void_black(px, ceiling):
    """Negro de marca real: oscuro pero NO #000000 puro."""
    return px != PURE_BLACK and max(px) <= ceiling


def check_image(path, expected, brand):
    """Devuelve lista de fallos (strings). Vacia = pasa."""
    ceiling = max(brand["brand_black"]) + TOLERANCE
    fails = []
    name = os.path.basename(path)
    try:
        im = Image.open(path)
    except Exception as exc:
        return ["%s: no se pudo abrir (%s)" % (name, exc)]
    with im:
        w, h = im.size
        ew, eh = expected
        if (w, h) != (ew, eh):
            fails.append("%s: dimensiones %dx%d, se esperaban %dx%d" % (name, w, h, ew, eh))
        # aspect derivado -- atrapa estiramiento aunque las dimensiones cuadren por poco
        if abs((w / h) - (ew / eh)) > 0.001:
            fails.append("%s: aspect %.4f, se esperaba %.4f (imagen estirada)"
                         % (name, w / h, ew / eh))
        pts = sample_points(im)
        # 1. Negro puro = defecto duro, en cualquier punto.
        for pt, px in pts:
            if px == PURE_BLACK:
                fails.append("%s: pixel %s es negro puro #000000 -- el negro de marca es %s %s"
                             % (name, pt, brand["hex"], brand["brand_black"]))
        # 2. Tiene que existir region de negro de marca en algun borde.
        if not any(is_void_black(px, ceiling) for _pt, px in pts):
            muestras = ", ".join(str(px) for _pt, px in pts[:4])
            fails.append("%s: ningun borde es negro de marca %s (<=%d por canal). Muestras: %s"
                         % (name, brand["hex"], ceiling, muestras))
    return fails


def collect(root, slug):
    """Mapea variante -> ruta, ignorando backups y fuentes intermedias."""
    found, skipped = {}, []
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            if not fn.lower().endswith(".png"):
                continue
            if EXCLUDE_RE.search(fn):
                skipped.append(fn)
                continue
            if slug.upper() not in fn.upper():
                continue
            full = os.path.join(dirpath, fn)
            if CARD_RE.search(fn):
                found[fn] = (full, CARD_SIZE)
                continue
            for key, size in VARIANTS.items():
                if key.upper() in fn.upper():
                    found[key] = (full, size)
                    break
    return found, skipped


def check_lengths(meta_path):
    fails = []
    if not meta_path:
        return fails, 0
    with open(meta_path, encoding="utf-8") as fh:
        meta = json.load(fh)
    checked = 0
    for field, cap in LIMITS.items():
        if field in meta:
            checked += 1
            n = len(meta[field])
            if n > cap:
                fails.append("%s: %d caracteres, limite %d (sobran %d)" % (field, n, cap, n - cap))
            else:
                print("   %-28s %4d/%d ok" % (field, n, cap))
    return fails, checked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", help="ej. EP022")
    ap.add_argument("--root", required=True, help="carpeta con los assets renderizados")
    ap.add_argument("--show", default="btq", choices=sorted(SHOWS),
                    help="define el negro de marca (btq #0A0A0A, mpd #1A1A1A, ccc #141414)")
    ap.add_argument("--metadata", help="JSON opcional con los campos de texto publicables")
    args = ap.parse_args()

    if not os.path.isdir(args.root):
        print("FATAL: no existe la carpeta %s" % args.root)
        return 2

    brand = SHOWS[args.show]
    found, skipped = collect(args.root, args.slug)
    fails = []

    print("=== %s [%s] en %s ===" % (args.slug, args.show.upper(), args.root))
    print("negro de marca: %s %s (tope %d) -- fuente: %s"
          % (brand["hex"], brand["brand_black"],
             max(brand["brand_black"]) + TOLERANCE, brand["source"]))
    if skipped:
        print("ignorados (backup/fuente): %d" % len(skipped))

    for key in VARIANTS:
        if key not in found:
            fails.append("falta la variante %s" % key)

    if not any(CARD_RE.search(k) for k in found):
        fails.append("no se encontro ninguna quote card (-CARDn-16x9.png)")

    for key in sorted(found):
        path, expected = found[key]
        f = check_image(path, expected, brand)
        print("   %-28s %s" % (key, "PASS" if not f else "FAIL"))
        fails.extend(f)

    lf, checked = check_lengths(args.metadata)
    fails.extend(lf)

    print()
    if fails:
        print("FALLOS (%d):" % len(fails))
        for f in fails:
            print("  - %s" % f)
        print("\nGATE: FAIL")
        return 1

    print("GATE MECANICO: PASS (%d imagenes, %d campos de texto)" % (len(found), checked))
    print("PENDIENTE stage 2: leer cada imagen contra scripts/banned-patterns.json.")
    print("El script NO ve anillos, typos ni siluetas planas. Sin el stage 2 esto no esta aprobado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
