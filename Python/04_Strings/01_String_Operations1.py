#string
s="Python Programming"
print(s[0])
print(s[7])
print(s[2:8])
print(s[:5])
print(s[6:])
print(s[-1])

#update with same variable
original_string = "Hello"
print("Before original_string is:", original_string)
original_string = "Goodbye"
print("After original_string is:", original_string)

#escape character using
s1 = 'It\'s a beautiful day'
s2 = "He said \"hello\""
print(s1)
print(s2)

#string concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
#for numbers
age = 25
print("Age: " + str(age))

#string repetetion
s="Python Programming"
result = s * 3
print(result)

#in operator
if "Python" in s:
    print("Substring exists")
else :
    print("Substring does not exist")

#using not in operator
if "Python" not in s:
    print("Substring does not exist")
else:
    print("Substring exists")




