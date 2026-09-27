name="Alice"
age=30

#fstring formatting method to create string
print(f"{name} is {age} years old")

#String to all lower and upper case
text = " Python is FUN! "
print(text.lower())
print(text.upper())

#Remove whitespaces
print(text.strip())
#print(s.lstrip())
#print(s.rstrip())

#replace fun with amazing
print(text.replace("FUN","amazing"))

#check if it starts with "Py" and ends with "!"
print(text.strip().startswith("Py"))
print(text.strip().endswith("!"))

#count the occurence of letter o
print(text.count("o"))
