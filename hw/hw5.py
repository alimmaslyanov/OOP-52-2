class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник (ширина: {self.width}, высота: {self.height})"

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        return NotImplemented

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 6)

print(r1)
print(r2)

print(r1.area())
print(r2.area())

print(r1 == r2)
print(r1 > r2)
print(r1 < r2)
