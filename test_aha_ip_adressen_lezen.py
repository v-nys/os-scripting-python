import pytest
from unittest.mock import patch, MagicMock
import aha_ip_adressen_lezen

def _two_opened_file_mocks(model,student):
    base_mock = MagicMock(name='mock for open')
    mock_context_manager_1 = MagicMock(name='mock for context manager 1')
    mock_context_manager_1.__enter__.return_value.read.return_value = model
    mock_context_manager_2 = MagicMock(name='mock for context manager 2')
    mock_context_manager_2.__enter__.return_value.read.return_value = student
    base_mock.side_effect=[mock_context_manager_1, mock_context_manager_2]
    return base_mock

def _model_solution():
    with open('ips.txt') as fh:
        return [[int(text_elem) for text_elem in line.split(".")] for line in fh.readlines()]

def test_read_ips():
    lines = """192.168.0.1
4.9.13.7
200.200.200.200
17.13.8.101
1.20.150.255"""
    base_mock = _two_opened_file_mocks(lines,lines)
    with patch('builtins.open',base_mock):
        assert aha_ip_adressen_lezen.read_ips() == _model_solution(), f"Je script levert een foutief resultaat voor minstens één adres in een file met volgende IP's:\n{lines}.\nProbeer zelf de regel vast te stellen waar het fout loopt door de inhoud van je file aan te passen en je script uit te voeren."
