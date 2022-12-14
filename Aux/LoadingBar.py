import threading
import time
import math
import os

# Clase para que se vea bomnito el proceso, no tiene nada que ver con el ejercicio
class LoadingBar(threading.Thread):
    def __init__(self, total: int) -> None:
        threading.Thread.__init__(self)
        self.total = total
        self.progress = 0
        self.stop = False
        
    def run(self) -> None:
        self.stop = False
        while not self.stop:
            time.sleep(0.1)
            consoleTotal = math.floor(os.get_terminal_size().columns * 0.7) - 10
            consoleProgress = math.ceil(self.progress / self.total * consoleTotal)
            percentProgress = round(self.progress / self.total * 100, 3)
            consoleProgress = "=" * consoleProgress
            print(f"\r|{consoleProgress.ljust(consoleTotal)}| {percentProgress}%\t\t", end="")

    def plusProgress(self) -> None:
        self.progress += 1
    
    def updateProgress(self, progress, final=False) -> None:
        if not self.stop:
            self.progress = progress
            self.stop = final
    
    def stopThread(self) -> None:
        self.stop = True
    
    def restart(self, total) -> None:
        self.progress = 0
        self.total = total
        self.start()
    
    def finalize(self) -> None:
        self.updateProgress(self.total, final=True)
        self.join()