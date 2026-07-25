# Uso: python portada-compose.py <escena.png> <EP.NN> "<titulo>" <salida.png>
#
# Compone la tipografia BTQ v4 "Sala de Maquinas" sobre una escena ya generada.
# Fuente canonica de las reglas: episode-launch/docs/brand-constants.md
#
# Cambios respecto a v3 (que vive en el historial de git de este archivo):
#   - Paleta nueva: Void #0E1113 / Cream #F4EFE7 / Senal #FF3D00. Se fue el oro.
#   - Fuentes reales instaladas (Cabinet Grotesk / Supreme / Martian Mono).
#     Ya no se usa Impact como sustituto de Bebas.
#   - Wordmark a la izquierda en dos lineas, no centrado.
#   - Se retiran los 5 puntos dorados y la barra de footer con iconos de
#     plataforma: a 300 px eran una mancha gris. Queda solo EP.NN.
#   - Formato de label: 2 digitos ("EP.23"), unificado con los titulos
#     publicados en Spotify el 2026-07-25.
#
# Requiere PIL. Las fuentes deben estar instaladas por usuario -- ver
# brand-constants.md seccion "Fuentes - instalacion".
import os
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

scene_path = sys.argv[1]
ep_number = sys.argv[2]
title = sys.argv[3]
out_path = sys.argv[4]

FONT_DIR = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Fonts")
DISP = os.path.join(FONT_DIR, "CabinetGrotesk-Extrabold.otf")
BODY = os.path.join(FONT_DIR, "Supreme-Medium.otf")
MONO = os.path.join(FONT_DIR, "MartianMono-Variable.ttf")

for _p in (DISP, BODY, MONO):
    if not os.path.exists(_p):
        sys.exit("FALTA LA FUENTE: %s\nVer brand-constants.md seccion Fuentes." % _p)

VOID = (14, 17, 19)
STEEL = (57, 67, 74)
CREAM = (244, 239, 231)
SIGNAL = (255, 61, 0)
MUTED = (139, 148, 146)

KICKER = "OPERACIÓN  ·  CALIDAD  ·  LIDERAZGO"
WORD = ["BEHIND", "THE QUEUE"]

scene = Image.open(scene_path).convert("RGB")
W, H = scene.size
canvas = scene.copy()


def mono_font(size):
    f = ImageFont.truetype(MONO, size)
    # El default de la variable es SemiExpanded: sale mas ancha de lo previsto.
    f.set_variation_by_name("Regular")
    return f


def scrim(box, top_down):
    """Degradado de VOID a transparente para que el texto lea sobre cualquier escena."""
    x0, y0, x1, y1 = box
    h = y1 - y0
    layer = Image.new("RGBA", (x1 - x0, h))
    ld = ImageDraw.Draw(layer)
    for i in range(h):
        t = i / max(1, h - 1)
        a = int(255 * ((1 - t) if top_down else t) ** 1.4)
        ld.line([(0, i), (x1 - x0, i)], fill=VOID + (a,))
    canvas.paste(Image.alpha_composite(
        canvas.crop(box).convert("RGBA"), layer).convert("RGB"), (x0, y0))


scrim((0, 0, W, int(H * 0.30)), True)
scrim((0, int(H * 0.70), W, H), False)

draw = ImageDraw.Draw(canvas)
M = int(W * 0.062)

# --- wordmark ---
fw = ImageFont.truetype(DISP, int(H * 0.108))
y = int(H * 0.058)
ink_bottom = y
for line in WORD:
    draw.text((M, y), line, font=fw, fill=CREAM)
    ink_bottom = y + fw.getbbox(line)[3]
    y += int(H * 0.098)

# La regla se ancla al pixel de tinta mas bajo, NO al avance de linea:
# la cola de la Q de QUEUE cruza la regla si se calcula por interlineado.
rule_y = ink_bottom + int(H * 0.022)
draw.line([(M, rule_y), (W - M, rule_y)], fill=STEEL, width=max(2, int(H * 0.0035)))
draw.text((M, rule_y + int(H * 0.024)), KICKER, font=mono_font(int(H * 0.0175)), fill=MUTED)

# --- EP.NN abajo a la derecha ---
fe = mono_font(int(H * 0.030))
baseline = H - int(H * 0.062)
ep_w = draw.textbbox((0, 0), ep_number, font=fe)[2]
draw.text((W - M - ep_w, baseline - int(H * 0.030)), ep_number, font=fe, fill=SIGNAL)

# --- titulo: maximo 2 lineas, encoge hasta caber ---
title_max_w = W - 2 * M - ep_w - int(W * 0.04)
size = int(H * 0.0335)
while size > int(H * 0.019):
    ft = ImageFont.truetype(BODY, size)
    chars = max(10, int(title_max_w / (size * 0.50)))
    lines = textwrap.wrap(title, width=chars, break_long_words=False)
    if len(lines) <= 2 and max((ft.getlength(l) for l in lines), default=0) <= title_max_w:
        break
    size -= 2
else:
    lines = lines[:2]

line_h = int(size * 1.32)
ty = baseline - int(H * 0.030) - (len(lines) - 1) * line_h
for line in lines:
    draw.text((M, ty), line, font=ft, fill=CREAM)
    ty += line_h

foot_rule = min(ty, baseline) - (len(lines) * line_h) - int(H * 0.030)
draw.line([(M, foot_rule), (W - M, foot_rule)], fill=STEEL, width=max(2, int(H * 0.003)))

canvas.save(out_path)
print("saved", out_path, "| titulo", size, "px en", len(lines), "linea(s)")

# Contraprueba obligatoria de legibilidad -- brand-constants.md, checklist.
base, ext = os.path.splitext(out_path)
for px in (300, 96):
    p = "%s-%d%s" % (base, px, ext)
    canvas.resize((px, px), Image.LANCZOS).save(p)
    print("contraprueba:", p)
