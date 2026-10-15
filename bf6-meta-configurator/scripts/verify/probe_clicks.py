"""Write a probe copy of the app that clicks through it like a user.

Usage: python probe_clicks.py <app.html> <out.html>

Opens the first build, switches to VEHICLES, to REDSEC, back to WEAPONS, and reports into
<pre id="dbg">: build height closed/open (open must be > 0: the timer pins it even in
headless), row counts per view, zones left faded (.swap-zone.out, must be 0), and JS errors.
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
html = open(src, encoding='utf-8').read()
head = "<script>window.__err=[];addEventListener('error',e=>__err.push(String(e.message)));try{localStorage.removeItem('bf6ops')}catch(e){}</script>"
tail = r"""<script>
const wait = ms => new Promise(r => setTimeout(r, ms));
addEventListener('load', async () => {
  const R = {};
  await wait(600);
  const row = document.querySelector('#main .row');
  R.loClosedH = Math.round(row.querySelector('.lo').getBoundingClientRect().height);
  row.querySelector('.row-main').click();
  await wait(1800);
  R.loOpenH = Math.round(row.querySelector('.lo').getBoundingClientRect().height);
  R.reelDone = row.querySelector('.loadout').classList.contains('done');
  R.weapRows = document.querySelectorAll('#main .row').length;
  document.querySelector('.views button[data-view="vehicles"]').click();
  await wait(1500);
  R.vehRows = document.querySelectorAll('#main .row').length;
  R.zonesStuck = document.querySelectorAll('.swap-zone.out').length;
  document.querySelector('#c-mode button[data-v="REDSEC"]').click();
  await wait(1500);
  R.redsecNote = !!document.querySelector('#mode-note .note');
  document.querySelector('.views button[data-view="weapons"]').click();
  await wait(1500);
  R.redsecWeapRows = document.querySelectorAll('#main .row').length;
  R.zonesStuck2 = document.querySelectorAll('.swap-zone.out').length;
  R.errors = window.__err;
  const pre = document.createElement('pre'); pre.id = 'dbg'; pre.textContent = JSON.stringify(R); document.body.appendChild(pre);
});
</script></body>"""
assert html.count('<head>') == 1 and html.count('</body>') == 1, 'unexpected template shape'
open(dst, 'w', encoding='utf-8').write(html.replace('<head>', '<head>' + head).replace('</body>', tail))
