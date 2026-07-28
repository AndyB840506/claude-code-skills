#!/bin/bash
# Fraccion de tiempo con voz via silencedetect. Mismo umbral para todos los
# archivos, para que la comparacion sea con el mismo instrumento.
# Se calibra contra MPD 04, del que tenemos SRT ademas del audio.

measure () {
  local F="$1"; local LABEL="$2"; local TH="$3"
  local DUR
  DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F")
  ffmpeg -hide_banner -i "$F" -af "silencedetect=noise=${TH}dB:d=0.35" -f null - 2>&1 \
    | grep -o "silence_duration: [0-9.]*" | awk -v d="$DUR" -v l="$LABEL" -v t="$TH" '
        {s += $2}
        END {
          voiced = d - s
          printf "  %-22s umbral %sdB | total %6.1f min | voz %6.1f min | %5.1f%% con voz\n", l, t, d/60, voiced/60, 100*voiced/d
        }'
}

for TH in -35 -40; do
  echo "=== umbral ${TH} dB ==="
  measure "/e/Podcast/MPD/EP 04/MPD 04 PT 1.mp3" "MPD EP04 P1 (co-host)" "$TH"
  measure "/e/Podcast/MPD/EP 04/MPD 04 PT 2.mp3" "MPD EP04 P2 (co-host)" "$TH"
  measure "/e/Podcast/MPD/Temporada 2/EP 01/MPD EP 01.mp3" "PILOTO T2 (solo)" "$TH"
  echo ""
done
