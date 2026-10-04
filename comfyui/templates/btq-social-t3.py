# Piezas de redes BTQ T3 (identidad "EN VIVO"): teaser 1:1, 3 stories 9:16, quote cards 4:5,
# lamina de reel 9:16 (+ mp4 con el clip). Compuesto con PIL, nunca generado.
# Uso: python btq-social-t3.py <out_dir>
# El texto de cada episodio vive en EP abajo. Las citas van TEXTUALES del SRT (regla de quote cards).
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
WEB = REPO / "btq-production" / "website"
LOGO = REPO / "btq-production" / "brand" / "btq-t3-logo-1024.png"
FONT = "C:/Windows/Fonts/ariblk.ttf"
FONT_B = "C:/Windows/Fonts/arialbd.ttf"
CREMA, NAVY = (253, 249, 239), (3, 5, 60)
CORAL, CORAL_TXT, AZUL = (246, 91, 81), (210, 56, 46), (18, 104, 252)
HOST = {"andres": ("host-andres.jpg", CORAL, CORAL_TXT, "ANDR\u00c9S BERM\u00daDEZ"),
        "alejo": ("host-alejandro.jpg", AZUL, AZUL, "ALEJANDRO AGUIRRE")}

EP = {
    "ep": "EP.01",
    "teaser": ["EN 2006 ENTRAMOS", "A UN CALL CENTER", '*"MIENTRAS TANTO"*'],
    "teaser_pill": "TEMPORADA 3  \u00b7  HOY 11 PM",
    "stories": [["EN 2006", "ENTRAMOS A UN", "CALL CENTER", '*"MIENTRAS*', '*TANTO"*'],
                ["VEINTE A\u00d1OS", "DESPU\u00c9S,", "*SEGUIMOS*", "*AQU\u00cd.*"]],
    "story3_pill": "HOY  \u00b7  11 PM",
    "story3_sub": "TEMPORADA 3 EN SPOTIFY",
    "quotes": [  # (slug, host, cita textual, timestamp del SRT)
        ("alejo", "alejo", "No siempre el top performer tiene madera de l\u00edder.", "1:04:23"),
        ("andres", "andres", "Aqu\u00ed estamos Alejo y yo como prueba de que s\u00ed se puede, cuando uno se toma las cosas en serio.", "1:23:39"),
    ],
    "reel_quote": "alejo",
}


def font(px, f=FONT):
    return ImageFont.truetype(f, px)


def ancho(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0]


INTER = 1.12  # interlineado de titulares: con 1.04 la coma de una linea tocaba la siguiente


def lineas_fit(d, lineas, w, h, px_max):
    # lineas fijas ("*x*" = coral): mayor tamano que cabe en w x h.
    px = px_max
    while px > 16:
        f = font(px)
        if all(ancho(d, t.strip("*"), f) <= w for t in lineas) and int(px * INTER) * len(lineas) <= h:
            return f, px
        px -= 2
    raise SystemExit("no cabe: %r" % lineas)


def dibujar_lineas(d, x, y, lineas, f, px, color_acento=CORAL_TXT):
    # Por linea base, no por caja: una tilde (AQUI) no desplaza su linea.
    base = y + int(px * 0.78)
    for t in lineas:
        acento = t.startswith("*")
        t = t.strip("*")
        d.text((x, base), t, font=f, fill=color_acento if acento else NAVY, anchor="ls")
        base += int(px * INTER)
    return base


def envolver(d, texto, w, h, px_max, f_path=FONT, inter=1.12):
    # texto corrido: ajuste de palabras + mayor tamano que cabe.
    px = px_max
    while px > 16:
        f = font(px, f_path)
        lineas, act = [], ""
        for pal in texto.split():
            prueba = (act + " " + pal).strip()
            if ancho(d, prueba, f) <= w:
                act = prueba
            else:
                lineas.append(act); act = pal
        lineas.append(act)
        if all(ancho(d, l, f) <= w for l in lineas) and int(px * inter) * len(lineas) <= h:
            return f, px, lineas
        px -= 2
    raise SystemExit("no cabe: %r" % texto)


def pastilla(d, x, y, txt, px, fondo=NAVY, tinta=CREMA, centro=False):
    f = font(px)
    b = d.textbbox((0, 0), txt, font=f)
    pw, ph = int(px * 0.9), int(px * 0.45)
    w, h = b[2] - b[0] + 2 * pw, b[3] - b[1] + 2 * ph
    if centro:
        x = x - w // 2
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=fondo)
    d.text((x + pw - b[0], y + ph - b[1]), txt, font=f, fill=tinta)
    return w, h


def logo(img, x, y, lado):
    l = Image.open(LOGO).convert("RGB").resize((lado, lado), Image.LANCZOS)
    a = Image.new("L", l.size)
    a.putdata([min(255, max(0, (abs(r - 253) + abs(g - 249) + abs(b - 239) - 12) * 10)) for r, g, b in l.get_flattened_data()])
    img.paste(l, (x, y), a)


def foto(img, d, x, y, w, h, quien):
    archivo, sombra = HOST[quien][0], HOST[quien][1]
    off, r, borde = max(6, w // 22), max(10, w // 14), max(3, w // 90)
    d.rounded_rectangle((x + off, y + off, x + w + off, y + h + off), radius=r, fill=sombra)
    d.rounded_rectangle((x, y, x + w, y + h), radius=r, fill=NAVY)
    src = Image.open(WEB / archivo).convert("RGB")
    sw, sh = src.size
    ratio = h / w
    if sh / sw > ratio:
        ch = int(sw * ratio); top = int((sh - ch) * 0.25); src = src.crop((0, top, sw, top + ch))
    else:
        cw = int(sh / ratio); left = (sw - cw) // 2; src = src.crop((left, 0, left + cw, sh))
    p = src.resize((w - 2 * borde, h - 2 * borde), Image.LANCZOS)
    m = Image.new("L", p.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0) + p.size, radius=r - borde, fill=255)
    img.paste(p, (x + borde, y + borde), m)


def lienzo(w, h):
    img = Image.new("RGB", (w, h), CREMA)
    return img, ImageDraw.Draw(img)


def teaser():
    W = H = 1080
    img, d = lienzo(W, H)
    m = 80
    logo(img, W - m - 300 + 20, m - 30, 300)
    pastilla(d, m, m + 20, EP["teaser_pill"], 30, fondo=CORAL, tinta=(255, 255, 255))
    f, px = lineas_fit(d, EP["teaser"], W - 2 * m, 360, 120)
    dibujar_lineas(d, m, 380, EP["teaser"], f, px)
    fw = 270
    foto(img, d, m, H - m - 300, fw, 300, "andres")
    foto(img, d, m + fw + 50, H - m - 300, fw, 300, "alejo")
    # plataformas apiladas y alineadas a la derecha: en una sola linea pisaban la foto de Alejo
    fb = font(26, FONT_B)
    for i, t in enumerate(["SPOTIFY", "APPLE PODCASTS", "YOUTUBE"]):
        d.text((W - m, H - m - 300 + 60 + i * 44), t, font=fb, fill=NAVY, anchor="rs")
    return img


def story(n):
    W, H = 1080, 1920
    img, d = lienzo(W, H)
    m = 90
    # zona segura de stories: Instagram tapa ~250 px arriba (progreso, perfil) y ~250 abajo (respuesta)
    if n < 2:
        lin = EP["stories"][n]
        f, px = lineas_fit(d, lin, W - 2 * m, 1000, 190)
        alto = int(px * INTER) * len(lin)
        dibujar_lineas(d, m, (H - alto) // 2 - 120, lin, f, px)
        logo(img, (W - 260) // 2, H - 290 - 260, 260)
    else:
        logo(img, (W - 600) // 2, 260, 600)
        fw, fh = 360, 440
        fy = 260 + 600 + 50
        foto(img, d, (W - 2 * fw - 70) // 2, fy, fw, fh, "andres")
        foto(img, d, (W - 2 * fw - 70) // 2 + fw + 70, fy, fw, fh, "alejo")
        y = fy + fh + 80
        _, ph = pastilla(d, W // 2, y, EP["story3_pill"], 64, fondo=CORAL, tinta=(255, 255, 255), centro=True)
        d.text((W // 2, y + ph + 70), EP["story3_sub"], font=font(44), fill=NAVY, anchor="mt")
        # los ~260 px de abajo quedan libres para el sticker de enlace
    return img


def tarjeta_cita(slug, quien, cita, ts, w, h):
    img, d = lienzo(w, h)
    color = HOST[quien][2]
    m = int(w * 0.08)
    # en 9:16 (reel) Instagram/TikTok tapan ~220 px arriba y ~420 abajo (descripcion, botones)
    top = m if h / w < 1.5 else 220
    bot = m if h / w < 1.5 else 420
    logo(img, w - m - 230 + 15, top - 25, 230)
    d.text((m - 8, top - 40), "\u201c", font=font(int(w * 0.32)), fill=HOST[quien][1])
    caja_y = top + int(w * 0.26)
    foto_h = int(w * 0.24)
    pie_y = h - bot - foto_h
    f, px, lineas = envolver(d, cita, w - 2 * m, pie_y - caja_y - int(w * 0.08), int(w * 0.11))
    alto = int(px * 1.12) * len(lineas)
    y = caja_y + (pie_y - int(w * 0.06) - caja_y - alto) // 2
    for l in lineas:
        b = d.textbbox((0, 0), l, font=f)
        d.text((m - b[0], y - b[1]), l, font=f, fill=NAVY)
        y += int(px * 1.12)
    foto(img, d, m, pie_y, foto_h, foto_h, quien)
    tx = m + foto_h + int(w * 0.06)
    d.text((tx, pie_y + int(foto_h * 0.36)), HOST[quien][3], font=font(int(w * 0.034)), fill=color, anchor="ls")
    d.text((tx, pie_y + int(foto_h * 0.62)), "BEHIND THE QUEUE  \u00b7  %s  \u00b7  T3" % EP["ep"], font=font(int(w * 0.024), FONT_B), fill=NAVY, anchor="ls")
    d.text((tx, pie_y + int(foto_h * 0.86)), "Episodio completo en Spotify", font=font(int(w * 0.024), FONT_B), fill=NAVY, anchor="ls")
    return img


def guardar(img, ruta):
    img.save(ruta, optimize=True)
    print(ruta, img.size)


if __name__ == "__main__":
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    p = "BTQ-T3-%s" % EP["ep"].replace(".", "")
    guardar(teaser(), out / ("%s-teaser-1x1.png" % p))
    for i in range(3):
        guardar(story(i), out / ("%s-story-%d-9x16.png" % (p, i + 1)))
    for slug, quien, cita, ts in EP["quotes"]:
        guardar(tarjeta_cita(slug, quien, cita, ts, 1080, 1350), out / ("%s-cita-%s-4x5.png" % (p, slug)))
    q = [x for x in EP["quotes"] if x[0] == EP["reel_quote"]][0]
    guardar(tarjeta_cita(*q, 1080, 1920), out / ("%s-reel-%s-9x16.png" % (p, q[0])))
