class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"{self.brand} движется вперёд."

class Electric:
    def charge(self):
        return f"{self.brand} заряжается от электросети."

class HybridCar(Vehicle, Electric):
    def move(self):
        return f"{self.brand} использует гибридный режим движения."

toyota = HybridCar("Toyota")
print(toyota.move())
print(toyota.charge())
