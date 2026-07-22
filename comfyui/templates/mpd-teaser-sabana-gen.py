# -*- coding: utf-8 -*-
"""Genera la tela (sabana guardapolvo) para el teaser de revelacion de la portada T2.

Se genera SOLO la tela sobre fondo negro, no la escena completa con un cuadro debajo.
Razon: si el modelo pinta tambien lo que hay bajo la tela, lo que se revela es una
invencion suya, no nuestra portada. Con la tela aislada, el compositor PIL controla
exactamente cuanto artwork real se ve.
"""
import json
import time
import urllib.request

API = "http://127.0.0.1:8188"
TPL = r"c:\Users\andre\.claude\skills\comfyui\templates\zimage-txt2img-api.json"

POSITIVE = (
    "a heavy white cotton dust sheet with deep soft folds and creases, draped over an "
    "unseen rectangular object, the top edge of the sheet falling in a diagonal line "
    "across the frame, the sheet occupies the lower part of the frame, pure black empty "
    "background above the sheet, dramatic low side lighting from the left, warm dim light "
    "grazing the fabric, deep shadows in the folds, photographic, sharp fabric texture, "
    "linen weave visible, dusty aged cloth, still life, no people, no furniture, no text"
)

g = json.load(open(TPL, encoding="utf-8"))["prompt"]
g["67"]["inputs"]["text"] = POSITIVE
g["68"]["inputs"]["width"] = 1024
g["68"]["inputs"]["height"] = 1024
g["70"]["inputs"]["seed"] = 771969        # 3-jul-1969 / 3-jul-1971, por si hay que repetir
g["9"]["inputs"]["filename_prefix"] = "MPD-T2-sabana"

req = urllib.request.Request(API + "/prompt", method="POST",
                             data=json.dumps({"prompt": g}).encode("utf-8"),
                             headers={"Content-Type": "application/json"})
resp = json.loads(urllib.request.urlopen(req).read())
pid = resp["prompt_id"]
print("encolado:", pid, "| node_errors:", resp.get("node_errors"))

for i in range(150):
    time.sleep(4)
    h = json.loads(urllib.request.urlopen(API + "/history/" + pid).read())
    if h:
        st = h[pid]["status"]
        print("estado:", st.get("status_str"), "tras", (i + 1) * 4, "s")
        if st.get("status_str") == "success":
            for node in h[pid]["outputs"].values():
                for img in node.get("images", []):
                    print("archivo:", img["filename"], "|", img["subfolder"], "|", img["type"])
        break
else:
    print("timeout")
