from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("hi!") == 20
    assert value("What's up?") == 100