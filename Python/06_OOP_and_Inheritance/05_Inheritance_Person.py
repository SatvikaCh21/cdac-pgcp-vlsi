class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class City(Person):
    def __init__(self,city):
        self.city=city

class Employee(Person,City):
    def __init__(self,name,age,city,monthly_income):
        Person.__init__(self,name,age)
        City.__init__(self,city)
        self.monthly_income=monthly_income

        def annual_income(self):
            return self.monthly_income*12

employees = [
    Employee("Satvika",21,"Pune",50000)
    Employee("Niharika",22,"Pune",40000)
    Employee("Keshav",23,"Mumbai",30000)
    Employee("Saswat",22,"Noida",10000)
]

Pune_count = 0
Pune_total = 0
Mumbai_count = 0
Mumbai_total = 0

for employee in employees:
    print("Name:",employee.name)
    print("Age:",employee.age)
    print("City:",employee.city)
    print("Monthly income:",employee.monthly_income())
    print("Annual income:",employee.annual_income())

    print()

    if employee.age>18: 








