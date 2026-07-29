<#
    Masteriza un episodio de Mr. Putrid's Den al estandar de publicacion.

    Uso:
        .\masterizar-mpd.ps1 "E:\Podcast\MPD\Temporada 2\EP 01\MPD EP 01.wav"

    Entra un WAV renderizado de Reaper, sale el MP3 final medido y verificado.
    Los parametros salieron de la calibracion de T2E01 (2026-07-28); el porque
    de cada uno esta en guion-style-mpd.md, seccion Loudness.
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$Wav,

    [string]$Salida = "",

    # Ganancia pre-limitador. Subir si el render de Reaper viene mas bajo
    # de -18,3 LUFS; el script avisa cuanto sobra o falta.
    [double]$Ganancia = 3.2
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $Wav)) { throw "No existe: $Wav" }
if ($Salida -eq "") {
    $Salida = [IO.Path]::ChangeExtension($Wav, $null) + "MASTER.mp3"
    $Salida = $Salida -replace "\.MASTER\.mp3$", " MASTER.mp3"
}

# --- Targets de publicacion ---------------------------------------------
$T_LUFS = -16.0
$T_LRA  = 6.0
$T_TP   = -1.0     # limite duro de Spotify/Apple; apuntamos a -1,5

# ffmpeg escribe sus medidas a stderr. En PS 5.1, "2>&1" sobre un ejecutable
# nativo envuelve cada linea en un ErrorRecord y con ErrorActionPreference=Stop
# la primera linea aborta el script aunque ffmpeg salga con codigo 0. Por eso
# se baja a Continue solo alrededor de las llamadas y se verifica a mano.
function Invocar-Ffmpeg([string[]]$argumentos) {
    $previo = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $salida = & ffmpeg @argumentos 2>&1 | ForEach-Object { "$_" }
    } finally {
        $ErrorActionPreference = $previo
    }
    return $salida
}

function Medir($archivo) {
    $txt = Invocar-Ffmpeg @("-hide_banner", "-nostats", "-i", $archivo,
                            "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "NUL")
    $o = [ordered]@{}
    foreach ($l in $txt) {
        if ($l -match "I:\s*(-?[\d.]+)\s*LUFS")   { $o.LUFS = [double]$Matches[1] }
        if ($l -match "LRA:\s*([\d.]+)\s*LU")     { $o.LRA  = [double]$Matches[1] }
        if ($l -match "Peak:\s*(-?[\d.]+)\s*dBFS"){ $o.TP   = [double]$Matches[1] }
    }
    if (-not $o.Contains("LUFS")) { throw "No se pudo medir $archivo" }
    return $o
}

Write-Output "== Midiendo el render de Reaper =="
$antes = Medir $Wav
$dur = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 $Wav)
Write-Output ("  duracion   : {0:mm\:ss}" -f [TimeSpan]::FromSeconds($dur))
Write-Output ("  integrado  : {0} LUFS" -f $antes.LUFS)
Write-Output ("  LRA        : {0} LU" -f $antes.LRA)
Write-Output ("  true peak  : {0} dBFS" -f $antes.TP)

$sugerida = [math]::Round($T_LUFS - $antes.LUFS + 0.9, 1)
if ([math]::Abs($sugerida - $Ganancia) -gt 0.6) {
    Write-Output ""
    Write-Output ("  AVISO: con {0} LUFS de entrada la ganancia sugerida es {1} dB, no {2}." -f $antes.LUFS, $sugerida, $Ganancia)
    Write-Output ("         Si el resultado no aterriza en -16, reintentar con -Ganancia {0}" -f $sugerida)
}

Write-Output ""
Write-Output "== Masterizando =="
Write-Output ("  cadena: volume={0}dB -> alimiter(techo -2,0 dBFS, atk 2ms, rel 80ms) -> mp3 128k" -f $Ganancia)

$filtro = "volume={0}dB,alimiter=limit=0.7943:attack=2:release=80:level=0" -f $Ganancia
Invocar-Ffmpeg @("-hide_banner", "-nostats", "-y", "-i", $Wav, "-af", $filtro,
                 "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "2", $Salida) | Out-Null
if (-not (Test-Path $Salida)) { throw "El encode fallo" }

Write-Output ""
Write-Output "== Verificacion sobre el MP3 final =="
$post = Medir $Salida

$filas = @(
    @{ n = "Integrado"; v = $post.LUFS; u = "LUFS"; ok = ([math]::Abs($post.LUFS - $T_LUFS) -le 0.5); t = "-16 +-0,5" }
    @{ n = "LRA";       v = $post.LRA;  u = "LU";   ok = ($post.LRA -ge 4.5 -and $post.LRA -le 8.0); t = "4,5 - 8,0" }
    @{ n = "True peak"; v = $post.TP;   u = "dBFS"; ok = ($post.TP -le $T_TP); t = "<= -1,0" }
)
$todo = $true
foreach ($f in $filas) {
    $marca = "OK  "
    if (-not $f.ok) { $marca = "FALLA"; $todo = $false }
    Write-Output ("  [{0}] {1,-10} {2,8} {3,-5} (target {4})" -f $marca, $f.n, $f.v, $f.u, $f.t)
}

$caida = $antes.LRA - $post.LRA
if ($caida -gt 0.5) {
    Write-Output ""
    Write-Output ("  AVISO: el LRA cayo {0} LU ({1} -> {2}). Mas de 0,5 significa que el limitador" -f [math]::Round($caida,1), $antes.LRA, $post.LRA)
    Write-Output  "         esta aplastando dinamica, no solo picos. Bajar -Ganancia medio dB."
}

Write-Output ""
if ($todo) {
    Write-Output "LISTO PARA PUBLICAR"
} else {
    Write-Output "NO PUBLICAR - revisar las filas marcadas FALLA"
}
Write-Output ("Archivo: {0}" -f $Salida)
