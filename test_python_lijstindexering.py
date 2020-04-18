import pytest

def test_read_stdout(capfd,monkeypatch):
    import python_lijstindexering
    captured = capfd.readouterr().out.split("\n")
    assert captured[0].strip() == "hello world how are you?"
