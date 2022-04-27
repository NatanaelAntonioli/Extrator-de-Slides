import pytest
from tkinter import filedialog as fd

def return_proper_video_file(title = None):
    return 'aula.mp4'

@pytest.fixture
def file_dialog_mock(monkeypatch):
    monkeypatch.setattr(fd, 'askopenfilename',  return_proper_video_file)

@pytest.fixture
def proper_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10")
