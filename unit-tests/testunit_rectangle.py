from rectangle import Rectangle

def test_area_positive_dimensions():
    rect = Rectangle(5, 10)
    assert rect.area() == 50

def test_area_zero_width():
    rect = Rectangle(0, 10)
    assert rect.area() == 0

def test_area_zero_height():
    rect = Rectangle(10, 0)
    assert rect.area() == 0

def test_area_zero_dimensions():
    rect = Rectangle(0, 0)
    assert rect.area() == 0

def test_area_large_dimensions():
    rect = Rectangle(1000000, 2000000)
    assert rect.area() == 2000000000000

def test_area_negative_dimensions():
    rect = Rectangle(-5, 10)
    assert rect.area() == -50

def test_area_mixed_dimensions():
    rect = Rectangle(5, -10)
    assert rect.area() == -50

def test_area_float_dimensions():
    rect = Rectangle(4.5, 3.2)
    assert round(rect.area(), 2) == 14.4
