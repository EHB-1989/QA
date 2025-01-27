# Code source (calc.py)
import unittest

def somme(a, b):
    return a + b

class AssertionSomme(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme(1, 2), 3)
        self.assertEqual(somme(1, 3), 4)
    
    def test_invalid(self):
        self.assertLess(somme(1, 2), 4)
        self.assertLess(somme(1, 3), 5)

if __name__ == '__main__':
    unittest.main()

