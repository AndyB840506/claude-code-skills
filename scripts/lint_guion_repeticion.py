# -*- coding: utf-8 -*-
"""Detecta frases-molde: repeticion literal entre el CUERPO de un guion nuevo y
los guiones ya publicados.

Excluye apertura, cierre y recomendaciones: el ritual canonico de BTQ DEBE
repetirse ("Buenas y santas", el cierre, LinkedIn) y sin excluirlo el
instrumento se ahoga en falsos positivos -- medido el 2026-07-25: 25 de 25
hallazgos eran ritual.

Mide repeticion LITERAL, no humor. Si el chiste cambia pero el andamiaje es
identico, igual suena a formula -- por eso 6-gramas y no frases completas.

Uso:
    python lint_guion_repeticion.py <guion-nuevo.html> [carpeta_de_guiones]

Regla que hace cumplir: guion-style-btq.md seccion "Frases-molde".
"""
import io
import itertools
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

N = 6                      # tamano del n-grama
RITUAL = re.compile(r"apertura|cierre|recomendaciones", re.I)


def cuerpo(path):
    """Texto hablado, sin los segmentos de ritual."""
    s = io.open(path, encoding="utf-8").read()
    segs = re.findall(r'(?s)<div class="segment">(.*?)(?=<div class="segment">|\Z)', s)
    out = []
    for seg in segs:
        if RITUAL.search(re.sub("<[^>]+>", " ", seg[:400])):
            continue
        out += [" ".join(re.sub("<[^>]+>", " ", p).split())
                for p in re.findall(
                    r'(?s)<(?:p class="line"|div class="remate")[^>]*>(.*?)</(?:p|div)>', seg)]
    return " ".join(out)


def gramas(texto):
    w = re.sub(r"[^\wáéíóúñü ]", " ", texto.lower()).split()
    return set(tuple(w[i:i + N]) for i in range(len(w) - N + 1))


nuevo = sys.argv[1]
carpeta = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(nuevo) or "."

g_nuevo = gramas(cuerpo(nuevo))
if not g_nuevo:
    sys.exit("No se extrajo cuerpo de %s -- revisar que use <p class=\"line\">." % nuevo)

def es_comparable(f, ep_propio):
    """Un guion publicado distinto al que se esta revisando.

    Ojo: descarta 'artifact', 'draft' y 'backup'. Sin esto, la copia
    <ep>.artifact.html del propio episodio entra como si fuera otro guion y
    TODOS sus n-gramas matchean -- 19.000 falsos positivos (mordio 2026-07-25).
    Y descarta cualquier archivo del MISMO episodio, sea cual sea el sufijo.
    """
    fl = f.lower()
    if not fl.endswith(".html") or "guion" not in fl:
        return False
    if re.search(r"artifact|draft|backup|\.bak", fl):
        return False
    m = re.match(r"(ep\d+)", fl)
    return not (m and m.group(1) == ep_propio)


ep_propio = (re.match(r"(ep\d+)", os.path.basename(nuevo).lower()) or [None, ""])[1]
comparables = [f for f in sorted(os.listdir(carpeta)) if es_comparable(f, ep_propio)]

hallazgos = []
for f in comparables:
    for g in sorted(g_nuevo & gramas(cuerpo(os.path.join(carpeta, f)))):
        hallazgos.append((f, " ".join(g)))

print("=== frases-molde: %s vs %d guiones anteriores ===" % (
    os.path.basename(nuevo), len(comparables)))
if not hallazgos:
    print("\nPASS -- cero %d-gramas compartidos en el cuerpo." % N)
    sys.exit(0)

for f, frase in hallazgos:
    print("  [%s]  %s" % (f[:5], frase))
print("\nFAIL (%d) -- reescribir cada una. Ver guion-style-btq.md seccion Frases-molde."
      % len(hallazgos))
sys.exit(1)
