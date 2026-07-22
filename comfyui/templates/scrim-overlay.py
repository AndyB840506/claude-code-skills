# Degradados oscuros (scrims) para que tipografia clara lea sobre una escena clara.
#
# Necesario cuando la escena generada tiene zonas luminosas justo donde va el wordmark
# o el bloque de titulo (mordio 2026-07-22, portada MPD T2: el tercio superior era marmol
# palido y el wordmark blanco se perdia). Aplicar ANTES de componer la tipografia; el
# resultado se pasa como `scene_path` a *-portada-compose.py.
#
# Importable: from scrim_overlay import add_scrims
from PIL import Image, ImageDraw


def add_scrims(src_path, dst_path, top_frac=0.26, top_alpha=205,
               bottom_start=0.68, bottom_end=0.92, bottom_alpha=150,
               dark=(8, 8, 8)):
    """Oscurece la franja superior (degradado a transparente hacia abajo) y la franja
    inferior (degradado a transparente hacia arriba, solido de bottom_end en adelante).

    top_frac      : alto de la franja superior como fraccion de la imagen
    top_alpha     : opacidad maxima arriba (0-255)
    bottom_start/end : fracciones donde arranca y termina el degradado inferior
    bottom_alpha  : opacidad del velo inferior
    dark          : color del velo (casi negro, no negro puro, para no marcar costura)
    """
    im = Image.open(src_path).convert("RGB")
    W, H = im.size
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)

    top_h = int(H * top_frac)
    for y in range(top_h):
        a = int(top_alpha * (1 - y / top_h) ** 1.35)
        d.line([(0, y), (W, y)], fill=a)

    b0, b1 = int(H * bottom_start), int(H * bottom_end)
    for y in range(b0, b1):
        t = (y - b0) / max(1, (b1 - b0))
        d.line([(0, y), (W, y)], fill=int(bottom_alpha * t ** 1.2))
    d.rectangle([0, b1, W, H], fill=bottom_alpha)

    out = Image.composite(Image.new("RGB", (W, H), dark), im, mask)
    out.save(dst_path)
    return dst_path
