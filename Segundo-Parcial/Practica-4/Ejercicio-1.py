import sys
import math
import requests
import pandas as pd
import io
from PIL import Image
sys.path.append( './../../' )
from Aux.LoadingBar import LoadingBar

def rotate_image(image: Image, clkwise) -> Image:
    global loading
    global prog
    prog += 1
    prog += 1
    width, height = image.size
    result = Image.new("RGB", (height, width))
    
    # Límite de imagen, si tiene 1px de alto o ancho ya no se puede dividir y tenemos que rotar los pixeles uno a uno
    prog += 1
    prog += 1
    if width == 1:
        prog += 1
        prog += 1
        loading.plusProgress()
        forRange = range(height)
        prog += 1
        if not clkwise:
            prog += 1
            forRange = reversed(forRange)

        # Rotar los píxeles uno a uno
        prog += 1
        for i in forRange:
            prog += 1
            result.paste(image.crop((0, i, 1, i+1)), box=(i, 0))
        prog += 1

        prog += 1
        return result
    elif height == 1:
        prog += 1
        prog += 1
        loading.plusProgress()
        forRange = range(width)
        prog += 1
        if not clkwise:
            prog += 1
            forRange = reversed(forRange)

        # Rotar los píxeles uno a uno
        prog += 1
        for i in forRange:
            prog += 1
            result.paste(image.crop((i, 0, i+1, 1)), box=(0, i))
        prog += 1
        
        prog += 1
        return result
    else:
        prog += 1
        prog += 1
        prog += 1
        prog += 1
        # Si aún se puede dividir, dividir en 4 cuadrantes (00, 01, 10, 11)
        image00 = image.crop((0, 0, math.floor(width / 2), math.floor(height / 2)))
        image01 = image.crop((math.floor(width / 2), 0, width, math.floor(height / 2)))
        image10 = image.crop((0, math.floor(height / 2), math.floor(width / 2), height))
        image11 = image.crop((math.floor(width / 2), math.floor(height / 2), width, height))
        
        prog += 1
        prog += 1
        prog += 1
        prog += 1
        # Rotar dichos cuadrantes con recursión
        image00 = rotate_image(image00, clkwise)
        image01 = rotate_image(image01, clkwise)
        image10 = rotate_image(image10, clkwise)
        image11 = rotate_image(image11, clkwise)

        prog += 1
        aux = image00
        prog += 1
        # Intercambiar los cuadrantes, dependiendo de la dirección de rotación
        if clkwise:
            prog += 1
            prog += 1
            prog += 1
            prog += 1
            image00 = image10
            image10 = image11
            image11 = image01
            image01 = aux
        else:
            prog += 1
            prog += 1
            prog += 1
            prog += 1
            image00 = image01
            image01 = image11
            image11 = image10
            image10 = aux

        prog += 1
        prog += 1
        prog += 1
        prog += 1
        # Rearmar imagen final
        result.paste(image00, box=(0, 0))
        result.paste(image01, box=(image00.size[0], 0))
        result.paste(image10, box=(0, image00.size[1]))
        result.paste(image11, box=(image00.size[0], image00.size[1]))
        prog += 1
        return result

global prog
prog = 1

def getImage(w, h):
    request = requests.get(f"https://placekitten.com/{w}/{h}")
    image_file = io.BytesIO(request.content)
    return Image.open(image_file)

def analisis_rotate_image(n, fileName):
    global prog
    global loading
    res = []

    for i in range(1, n):
        for j in range(1, n):
            # Usar imagenes grandes para probar bien el algoritmo (y también para que se vean bien)
            prog = 0
            w = i*100
            h = j*100
            print(f"\nDescargando imagen de {w}x{h}")
            image = getImage(w, h)
            print("Rotando...")
            loading = LoadingBar(w * h)
            loading.start()
            result = rotate_image(image, True)
            loading.finalize()

            result.save(f"result{w}x{h}.png")
            res.append([w, h, prog])
            
    print("\nEscribiendo a csv...                 ")

    df = pd.DataFrame()
    df['Results'] = pd.Series(res)
    df.to_csv(fileName)

analisis_rotate_image(5, "results.csv")