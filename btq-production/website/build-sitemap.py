# -*- coding: utf-8 -*-
"""Genera sitemap.xml recorriendo los HTML reales del sitio.

Se corre desde btq-production/website/ ANTES de cada deploy:
    python build-sitemap.py

Nace de un defecto real: robots.txt anunciaba /sitemap.xml desde siempre y el
archivo nunca existio (404 verificado el 2026-07-28). Un sitemap escrito a mano
se desincroniza en cuanto se agrega una pagina; este se deriva del disco.
"""
import io
import os
import sys
from datetime import date

BASE = "https://behind-thequeue.com"
AQUI = os.path.dirname(os.path.abspath(__file__))

# HTML que NO son paginas publicas: borradores de rediseno y variantes viejas.
EXCLUIR = {"index-v2.html", "index-v3.html", "index-liner.html"}

# Prioridad por tipo de pagina. La portada manda; el archivo y los episodios
# valen igual entre si.
def prioridad(rel):
    if rel == "/":
        return "1.0"
    if rel == "/episodios":
        return "0.8"
    return "0.7"


def rutas():
    out = []
    for dirpath, dirnames, filenames in os.walk(AQUI):
        dirnames[:] = [d for d in dirnames if not d.startswith((".", "node_modules"))]
        for fn in sorted(filenames):
            if not fn.endswith(".html") or fn in EXCLUIR:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, AQUI).replace(os.sep, "/")
            # vercel.json tiene cleanUrls + trailingSlash:false -> se publica sin
            # la extension y SIN barra final. Emitir la barra aqui costaria un
            # redirect 308 por cada URL del sitemap.
            if rel == "index.html":
                url = "/"
            elif rel.endswith("/index.html"):
                url = "/" + rel[: -len("/index.html")]
            else:
                url = "/" + rel[: -len(".html")]
            ts = date.fromtimestamp(os.path.getmtime(full)).isoformat()
            out.append((url, ts))
    return sorted(set(out))


def main():
    urls = rutas()
    lineas = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, ts in urls:
        lineas += ["  <url>",
                   "    <loc>%s%s</loc>" % (BASE, url),
                   "    <lastmod>%s</lastmod>" % ts,
                   "    <priority>%s</priority>" % prioridad(url),
                   "  </url>"]
    lineas.append("</urlset>")
    destino = os.path.join(AQUI, "sitemap.xml")
    io.open(destino, "w", encoding="utf-8", newline="\n").write("\n".join(lineas) + "\n")
    print("sitemap.xml escrito con %d URL:" % len(urls))
    for url, ts in urls:
        print("  %s%s  (%s)" % (BASE, url, ts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
