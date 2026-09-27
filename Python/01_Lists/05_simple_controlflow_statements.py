v_fnum=int(input("enter the number:"))

if(v_fnum==10):
    print("v_fnum is",v_fnum)
elif(v_fnum>10 and v_fnum<20):
    print("v_fnum between 10 and 20")

list= [10,20,30,40]
for i in range(1,5):
    print(i)
for i in list:
    print(i)
for i in range(0,len(list)):
    print(i)
for i in range(50,71,2):
    print(i)
for i in range(1,5):
    print(i,end=" ") #end is going to be with space