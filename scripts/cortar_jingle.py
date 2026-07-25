# -*- coding: utf-8 -*-
"""Extrae el stinger de BTQ de un track largo generado por IA.

Los generadores de musica por texto ignoran las duraciones cortas: uno pide 3
segundos y devuelven 60. El flujo correcto no es insistir con el prompt, es
recortar. Este script hace el recorte de forma determinista.

Dos modos:

  1. MAPA (por defecto, sin --start) -- decodifica el audio, imprime la envolvente
     de energia y propone los 3 mejores puntos de arranque: los golpes mas secos,
     donde el sonido entra de la nada. Ahi es donde empieza un buen stinger.

         python cortar_jingle.py track.wav

  2. CORTE (con --start) -- recorta, aplica fade de salida corto para que no
     "clickee", normaliza a un pico predecible y exporta.

         python cortar_jingle.py track.wav --start 12.4 --dur 3.0

Siempre exporta ademas una PRUEBA DE EMPALME: stinger + silencio + stinger, que
es como se va a oir en el episodio (apertura y cierre). Escuchar esa.

Requiere ffmpeg/ffprobe en el PATH. Ver btq-production/jingle-brief.md.
"""
import argparse
import array
import math
import os
import subprocess
import sys

SR = 48000
PICO_OBJETIVO = -3.0          # dBFS: deja aire para que no pique sobre la voz
FADE_SALIDA = 0.045           # 45 ms -- corta el "click" sin sonar a fade
FADE_ENTRADA = 0.004          # 4 ms -- solo anti-click, no suaviza el ataque


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", **kw)


def pcm_mono(path):
    """Decodifica a PCM 16-bit mono para analizar."""
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR),
         "-f", "s16le", "-"], capture_output=True)
    if p.returncode != 0 or not p.stdout:
        sys.exit("ffmpeg no pudo leer %s\n%s" % (path, p.stderr.decode("utf-8", "replace")))
    a = array.array("h")
    a.frombytes(p.stdout[:len(p.stdout) // 2 * 2])
    return a


def envolvente(muestras, ventana=0.02):
    """RMS por ventana. Devuelve lista de (segundo, dBFS)."""
    n = int(SR * ventana)
    out = []
    for i in range(0, len(muestras) - n, n):
        s = 0
        for v in muestras[i:i + n]:
            s += v * v
        rms = math.sqrt(s / n)
        db = 20 * math.log10(rms / 32768.0) if rms > 0 else -120.0
        out.append((i / SR, db))
    return out


def candidatos(env, n=3, sep=1.5):
    """Golpes secos: mayor salto de energia respecto a la ventana anterior."""
    saltos = []
    for i in range(1, len(env)):
        saltos.append((env[i][1] - env[i - 1][1], env[i][0], env[i][1]))
    saltos.sort(reverse=True)
    elegidos = []
    for delta, t, db in saltos:
        if delta < 3:
            break
        if all(abs(t - e[0]) > sep for e in elegidos):
            elegidos.append((t, delta, db))
        if len(elegidos) == n:
            break
    return elegidos


def pico_dbfs(path):
    r = run(["ffmpeg", "-v", "info", "-i", path, "-af", "volumedetect",
             "-f", "null", "-"])
    for linea in r.stderr.splitlines():
        if "max_volume:" in linea:
            return float(linea.split("max_volume:")[1].split("dB")[0].strip())
    return 0.0


ap = argparse.ArgumentParser()
ap.add_argument("entrada")
ap.add_argument("--start", type=float, help="segundo donde arranca el stinger")
ap.add_argument("--dur", type=float, default=3.0, help="duracion (brief: 2-4 s)")
ap.add_argument("--out", help="carpeta de salida (default: la del archivo)")
args = ap.parse_args()

if not os.path.exists(args.entrada):
    sys.exit("No existe: %s" % args.entrada)
salida = args.out or os.path.dirname(os.path.abspath(args.entrada))
os.makedirs(salida, exist_ok=True)

# ------------------------------------------------------------------ modo MAPA
if args.start is None:
    env = envolvente(pcm_mono(args.entrada))
    dur = env[-1][0] if env else 0
    print("=== %s -- %.1f s ===\n" % (os.path.basename(args.entrada), dur))
    # ~30 filas pase lo que pase: un track de 60 s a 0.5 s daba 120 lineas.
    filas = 30
    paso = max(1, len(env) // filas)
    print("envolvente (%.1f s por fila, escala -60..0 dBFS):" % (paso * 0.02))
    for i in range(0, len(env), paso):
        t = env[i][0]
        db = max(d for _, d in env[i:i + paso])   # pico del tramo, no promedio:
        barras = max(0, int((db + 60) / 60 * 44)) # si no, los golpes se diluyen
        print("  %6.1f s  %6.1f dB  %s" % (t, db, "#" * barras))
    print("\ncandidatos -- golpes mas secos (donde el sonido entra de la nada):")
    cs = candidatos(env)
    if not cs:
        print("  ninguno claro. El track no tiene ataques marcados: pida otra")
        print("  generacion con 'hard percussive hit at the very beginning'.")
    for t, delta, db in cs:
        print("    --start %.2f    (salto de %.1f dB)" % (max(0, t - 0.02), delta))
    print("\nEscuche y elija. Despues:")
    print('  python cortar_jingle.py "%s" --start <segundo>' % args.entrada)
    sys.exit(0)

# ------------------------------------------------------------------ modo CORTE
if not (1.5 <= args.dur <= 5.0):
    sys.exit("--dur fuera de rango: el brief pide 2-4 s (tope duro 5).")

base = os.path.join(salida, "BTQ-jingle")
crudo = base + "-crudo.wav"
final = base + ".wav"
prueba = base + "-PRUEBA-empalme.wav"

fade_ini = max(0.0, args.dur - FADE_SALIDA)
r = run(["ffmpeg", "-y", "-v", "error", "-ss", str(args.start), "-t", str(args.dur),
         "-i", args.entrada, "-ac", "2", "-ar", str(SR),
         "-af", "afade=t=in:st=0:d=%.3f,afade=t=out:st=%.3f:d=%.3f"
                % (FADE_ENTRADA, fade_ini, FADE_SALIDA),
         "-c:a", "pcm_s24le", crudo])
if r.returncode != 0:
    sys.exit("fallo el recorte:\n" + r.stderr)

ganancia = PICO_OBJETIVO - pico_dbfs(crudo)
r = run(["ffmpeg", "-y", "-v", "error", "-i", crudo,
         "-af", "volume=%.2fdB" % ganancia, "-c:a", "pcm_s24le", final])
if r.returncode != 0:
    sys.exit("fallo la normalizacion:\n" + r.stderr)
os.remove(crudo)

# Prueba de empalme: como se oye al abrir y al cerrar el episodio.
r = run(["ffmpeg", "-y", "-v", "error",
         "-i", final, "-f", "lavfi", "-t", "2.5", "-i", "anullsrc=r=48000:cl=stereo",
         "-filter_complex", "[0][1][0]concat=n=3:v=0:a=1",
         "-c:a", "pcm_s24le", prueba])
if r.returncode != 0:
    sys.exit("fallo la prueba de empalme:\n" + r.stderr)

print("stinger : %s" % final)
print("          %.2f s, pico %.1f dBFS, 48 kHz estereo, corte seco" % (args.dur, PICO_OBJETIVO))
print("prueba  : %s" % prueba)
print("          stinger + 2.5 s de silencio + stinger -- escuche ESTE.")
print("\nSi al oirlo tiene cola de reverb o se siente largo, vuelva a cortar")
print("con --dur mas corto o con otro --start. No hay que regenerar el track.")
