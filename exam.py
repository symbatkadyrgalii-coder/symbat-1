class Fighter:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.alive = True

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 1:
            damage = 1
        print(f"{self.name} attacks {enemy.name}")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
            print(f"{self.name} has died")
        else:
            print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.alive

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Alive: {self.alive}")
        print()
import random

class BattleArena:
    def __init__(self):
        self.fighters = []

    def add_fighter(self, fighter):
        self.fighters.append(fighter)

    def get_alive_fighters(self):
        return [fighter for fighter in self.fighters if fighter.is_alive()]

    def start_battle(self):
        print("Battle started!\n")

        while len(self.get_alive_fighters()) > 1:
            alive_fighters = self.get_alive_fighters()
            fighter1, fighter2 = random.sample(alive_fighters, 2)

            fighter1.attack_enemy(fighter2)

            if fighter2.is_alive():
                fighter2.attack_enemy(fighter1)

            print("\nCurrent fighters stats:")
            for fighter in self.fighters:
                fighter.show_stats()
            print("-" * 30)

    def show_winner(self):
        winner = self.get_alive_fighters()[0]
        print(f"Winner: {winner.name}")
# Create fighters
knight = Fighter("Knight", 50, 15, 5)
orc = Fighter("Orc", 60, 18, 6)
mage = Fighter("Mage", 40, 20, 3)

# Create battle arena
arena = BattleArena()

# Add fighters to arena
arena.add_fighter(knight)
arena.add_fighter(orc)
arena.add_fighter(mage)

# Start battle
arena.start_battle()

# Show winner
arena.show_winner()