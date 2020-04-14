import pytest
import rem_ip_adres_controleren

def _model(s):
    return all([int(b) >= 0 and int(b) <= 255 for b in s.split(".")])

@pytest.mark.parametrize("ip",["192.168.0.1","1080.168.0.1","9.9.9.9.9.9.9.9.9","100.100.100.1000000"])
def test_ip_adres_controleren(capfd,monkeypatch,ip):
    assert rem_ip_adres_controleren.bestaat_uit_bytes(ip) == _model(ip), f"Je oplossing verschilt van de modeloplossing voor getallenreeks {ip}"
