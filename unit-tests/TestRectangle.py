import unittest
from rectangle import Rectangle

class TestIsValidEmail(unittest.TestCase):
    def test_area(self):

        rectangle = Rectangle(4,5)

        assert Rectangle.area(rectangle) == 20

        
if __name__ == "__main__":
    unittest.main()