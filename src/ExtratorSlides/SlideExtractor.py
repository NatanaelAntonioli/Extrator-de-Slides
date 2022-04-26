# Rewriting code for simplicity's sake. 
import mimetypes
from tkinter import filedialog as fd

def receive_input() -> int:
    """Asks the user for the minimal time, in seconds, that makes a slide relevant. Only accepts positive numbers.

    Raises:
        ValueError: If the provided input is not convertible to int.
        ValueError: If the provided input is negative or equal to 0.
    Returns:
        int: The int value in seconds inputed by the user.
    """
    raw_seconds = input("Quanto deve durar um slide (em segundos) para que seja relevante? ")
    try:
        seconds = int(raw_seconds)
    except:
        raise ValueError("Valor inválido. Segundos são um número inteiro maior que 0.")
    if seconds <= 0:
        raise ValueError("Valor inválido. Segundos são um número inteiro maior que 0.")
    return seconds 


def open_video() -> str:
    """Prompts the user with a dialog to choose a file to be processed by the program. Expects a video.

    Raises:
        ValueError: If the file extension is not recognized as a valid video type.

    Returns:
        str: The full path to the file chosen by the user.
    """
    filename = fd.askopenfilename(title= 'Escolha um arquivo de vídeo.')
    if not mimetypes.guess_type(filename)[0].startswith('video'): # Verifica se é um arquivo de vídeo válido
        raise ValueError("O programa apenas suporta arquivos de vídeo. Escolha um arquivo de vídeo.")
    return filename

