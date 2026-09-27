#reverse the tuple
t1=(10,20,30,40,50)
reverse=t1[::-1]
print(reverse)

#access value 20 from tuple
print(t1[1])

#swap two tuples
t2=(5,6,7,8,9)
t1,t2=t2,t1
print(t1)
print(t2)

#copy specific elements from one tuple to new tuple
t3=(t1[1],t1[3])
print(t3)

#sort a tuple of tuples by second item
t4=((1,5),(2,3),(3,4),(4,1))
res=sorted(t4, key=lambda x:x[1])
print(res)

#count no.of item 50 from a tuple
t5=(10,20,30,40,20,20,20,10,30,50,60,20)
count=t5.count(20)
print(count)