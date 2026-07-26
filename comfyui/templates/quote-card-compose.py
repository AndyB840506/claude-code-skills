# -*- coding: utf-8 -*-
"""Quote cards de BTQ — direccion v4, TIPOGRAFIA PURA.

No usa ComfyUI ni ningun modelo: todo determinista con PIL, igual que
brand-covers-compose.py y portada-ep-compose.py.

Cambio 2026-07-25 (decision de Andy): antes cada card llevaba una escena
renderizada en la mitad derecha. Eso era v3 y sobrevivio por descuido al giro a
tipografia pura -- generaba anillos vetados, fondos de estudio blancos y una
ronda de iteraciones por card. La cita ES el contenido; no necesita ilustracion.

Uso CLI: python quote-card-compose.py "<cita>" "<atribucion>" <salida.png>
Importable: compose_quote_card(quote, attribution, out_path)
Para citas con tildes preferir el import directo -- el escaping de shell las pierde.
"""
import os
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
VOID = (14, 17, 19)        # #0E1113 — nunca negro puro
CREAM = (244, 239, 231)    # #F4EFE7 — cita
SIGNAL = (255, 61, 0)      # #FF3D00 — atribucion, UNICO elemento saturado
GRID = (31, 36, 40)        # #1F2428 — rejilla de ventilacion, marca de agua

MARGIN_X = 150
MARGIN_Y = 130

_FD = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Fonts")
QUOTE_FONT = os.path.join(_FD, "Supreme-Bold.otf")
ATTR_FONT = os.path.join(_FD, "MartianMono-Variable.ttf")
for _p in (QUOTE_FONT, ATTR_FONT):
    if not os.path.exists(_p):
        sys.exit("FALTA LA FUENTE: %s\nVer brand-constants.md seccion Fuentes." % _p)


def _attr(px):
    f = ImageFont.truetype(ATTR_FONT, px)
    f.set_variation_by_name("Regular")   # el default de la variable es SemiExpanded
    return f


def _fit(quote, max_w, max_h):
    """Baja el cuerpo hasta que la cita envuelta quepa a lo ancho y a lo alto."""
    for size in range(104, 39, -2):
        font = ImageFont.truetype(QUOTE_FONT, size)
        wrapped = textwrap.wrap(quote, width=max(12, int(max_w / (size * 0.50))),
                                break_long_words=False)
        line_h = int(size * 1.24)
        if (max((font.getlength(l) for l in wrapped), default=0) <= max_w
                and line_h * len(wrapped) <= max_h):
            return font, wrapped, line_h, size
    raise ValueError("cita demasiado larga para la card: %r" % quote)


def compose_quote_card(quote, attribution, out_path):
    card = Image.new("RGB", (W, H), VOID)
    d = ImageDraw.Draw(card)

    # Rejilla vertical fina, como las ranuras de ventilacion de un panel de equipo.
    for x in range(0, W, 24):
        d.line([(x, 0), (x, H)], fill=GRID, width=1)

    attr_size = 30
    af = _attr(attr_size)
    attr_h = af.getbbox(attribution)[3]

    avail_w = W - 2 * MARGIN_X
    avail_h = H - 2 * MARGIN_Y - attr_h - 60
    font, lines, line_h, size = _fit(quote, avail_w, avail_h)

    block_h = line_h * len(lines) + 60 + attr_h
    y = (H - block_h) // 2 - font.getbbox(lines[0])[1]

    for line in lines:
        d.text((MARGIN_X, y), line, font=font, fill=CREAM)
        y += line_h

    d.text((MARGIN_X, y + 60), attribution, font=af, fill=SIGNAL)

    card.save(out_path)
    print("guardada %s  (cuerpo %dpx, %d lineas)" % (out_path, size, len(lines)))


if __name__ == "__main__":
    compose_quote_card(sys.argv[1], sys.argv[2], sys.argv[3])
