# Portada de episodio BTQ T3 (identidad "EN VIVO"): 1:1 (3000), 9:16 (1080x1920), 16:9 (1920x1080).
# Uso: python btq-portada-t3.py "EP.01" "LINEA 1|*LINEA 2*" <out_prefix>
#   "|" parte lineas; una linea entre *asteriscos* va en coral (Andres).
#   out_prefix va a E:\ (escritorio) o D:\ (portatil), nunca a C:\.
# Sistema tomado de og-image-t3.jpg y brand-constants.md Identidad T3. Texto siempre con PIL.
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
WEB = str(REPO / "btq-production" / "website") + "/"   # host-andres.jpg, host-alejandro.jpg (720x900)
LOGO = str(REPO / "btq-production" / "brand" / "btq-t3-logo-1024.png")
FONT = "C:/Windows/Fonts/ariblk.ttf"
CREMA, NAVY = (253, 249, 239), (3, 5, 60)
CORAL, CORAL_TXT, AZUL = (246, 91, 81), (210, 56, 46), (18, 104, 252)
# Episodios con invitadas: portada de 4. (foto, nombre, apellido, recorte); las fotos viven en E:\ (solo escritorio).
# Recorte = (centro x, tope y, ancho) en px de la foto, para que las 4 caras queden a escala parecida.
RECORTE_HOSTS = {"host-andres.jpg": (420, 50, 600), "host-alejandro.jpg": (367, 40, 500)}
INVITADAS = {"EP.04": [
    ("E:/Podcast/BTQ/T3/1715703004044.jpg", "ADRIANA", "SIMBAQUEBA", (185, 0, 320)),
    ("E:/Podcast/BTQ/T3/WhatsApp Image 2026-10-31 at 9.15.34 PM.jpeg", "PAULA", "CANTOR", (255, 70, 300)),
]}

ep, titulo, out = sys.argv[1], sys.argv[2], sys.argv[3]
lineas = [(l.strip("*"), l.startswith("*")) for l in titulo.split("|")]


def font(px):
    return ImageFont.truetype(FONT, px)


def ancho(d, txt, f):
    b = d.textbbox((0, 0), txt, font=f)
    return b[2] - b[0]


def titulo_fit(d, w, h_max, px_max):
    # Tamano mayor en que TODAS las lineas caben en w y el bloque en h_max.
    px = px_max
    while px > 20:
        f = font(px)
        alto = int(px * 1.02) * len(lineas)
        if all(ancho(d, t, f) <= w for t, _ in lineas) and alto <= h_max:
            return f, px
        px -= 4
    raise SystemExit("titulo no cabe")


def dibujar_titulo(d, x, y, f, px):
    # Tope comun de mayuscula ("H"): con el tope de cada linea, una con Ñ/Ú bajaba y se pegaba a la siguiente (EP.03).
    tope = d.textbbox((0, 0), "H", font=f)[1]
    for t, acento in lineas:
        b = d.textbbox((0, 0), t, font=f)
        d.text((x - b[0], y - tope), t, font=f, fill=CORAL_TXT if acento else NAVY)
        y += int(px * 1.02)
    return y


def pastilla(d, x, y, txt, px):
    f = font(px)
    b = d.textbbox((0, 0), txt, font=f)
    pw, ph = int(px * 0.9), int(px * 0.45)
    w, h = b[2] - b[0] + 2 * pw, b[3] - b[1] + 2 * ph
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=NAVY)
    d.text((x + pw - b[0], y + ph - b[1]), txt, font=f, fill=CREMA)
    return h


def host_alto(w, ratio, px):
    # Alto total del bloque foto + sombra + nombre + apellido.
    return int(w * ratio) + max(8, w // 22) + int(px * 3.2)


def caja(sw, sh, recorte, ratio):
    cx, top, cw = recorte
    cw = min(cw, sw, int(sh / ratio))
    ch = int(cw * ratio)
    x0 = min(max(0, cx - cw // 2), sw - cw)
    y0 = min(max(0, top), sh - ch)
    return (x0, y0, x0 + cw, y0 + ch)


def host(img, d, x, y, w, ratio, foto, sombra, nombre, apellido, px, recorte=None):
    h = int(w * ratio)
    off, r, borde = max(8, w // 22), max(10, w // 18), max(4, w // 90)
    d.rounded_rectangle((x + off, y + off, x + w + off, y + h + off), radius=r, fill=sombra)
    d.rounded_rectangle((x, y, x + w, y + h), radius=r, fill=NAVY)
    src = Image.open(Path(WEB) / foto).convert("RGB")
    sw, sh = src.size
    if recorte:
        cuadro = caja(sw, sh, recorte, ratio)
    else:
        ch = min(sh, int(sw * ratio))
        top = int((sh - ch) * 0.25)  # recorte cargado arriba para conservar las caras
        cuadro = (0, top, sw, top + ch)
    p = src.crop(cuadro).resize((w - 2 * borde, h - 2 * borde), Image.LANCZOS)
    m = Image.new("L", p.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0) + p.size, radius=r - borde, fill=255)
    img.paste(p, (x + borde, y + borde), m)
    f = font(px)
    base = y + h + off + int(px * 1.75)  # linea base: la tilde de la E no desalinea
    d.text((x, base), nombre, font=f, fill=NAVY, anchor="ls")
    color = CORAL_TXT if sombra == CORAL else AZUL if sombra == AZUL else NAVY
    d.text((x, base + int(px * 1.2)), apellido, font=f, fill=color, anchor="ls")


def logo(img, x, y, lado):
    # Fondo crema del logo -> transparente, para que no se vea su recuadro sobre el lienzo.
    l = Image.open(LOGO).convert("RGB").resize((lado, lado), Image.LANCZOS)
    a = Image.new("L", l.size)
    a.putdata([min(255, max(0, (abs(r - 253) + abs(g - 249) + abs(b - 239) - 12) * 10)) for r, g, b in l.get_flattened_data()])
    img.paste(l, (x, y), a)


def componer4(W, H, lay):
    # Hosts + 2 invitadas: en fila en 1:1, en 2x2 en 9:16 y 16:9.
    img = Image.new("RGB", (W, H), CREMA)
    d = ImageDraw.Draw(img)
    u = W / 100.0
    gente = [("host-andres.jpg", CORAL, "ANDRÉS", "BERMÚDEZ", RECORTE_HOSTS["host-andres.jpg"]),
             ("host-alejandro.jpg", AZUL, "ALEJANDRO", "AGUIRRE", RECORTE_HOSTS["host-alejandro.jpg"])]
    gente += [(fo, NAVY, n, a, r) for fo, n, a, r in INVITADAS[ep]]
    if lay == "1x1":
        m, gap = int(6 * u), int(3 * u)
        fw = (W - 2 * m - 3 * gap - int(1 * u)) // 4
        ratio, npx = 1.4, int(2 * u)
        fy = H - m - host_alto(fw, ratio, npx)
        lado = int(30 * u)
        logo(img, W - m - lado + int(2 * u), m - int(4 * u), lado)
        pastilla(d, m, m + int(2 * u), ep + "  ·  TEMPORADA 3", int(2.4 * u))
        ty, tw = int(30 * u), W - 2 * m  # bajo el logo y a todo el ancho: con 4 fotos no cabe al lado
        h_disp = fy - ty - int(3 * u)
        f, px = titulo_fit(d, tw, h_disp, int(16 * u))
        dibujar_titulo(d, m, ty + (h_disp - int(px * 1.02) * len(lineas)) // 2, f, px)
        pos = [(m + i * (fw + gap), fy) for i in range(4)]
    elif lay == "9x16":
        m, gap = int(8 * u), int(7 * u)
        fw = (W - 2 * m - gap - int(2 * u)) // 2
        ratio, npx = 0.95, int(3.6 * u)
        alto = host_alto(fw, ratio, npx)
        fy2 = H - m - alto
        fy = fy2 - alto - int(3 * u)
        lado = int(34 * u)
        logo(img, (W - lado) // 2, int(3 * u), lado)
        ty = int(37 * u)
        ty += pastilla(d, m, ty, ep + "  ·  TEMPORADA 3", int(3.6 * u)) + int(3 * u)
        h_disp = fy - ty - int(3 * u)
        f, px = titulo_fit(d, W - 2 * m, h_disp, int(20 * u))
        dibujar_titulo(d, m, ty + (h_disp - int(px * 1.02) * len(lineas)) // 2, f, px)
        pos = [(m + i * (fw + gap), yy) for yy in (fy, fy2) for i in range(2)]
    else:  # 16x9
        m = int(4.5 * u)
        logo(img, m - int(2 * u), m - int(2.5 * u), int(20 * u))
        y = m + int(19 * u)
        y += pastilla(d, m, y, ep + "  ·  TEMPORADA 3", int(1.7 * u)) + int(2.5 * u)
        f, px = titulo_fit(d, int(52 * u), H - y - m, int(8 * u))
        dibujar_titulo(d, m, y, f, px)
        fw, gap = int(14 * u), int(4 * u)
        ratio, npx = 0.95, int(1.25 * u)
        alto = host_alto(fw, ratio, npx)
        fy = (H - 2 * alto - int(1.5 * u)) // 2
        x0 = W - m - 2 * fw - gap - int(1 * u)
        pos = [(x0 + i * (fw + gap), yy) for yy in (fy, fy + alto + int(1.5 * u)) for i in range(2)]
    for (x, y), (fo, sombra, n, a, r) in zip(pos, gente):
        host(img, d, x, y, fw, ratio, fo, sombra, n, a, npx, recorte=r)
    return img, px


def componer(W, H, lay):
    if ep in INVITADAS:
        return componer4(W, H, lay)
    img = Image.new("RGB", (W, H), CREMA)
    d = ImageDraw.Draw(img)
    u = W / 100.0  # unidad = 1% del ancho
    hosts = [("host-andres.jpg", CORAL, "ANDR\u00c9S", "BERM\u00daDEZ"),
             ("host-alejandro.jpg", AZUL, "ALEJANDRO", "AGUIRRE")]
    if lay in ("1x1", "9x16"):
        # Arriba: pastilla (+ logo). Medio: titulo, acotado por las fotos. Abajo: dos fotos a todo el ancho.
        m = int(6 * u) if lay == "1x1" else int(8 * u)
        gap = int(7 * u)
        fw = (W - 2 * m - gap - int(2 * u)) // 2
        ratio = 1.12 if lay == "1x1" else 1.2
        npx = int(2.4 * u) if lay == "1x1" else int(4.2 * u)
        fy = H - m - host_alto(fw, ratio, npx)
        if lay == "1x1":
            lado = int(30 * u)
            logo(img, W - m - lado + int(2 * u), m - int(4 * u), lado)
            pastilla(d, m, m + int(2 * u), ep + "  \u00b7  TEMPORADA 3", int(2.4 * u))
            ty, tw = m + int(9 * u), int(60 * u)  # columna izquierda, al lado del logo
        else:
            lado = int(52 * u)
            logo(img, (W - lado) // 2, int(4 * u), lado)
            ty = int(56 * u)
            ty += pastilla(d, m, ty, ep + "  \u00b7  TEMPORADA 3", int(4.2 * u)) + int(5 * u)
            tw = W - 2 * m
        h_disp = fy - ty - int(6 * u)
        f, px = titulo_fit(d, tw, h_disp, int(16 * u) if lay == "1x1" else int(20 * u))
        # Centrado vertical en su hueco: un titulo de 2 lineas no deja un vacio sobre las fotos.
        dibujar_titulo(d, m, ty + (h_disp - int(px * 1.02) * len(lineas)) // 2, f, px)
        for i, hh in enumerate(hosts):
            host(img, d, m + i * (fw + gap), fy, fw, ratio, *hh, npx)
    else:  # 16x9
        m = int(4.5 * u)
        logo(img, m - int(2 * u), m - int(2.5 * u), int(20 * u))
        y = m + int(19 * u)
        y += pastilla(d, m, y, ep + "  \u00b7  TEMPORADA 3", int(1.7 * u)) + int(2.5 * u)
        f, px = titulo_fit(d, int(50 * u), H - y - m, int(8 * u))
        dibujar_titulo(d, m, y, f, px)
        fw = int(17 * u)
        fy = (H - int(fw * 1.25)) // 2 - int(3 * u)
        host(img, d, W - m - 2 * fw - int(6 * u), fy, fw, 1.25, *hosts[0], int(1.7 * u))
        host(img, d, W - m - fw - int(1 * u), fy, fw, 1.25, *hosts[1], int(1.7 * u))
    return img, px


for lay, (W, H) in {"1x1": (3000, 3000), "9x16": (1080, 1920), "16x9": (1920, 1080)}.items():
    img, px = componer(W, H, lay)
    p = f"{out}-{lay}.png"
    img.save(p, optimize=True)
    print(p, img.size, "titulo px", px)
