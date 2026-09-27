list=[] #defined in global
tuple=() #defined in global

def addlist():
    l=int(input("enter the list members"))
    list.append(l)
    return list

def displaylist():
    print("List is", list)
def searchlist(list):
    i=int(input("enter number to be searched"))
    if i in list:
        print("it exists")
    else:
        print("it does not exist")

def searchtuple(tuple):
    i=int(input("enter number to be searched"))
    if i in tuple:
        print("it exists")
    else:
        print("it does not exist")
def tupledisplay():
    print("tuple is",tuple)
    return tuple
print("Menu Display ")
while  True:
    print("\nMAIN MENU")
    print("1. add list")
    print("2. add tuple")
    print("3. search list")
    print("4. search tuple")
    print("5. Exit")
    choice= int(input("enter the choice:"))

    if choice==1:
        #l=[]
        list=addlist()
        print("the list is",list)

    elif choice==2:
        #tuple=()
        d=int(input("enter the tuple members"))
        tuple=tuple+(d,)
        #print("tuple is",tuple)
        tupledisplay()

    elif choice==3:
        displaylist()
        searchlist(list)
        #print("the list is",list)

    elif choice==4:
        searchtuple(tuple)

    elif choice==5:
        break

    else:
        print("please enter a valid choice")



