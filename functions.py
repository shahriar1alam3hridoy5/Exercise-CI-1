def add(a, b):
    return a + b

def subtract(a, b):
    return a - b   # bug fix

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    # absolute zero check
    assert fahrenheit >= -459.67
    return multiply(subtract(fahrenheit, 32), 5 / 9)