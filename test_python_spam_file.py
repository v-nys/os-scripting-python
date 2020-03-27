import pytest
import importlib
import sys
from unittest.mock import MagicMock

def _opened_file_mock(lines):
    base_mock = MagicMock(name='mock for open')
    mock_context_manager = MagicMock(name='mock for context manager')
    mock_context_manager.__enter__.return_value.read.return_value = lines
    base_mock.return_value = mock_context_manager
    return base_mock

BEVAT_SPAM = "Deze file bevat spam!"
IN_ORDE = "Deze file is in orde!"

@pytest.mark.parametrize("lines,outcome",[("you have won the lottery",BEVAT_SPAM),\
                                          ("you are lucky\nyou have won the lottery",BEVAT_SPAM),\
                                          ("""you are lucky
                                              you have received an inheritance
                                              please pay the transfer fee""",BEVAT_SPAM),\
                                          ("192.168.0.1\n13.13.13.13",IN_ORDE)])
def test_run_as_script(capfd,monkeypatch,lines,outcome):
    opens_mock = _opened_file_mock(lines)
    inputs_mock = MagicMock(name="mock for input")
    with monkeypatch.context() as m:
        m.setattr("builtins.open", opens_mock)
        m.setattr("builtins.input", inputs_mock)
        if("python_spam_file" in sys.modules):
            importlib.reload(sys.modules["python_spam_file"])
        else:
            import python_spam_file
        captured = capfd.readouterr()
    assert outcome in captured.out
