from random import random
import sys

class Character:
    def __init__(self, name, hp, stamina, cool, debt, money):
        self.name = name
        self.hp = hp
        self.stamina = stamina
        self.cool = cool
        self.debt = debt
        self.money = money


    def eat_weeds(self, amount):
        chance = random.random()
        MAX_HP = 100
        
        if chance < 0.1:
            self.hp -= amount
            print(f"💀 '{self.name}... that was a hemlock.' {self.name} is seeing the light. Lost {amount} HP.")
            if self.hp <= 0:
                sys.exit()
            
        elif chance < 0.2:
            self.hp = min(MAX_HP, self.hp + (amount * 2))
            print(f"✨ '{self.name} found a truffle! Just kidding, it's just a really good root.' +{amount} HP.")
            
        else:
            self.hp = min(MAX_HP, self.hp + amount)
            print(f"🌿 {self.name} is munching on the lawn again. 'It's an organic, grass-fed lifestyle.' +{amount} HP.")