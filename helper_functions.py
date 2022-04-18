
from skimage.metrics import structural_similarity as compare_ssim
import traceback
import cv2
import datetime
import time
from PIL import Image
from os.path import exists

def image_comparison(imageA: cv2.Mat, imageB: cv2.Mat, threshold = 0.05) -> bool:
    # Greyscale the images:
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY) 
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    score = compare_ssim(grayA, grayB) 
    return abs(score) < threshold
