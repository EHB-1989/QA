import unittest 
import calc

a = 2
b = 5

def test_is_valid_email():
    assert calc.somme(a,b) == 7

if __name__ == '__main__':
    test_is_valid_email()