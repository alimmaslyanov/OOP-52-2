

class car:
    # Конструктор класса
    def __init__(self, model, year, color):
        # Атрибуты класса
        self.model = model
        self.year = year
        self.color = color

    # Метод класса
    def action(self):
        return print(f"{self.model} start action")

# Объект класса
bmw = car("BMW", 2020, "red")
bmw.action()