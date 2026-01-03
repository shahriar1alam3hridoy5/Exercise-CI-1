import pytest
import functions   # সরাসরি module import

def test_add():
    assert functions.add(2, 3) == 5
    assert functions.add('space', 'ship') == 'spaceship'

def test_subtract():
    assert functions.subtract(2, 3) == -1

def test_multiply():
    assert functions.multiply(4, 5) == 20

def test_convert_fahrenheit_to_celsius():
    assert functions.convert_fahrenheit_to_celsius(32) == 0
    assert functions.convert_fahrenheit_to_celsius(122) == pytest.approx(50)
    with pytest.raises(AssertionError):
        functions.convert_fahrenheit_to_celsius(-600)