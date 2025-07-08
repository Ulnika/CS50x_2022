from fuel import *
import pytest

def test_convert():
    assert convert('3 / 4') == 75

def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1 / 0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('3 / 2')
