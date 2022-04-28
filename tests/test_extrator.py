
from py import process
from ExtratorSlides.SlideExtractor import *
# Isso ainda não funciona até que o seu pacote seja lido como instalável. 

import pytest
from tkinter import filedialog as fd

def return_non_video_file(title = None):
    return 'texto.txt'


def return_proper_video_file(title = None):
    return 'aula.mp4'


class TestInput:
    
    def test_negative_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "-1")
        with pytest.raises(ValueError, match=  "Valor inválido. Segundos são um número inteiro maior que 0.") as err:
            receive_input()
    
    def test_not_integer_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Mark")
        with pytest.raises(ValueError, match=  "Valor inválido. Segundos são um número inteiro maior que 0.") as err:
            receive_input()

    def test_normal_input(self, proper_input):
        assert receive_input() == 10 

class TestOpenVideoFile:
    
    def test_if_not_video(self, monkeypatch):
        monkeypatch.setattr(fd, 'askopenfilename',  return_non_video_file)
        with pytest.raises(ValueError, match = "O programa apenas suporta arquivos de vídeo. Escolha um arquivo de vídeo.") as err:
            choose_video()
    
    def test_valid_video(self, file_dialog_mock):
        assert choose_video() == return_proper_video_file()

class TestProcessVideo: 
    @pytest.mark.skip(reason="This feature shouldn't be tested yet.")
    def test_video_opens(self, file_dialog_mock, proper_input): 

        assert process_video() == True 
    
    def test_can_calculate_video_size(self, file_dialog_mock):
        cap = cv2.VideoCapture(choose_video())
        r = calculate_length_video(cap)
        assert r == 1198
    
    def test_no_possible_iterations(self, monkeypatch, file_dialog_mock):
        monkeypatch.setattr('builtins.input', lambda _: "2000")
        seconds = receive_input()
        cap = cv2.VideoCapture(choose_video())
        video_length = calculate_length_video(cap)
        with pytest.raises(ValueError, match = f"Você escolheu {seconds} para um slide ser relevante, mas o vídeo dura menos {video_length} segundos") as err:
            calculate_iterations(video_length, seconds)

    def test_can_properly_calculate_iterations(self, file_dialog_mock, proper_input):
        seconds = receive_input()
        cap = cv2.VideoCapture(choose_video())
        video_length = calculate_length_video(cap)
        assert calculate_iterations(video_length, seconds) == 120

    def test_can_distinguish_images(self, file_dialog_mock, proper_input):
        cap = cv2.VideoCapture(choose_video())
        _, imageA = cap.read() # First frame of video 
        video_length = calculate_length_video(cap)
        # 0 is the enum for position in MSEC
        cap.set(0, video_length * 1000)  # To get last frame, video_length in seconds converted to MS.
        _, imageB = cap.read()
        assert image_comparison(imageA, imageB) == True 
