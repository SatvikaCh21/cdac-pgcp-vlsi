def is_valid_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10
print(is_valid_phone_number(input("Enter phone number: ")))
