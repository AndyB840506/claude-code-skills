# Grading nocturno de Mr. Putrid's Den - Temporada 2.
#
# Split toning: enfria sombras y medios tonos hacia azul nocturno y deja el calido
# unicamente en las altas luces (el fuego). El punto no es "poner un filtro azul" sino
# crear contraste termico: cuando la escena entera es calida se aplana y lee acogedora;
# cuando solo el fuego es calido, el fuego manda y la escena lee nocturna.
#
# Parametros congelados el 2026-07-22 con la variante E, elegida sobre B/C/D.
# Se aplica DESPUES del upscale y DESPUES de vintage_grade, antes de componer el lockup.
#
# Uso CLI: python night_grade.py <entrada.jpg> <salida.jpg>
# Importable: from night_grade import night_grade, apply_to_file
import sys
from PIL import Image, ImageEnhance

# Variante E - oficial de Temporada 2
SHADOW_RGB = (16, 38, 92)     # azul nocturno para sombras y medios
SHADOW_AMT = 0.66
HIGHLIGHT_RGB = (255, 172, 92)  # calido reservado al fuego
HIGHLIGHT_AMT = 0.20
PIVOT = 152                   # luminancia que separa sombra de alta luz
SATURATION = 0.50             # baja el marron dominante de la escena base


def night_grade(im, shadow_rgb=SHADOW_RGB, shadow_amt=SHADOW_AMT,
                highlight_rgb=HIGHLIGHT_RGB, highlight_amt=HIGHLIGHT_AMT,
                pivot=PIVOT, saturation=SATURATION):
    im = ImageEnhance.Color(im.convert("RGB")).enhance(saturation)
    lum = im.convert("L")
    shadow_w = lum.point(lambda v: int((pivot - v) / pivot * 255) if v < pivot else 0)
    highlight_w = lum.point(lambda v: int((v - pivot) / (255 - pivot) * 255) if v > pivot else 0)
    im = Image.composite(
        Image.blend(im, Image.new("RGB", im.size, shadow_rgb), shadow_amt), im, shadow_w)
    return Image.composite(
        Image.blend(im, Image.new("RGB", im.size, highlight_rgb), highlight_amt), im, highlight_w)


def apply_to_file(src_path, out_path, **kwargs):
    night_grade(Image.open(src_path), **kwargs).save(out_path, quality=94)
    print("saved", out_path)


if __name__ == "__main__":
    apply_to_file(sys.argv[1], sys.argv[2])
