def standardize_phone(number):
    digits = number.replace(" ", "").replace("-", "").replace(".", "").replace("+", "")
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    if digits.startswith("0") and len(digits) == 11:
        digits = digits[1:]
    if len(digits) != 10 or not digits.isdigit():
        return "Invalid phone number! Must contain exactly 10 digits."
    formatted = "+91-" + digits[:5] + "-" + digits[5:]
    return formatted
number = input("Enter your phone number: ")
print(standardize_phone(number))