import random
from abc import ABC, abstractmethod

from lesson_2 import kirito


class Hero(ABC):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.__random_int = random.randint(1, 3)

    def attack(self):
        print(f"{self.name} атакует и наносит {self.damage} урона!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает и восстанавливает силы!")

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
