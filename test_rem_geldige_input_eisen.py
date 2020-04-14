import pytest
import functools
from unittest.mock import MagicMock, mock_open
import rem_geldige_input_eisen

def _passthrough_input(generator,prompt):
    print(prompt,end='') # input does not print a newline
    return generator.__next__()

@pytest.mark.parametrize("user_inputs",[["ja"],["neen"],["boe","ja"],["boe","neen"],["boe","boe","boe","ja"]])
def test_vraag_ja_of_neen(capfd,monkeypatch,user_inputs):
    # assume there is always an acceptable answer at the end
    question = "Gelieve ja of neen te antwoorden."
    thank_you = "Bedankt voor je input!"
    input_mock = MagicMock(name="mock for input")
    # need trickier patch here
    # cannot just make input function return something; has to print the prompt!
    # also: side_effect can be an iterable or a callable, but not a list of callables and prompt can be different on each call
    generator = (u_i for u_i in user_inputs)
    input_mock.side_effect = functools.partial(_passthrough_input,generator)
    expected = "\n".join([question] * len(user_inputs) + [thank_you])
    with monkeypatch.context() as m:
        m.setattr("builtins.input", input_mock)
        rem_geldige_input_eisen.vraag_ja_of_neen()
        captured = capfd.readouterr()
        # allow for some deviation (WS,...)
        assert expected in captured.out, f"Je oplossing doet niet het gevraagde bij inputreeks {user_inputs}. Let er ook op dat de schrijfwijze van de vraag en het bedankje *identiek* moeten zijn aan die in het voorbeeld, inclusief de newline na de vraag."
