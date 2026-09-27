with open('data.txt', 'w') as file:
    file.write("Python Programming is fun!\n")
    file.write("Python file handling is easy!\n")
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)