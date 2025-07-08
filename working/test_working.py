from working import *
import pytest

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_value_error_to():
    with pytest.raises(ValueError):
        convert('9:00 AM 5:00 PM')

def test_value_error_hours():
    with pytest.raises(ValueError):
        convert('9:00 AM to 13:00 PM')

def test_value_error_min():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:00 PM')

def test_value_error_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')