import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if re.search("[a-z]", password):
        return False
    if re.search("[A-Z]", password):
        return False
    if re.search("[0-9]", password):
        return False
    if re.search("[!@#$%^&*]",password):
        return False
    return True

print(is_strong_password("Satvika@123!"))
print(is_strong_password("1234567"))
print(is_strong_password("abcdef"))
