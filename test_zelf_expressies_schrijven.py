import pytest

def test_correct_values():
    with open('python-zelf-expressies-schrijven.py') as fh:
        lines = fh.readlines()
        assert len(lines) >= 4, f"Je bestand bevat geen vier regels en voldoet dus niet aan de opgave."
        assert eval(lines[0]) == 4 * 2 + 9, f"De som van het product van 4 en 2 en 9 betekent dat je eerst het product van 4 en 2 moet nemen..."
        assert eval(lines[1]) == (4 + 2) * 9, f"Het product van de som van 4 en 2 en 9 betekent dat je eerst de som van 4 en 2 moet nemen..."
        assert eval(lines[2]) - 7 / (3 / 2) < 0.001, f"Heb je eerst 3 gedeeld door 2 en dan pas 7 gedeeld...?"
        assert eval(lines[3]) == "hello world", f'Je vierde expressie produceert geen "hello world" (staat alles in kleine letters, ben je geen quotes vergeten?)'
