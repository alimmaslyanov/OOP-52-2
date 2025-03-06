class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
         return print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.hp}")

    def is_adult(self):
        return print(f'{self.name} выполняет базовое действие')

class Warrior(Hero):

    def __init__(self, name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st

    def attack(self):
        if self.st >= 0:
            self.st -= 1
            return print(f'{self.name} атакует мечем')
        else:
            return print(f'{self.name} мало стамины')

class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

kirito = Warrior("Kirito", 10, 100, 10)
gandalf = MageHero("Gandalf", 10, 100, 10)

gandalf.introduce()
kirito.introduce()