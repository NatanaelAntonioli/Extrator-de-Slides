from ExtratorSlides.SlideExtractor import (image_comparison, receive_input, choose_video, calculate_iterations, 
    calculate_length_video, create_folder, process_video, main)
import pytest
import cv2
from tkinter import filedialog as fd
import os
from pathlib import Path

def return_non_video_file(title = None):
    return 'texto.txt'


def return_proper_video_file(title = None):
    return 'aula.mp4'


class TestInput:

    def test_negative_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "-1")
        with pytest.raises(ValueError, match = "Valor inválido. Segundos são um número inteiro maior que 0."):
            receive_input()

    def test_not_integer_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Mark")
        with pytest.raises(ValueError, match = "Valor inválido. Segundos são um número inteiro maior que 0."):
            receive_input()

    def test_normal_input(self, proper_input):
        assert receive_input() == 10


class TestOpenVideoFile:

    def test_if_not_video(self, monkeypatch):
        monkeypatch.setattr(fd, 'askopenfilename',  return_non_video_file)
        with pytest.raises(ValueError, match = "O programa apenas suporta arquivos de vídeo. Escolha um arquivo de vídeo."):
            choose_video()

    def test_valid_video(self, file_dialog_mock):
        assert choose_video() == return_proper_video_file()


class TestVideoLengthFunction: 
    def test_can_calculate_video_size(self, file_dialog_mock):
        cap = cv2.VideoCapture(choose_video())
        r = calculate_length_video(cap)
        assert r == 1198

    def test_no_possible_iterations(self, monkeypatch, file_dialog_mock):
        monkeypatch.setattr('builtins.input', lambda _: "2000")
        seconds = receive_input()
        cap = cv2.VideoCapture(choose_video())
        video_length = calculate_length_video(cap)
        with pytest.raises(ValueError, match = f"Você escolheu {seconds} segundos para um slide ser relevante, mas o vídeo dura só {video_length} segundos"):
            calculate_iterations(video_length, seconds)

    def test_can_properly_calculate_iterations(self, file_dialog_mock, proper_input):
        seconds = receive_input()
        cap = cv2.VideoCapture(choose_video())
        video_length = calculate_length_video(cap)
        assert calculate_iterations(video_length, seconds) == 120


class TestImageComparison: 

    def test_can_distinguish_images(self, file_dialog_mock):
        cap = cv2.VideoCapture(choose_video())
        _, imageA = cap.read()  # First frame of video
        video_length = calculate_length_video(cap)
        # 0 is the enum for position in MSEC
        cap.set(0, video_length * 1000)  # To get last frame, video_length in seconds converted to MS.
        _, imageB = cap.read()
        assert image_comparison(imageA, imageB) == True

    def test_image_comparison_invalid_threshold(self, file_dialog_mock):
        cap = cv2.VideoCapture(choose_video())
        _, imageA = cap.read()
        with pytest.raises(ValueError, match = "A tolerância para similaridade tem que ser um número positivo entre 0 e 1."):
            image_comparison(imageA, imageA, threshold = 10)
        with pytest.raises(ValueError, match = "A tolerância para similaridade tem que ser um número positivo entre 0 e 1."):
            image_comparison(imageA, imageA, threshold = -1)

class TestFolderCreation:
    """This class of tests seeks to verify whether we can properly create the folder named after the file in the user's directory where the .py file is.
    """
    def test_create_new_folder(self, file_dialog_mock, folder_cleanup):
        video = choose_video()
        P = Path(video)
        prints_directory_name = f"Slides de {P.stem}"
        create_folder(video)
        assert os.path.exists(prints_directory_name) == True 
    
    def test_create_new_folder_with_absolute_path(self, file_dialog_mock, folder_cleanup):
        current_dir = os.getcwd()
        video = choose_video()
        P = Path(video)
        prints_directory_name = f"Slides de {P.stem}"
        absolute_path_video = f"{current_dir}/{video}"
        create_folder(absolute_path_video)
        assert os.path.exists(prints_directory_name) == True 


class TestVideoProcessing:
    def test_save_first_frame(self, file_dialog_mock, proper_input, folder_cleanup):
        video = choose_video()
        cap = cv2.VideoCapture(video)
        video_length = calculate_length_video(cap)
        seconds = receive_input()
        iterations = calculate_iterations(video_length=video_length, seconds= seconds)
        create_folder(video)
        P = Path(video)
        prints_directory_name = f"Slides de {P.stem}"
        process_video(cap, iterations, prints_directory_name, seconds)
        assert os.path.exists(f"{prints_directory_name}/current_image.png")

    def test_save_next_frame(self, file_dialog_mock, proper_input, folder_cleanup):
        video = choose_video()
        cap = cv2.VideoCapture(video)
        video_length = calculate_length_video(cap)
        seconds = receive_input()
        iterations = calculate_iterations(video_length=video_length, seconds= seconds)
        create_folder(video)
        P = Path(video)
        prints_directory_name = f"Slides de {P.stem}"
        process_video(cap, iterations, prints_directory_name, seconds)
        assert os.path.exists(f"{prints_directory_name}/next_image.png")

    def test_processed_video(self, file_dialog_mock, proper_input, folder_cleanup):
        video = choose_video()
        cap = cv2.VideoCapture(video)
        video_length = calculate_length_video(cap)
        seconds = receive_input()
        iterations = calculate_iterations(video_length=video_length, seconds= seconds)
        create_folder(video)
        P = Path(video)
        prints_directory_name = f"Slides de {P.stem}"
        process_video(cap, iterations, prints_directory_name, seconds)
        assert os.path.exists(f"{prints_directory_name}/119.png")

    def test_processed_video(self, file_dialog_mock, proper_input, folder_cleanup):
        video = choose_video()
        cap = cv2.VideoCapture(video)
        video_length = calculate_length_video(cap)
        seconds = receive_input()
        iterations = calculate_iterations(video_length=video_length, seconds= seconds)
        create_folder(video)
        P = Path(video)
        prints_directory_name = f"Slides de {P.stem}"
        process_video(cap, iterations, prints_directory_name, seconds)
        assert os.path.exists(f"{prints_directory_name}/slides.pdf")

class TestIntegration:
    
    def test_all(self, file_dialog_mock, proper_input, folder_cleanup):
        main()
        assert os.path.exists(f"Slides de aula/slides.pdf")