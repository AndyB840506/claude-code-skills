"""Build bf6-meta-app.html from the template and the two data files.

Usage: python build.py <weapons.json> <vehicles.json> <out.html> [<copy-to.html> ...]

Visible copy is cleaned on the way in: an em dash between clauses becomes a period,
a middot list separator becomes a comma. Stats strings keep their middot because the
app splits them into chips on it. Aborts if a banned character survives.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
EM, MID = '—', '·'

def clean(s):
    s = re.sub(r'\s+' + EM + r'\s+(\w)', lambda m: '. ' + m.group(1).upper(), s)
    s = s.replace(EM, ', ')
    return s.replace(' ' + MID + ' ', ', ').replace(MID, ',')

def walk(o, key=None):
    if isinstance(o, dict):
        return {k: (v if k == 'stats' else walk(v, k)) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(v, key) for v in o]
    if isinstance(o, str) and key not in ('url',):
        return clean(o)
    return o

def main():
    weapons, vehicles, out = sys.argv[1], sys.argv[2], sys.argv[3]
    data = json.loads(Path(weapons).read_text(encoding='utf-8'))
    data['vehicles'] = json.loads(Path(vehicles).read_text(encoding='utf-8'))
    data = walk(data)
    bad = [m.group(0) for m in re.finditer(EM, json.dumps(data, ensure_ascii=False))]
    if bad:
        sys.exit(f'em dash survived cleaning: {len(bad)}')
    blob = json.dumps(data, ensure_ascii=False, indent=1).replace('</', '<\\/')
    tpl = (HERE.parent / 'templates' / 'template.html').read_text(encoding='utf-8')
    if tpl.count('__DATA__') != 1:
        sys.exit('template must contain __DATA__ exactly once')
    html = tpl.replace('__DATA__', blob)
    for dest in [out] + sys.argv[4:]:
        Path(dest).parent.mkdir(parents=True, exist_ok=True)
        Path(dest).write_text(html, encoding='utf-8', newline='\n')
        print('wrote', dest, len(html.encode('utf-8')), 'bytes')

if __name__ == '__main__':
    main()
