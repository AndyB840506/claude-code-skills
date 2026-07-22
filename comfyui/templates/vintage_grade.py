# Tratamiento "foto antigua" determinista para artwork de MPD.
# Post-proceso en PIL/numpy sobre un render limpio: es mucho mas controlable
# que pedirle el envejecido al modelo de imagen.
import sys
import numpy as np
from PIL import Image, ImageFilter


def vintage(img, strength=1.0, seed=7):
    """Devuelve una copia envejecida de img (PIL.Image RGB).
    strength escala el efecto global (0 = sin efecto, 1 = tratamiento completo)."""
    rng = np.random.default_rng(seed)
    a = np.asarray(img.convert("RGB")).astype(np.float32) / 255.0
    h, w, _ = a.shape

    # 1. Desaturar parcialmente
    lum = a @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    a = a + (lum[..., None] - a) * (0.30 * strength)

    # 2. Split-tone calido: sombras al marron, altas luces a crema
    sh = np.array([0.16, 0.09, 0.03], dtype=np.float32)   # empuje en sombras
    hl = np.array([0.10, 0.07, 0.01], dtype=np.float32)   # empuje en altas
    t = lum[..., None]
    a = a + (sh * (1.0 - t) + hl * t) * (0.55 * strength)

    # 3. Negros lavados + contraste bajado (look de pelicula vieja)
    lift = 0.075 * strength
    gain = 1.0 - 0.10 * strength
    a = a * gain + lift

    # 4. Vineta radial
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    cx, cy = (w - 1) / 2.0, (h - 1) / 2.0
    r = np.sqrt(((xx - cx) / cx) ** 2 + ((yy - cy) / cy) ** 2) / np.sqrt(2.0)
    vig = 1.0 - (0.62 * strength) * np.clip(r - 0.28, 0, None) ** 1.7
    a = a * vig[..., None]

    # 5. Grano de pelicula (mas visible en medios tonos)
    l2 = np.clip(a @ np.array([0.299, 0.587, 0.114], dtype=np.float32), 0, 1)
    mid = 1.0 - np.abs(l2 - 0.5) * 2.0
    grain = rng.normal(0.0, 0.030 * strength, size=(h, w)).astype(np.float32)
    a = a + (grain * (0.45 + 0.55 * mid))[..., None]

    # 6. Polvo y rayas finas de la emulsion
    # Las rayas se confinan a los margenes laterales: nunca cruzan el sujeto central.
    n_scratch = int(7 * strength)
    for _ in range(n_scratch):
        if rng.random() < 0.5:
            x0 = rng.integers(0, int(w * 0.22))
        else:
            x0 = rng.integers(int(w * 0.78), w)
        length = rng.integers(int(h * 0.10), int(h * 0.55))
        y0 = rng.integers(0, max(1, h - length))
        drift = rng.normal(0, 0.7)
        val = rng.uniform(0.10, 0.26) * strength
        for k in range(length):
            x = int(x0 + drift * k / 12.0)
            if 0 <= x < w:
                a[y0 + k, x, :] += val
    n_dust = int(320 * strength)
    ys = rng.integers(0, h, n_dust)
    xs = rng.integers(0, w, n_dust)
    a[ys, xs, :] += rng.uniform(0.06, 0.30, (n_dust, 1)).astype(np.float32) * strength

    a = np.clip(a, 0.0, 1.0)
    out = Image.fromarray((a * 255).astype(np.uint8), "RGB")

    # 7. Suavizado leve: las copias viejas no son nitidas
    out = out.filter(ImageFilter.GaussianBlur(radius=0.4 * strength))
    return out


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    s = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    im = Image.open(src)
    vintage(im, strength=s).save(dst, quality=96)
    print("escrito:", dst, "strength:", s)
