import pytest
import python_zelf_functies_schrijven

def _model_solution(number):
    return number >= 0 and number <= 255

@pytest.mark.parametrize("input1",[0,255,128,-1,256])
def test_is_byte(input1):
    assert python_printen.is_byte(input1) == _model_solution(input1),f"verschil met modeloplossing voor invoer {input1}"
