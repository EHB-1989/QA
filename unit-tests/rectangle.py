# rectangle.py
import pytest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def test_rectangle_area():
    recZero=Rectangle(0,0)
    rec=Rectangle(3,4)
    recNeg=Rectangle(-3,4)
    
    assert recZero.area() == 0
    assert rec.area() == 12
    assert recNeg.area() == -12
    