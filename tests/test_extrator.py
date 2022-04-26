from ExtratorSlides.SlideExtractor import *
# Isso ainda não funciona até que o seu pacote seja lido como instalável. 

import pytest

class TestInput:
    
    def test_negative_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "-1")
        with pytest.raises(ValueError, match=  "Valor inválido. Segundos são um número inteiro maior que 0.") as err:
            receive_input()
    
    def test_not_integer_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Mark")
        with pytest.raises(ValueError, match=  "Valor inválido. Segundos são um número inteiro maior que 0.") as err:
            receive_input()

    def test_normal_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "20")
        assert receive_input() is 20 
        
    