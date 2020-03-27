import pytest
from unittest.mock import MagicMock, mock_open
import python_spam_filter

def _opened_file_mock(*args):
    base_mock = MagicMock(name='mock for open')
    mock_context_managers = []
    for (arg_number,arg) in enumerate(args):
        mock_context_manager = MagicMock(name=f"mock for opened file context manager {arg_number}")
        mock_context_manager.__enter__.return_value.read.return_value = arg
        mock_context_managers.append(mock_context_manager)
    base_mock.side_effect=mock_context_managers
    return base_mock

contents1 = "you have won the lottery"
contents2 = """congratulations on your inheritance
se pay the transfer fee"""
contents3 = """important message from school
lala"""
contents4 = "buy cheap viagra online"
contents5 = "this is not spam"
@pytest.mark.parametrize("contents,outcome",[(contents1,True),(contents2,True),(contents3,False),\
                                             (contents4,True),(contents5,False)])
def test_spam_filter(capfd,monkeypatch,contents,outcome):
    opens_mock = mock_open(read_data=contents)
    input_mock = MagicMock(name="mock for input")
    input_mock.return_value = "/home/test"
    listdir_mock = MagicMock(name="mock for listdir")
    listdir_mock.return_value = "file.txt"
    with monkeypatch.context() as m:
        m.setattr("builtins.open", opens_mock)
        m.setattr("builtins.input", input_mock)
        m.setattr("os.listdir", listdir_mock)
        python_spam_filter.spam_filter()
        captured = capfd.readouterr()
        if outcome:
            assert "spam" in captured.out and "geen" not in captured.out
        else:
            assert "geen spam" in captured.out
