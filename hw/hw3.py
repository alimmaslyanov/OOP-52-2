from main import Hero

class Jester(Hero):
    def unique_attack(self):
        print(f"{self.name} кидает бомбу смеха, оглушая врагов!")

    def unique_scream(self):
        print(f"{self.name} кричит: 'Ха-ха! Кто не смеется, тот ЛоХ!'")

    def action(self):
        rand_value = self.get_random_int()
        if rand_value == 1:
            self.attack()
        elif rand_value == 2:
            self.protection()
        elif rand_value == 3:
            self.rest()
