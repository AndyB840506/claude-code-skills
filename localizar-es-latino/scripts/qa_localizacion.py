#!/usr/bin/env python3
"""Validador determinista del contrato mecanico de localizacion EN -> ES.

Uso:  python qa_localizacion.py trabajo.json [--salida salida-es.txt]

Lee el archivo de trabajo, compara cada fila contra su original en ingles y
reporta ERROR (rompe el build, hay que corregir) o AVISO (revisar y decidir).
Codigo de salida 1 si hay algun ERROR.

Estandar de idioma: ESPANOL NEUTRO latinoamericano (registro de doblaje).
Lexico neutro siempre, caracter regional nunca -- de ningun pais.
"""

import argparse
import json
import re
import sys
import unicodedata

TAG = re.compile(r"<[^>]+>")
# Debe coincidir con la constante TOKENS de page/columna-es.html. Si se toca
# una, tocar la otra: son dos mediciones del mismo contrato a proposito, pero
# solo sirven como cruce mientras midan lo mismo.
PLACEHOLDERS = [
    re.compile(r"\\[nrt]"),          # escapes literales dentro del string
    re.compile(r"\([A-Z0-9_]{2,14}\)"),
    re.compile(r"\{[^{}]*\}"),
    re.compile(r"\[[^\[\]]*\]"),
    re.compile(r"%\d+\$[sd]|%[sd]"),
    re.compile(r"\$[A-Za-z_][A-Za-z0-9_]*"),
]

FIN = ".!?…"
BORDES = "\"'»”’)]"

# (etiqueta, patron sobre el texto en minusculas y sin tildes, nota)
#
# El estandar es ESPANOL NEUTRO: ninguna jerga local, venga del pais que venga.
# Mexico no es la excepcion -- es el regionalismo que mas se cuela, porque el
# neutro se construye sobre una base mexicana y es facil pasarse de ahi.
#
# Todos son AVISO: el contexto manda y el validador no lo conoce.
REGIONALISMOS = [
    # --- Mexico ---
    ("chingar", r"\bching\w*",
     "mexicanismo fuerte; en neutro: mierda/carajo/maldita sea/maldito"),
    ("pinche", r"\bpinches?\b", "mexicanismo; en neutro: maldito/puto"),
    ("guey", r"\b(guey|wey)\b", "mexicanismo; en neutro: amigo/idiota segun el caso"),
    ("no mames", r"\bno (mames|manches)\b",
     "mexicanismo; en neutro: no puede ser / no jodas / es en serio"),
    ("orale", r"\borale\b", "mexicanismo; en neutro: vamos/anda/esta bien"),
    ("chido", r"\bchido\w*", "mexicanismo; en neutro: genial/buenisimo"),
    ("neta", r"\bneta\b", "mexicanismo; en neutro: en serio/de verdad"),
    ("carnal", r"\bcarnal(es)?\b",
     "si es 'amigo' es mexicanismo (usar hermano/amigo). Ignorar si es "
     "'deseo carnal'"),
    ("pendejo", r"\bpendej\w*", "marcado MX; en neutro: idiota/imbecil/estupido"),
    ("cabron", r"\bcabron\w*", "marcado MX; en neutro: desgraciado/maldito/bastardo"),
    ("panocha", r"\bpanocha\w*", "mexicanismo; ver la seccion de contenido adulto"),
    ("chichis", r"\bchichis\b", "mexicanismo; en neutro: tetas/senos"),
    ("puta madre", r"\bputa madre\b",
     "marcado MX/ES; en neutro: mierda/carajo/maldita sea"),
    # --- Espana ---
    ("vosotros", r"\b(vosotros|vuestr\w+|\w{3,}(ais|eis))\b",
     "conjugacion de Espana; usar ustedes"),
    ("follar", r"\bfoll\w*", "de Espana; ver la seccion de contenido adulto"),
    ("polla", r"\bpollas?\b", "de Espana; en neutro: verga/miembro"),
    ("gilipollas", r"\bgilipollas\b", "de Espana; en neutro: idiota/imbecil/estupido"),
    ("hostia", r"\bhostias?\b", "de Espana; en neutro: mierda/carajo (no suavizar)"),
    ("joder", r"\bjoder\b",
     "como interjeccion es de Espana; en neutro: mierda/carajo. "
     "'jodete' y 'jodido' si son neutros"),
    ("chaval", r"\bchaval\w*", "de Espana; usar chico/muchacho/joven"),
    ("ordenador", r"\bordenador\w*", "de Espana; usar computadora"),
    ("movil", r"\bmovil\b", "de Espana; usar celular"),
    ("zumo", r"\bzumo\w*", "de Espana; usar jugo"),
    ("guay", r"\bguay\b", "de Espana; usar genial/buenisimo"),
    ("aparcar", r"\baparc\w*", "de Espana; usar estacionar"),
    ("correrse", r"\b(correte|me corro|te corres|corriendome)\b",
     "en sentido sexual es de Espana; en neutro: acabar/venirse"),
    ("vale", r"\bvale\b",
     "si es 'ok' es de Espana; usar esta bien/de acuerdo/listo. Ignorar si es "
     "el verbo valer"),
    # --- Cono Sur ---
    ("voseo", r"\b(sos|vos|che|tenes|queres|podes|venis|decis)\b",
     "voseo rioplatense; usar tu (eres/tienes/quieres/puedes)"),
    ("boludo", r"\bbolud\w*", "de AR; en neutro: idiota/imbecil"),
    ("pija", r"\bpijas?\b", "de AR; en neutro: verga/miembro"),
    ("concha", r"\bconchas?\b",
     "vulgar en Cono Sur; ver la seccion de contenido adulto"),
    ("huevon", r"\bhuevon\w*", "de CL/CO; en neutro: idiota/imbecil"),
    ("culear", r"\bcule\w*", "de Cono Sur/CO; ver la seccion de contenido adulto"),
    # --- Colombia y Caribe ---
    ("malparido", r"\bmalparid\w*", "de CO; en neutro: desgraciado/hijo de puta"),
    ("parcero", r"\bparcer\w*", "de CO; en neutro: amigo/hermano"),
    ("pinga", r"\bpinga\b", "del Caribe; en neutro: verga/miembro"),
    # --- transversal ---
    ("coger", r"\bcog(e|i)\w*",
     "ambiguo y marcado: verbo sexual en MX/AR, 'agarrar' en otros paises. "
     "Para agarrar un objeto usar agarrar/tomar; en escena sexual, reformular"),
]
REGIONALISMOS = [(n, re.compile(p), nota) for n, p, nota in REGIONALISMOS]


def sin_tildes(texto):
    desc = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in desc if unicodedata.category(c) != "Mn")


def plano(texto):
    return TAG.sub("", texto)


def firma_final(texto):
    limpio = plano(texto).rstrip()
    while limpio and limpio[-1] in BORDES:
        limpio = limpio[:-1].rstrip()
    corte = len(limpio)
    while corte > 0 and limpio[corte - 1] in FIN:
        corte -= 1
    return limpio[corte:]


def placeholders(texto):
    hallados = []
    for patron in PLACEHOLDERS:
        hallados.extend(patron.findall(texto))
    return sorted(hallados)


def revisar(fila, vistos, problemas):
    fid = fila.get("id", "?")
    en = fila.get("en", "")
    es = fila.get("es", "")

    def err(check, detalle):
        problemas.append(("ERROR", fid, check, detalle))

    def avi(check, detalle):
        problemas.append(("AVISO", fid, check, detalle))

    if en.strip() and not es.strip():
        err("vacio", "el ingles tiene texto y el espanol esta vacio")
        return
    if not en.strip() and not es.strip():
        return

    if es != es.strip():
        err("espacios", "hay espacio o salto al inicio o al final de la celda")
    if "  " in es:
        err("espacios", "hay espacio doble dentro del texto")
    if "\r" in es:
        err("saltos", "hay retorno de carro (\\r) en la celda")

    if es.count("\n") != en.count("\n"):
        err("saltos", "saltos de linea internos EN=%d ES=%d"
            % (en.count("\n"), es.count("\n")))

    fe, fs = firma_final(en), firma_final(es)
    if fe != fs:
        err("puntuacion", "final EN=%r ES=%r" % (fe, fs))

    te, ts = TAG.findall(en), TAG.findall(es)
    if te != ts:
        err("tags", "EN=%s ES=%s" % (te, ts))

    pe, ps = placeholders(en), placeholders(es)
    if pe != ps:
        err("placeholders", "EN=%s ES=%s" % (pe, ps))

    if re.search(r"\s[!?;:]", es):
        err("espacio-signo", "espacio antes de signo (norma francesa, no espanola)")

    normal = sin_tildes(plano(es))
    for etiqueta, patron, nota in REGIONALISMOS:
        if patron.search(normal):
            avi("regionalismo", "'%s' - %s" % (etiqueta, nota))

    plano_es = plano(es)
    if plano_es.count("¿") > plano_es.count("?"):
        avi("signos", "hay '¿' sin cerrar (esperable si el EN no cierra - confirmar)")
    if plano_es.count("¡") > plano_es.count("!"):
        avi("signos", "hay '¡' sin cerrar (esperable si el EN no cierra - confirmar)")

    le, ls = len(plano(en)), len(plano_es)
    if le >= 8 and ls > le * 1.4:
        avi("largo", "expansion +%d%% (%d -> %d) - revisar si es string de UI"
            % (round((ls / le - 1) * 100), le, ls))

    if en in vistos and vistos[en][0] != es:
        err("consistencia", "el mismo texto ingles ya se tradujo distinto en la fila %s"
            % vistos[en][1])
    else:
        vistos.setdefault(en, (es, fid))


def analizar(filas):
    """Corre todos los checks sobre el lote y devuelve la lista de problemas.

    Fuente unica de verdad: la compuerta de QA y el generador de la pagina de
    revision llaman a esta misma funcion, para que no puedan divergir.
    """
    problemas = []
    vistos = {}
    for fila in filas:
        revisar(fila, vistos, problemas)

    cola = 0
    for fila in reversed(filas):
        if fila.get("en", "").strip() or fila.get("es", "").strip():
            break
        cola += 1
    if cola:
        problemas.append(("ERROR", "-", "filas-cola",
                          "hay %d fila(s) vacia(s) al final del lote" % cola))
    return problemas


def cargar(ruta):
    with open(ruta, encoding="utf-8-sig") as fh:
        return json.load(fh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivo")
    ap.add_argument("--salida", help="escribe la columna ES, una fila por linea")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    datos = cargar(args.archivo)
    filas = datos["filas"]
    problemas = analizar(filas)

    errores = sum(1 for p in problemas if p[0] == "ERROR")
    avisos = len(problemas) - errores

    print("Lote: %s" % datos.get("proyecto", args.archivo))
    print("Filas: %d" % len(filas))
    print("")
    if problemas:
        print("%-6s %-6s %-14s %s" % ("NIVEL", "FILA", "CHECK", "DETALLE"))
        print("-" * 78)
        for nivel, fid, check, detalle in problemas:
            print("%-6s %-6s %-14s %s" % (nivel, fid, check, detalle))
        print("")
    print("RESULTADO: %d error(es), %d aviso(s)" % (errores, avisos))
    if errores == 0:
        print("Contrato mecanico OK - el lote se puede pegar en la columna.")

    if args.salida and errores == 0:
        with open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(f.get("es", "") for f in filas))
        print("Columna escrita en: %s" % args.salida)

    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
