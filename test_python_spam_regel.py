import pytest
import importlib
import sys
import io
import random
import string

def _random_text_with_word(word):
    rndm = "".join([random.choice(string.ascii_letters) for _ in range(random.randint(1,10))])
    return f"{rndm} {word} {rndm}"

@pytest.mark.parametrize("line,outcome",[("buy cheap viagra online","is spam"),\
                                         ("you have won the lottery","is spam"),\
                                         ("your great-uncle has left you an inheritance","is spam"),\
                                         ("belangrijke mededeling","is geen spam"),\
                                         ("blabla","is geen spam"),\
                                         (_random_text_with_word("viagra"),"is spam"),\
                                         (_random_text_with_word("lottery"),"is spam"),\
                                         (_random_text_with_word("inheritance"),"is spam"),\
                                         ("testtest","is geen spam")])
def test_run_as_script(capfd,monkeypatch,line,outcome):
    monkeypatch.setattr("sys.stdin", io.StringIO(line))
    if("python_spam_regel" in sys.modules):
        importlib.reload(sys.modules["python_spam_regel"])
    else:
        import python_spam_regel
    captured = capfd.readouterr()
    assert outcome in captured.out, f"""de tekst "{line}" {outcome}, maar is in jouw script niet zo geklasseerd"""
