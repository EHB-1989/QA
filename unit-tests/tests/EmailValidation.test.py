import EmailValidation

def test_is_valid_email(email):
    assert isinstance(email, str)
    assert(EmailValidation.is_valid_email('toto@gmail.com') == True, 'Fail')
    assert(EmailValidation.is_valid_email('toto.gmail.com') == False, 'Fail')
    assert(EmailValidation.is_valid_email('toto@gmail-com') == False, 'Fail')

    return True
 