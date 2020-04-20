import pytest

def test_read_stdout(capfd,monkeypatch):
    import python_lijstindexering
    captured = capfd.readouterr().out.split("\n")
    assert captured[0].strip() == "hello world how are you?", "Je output matcht niet exact met de verwachte output. Dit kan aan een detail liggen. Staat er misschien een extra spatie of worden er aanhalingstekens geprint?"
