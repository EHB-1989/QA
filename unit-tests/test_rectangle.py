from rectangle import Rectangle

def is_rectangle(rectangle):
    if rectangle.width <= 0 or rectangle.height <= 0:
        return False
    else:
        return True

rectangle1 = Rectangle(4, 5)
print(is_rectangle(rectangle1))

rectangle2 = Rectangle(0, 5)
print(is_rectangle(rectangle2))
