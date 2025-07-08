from numb3rs import *
import pytest

def test_validate_numbers():
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('1.196.3.127') == True
    assert validate('123.456.76.65') == False

def test_validate_nonnumbers():
    assert validate('cat') == False

def test_validate_dots():
    assert validate('255,255,255,255') == False
    assert validate('1') == False

