import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_square():

    num = 7
    assert num*num == 49

def test_check():
    x = 100
    
    assert x >= 100

def test_fun():
    x = 7
    assert x + 1 == 8

def test_multiply():
    x = 6
    y = 5
    assert x*y == 30