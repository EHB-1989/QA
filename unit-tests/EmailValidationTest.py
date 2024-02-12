import unittest 
import EmailValidation

toto = "toto@gmail.com"
fofo = "fofo.gngn.com"
tolo = "tolo@gmail.fr"

def test_is_valid_email():
    assert EmailValidation.is_valid_email(toto) == True
    assert EmailValidation.is_valid_email(fofo) == False
    assert EmailValidation.is_valid_email(tolo) == True


if __name__ == '__main__':
    test_is_valid_email()