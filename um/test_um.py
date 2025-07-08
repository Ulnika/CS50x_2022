from um import *
import pytest

def test_count():
    assert count("Um") == 1
    assert count("um") == 1
    assert count("album") == 0
    assert count("Um, thanks, um...") == 2