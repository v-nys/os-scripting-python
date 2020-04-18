import pytest

def test_read_stdout(capfd,monkeypatch):
    host_address_1 = [174,38,13,222]
    host_address_1_binary_number = int("".join([f"{host_byte:08b}" for host_byte in host_address_1]),2)
    netmask = int(19*"1",2) << 13
    host_address_1_network_address_string = f"{host_address_1_binary_number & netmask:b}"

    host_address_2 = [192,168,0,191]
    host_address_2_binary_string = "".join([f"{host_byte:08b}" for host_byte in host_address_2])
    import python_bitwise_ops
    captured = capfd.readouterr().out.split("\n")
    assert captured[0].strip() == host_address_1_network_address_string, "Het gevraagde netwerkadres klopt niet. Je moet een bitwise and van het netmasker en het hostadres doen. Doe dit stap voor stap op papier en kijk na wat jouw code anders doet."
    assert captured[1].strip() == host_address_2_binary_string, "Het gevraagde hostadres klopt niet. Je moet een bitwise or van het netwerkadres en het hostgedeelte doen. Doe dit stap voor stap op papier en kijk na wat jouw code anders doet."
