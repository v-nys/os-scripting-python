import pytest
from unittest.mock import MagicMock, mock_open
import python_files_doorlopen
import os

def test_run_as_script(capfd,monkeypatch):
    listdir_mock = MagicMock(name="mock for listdir") # file_is_spam vraagt om pad
    listdir_mock.return_value = ["karweitjes.txt","verlanglijstje.txt","boodschappenlijstje.txt"]
    input_mock = MagicMock(name="mock for input")
    input_mock.return_value = "/home/test"
    with monkeypatch.context() as m:
        m.setattr("os.listdir", listdir_mock)
        m.setattr("builtins.input", input_mock)
        python_files_doorlopen.show_files_in_directory()
        captured = capfd.readouterr()
        assert "/home/test/karweittjes.txt\n" in captured.out
        assert "/home/test/verlanglijstje.txt\n" in captured.out
        assert "/home/test/boodschappenlijstje.txt" in captured.out
