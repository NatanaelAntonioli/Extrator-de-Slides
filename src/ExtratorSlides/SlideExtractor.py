# Rewriting code for simplicity's sake. 
import mimetypes
from tkinter import filedialog as fd

def receive_input():
    raw_seconds = input("Quanto deve durar um slide (em segundos) para que seja relevante? ")
    try:
        seconds = int(raw_seconds)
    except:
        raise ValueError("Valor inválido. Segundos são um número inteiro maior que 0.")
    if seconds <= 0:
        raise ValueError("Valor inválido. Segundos são um número inteiro maior que 0.")
    return seconds 


def open_video():
    filename = fd.askopenfilename('Escolha um arquivo de vídeo.')
    if not mimetypes.guess_type(filename)[0].startswith('video'): # Verifica se é um arquivo de vídeo válido
        raise ValueError("O programa apenas suporta arquivos de vídeo. Escolha um arquivo de vídeo.")
    return filename
