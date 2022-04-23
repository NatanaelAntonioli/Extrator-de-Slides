
from skimage.metrics import structural_similarity as compare_ssim
import traceback
import cv2
import datetime
import time
from PIL import Image
from os.path import exists

def image_comparison(imageA, imageB, threshold = 0.05) -> bool:
    # Greyscale the images:
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY) 
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    score = compare_ssim(grayA, grayB) 
    return abs(score) < threshold


def pdf_generation(iteracoes, prints_directory):
    # Por fim, produzir o PDF.
    lista_imagens = []

    # Isso aqui faz com que a pesquisa ocorra em ordem numérica e não alfabética.
    # Se não, o programa faz algo como 1, 10, 11,...19, 100, 101, ... 199, 2, 20,21,...29,200,201,...299
    for i in range(iteracoes + 5):
        try:
            im = Image.open(f"{prints_directory}/" + str(i) + ".png")
            lista_imagens.append(im)
        except:
            pass

    pdf1_filename = f"{prints_directory}/{prints_directory}.pdf" 
    capa = lista_imagens[0]

    capa.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=lista_imagens)
    return 
