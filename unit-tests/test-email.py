import unittest
import EmailValidation as ev

class TestEmail(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(ev.is_valid_email('lucas@gmail.com'))
        self.assertFalse(ev.is_valid_email('@gmail.com'))
        self.assertFalse(ev.is_valid_email('lucas@.com'))
        self.assertFalse(ev.is_valid_email('lucas@gmail.'))

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()