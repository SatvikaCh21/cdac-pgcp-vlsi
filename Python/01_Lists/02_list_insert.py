"""list =[10,20,30,40,50] #given list
list.insert(3,60)
print(list)
"""
n = int(input("Enter number of elements in the list: "))

my_list = []
for i in range(n):
    val = input(f"Enter element {i+1}: ")
    my_list.append(val)

print("Original list:", my_list)

pos = int(input("Enter the position to insert at: "))
num = int(input("Enter the number to insert: "))
my_list.insert(pos,num)

print("Updated List:",my_list)