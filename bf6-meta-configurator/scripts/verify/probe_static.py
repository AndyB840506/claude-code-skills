"""Write a probe copy of the app that reports its rendered state into <pre id="dbg">.

Usage: python probe_static.py <app.html> <out.html> <view: weapons|vehicles> <mode: MP|REDSEC>

The page is preset to the given view and mode through localStorage. After load it reports
JS errors, horizontal overflow, row and section counts, em dashes and middots in the
VISIBLE text, source-site names in the visible text, and elements still hidden in .pre.
Read the result with `msedge --dump-dom` (see verify-all.ps1).
"""
import json, sys

src, dst, view, mode = sys.argv[1:5]
html = open(src, encoding='utf-8').read()
head = ("<script>window.__err=[];addEventListener('error',e=>__err.push(String(e.message)));"
        "try{localStorage.setItem('bf6ops',JSON.stringify({view:%s,mode:%s}))}catch(e){}</script>") % (json.dumps(view), json.dumps(mode))
tail = r"""<script>
addEventListener('load', () => setTimeout(() => {
  const vw = document.documentElement.clientWidth, sw = document.documentElement.scrollWidth;
  const t = document.body.innerText;
  const sites = (t.match(/wzstats|battlefinity|bfhub|dexerto|gamerant|bftactics|timesaver|switchblade|overgear|gamesradar/gi) || []);
  const out = {
    view: %s, mode: %s, vw, sw, hscroll: sw > vw,
    rows: document.querySelectorAll('#main .row').length,
    sections: document.querySelectorAll('#main > section').length,
    emdash: (t.match(/—/g) || []).length, middot: (t.match(/·/g) || []).length,
    sitesVisible: sites.length, sitesSample: sites.slice(0, 5),
    stillPre: document.querySelectorAll('.pre').length,
    errors: window.__err
  };
  const pre = document.createElement('pre'); pre.id = 'dbg'; pre.textContent = JSON.stringify(out); document.body.appendChild(pre);
}, 3200));
</script></body>""" % (json.dumps(view), json.dumps(mode))
assert html.count('<head>') == 1 and html.count('</body>') == 1, 'unexpected template shape'
open(dst, 'w', encoding='utf-8').write(html.replace('<head>', '<head>' + head).replace('</body>', tail))
