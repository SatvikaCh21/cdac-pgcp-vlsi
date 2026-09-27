import os

file = open('myfile.txt','r') #file is opened in read mode using open function, if you didnt give the file name and path, python will default take the pycharm path itself
print(file.read())
print(file)
#file1.close()

file = open('myfile.txt','w')
file.write("Hi How are you doing?")
print(file)

"""file = open('myfile.txt','w+')
file.write("Hello learning python read")
#file.seek(0)
#print(file.read()
#print(file)"""

file = open('myfile.txt','a+')
print(file.read())
#file.seek(0)
file.write("Hello learning python read write")
print(file)

"""file = open('myfile.txt','r')
print(file.readline()) #readlines in the file as list"""

"""with open('myfile.txt','r') as file:
    data = file.readlines()
    print(data)
    for line in data:
        word=line.splitlines()
        print(word)
    data=file.write("Hello Python")"""
