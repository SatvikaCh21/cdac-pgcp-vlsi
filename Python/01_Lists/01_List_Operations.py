# Take 2 Lists
list1=[10,40,20,60,30]
list2=[700, 50,5,0]
list3=[]
list4=[]

#reverse a list
list1.reverse()
print(list1)
list2.reverse()
print(list2)

#concatenate 2 lists index wise
for i in range(min(len(list1),len(list2))):
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)

#turn every item of into its square
for i in range(len(list3)):
    list3[i]=list3[i]**2
print(list3)

# iterate both lists simultaneously
for i in range(min(len(list1), len(list2))):
    print(list1[i], list2[i])

#add new item
item = int(input("enter existing number"))
new_item = int(input("enter new item to add"))

if item in list1:
    index = list1.index(item)
    list1.insert(index+1,new_item)
print("updated list",list1)

#replace list item with new
old=int(input("enter old value"))
new=int(input("enter new value to replace"))
if old in list1:
    index = list1.index(old)
    list1[index]=new
    print("Replaced list",list1)

#remove all occurrences of a specific items from a list
rem=int(input("enter item to remove"))
if rem in list1:
    list1.remove(rem)
print("List after removing item :",list1)


