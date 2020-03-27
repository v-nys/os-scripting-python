import pytest
from unittest.mock import MagicMock
import python_lijst_absolute_paden

def test_get_files_in_directory(capfd,monkeypatch):
    listdir_mock = MagicMock(name="mock for listdir") # file_is_spam vraagt om pad
    listdir_mock.return_value = ["karweitjes.txt","verlanglijstje.txt","boodschappenlijstje.txt"]
    with monkeypatch.context() as m:
        m.setattr("os.listdir", listdir_mock)
        answer = python_lijst_absolute_paden.get_files_in_directory("/home/test")
        assert "/home/test/karweitjes.txt" in answer, "/home/test bevat karweitjes.txt maar /home/test/karweitjes.txt kwam niet voor in resultaat"
        assert "/home/test/verlanglijstje.txt" in answer, "/home/test bevat verlanglijstje.txt maar /home/test/verlanglijstje.txt kwam niet voor in resultaat"
        assert "/home/test/boodschappenlijstje.txt" in answer, "/home/test bevat boodschappenlijstje.txt maar /home/test/boodschappenlijstje.txt kwam niet voor in resultaat"
