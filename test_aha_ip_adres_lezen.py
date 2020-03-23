import pytest
import aha_ip_adres_lezen

def _model_solution(text):
    return [int(text_elem) for text_elem in text.split(".")]

@pytest.mark.parametrize("input1",["192.168.0.1","0.0.0.0","255.255.255.255","10.0.0.0","1.99.100.255"])
def test_read_ip(input1):
    assert aha_ip_adres_lezen.read_ip(input1) == _model_solution(input1),f"verschil met modeloplossing voor invoer {input1}"
