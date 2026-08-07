# -*- coding: utf-8 -*-
"""
Genera el .artifact.html de un guion de MPD para publicarlo con la herramienta Artifact.

Por que existe: el Artifact envuelve el archivo en <!doctype><head><body>, asi que pasarle
el .html completo del guion mete html/head/body anidados. El patron correcto (memoria
feedback_episodes_always_artifact) es publicar SOLO el bloque <style> + el interior de <body>.

Uso:
    python mk-artifact.py scripts/EP02-el-rock-y-el-diablo.html

Escribe <mismo nombre>.artifact.html al lado del original e imprime comprobaciones de
integridad. Reusa los tokens del guion tal cual: la direccion visual "La Guarida" esta
congelada (2026-07-22) y este script NO la altera.
"""
import re
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Ajustes que solo aplican al artifact publicado. "La Guarida" es un mundo visual
# unico y deliberado (nocturno), asi que se fija el fondo en AMBOS temas en vez de
# dejar que el visor lo aclare cuando el lector tiene tema claro.
EXTRA = """
        /* --- Ajustes solo para el artifact publicado --- */
        html, body { background: var(--medianoche); }
        :root[data-theme="light"] body, :root[data-theme="dark"] body { background: var(--medianoche); color: var(--polvo); }
        .container { box-shadow: 0 0 90px rgba(0,0,0,0.55); }
        img, table { max-width: 100%; }
        a { color: var(--brasa); }
        :focus-visible { outline: 2px solid var(--brasa); outline-offset: 3px; }
        @media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
"""


def build(src):
    h = open(src, encoding='utf-8').read()

    m_style = re.search(r'<style>(.*?)</style>', h, re.S)
    m_body = re.search(r'<body>(.*?)</body>', h, re.S)
    if not m_style or not m_body:
        raise SystemExit("ERROR: el archivo no tiene <style> o <body>. No parece un guion de MPD.")

    out = "<style>\n" + m_style.group(1).rstrip() + "\n" + EXTRA + "    </style>\n" + m_body.group(1).strip() + "\n"

    dst = re.sub(r'\.html$', '.artifact.html', src)
    if dst == src:
        raise SystemExit("ERROR: el archivo de entrada tiene que terminar en .html")

    # newline='\n' a proposito: el archivo lo consume el publicador, no Windows.
    open(dst, 'w', encoding='utf-8', newline='\n').write(out)
    return dst, out


def check(dst, out):
    print("escrito:", dst)
    print("bytes  :", len(out))

    # Comprobaciones de integridad baratas. Si alguna falla, NO publicar.
    sobrantes = bool(re.search(r'<!DOCTYPE|<html|<head|<body', out, re.I))
    print("doctype/html/head/body sobrantes:", sobrantes, "" if not sobrantes else "  <-- FALLA")

    ok = not sobrantes
    for tag in ('div', 'span'):
        ab = len(re.findall(r'<%s\b' % tag, out))
        ce = len(re.findall(r'</%s>' % tag, out))
        estado = "OK" if ab == ce else "FALLA"
        if ab != ce:
            ok = False
        print("<%s> abiertos: %d  cerrados: %d   %s" % (tag, ab, ce, estado))

    print()
    print("LISTO PARA PUBLICAR" if ok else "NO PUBLICAR — corregir las fallas de arriba")
    return ok


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit("uso: python mk-artifact.py <ruta del guion .html>")
    ruta = sys.argv[1]
    if not os.path.isfile(ruta):
        raise SystemExit("ERROR: no existe el archivo %s" % ruta)
    d, o = build(ruta)
    sys.exit(0 if check(d, o) else 1)
