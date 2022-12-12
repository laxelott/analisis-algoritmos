import os
import math
import time
import threading
from PIL import Image

def rotate_image(image: Image, clkwise) -> Image:
    global loading
    width, height = image.size
    result = Image.new("RGB", (height, width))
    
    # Límite de imagen, si tiene 1px de alto o ancho ya no se puede dividir y tenemos que rotar los pixeles uno a uno
    if width == 1:
        loading.plusProgress()
        forRange = range(height)
        if not clkwise:
            forRange = reversed(forRange)

        # Rotar los píxeles uno a uno
        for i in forRange:
            result.paste(image.crop((0, i, 1, i+1)), box=(i, 0))

        return result
    elif height == 1:
        loading.plusProgress()
        forRange = range(width)
        if not clkwise:
            forRange = reversed(forRange)

        # Rotar los píxeles uno a uno
        for i in forRange:
            result.paste(image.crop((i, 0, i+1, 1)), box=(0, i))
        
        return result
    else:
        # Si aún se puede dividir, dividir en 4 cuadrantes (00, 01, 10, 11)
        image00 = image.crop((0, 0, math.floor(width / 2), math.floor(height / 2)))
        image01 = image.crop((math.floor(width / 2), 0, width, math.floor(height / 2)))
        image10 = image.crop((0, math.floor(height / 2), math.floor(width / 2), height))
        image11 = image.crop((math.floor(width / 2), math.floor(height / 2), width, height))
        
        # Rotar dichos cuadrantes con recursión
        image00 = rotate_image(image00, clkwise)
        image01 = rotate_image(image01, clkwise)
        image10 = rotate_image(image10, clkwise)
        image11 = rotate_image(image11, clkwise)

        aux = image00
        # Intercambiar los cuadrantes, dependiendo de la dirección de rotación
        if clkwise:
            image00 = image10
            image10 = image11
            image11 = image01
            image01 = aux
        else:
            image00 = image01
            image01 = image11
            image11 = image10
            image10 = aux

        # Rearmar imagen final
        result.paste(image00, box=(0, 0))
        result.paste(image01, box=(image00.size[0], 0))
        result.paste(image10, box=(0, image00.size[1]))
        result.paste(image11, box=(image00.size[0], image00.size[1]))
        return result

# Clase para que se vea bomnito el proceso, no tiene nada que ver con el ejercicio
class LoadingBar(threading.Thread):
    def __init__(self, total: int) -> None:
        threading.Thread.__init__(self)
        self.total = total
        self.progress = 0
        self.stop = False
        
    def run(self) -> None:
        while not self.stop:
            time.sleep(0.1)
            consoleTotal = math.floor(os.get_terminal_size().columns * 0.7) - 10
            consoleProgress = math.ceil(self.progress / self.total * consoleTotal)
            percentProgress = round(self.progress / self.total * 100, 3)
            consoleProgress = "=" * consoleProgress
            print(f"\r|{consoleProgress.ljust(consoleTotal)}| {percentProgress}%", end="")
        
    
    def plusProgress(self) -> None:
        self.progress += 1
    
    def updateProgress(self, progress) -> None:
        self.progress = progress
    
    def stopThread(self) -> None:
        self.stop = True

input = Image.open("dino-test.jpg")
width, height = input.size
total = min(width, height) * min(width, height) * 1.3

global loading
loading = LoadingBar(total)

print(width)
print(height)

print("Rotando imagen...")
loading.start()
result = rotate_image(input, False)
loading.updateProgress(total)
loading.stopThread()
loading.join()
print(loading.progress)
print("Imagen rotada c:")

result.save("final.png")
