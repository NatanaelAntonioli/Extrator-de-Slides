# Rewriting code for simplicity's sake. 
import mimetypes
from tkinter import filedialog as fd
import cv2 

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


def choose_video() -> str:
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

def calculate_length_video(video: cv2.VideoCapture) -> int:
    """Calculates the approximate length, in minutes, of a given video file.

    Args:
        video (cv2.VideoCapture): Video file previously chosen by user.

    Returns:
        int: Duration of the video in minutes, with more or less a minute of leeway.
    """
    fps = video.get(cv2.CAP_PROP_FPS)      #
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    minutes = int(duration / 60) + 1 # Divide the duration in seconds to get minutes, add +1 for margin. 
    return minutes 

def process_video() -> bool:
    seconds = receive_input()
    video_file = choose_video()
    capture = cv2.VideoCapture(video_file)
    ret, frame = capture.read() 
    pass