with open('data.txt','w') as file:
    file.write("Python Programming is fun! \n")
    file.write("Hello world \n")
with open ('data.txt','r') as file:
    content=file.read()
    print(content)
with open('data.txt','r') as file:
    count=0
    for line in file:
        count+=1
    print("Number of lines in file is:",count)