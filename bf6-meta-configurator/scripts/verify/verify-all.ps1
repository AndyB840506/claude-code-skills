# Verify a built bf6-meta-app.html in headless Edge (no human needed).
# Usage: powershell -File verify-all.ps1 -Html <path to bf6-meta-app.html> [-Work <dir>]
# Runs 8 static cases (weapons/vehicles x MP/REDSEC x desktop/390px iframe) plus a click
# test. The verdict is computed against the EXPECTED list of checks: a missing result
# counts as FAIL, never as pass. Method notes: web-page-kit/docs/mobile-qa-headless.md
param(
  [Parameter(Mandatory = $true)][string]$Html,
  [string]$Work = "$env:TEMP\bf6-verify"
)
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$edge = "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
New-Item -ItemType Directory -Force $Work | Out-Null
Copy-Item $Html "$Work\app.html" -Force
$base = "file:///" + ($Work -replace '\\', '/')
$fails = New-Object System.Collections.ArrayList

function Get-Dbg([string]$url, [string]$size, [string]$id) {
  $a = @('--headless', '--no-first-run', "--user-data-dir=$Work\edgeprof", '--allow-file-access-from-files',
         "--window-size=$size", '--virtual-time-budget=15000', '--dump-dom', $url)
  Start-Process -FilePath $edge -ArgumentList $a -Wait -RedirectStandardOutput "$Work\out.html" -RedirectStandardError "$Work\out.log"
  $d = Get-Content "$Work\out.html" -Raw
  if ($d -match "(?s)<pre id=`"$id`">(.*?)</pre>") { return ($Matches[1] -replace '&quot;', '"' -replace '&amp;', '&') }
  return $null
}

$cases = @(@('weapons', 'MP'), @('weapons', 'REDSEC'), @('vehicles', 'MP'), @('vehicles', 'REDSEC'))
foreach ($c in $cases) {
  $name = "p-" + $c[0] + "-" + $c[1]
  python "$here\probe_static.py" "$Work\app.html" "$Work\$name.html" $c[0] $c[1]
  $frame = "<!doctype html><html><head><meta charset='utf-8'><style>body{margin:0}iframe{border:0;width:390px;height:900px}</style></head><body><iframe id='f' src='$name.html'></iframe><script>setTimeout(()=>{let t='';try{const d=document.getElementById('f').contentDocument.getElementById('dbg');if(d)t=d.textContent}catch(e){}const p=document.createElement('pre');p.id='outer';p.textContent=t;document.body.appendChild(p)},5200)</script></body></html>"
  [System.IO.File]::WriteAllText("$Work\f-$name.html", $frame, (New-Object System.Text.UTF8Encoding($false)))
  foreach ($w in @(@('desk', "$base/$name.html", '1440,900', 'dbg'), @('m390', "$base/f-$name.html", '600,1000', 'outer'))) {
    $label = $w[0] + " " + $c[0] + " " + $c[1]
    $raw = Get-Dbg $w[1] $w[2] $w[3]
    if (-not $raw) { [void]$fails.Add("$label : NO RESULT"); "$label : NO RESULT"; continue }
    $r = $raw | ConvertFrom-Json
    "$label : $raw"
    if ($r.errors.Count -gt 0) { [void]$fails.Add("$label : JS errors") }
    if ($r.hscroll) { [void]$fails.Add("$label : horizontal scroll") }
    if ($r.emdash -ne 0 -or $r.middot -ne 0) { [void]$fails.Add("$label : banned punctuation visible") }
    if ($r.sitesVisible -ne 0) { [void]$fails.Add("$label : source site names visible") }
    if ($r.stillPre -ne 0) { [void]$fails.Add("$label : elements left hidden (.pre)") }
    if ($r.rows -lt 1) { [void]$fails.Add("$label : no rows rendered") }
  }
}

python "$here\probe_clicks.py" "$Work\app.html" "$Work\p-clicks.html"
$raw = Get-Dbg "$base/p-clicks.html" '1440,900' 'dbg'
if (-not $raw) { [void]$fails.Add("clicks : NO RESULT"); "clicks : NO RESULT" }
else {
  "clicks : $raw"
  $r = $raw | ConvertFrom-Json
  if ($r.loOpenH -le 0) { [void]$fails.Add("clicks : opened build has no height") }
  if ($r.zonesStuck -ne 0 -or $r.zonesStuck2 -ne 0) { [void]$fails.Add("clicks : content left faded after a switch") }
  if (-not $r.redsecNote) { [void]$fails.Add("clicks : REDSEC vehicle note missing") }
  if ($r.errors.Count -gt 0) { [void]$fails.Add("clicks : JS errors") }
}

""
if ($fails.Count -eq 0) { "VERDICT: PASS (9 of 9 runs, every expected check present)" }
else { "VERDICT: FAIL"; $fails | ForEach-Object { " - $_" } }
