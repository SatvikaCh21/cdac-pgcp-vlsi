class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print("Student Info")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Student ID : {self.student_id}")

    def is_eligible_to_vote(self):
        return self.age >= 18

s1 = Student("Satvika", 21, "014")
s1.display_info()
print(f"Eligible to vote: {s1.is_eligible_to_vote()}")

s2 = Student("Niharika", 14, "019")
s2.display_info()
print(f"Eligible to vote: {s2.is_eligible_to_vote()}")