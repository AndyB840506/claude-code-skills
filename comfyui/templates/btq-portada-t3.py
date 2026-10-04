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
    for t, acento in lineas:
        b = d.textbbox((0, 0), t, font=f)
        d.text((x - b[0], y - b[1]), t, font=f, fill=CORAL_TXT if acento else NAVY)
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


def host(img, d, x, y, w, ratio, foto, sombra, nombre, apellido, px):
    h = int(w * ratio)
    off, r, borde = max(8, w // 22), max(10, w // 18), max(4, w // 90)
    d.rounded_rectangle((x + off, y + off, x + w + off, y + h + off), radius=r, fill=sombra)
    d.rounded_rectangle((x, y, x + w, y + h), radius=r, fill=NAVY)
    src = Image.open(WEB + foto).convert("RGB")
    sw, sh = src.size
    ch = min(sh, int(sw * ratio))
    top = int((sh - ch) * 0.25)  # recorte cargado arriba para conservar las caras
    p = src.crop((0, top, sw, top + ch)).resize((w - 2 * borde, h - 2 * borde), Image.LANCZOS)
    m = Image.new("L", p.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0) + p.size, radius=r - borde, fill=255)
    img.paste(p, (x + borde, y + borde), m)
    f = font(px)
    base = y + h + off + int(px * 1.75)  # linea base: la tilde de la E no desalinea
    d.text((x, base), nombre, font=f, fill=NAVY, anchor="ls")
    d.text((x, base + int(px * 1.2)), apellido, font=f, fill=CORAL_TXT if sombra == CORAL else AZUL, anchor="ls")


def logo(img, x, y, lado):
    # Fondo crema del logo -> transparente, para que no se vea su recuadro sobre el lienzo.
    l = Image.open(LOGO).convert("RGB").resize((lado, lado), Image.LANCZOS)
    a = Image.new("L", l.size)
    a.putdata([min(255, max(0, (abs(r - 253) + abs(g - 249) + abs(b - 239) - 12) * 10)) for r, g, b in l.get_flattened_data()])
    img.paste(l, (x, y), a)


def componer(W, H, lay):
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
