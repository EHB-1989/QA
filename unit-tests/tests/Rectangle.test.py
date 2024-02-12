import Rectangle 

def test_rectangle_area():
    rectangle_1 = Rectangle(4, 5)
    assert rectangle_1.area() == 20

    rectangle_2 = Rectangle(20, 3)
    assert rectangle_2.area() == 60

    return True
 