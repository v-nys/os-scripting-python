import pytest
import importlib
import sys
from unittest.mock import MagicMock

def _two_opened_file_mocks(model,student):
    base_mock = MagicMock(name='mock for open')
    mock_context_manager_1 = MagicMock(name='mock for context manager 1')
    mock_context_manager_1.__enter__.return_value.read.return_value = model
    mock_context_manager_2 = MagicMock(name='mock for context manager 2')
    mock_context_manager_2.__enter__.return_value.read.return_value = student
    base_mock.side_effect=[mock_context_manager_1, mock_context_manager_2]
    return base_mock

def _two_inputs_mock(model,student):
    base_mock = MagicMock(name='mock for input')
    base_mock.side_effect=[model,student]
    return base_mock

def _model_solution():
    path = input("Welke file moet gecontroleerd worden?\n")
    with open(path) as fh:
        is_spam = False
        for line in fh.readlines():
            words = line.split()
            for word in words:
                if word in ["viagra", "lottery", "inheritance"]:
                    is_spam = True
        if is_spam:
            print("Deze file bevat spam!")
        else:
            print("Deze file is in orde!")

@pytest.mark.parametrize("lines",["you have won the lottery",\
                                  "you are lucky\nyou have won the lottery",\
                                  "192.168.0.1\n13.13.13.13"])
def test_run_as_script(capfd,monkeypatch,lines):
    opens_mock = _two_opened_file_mocks(lines,lines)
    # eigenlijk negeren we pad gewoon
    inputs_mock = _two_inputs_mock("fakefile1.txt","fakefile2.txt")
    with monkeypatch.context() as m:
        m.setattr("builtins.open", opens_mock)
        m.setattr("builtins.input", inputs_mock)
        _model_solution()
        captured_model = capfd.readouterr()
        if("python_spam_file" in sys.modules):
            importlib.reload(sys.modules["python_spam_file"])
        else:
            import python_spam_file
        captured = capfd.readouterr()
    assert captured_model.out == captured.out
