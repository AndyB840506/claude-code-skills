# -*- coding: utf-8 -*-
"""Teaser de revelacion: la portada de T2 bajo una sabana guardapolvo.

La tela se genero aislada sobre negro (no la escena completa con un cuadro debajo)
justo para esto: asi el que decide cuanto artwork se revela es este compositor, no el
modelo. Se revela el tercio superior — el wordmark y las calaveras del marmol — y la
sabana sigue tapando el titulo de la temporada, que es lo que se guarda.
"""
import importlib.util
import os
import pathlib
from PIL import Image, ImageDraw, ImageFilter, ImageFont

F_DISPLAY = "C:/Windows/Fonts/BOOKOSB.TTF"
WORDMARK = "MR. PUTRID'S DEN"
POLVO = (231, 221, 201)
BRASA = (217, 191, 122)
SCENE = r"E:\Podcast\MPD\Temporada 2\artwork\MPD-T2-ESCENA-OFICIAL-3000.jpg"

T = pathlib.Path(r"c:\Users\andre\.claude\skills\comfyui\templates")
_spec = importlib.util.spec_from_file_location("night_grade", T / "night_grade.py")
_ng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ng)

CLOTH = r"E:\AI\outputs\MPD-T2-sabana_00001_.png"
COVER = r"E:\Podcast\MPD\Temporada 2\artwork\MPD-T2-PORTADA-CONTEXTO-3000.jpg"
OUT_DIR = r"E:\Podcast\MPD\Temporada 2\redes\teasers"
S = 1080
CLOTH_THRESHOLD = 88     # por encima de esto es tela; el piso del fondo queda debajo


def build(size, name, cover_shift=0.0):
    W, H = size
    cloth = Image.open(CLOTH).convert("RGB").resize((W, W), Image.LANCZOS)
    if H != W:                       # story: la tela se ancla abajo
        canvas = Image.new("RGB", (W, H), (0, 0, 0))
        canvas.paste(cloth, (0, H - W))
        cloth = canvas

    # Mascara de tela por luminancia. El fondo negro de arriba y el piso oscuro de la
    # esquina caen por debajo del umbral, que es justo lo que se quiere.
    lum = cloth.convert("L")
    mask = lum.point(lambda v: 255 if v > CLOTH_THRESHOLD else 0)

    # Borde superior de la tela, columna por columna. Lo que quede ARRIBA de ese borde
    # es lo que revela la portada; debajo manda la tela.
    px = mask.load()
    reveal = Image.new("L", (W, H), 0)
    rd = ImageDraw.Draw(reveal)
    for x in range(W):
        top = H
        for y in range(H):
            if px[x, y] > 0:
                top = y
                break
        if top > 0:
            rd.line([(x, 0), (x, top - 1)], fill=255)
    reveal = reveal.filter(ImageFilter.GaussianBlur(2.5))

    if H == W:
        cover = Image.open(COVER).convert("RGB").resize((W, W), Image.LANCZOS)
    else:
        # En vertical NO se usa la portada compuesta. Al llenar el cuadro, el titulo
        # "Misterios y Leyendas" queda a una altura donde la tela ya no cubre todo el
        # ancho y se asomaba un pedazo ("end") por el borde derecho — el teaser
        # revelaba justo lo que debe esconder. Se parte de la escena SIN texto y el
        # wordmark se dibuja aca, que es lo unico que se quiere mostrar.
        cover = Image.open(SCENE).convert("RGB").resize((H, H), Image.LANCZOS)
        x0 = (H - W) // 2
        cover = cover.crop((x0, 0, x0 + W, H))
        cd = ImageDraw.Draw(cover)
        wm_size = int(W * 0.062)
        wm_font = ImageFont.truetype(F_DISPLAY, wm_size)
        widths = [cd.textlength(c, font=wm_font) for c in WORDMARK]
        sp = int(wm_size * 0.10)
        total = sum(widths) + sp * (len(WORDMARK) - 1)
        x, y = (W - total) / 2, int(H * 0.055)
        for c, cw in zip(WORDMARK, widths):
            cd.text((x, y), c, font=wm_font, fill=POLVO)
            x += cw + sp
        rw = int(W * 0.085)
        ry = y + int(wm_size * 1.7)
        cd.rectangle([(W - rw) / 2, ry, (W + rw) / 2, ry + max(2, int(wm_size * 0.09))], fill=BRASA)

    out = Image.composite(cover, cloth, reveal)

    # Sombra que proyecta la tela sobre lo revelado: sin esto, la portada y la sabana
    # parecen dos recortes pegados en vez de una tela apoyada encima.
    shadow = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(shadow)
    for x in range(W):
        top = H
        for y in range(H):
            if px[x, y] > 0:
                top = y
                break
        sd.line([(x, max(0, top - 42)), (x, top)], fill=150)
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    out = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), out, shadow)

    # El grading unifica: la tela blanca cruda seria un segundo elemento brillante y
    # fuera de sistema. Graduada, entra en la noche azul y el unico calido sigue siendo
    # el fuego de la portada.
    out = _ng.night_grade(out)

    path = os.path.join(OUT_DIR, name)
    out.save(path, "JPEG", quality=92, optimize=True, progressive=True)
    print("  %-40s %s  %6.1f KB" % (name, "x".join(map(str, size)), os.path.getsize(path) / 1024))


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    build((S, S), "teaser-0-sabana-1080.jpg")
    build((S, 1920), "teaser-0-sabana-story.jpg", cover_shift=0.30)
