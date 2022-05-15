import pytest
from tkinter import filedialog as fd
import os 
import shutil

def return_proper_video_file(title = None):
    return 'aula.mp4'


def teardown_folder():
    directory = "Slides de aula"
    shutil.rmtree(directory, ignore_errors= True)


@pytest.fixture
def file_dialog_mock(monkeypatch):
    monkeypatch.setattr(fd, 'askopenfilename',  return_proper_video_file)

@pytest.fixture
def proper_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10")

@pytest.fixture
def folder_cleanup(request):
    request.addfinalizer(teardown_folder) # Executes something AFTER the test, removing the directory

