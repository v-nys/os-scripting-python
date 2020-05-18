import pytest
import subnetcalculator

def _is_valid_ip_address(numberlist):
    if len(numberlist) != 4:
        return False
    else:
        for number in numberlist:
            if number < 0 or number > 255:
                return False
    return True

def _is_valid_netmask(numberlist):
    if len(numberlist) != 4:
        return False
    binary_netmask = "".join([f"{number:08b}" for number in numberlist])
    checking_ones = True
    for symbol in binary_netmask:
        if checking_ones and symbol == "0":
            checking_ones = False
        elif not checking_ones and symbol == "1"
            return False
    return True

def _one_bits_in_netmask(numberlist):
    binary_netmask = "".join([f"{number:08b}" for number in numberlist])
    counter = 0
    for symbol in binary_netmask:
        if symbol == "1":
            counter += 1
    return counter

def _apply_network_mask(host_address,netmask):
    network_address = []
    for idx in range(4):
        broadcast_address.append(host_address & netmask)
    return network_address

def _netmask_to_wildcard_mask(numberlist):
    binary_netmask = "".join([f"{number:08b}" for number in numberlist])
    mirror = "".join(["1" for elem in binary_netmask if elem == "0" else "1"])

def _get_broadcast_address(network_address,wildcard_mask):
    broadcast_address = []
    for idx in range(4):
        broadcast_address.append(network_address | wildcard_mask)
    return broadcast_address

def _prefix_length_to_max_host(netmask_length):
    return 2 ** netmask_length - 2

@pytest.mark.parametrize("numberlist",[[192,168,0,191],[1,1,1,1],[192,168,0,191,1],[255,255,255,255],[0,0,0,0],[0,0,-1,0],[254,254,254,254]])
def test_is_valid_ip_address(numberlist):
    student = subnetcalculator.is_valid_ip_address(numberlist)
    model = _is_valid_ip_address(numberlist)
    assert student == model,f"verschil met modeloplossing is_valid_ip_address voor invoer {input1}: jouw oplossing levert {student}, de modeloplossing levert {model}"

@pytest.mark.parametrize("numberlist",[[192,168,0,191],[1,1,1,1],[192,168,0,191,1],[255,255,255,255],[0,0,0,0],[254,254,254,254],[255,0,0,0],[192,0,0,0],[192,168,0,0],[255,192,0,0]])
def test_is_valid_netmask(numberlist):
    student = subnetcalculator.is_valid_netmask(numberlist)
    model = _is_valid_netmask(numberlist)
    assert student == model,f"verschil met modeloplossing is_valid_netmask voor invoer {input1}: jouw oplossing levert {student}, de modeloplossing levert {model}"

@pytest.mark.parametrize("numberlist",[[255,255,255,255],[0,0,0,0],[255,0,0,0],[192,0,0,0],[255,192,0,0]])
def test_one_bits_in_netmask(numberlist):
    student = subnetcalculator.one_bits_in_netmask(numberlist)
    model = _one_bits_in_netmask(numberlist)
    assert student == model,f"verschil met modeloplossing one_bits_in_netmask voor invoer {input1}: jouw oplossing levert {student}, de modeloplossing levert {model}"

@pytest.mark.parametrize("host_address,netmask",[([192,168,0,191],[255,255,255,255]),\
                                                 ([192,168,0,191],[0,0,0,0]),\
                                                 ([192,168,0,191],[255,0,0,0]),\
                                                 ([192,168,0,191],[192,0,0,0]),\
                                                 ([192,168,0,191],[255,192,0,0])])
def test_apply_network_mask(host_address,netmask):
    student = subnetcalculator.apply_network_mask(host_address,netmask)
    model = _apply_network_mask(host_address,netmask)
    assert student == model,f"verschil met modeloplossing apply_network_mask voor hostadres {host_address} en netmasker {netmask}: jouw oplossing levert {student}, de modeloplossing levert {model}"

@pytest.mark.parametrize("numberlist",[[255,255,255,255],[0,0,0,0],[255,0,0,0],[192,0,0,0],[255,192,0,0]])
def test_netmask_to_wildcard_mask(numberlist):
    student = subnetcalculator.netmask_to_wildcard_mask(numberlist)
    model = _netmask_to_wildcard_mask(numberlist)
    assert student == model,f"verschil met modeloplossing netmask_to_wildcard_mask voor invoer {input1}: jouw oplossing levert {student}, de modeloplossing levert {model}"

@pytest.mark.parametrize("host_address,wildcard_mask",[([192,168,0,191],[255,255,255,255]),\
                                                       ([192,168,0,191],[0,0,0,0]),\
                                                       ([192,168,0,191],[0,255,255,255]),\
                                                       ([192,168,0,191],[63,255,255,255]),\
                                                       ([192,168,0,191],[0,63,255,255])])
def test_apply_network_mask(host_address,wildcard_mask):
    student = subnetcalculator.get_broadcast_address(host_address,wildcard_mask)
    model = _get_broadcast_address(host_address,wildcard_mask)
    assert student == model,f"verschil met modeloplossing get_broadcast_address voor hostadres {host_address} en wildcard mask {wildcard_mask}: jouw oplossing levert {student}, de modeloplossing levert {model}"


def test_prefix_length_to_max_hosts(prefix_length):
    student = subnetcalculator.prefix_length_to_max_hosts(prefix_length)
    model = _prefix_length_to_max_host(prefix_length)
    assert student == model,f"verschil met modeloplossing prefix_length_to_max_hosts voor lengte {prefix_length}: jouw oplossing levert {student}, de modeloplossing levert {model}"
