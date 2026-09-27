def validate_email(email):
    if '@' not in email:
        return False
    local, domain = email.split('@')
    if local == '':
        return False
    if domain != 'gmail.com':
        return False
    return True

# Ask user to enter email
email = input("Enter your email: ")

# Check and printresult
if validate_email(email):
    print("Valid email!")
else:
    print("Invalid email.")