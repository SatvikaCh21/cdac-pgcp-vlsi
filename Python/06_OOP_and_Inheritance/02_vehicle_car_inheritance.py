class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

v = Vehicle("Honda", "Activa", 2020)
print("Vehicle object:")
v.display_info()
c = Car("Maruti", "Swift", 2023, 4)
print("Car object:")
c.display_info()


