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
        MAX_HP = 100

        chance = random()
        
        if chance < 0.1:
            self.hp -= amount
            print(f"{self.name}... that was a hemlock. {self.name} is seeing the light. -{amount} HP.")
            if self.hp <= 0:
                sys.exit()
            
        elif chance < 0.2:
            self.hp = min(MAX_HP, self.hp + (amount * 2))
            print(f"{self.name} found a truffle! Just kidding, it's just a really good root. +{amount * 2} HP.")
            
        else:
            self.hp = min(MAX_HP, self.hp + amount)
            print(f"{self.name} is munching on the lawn again. It's an organic, grass-fed lifestyle. +{amount} HP.")
    
    def rest(self, amount):
        chance = random()
        if chance < 0.05:
            self.stamina = min(100, self.stamina + amount)
            self.cool = max(0, self.cool - amount)
            print(f"{self.name} fell asleep in a dumpster behind STARRY. It was cozy, but the fans saw. +{amount} STAMINA, -{amount} COOL.")
        elif chance < 0.1:
            self.stamina = min(100, self.stamina + (amount * 2))
            print(f"{self.name} reached a higher plane of musical consciousness in her sleep. +{amount} STAMINA.")
        else:
            self.stamina = min(100, self.stamina + amount)
            print(f"{self.name} is contemplating the silence. (She's just napping). +{amount} STAMINA.")

    def borrow_money(self):
        try:
            nominal = int(input("How much are you shaking Nijika down for: "))
        except ValueError:
            print("That's not even a number. Ryo is too hungry to understand.")
            return

        if nominal <= 0:
            print(f"{self.name}: If I'm not gaining money, I'm not interested.")
        elif nominal >= 5000:
            print(f"Nijika: NO WAY, RYO!")
        
        elif self.debt <= 1000:
            self.money += nominal
            self.debt += nominal
            print(f"{self.name}: Thanks, Nijika. I'll pay you back... eventually. Probably. Maybe. +{nominal} Yen")

        elif 1000 < self.debt <= 5000:
            self.money += nominal
            self.debt += nominal * 1.5  # Debt grows faster due to 'interest'
            self.cool = max(0, self.cool - 10) # Begging is uncool
            print(f"{self.name} used her puppy-dog eyes. It's super effective, but pathetic. +{nominal} Yen, -10 COOL.")

        else:
            print(f"{self.name}: Nijika won't even look me in the eye anymore. Time to go eat more weeds.")

    def find_job(self, amount):
        if self.stamina < 20:
            print(f"{self.name} is too hungry to even hold a bass. Go eat some weeds.")
            return

        job_chance = random()

        if self.cool > 50 and job_chance > 0.3:
            earnings = amount * 2
            self.money += earnings
            self.stamina -= 15
            print(f"{self.name} got a session gig! Her bass lines were impeccable. +{earnings} Yen, -15 STAMINA.")
        
        elif job_chance > 0.5:
            self.money += amount
            self.stamina -= 10
            self.cool -= 5
            print(f"{self.name} worked a shift at STARRY. Nijika made her wear an apron. +{amount} Yen, -10 STAMINA, -5 COOL.")
        
        else:
            self.stamina -= 5
            print(f"{self.name} spent all day looking for a 'Creative' job and found nothing. -5 STAMINA.")