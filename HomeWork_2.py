class Heroes:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} стоит на месте и осматривается.")

    def attack(self):
        print(f"{self.name} атакует врага!")

class Archer(Heroes):
    def __init__(self, name: str, hp: int, arrows: int, precision: float):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 0.5:
                print(f"{self.name} успешно попал в цель! Стрел осталось: {self.arrows}")
            else:
                print(f"{self.name} промахнулся! Стрел осталось: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать! Закончились стрелы.")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдохнул и пополнил стрелы. Теперь у него {self.arrows} стрел.")

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"

archer = Archer("Леголас", 100, 3, 0.8)

archer.status()
archer.attack()
archer.attack()
archer.rest()
archer.attack()
print(archer.status())
