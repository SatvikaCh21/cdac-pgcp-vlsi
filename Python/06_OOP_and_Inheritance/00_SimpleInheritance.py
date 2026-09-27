class Test(object):
    #__init__ is known as constructor
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class city(object):
    def __init__(self,location):
        self.location=location
    def display(self):
        print(self.location)

class course(city,Test):
    def __init__(self,name,idnumber,coursename,location):
        self.coursename=coursename
        Test.__init__(self,name,idnumber)
        city.__init__(self,location)
    def details(self):
        print("My name is {}".format(self.name))
        print("My idnumber is {}".format(self.idnumber))
        print("My course name is {}".format(self.coursename))
        print("My location is {}".format(self.location))

#creation of an object variable or an instance
a= course('Satvika','073','Python','Pune')

a.display()
a.details()
print(course.mro())
