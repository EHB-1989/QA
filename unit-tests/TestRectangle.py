import unittest

class TestRectangle(unittest.TestCase)
    def setUp(self):
        self.rectangle = Rectangle(5, 5)

    def test_area(self):
        self.assertEqual(self.rectangle.get_area(), 25)
        self.rectangle1 = Rectangle(4,6)
        self.assertNotEqual(self.rectangle1.get_area(), 25)