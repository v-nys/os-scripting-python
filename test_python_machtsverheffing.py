import pytest

def test_read_stdout(capfd):
    import python_machtsverheffing
    captured = capfd.readouterr().out.split("\n")
    assert captured[0].strip() == str(7**6), "7 tot de 6e macht zou hetzelfde moeten oplevern als 7*7*7*7*7*7"
    assert captured[1].strip() == str(4**3+9**2), "4 tot de derde macht is 4*4*4, 9 tot de tweede macht is 9*9 en je moet de som van beide nemen"
    assert captured[2].strip() == str(7**4*12**3), "7 tot de vierde macht is 7*7*7*7, 12 tot de derde macht is 12*12*12 en je moet het product van beide nemen"
