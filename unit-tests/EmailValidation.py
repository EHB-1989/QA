import re

def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+$',email))

def test_valid_email():
    assert is_valid_email('azerty') == False
    assert is_valid_email('azerty@') == False
    assert is_valid_email('azerty@azerty') == False
    assert is_valid_email('azerty@azerty.') == False
    assert is_valid_email('azerty@azerty.fr') == True
    assert is_valid_email('@azerty.fr') == False
    
if __name__ == "__main__":
    test_valid_email() 