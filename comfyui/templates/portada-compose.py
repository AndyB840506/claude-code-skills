# ############################################################################
# MUERTO desde 2026-07-25 -- VACIADO el 2026-08-01. NO USAR.
#
# Componia la tipografia BTQ v4 sobre una escena renderizada. BTQ paso a
# portadas de TIPOGRAFIA PURA: el generador vigente para portadas normales es
#   comfyui/templates/portada-ep-compose.py   (deterministico, sin modelo)
#
# Si alguna vez se vuelve a componer tipografia SOBRE una escena, el vigente es
#   comfyui/templates/portada-compose-ratios.py
# que es este mismo archivo con un bug corregido: aqui el wordmark se
# dimensionaba solo con la ALTURA, asi que en 9:16 "THE QUEUE" se salia del
# cuadro. Alla se achica hasta caber en el ANCHO.
#
# El cuerpo original (137 lineas) se vacio a proposito: tener dos copias casi
# identicas del mismo compositor hacia que la version CON el bug se viera igual
# de viva que la corregida. Sigue completo en el historial:
#   git show 74e71f5:comfyui/templates/portada-compose.py
# ############################################################################
import sys

sys.exit(
    "portada-compose.py esta MUERTO.\n"
    "  - Portada normal (tipografia pura): portada-ep-compose.py\n"
    "  - Tipografia sobre escena:          portada-compose-ratios.py\n"
    "  - Cuerpo original: git show 74e71f5:comfyui/templates/portada-compose.py"
)
