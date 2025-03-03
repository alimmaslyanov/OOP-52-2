class Hero:
    def __init__(self, name: str, lvl: int, HP: int):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

heroes = [
    Hero("Алим", 10, 100),
    Hero("Бек", 5, 80),
    Hero("Жан", 15, 120)
]

for hero in heroes:
    hero.introduce()
    print(f"Является ли {hero.name} 10+ уровнем? {hero.is_adult()}\n")