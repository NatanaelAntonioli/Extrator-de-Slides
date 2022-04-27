
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
    def test_video_opens(self, file_dialog_mock, proper_input): 

        assert process_video() is True 
    
    def test_can_calculate_video_size(self, file_dialog_mock):
        cap = cv2.VideoCapture(choose_video())
        r = calculate_length_video(cap)
        assert r == 20 

