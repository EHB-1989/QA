import re

def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+$',email))
