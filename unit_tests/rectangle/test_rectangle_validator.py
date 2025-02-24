#test_rectangle_validator.py
from unit_tests.rectangle.rectangle import Rectangle

  


def test_rectangle_area_success():
    myrect = Rectangle(4, 5)
    assert myrect.area() == 20, "L'aire du rectangle 4x5 devrait être 20."

def test_rectangle_area_zero():
    myrect1 = Rectangle(0, 5)
    assert myrect1.area() == 0, "L'aire avec une largeur de 0 devrait être 0."

    myrect2 = Rectangle(5, 0)
    assert myrect2.area() == 0, "L'aire avec une hauteur de 0 devrait être 0."

def test_area_negative():
    myrect = Rectangle(-4, 5)
    assert myrect.area() < 0, "L'aire devrait être inférieur à 0."

def test_rectangle_failed():
    rect = Rectangle(3, 5)
    assert rect.area() == 20, "Test volontairement faux pour me permettre de vérifier la détection d'échec."


