#!/usr/bin/env python3
"""Audita el solapamiento de triggers entre todas las skills del kit.

Uso:  python skill-management/scripts/audit-triggers.py [raiz]
      (raiz por defecto: el directorio actual)

Cinco tests. Los tres primeros detectan colisiones reales; D y E son heuristicas
de riesgo (marcan algo que HOY puede no estar chocando con nada).

  A  Colisiones exactas      dos skills declaran la misma frase
  B  Contencion             una frase esta contenida en otra ("lanzar episodio"
                            dentro de "lanzar episodio completo")
  C  Casi-duplicados        >=60% de palabras compartidas entre dos frases
  D  Alcance de proyecto    skill atada a un proyecto (BTQ/MPD/BF6...) con
                            triggers que NO nombran el proyecto
  E  Sin zona Triggers      skills que compiten con toda su prosa

Historial: escrito el 2026-07-23 tras una auditoria que fallo dos veces.
  - glob('**/SKILL.md') de Python OMITE carpetas que empiezan con punto: leia
    18 de 28 skills y reportaba "cero colisiones". Por eso aca se usa os.walk.
  - El test de coincidencia exacta NO veia el caso peor (episode-launch, que
    reclamaba "lanzar episodio" siendo skill exclusiva de BTQ). Por eso existen
    B y C.
"""
import re, io, os, sys, itertools, unicodedata

# Proyectos con skills dedicadas: regex que reconoce el proyecto en un trigger.
PROYECTOS = {
    'BTQ':  r'btq|behind the queue',
    'MPD':  r'mpd|putrid|guarida',
    'BF6':  r'bf6|battlefield|redsec',
}
# Prefijos que no son triggers sino prosa instructiva.
NO_TRIGGER = ('use ', 'usar ', 'when ', 'cuando ', 'not for', 'solo para')


def sin_tildes(s):
    """La consola de Windows (cp1252) rompe los acentos al imprimir."""
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()


def cargar(raiz):
    """Devuelve {nombre: {'ph': set(frases), 'desc': str, 'triggers': bool}}."""
    skills = {}
    for root, dirs, files in os.walk(raiz):
        if '.git' in root.split(os.sep):
            continue
        if 'SKILL.md' not in files:
            continue
        ruta = os.path.join(root, 'SKILL.md')
        texto = io.open(ruta, encoding='utf-8', errors='replace').read()
        m = re.search(r'^---\s*(.*?)^---', texto, re.S | re.M)
        if not m:
            print('  !! SIN FRONTMATTER: %s' % ruta)
            continue
        fm = m.group(1)
        nm = re.search(r'^name:\s*(.+)$', fm, re.M)
        nombre = nm.group(1).strip() if nm else os.path.basename(root)
        d = re.search(r'description:\s*(.+?)(?=\n[a-z_]+:\s|\Z)', fm, re.S)
        desc = d.group(1) if d else ''
        # Zona explicita de triggers (ES/EN) si existe; si no, toda la descripcion.
        zonas = re.findall(
            r'(?:short\s+)?triggers?(?:\s*\(?(?:es|en)\)?)?\s*[:\-]\s*(.+?)'
            r'(?=(?:short\s+)?triggers?\s*(?:\(?(?:es|en)\)?)?\s*[:\-]|$)',
            desc, re.I | re.S)
        crudo = ' , '.join(zonas) if zonas else desc
        frases = set()
        for x in re.split(r'[,;\n]|\.\s', crudo):
            x = re.sub(r'\s+', ' ', x.strip().strip('"\'.*` ').lower().lstrip('/'))
            if 4 <= len(x) <= 60 and not x.startswith(NO_TRIGGER):
                frases.add(x)
        skills[nombre] = {'ph': frases, 'desc': desc, 'triggers': bool(zonas)}
    return skills


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else '.'
    sk = cargar(raiz)
    nombres = sorted(sk)
    print('SKILLS ANALIZADAS: %d\n' % len(sk))
    hallazgos = 0

    inv = {}
    for n in nombres:
        for p in sk[n]['ph']:
            inv.setdefault(p, set()).add(n)
    exactas = {p: s for p, s in inv.items() if len(s) > 1}
    print('A) COLISIONES EXACTAS: %d' % len(exactas))
    for p, s in sorted(exactas.items()):
        print('   "%s" -> %s' % (sin_tildes(p), ', '.join(sorted(s))))
    hallazgos += len(exactas)

    cont = set()
    for a, b in itertools.permutations(nombres, 2):
        for pa in sk[a]['ph']:
            if len(pa.split()) < 2:
                continue
            for pb in sk[b]['ph']:
                if pa != pb and re.search(r'\b%s\b' % re.escape(pa), pb):
                    cont.add((sin_tildes(pa), a, sin_tildes(pb), b))
    print('\nB) CONTENCION: %d' % len(cont))
    for pa, a, pb, b in sorted(cont):
        print('   "%s" (%s) DENTRO DE "%s" (%s)' % (pa, a, pb, b))
    hallazgos += len(cont)

    casi = 0
    print('\nC) CASI-DUPLICADOS (>=60%):')
    for a, b in itertools.combinations(nombres, 2):
        for pa in sk[a]['ph']:
            for pb in sk[b]['ph']:
                A, B = set(pa.split()), set(pb.split())
                if len(A) < 2 or len(B) < 2:
                    continue
                if 0.6 <= len(A & B) / len(A | B) < 1.0:
                    print('   "%s" (%s) ~ "%s" (%s)'
                          % (sin_tildes(pa), a, sin_tildes(pb), b))
                    casi += 1
    print('   total: %d' % casi)
    hallazgos += casi

    print('\nD) SKILLS DE PROYECTO CON TRIGGERS GENERICOS (heuristica):')
    marcadas = 0
    for n in nombres:
        dl = sk[n]['desc'].lower()
        for tag, rx in PROYECTOS.items():
            if re.search(rx, dl):
                gen = [p for p in sk[n]['ph']
                       if not re.search(rx, p) and len(p.split()) >= 2
                       and not p.startswith(n[:6])]
                if gen:
                    marcadas += 1
                    print('   %s (%s): %s' % (n, tag, [sin_tildes(g) for g in sorted(gen)]))
                break
    if not marcadas:
        print('   ninguna')

    faltan = [n for n in nombres if not sk[n]['triggers']]
    print('\nE) SIN ZONA "Triggers:" EXPLICITA: %d de %d' % (len(faltan), len(sk)))
    for n in faltan:
        print('   - %s' % n)

    print('\n--- colisiones reales (A+B+C): %d ---' % hallazgos)
    print('D y E son avisos: marcan riesgo futuro, no un choque de hoy.')
    print('Un solapamiento puede ser ACEPTADO si ambas descripciones se')
    print('desambiguan entre si en el texto (ver handoff vs session-close).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
