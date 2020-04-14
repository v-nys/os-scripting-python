import pytest
import functools
from unittest.mock import MagicMock, mock_open
import rem_ip_adressen_verwerken_en_verzamelen

def _passthrough_input(generator,prompt):
    print(prompt,end='') # input does not print a newline
    return generator.__next__()

@pytest.mark.parametrize("user_inputs",[["      192.168.0.1 ","  10.10.10.10  ","     "],[""],["1.2.3.4      ","5.6.7.8",    "255.255.255.255","  "]])
def test_verzamel_ip_adressen(capfd,monkeypatch,user_inputs):
    # assume there is always an acceptable answer at the end
    question = "Wat is het volgende IP-adres? Duw meteen op enter om af te sluiten."
    input_mock = MagicMock(name="mock for input")
    # need trickier patch here
    # cannot just make input function return something; has to print the prompt!
    # also: side_effect can be an iterable or a callable, but not a list of callables and prompt can be different on each call
    generator = (u_i for u_i in user_inputs)
    input_mock.side_effect = functools.partial(_passthrough_input,generator)
    with monkeypatch.context() as m:
        m.setattr("builtins.input", input_mock)
        result = rem_ip_adressen_verwerken_en_verzamelen.verzamel_ip_adressen()
        assert result == [ui.strip() for ui in user_inputs[:-1]], f"Je functie levert niet het gewenste resultaat voor volgende reeks IP-adressen: {','.join(user_inputs[:-1])}"
