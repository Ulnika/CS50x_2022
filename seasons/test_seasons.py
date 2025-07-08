from seasons import *
import pytest

def test_get_date():
     assert get_date("2021-06-16") == date(2021, 6, 16)

def test_exit():
    with pytest.raises(SystemExit):
        get_date("January 1, 1999")

def test_transform_date():
     assert transform_date(date(2021, 6, 16)) == "Five hundred twenty-five thousand, six hundred minutes"