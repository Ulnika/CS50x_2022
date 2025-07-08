from plates import is_valid

def test_len():
    for i in ['a', 'CS501234']:
        assert is_valid(i) == False

def test_characters():
    for i in ['!', 'CS.50']:
        assert is_valid(i) == False

def test_alphabetical():
    for i in ['00FF', '0FFF']:
        assert is_valid(i) == False

def test_zero():
    for i in ['CS03', '00000']:
        assert is_valid(i) == False

def test_all_letters():
    assert is_valid('HELLO') == True

def test_numbers():
    assert is_valid('CS34P') == False
    assert is_valid('12345') == False