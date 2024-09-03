from src.utils.helpers import greet

def test_greet():
    assert greet('Sum') == 'Hello, Sum!'

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0