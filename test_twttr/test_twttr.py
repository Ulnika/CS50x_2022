from twttr import shorten

def test_shorten():
    assert shorten("word") == "wrd"
    assert shorten("name") == "nm"
    assert shorten("end") == "nd"
    assert shorten("1 day") == "1 dy"
    assert shorten("Ann") == "nn"
    assert shorten("What's your name?") == "Wht's yr nm?"