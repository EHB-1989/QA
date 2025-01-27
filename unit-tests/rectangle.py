import unittest


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = self.height

    def area(self):
        return self.width * self.height


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(3, 4)
        self.rect2 = Rectangle(5, 6)

    def test_area(self):
        self.assertEqual(self.rect1.area(), 12)
        self.assertEqual(self.rect2.area(), 30)

    def test_initialization(self):
        self.assertEqual(self.rect1.width, 3)
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect2.width, 5)
        self.assertEqual(self.rect2.height, 6)


if __name__ == "__main__":
    unittest.main()
