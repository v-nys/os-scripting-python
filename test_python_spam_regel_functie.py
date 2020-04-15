import pytest
import importlib
import sys
import io
import random
import string
import python_spam_regel_functie

def _random_text_with_word(word):
    rndm = "".join([random.choice(string.ascii_letters) for _ in range(random.randint(1,10))])
    return f"{rndm} {word} {rndm}"

@pytest.mark.parametrize("line,outcome",[("buy cheap viagra online",True),\
                                         ("you have won the lottery",True),\
                                         ("your great-uncle has left you an inheritance",True),\
                                         ("belangrijke mededeling",False),\
                                         ("blabla",False),\
                                         (_random_text_with_word("viagra"),True),\
                                         (_random_text_with_word("lottery"),True),\
                                         (_random_text_with_word("inheritance"),True),\
                                         ("testtest",False)])
def test_run_as_script(line,outcome):
    result = python_spam_regel_functie.line_is_spam(line)
    assert result == outcome, f"""de tekst "{line}" is{" geen" if (not outcome) else ""} spam, maar is in jouw functie anders geklasseerd"""
