# -*- coding: utf-8 -*-
"""Mide wpm REAL de habla desde un SRT: palabras habladas / tiempo con voz.
Excluye los huecos entre subtitulos (musica, silencios largos) para no
diluir el ritmo con pausas que no son habla."""
import re, io, os, sys

SRT_DIR = r"E:\Transcriptor\transcripciones"

TS = re.compile(r"(\d\d):(\d\d):(\d\d),(\d\d\d)\s*-->\s*(\d\d):(\d\d):(\d\d),(\d\d\d)")

def secs(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0

def analyze(path):
    try:
        raw = io.open(path, encoding="utf-8").read()
    except UnicodeDecodeError:
        raw = io.open(path, encoding="latin-1").read()
    blocks = re.split(r"\n\s*\n", raw)
    words = 0
    voiced = 0.0
    first, last = None, None
    for b in blocks:
        m = TS.search(b)
        if not m:
            continue
        a = secs(*m.groups()[:4])
        z = secs(*m.groups()[4:])
        if first is None:
            first = a
        last = z
        voiced += (z - a)
        text = TS.sub("", b)
        text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.M)
        text = re.sub(r"<[^>]+>", " ", text)
        # descartar el artefacto de intro musical (cadenas de A repetidas)
        if re.match(r"^\s*[Aa\s.,]+$", text) and len(text.strip()) > 25:
            continue
        words += len([w for w in text.split() if re.search(r"[A-Za-zÁÉÍÓÚáéíóúÑñ]", w)])
    wall = (last - first) if (first is not None) else 0
    return words, voiced, wall

rows = []
for fn in sorted(os.listdir(SRT_DIR)):
    if not fn.lower().endswith(".srt"):
        continue
    w, v, wall = analyze(os.path.join(SRT_DIR, fn))
    if v <= 0:
        continue
    rows.append((fn, w, v / 60.0, wall / 60.0, w / (v / 60.0), w / (wall / 60.0)))

print("%-34s %7s %8s %8s %8s %8s" % ("archivo", "palab", "voz_min", "total_m", "wpm_voz", "wpm_tot"))
print("-" * 82)
for r in rows:
    print("%-34s %7d %8.1f %8.1f %8.1f %8.1f" % r)

btq = [r for r in rows if r[0].startswith("BTQ") and "pre-fix" not in r[0]]
mpd = [r for r in rows if r[0].startswith("MPD")]
for label, group in (("BTQ", btq), ("MPD", mpd)):
    if group:
        print("")
        print("%s  n=%d" % (label, len(group)))
        print("  wpm sobre tiempo con voz : %.1f  (rango %.1f - %.1f)"
              % (sum(g[4] for g in group) / len(group),
                 min(g[4] for g in group), max(g[4] for g in group)))
        print("  wpm sobre duracion total : %.1f  (rango %.1f - %.1f)"
              % (sum(g[5] for g in group) / len(group),
                 min(g[5] for g in group), max(g[5] for g in group)))
