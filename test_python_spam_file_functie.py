import pytest
from unittest.mock import MagicMock, mock_open
import python_spam_file_functie

def _opened_file_mock(lines):
    base_mock = MagicMock(name='mock for open')
    mock_context_manager = MagicMock(name='mock for context manager')
    mock_context_manager.__enter__.return_value.read.return_value = lines
    base_mock.return_value = mock_context_manager
    return base_mock

@pytest.mark.parametrize("lines,outcome",[("you have won the lottery",True),\
                                          ("you are lucky\nyou have won the lottery",True),\
                                          ("""you are lucky
                                              you have received an inheritance
                                              please pay the transfer fee""",True),\
                                          ("192.168.0.1\n13.13.13.13",False)])
def test_run_as_script(monkeypatch,lines,outcome):
    opens_mock = mock_open(read_data=lines) # om te openen met file_is_spam_functie
    with monkeypatch.context() as m:
        m.setattr("builtins.open", opens_mock)
        answer = python_spam_file_functie.file_is_spam("fakepath")
    assert answer == outcome,\
           f"""De tekst "{lines}" leverde {answer}..."""
