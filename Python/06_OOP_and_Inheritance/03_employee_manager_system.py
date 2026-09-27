class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self.managed_employees = []
    def add_employee(self, employee):
        self.managed_employees.append(employee)
        print(f"{employee.name} added under manager {self.name}")
    def display_team(self):
        print(f"Manager: {self.name} (ID: {self.employee_id}) manages:")
        if not self.managed_employees:
            print("No employees assigned yet.")
        for emp in self.managed_employees:
            print(f"{emp.name} (ID: {emp.employee_id},Salary:{emp.salary})")

e1 = Employee("Anjali", "E101", 45000)
e2 = Employee("Vikram", "E102", 42000)
m1 = Manager("Suresh", "M201", 80000)
m1.add_employee(e1)
m1.add_employee(e2)
m1.display_team()