import unittest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

if __name__ == "__main__":
    unittest.main()