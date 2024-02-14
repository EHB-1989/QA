import unittest
import calc as c

class TestCalc(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(c.somme(5,3),8)

if __name__ == '__main__':
    unittest.main()