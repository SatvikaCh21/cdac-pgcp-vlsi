def  addfunction(v_fnum,v_snum):
    v_total = v_fnum+v_snum
    return v_total

v_sum=addfunction(3,4)
print("Total is",v_sum)

def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b

    return x,y,z,u

result=calc(10,5)
print(result)

def student(firstname, lastname):
    print(firstname,lastname)

#keyword arguments
student( 'Kocchar', 'King')
student(firstname= 'Kocchar', lastname= 'King')
student(lastname= 'King', firstname= 'Kocchar')


#with no defined number of parameters (use * pointer)
def myFunc(name,age,*argv):  #2 parameters will be used, others may or may not exist...so pointer *argv because we dont know how many arguments are required,so it dynamically allocates memory
    print(name,age,*argv)
    for arg in argv:
        print(arg)

myFunc("ABC",23, 1940,'Hello','welcome','to','learning','in sep')
myFunc('Jay',24)

def myFunc(**kwargs):
    for key,value in kwargs.items():  #here .items() in dictionary...so the output will be printed in that manner
        print("%s : %s " % (key,value))

myFunc(first='hello',mid= 'world',last='today')
myFunc(firstname='Jay',lastname='Kocchar')
myFunc()

def testfunc(s):
    #global s
    s='testing'
    s+=' evening'
    print(s)
    s="I like morning walk"
    print(s)

#Global Scope
s="Testing with Python"
testfunc(s)
print(s)