from main import get_a_string, get_a_int

def test_get_a_string():
    assert get_a_string() == "Hello World!"

def test_get_a_int():
    assert get_a_int() == 99