from random import choice, random

class Character:
    def __init__(self, name, battery, willpower, shame, money):
        self.name = name
        self.battery = battery
        self.willpower = willpower
        self.shame = shame
        self.money = money

    def take_damage(self, amount):
        if random() < 0.10:
            print(f"{self.name} dodge the attack!")
        else:
            self.battery -= amount
            print(f"{self.name} lost {amount} of Social Battery's!")

        if self.battery <= 0:
            print(f"{self.name} has turned into a slime!")
            exit()
    
    def gain_shame(self, amount):
        self.shame += amount
        print(f"{self.name} gained {amount} of Shame!")
        if self.shame >= 100:
            print(f"{self.name} implode from the shame!")
            exit()

    def lower_shame(self, method, amount):
        if method == "hide":
            if self.willpower >= 20:
                print(f"{self.name} hide in a trashcan!")
                self.shame = max(0, self.shame - amount)
                self.willpower -= amount
                print(f"{self.name} lost {amount} of Shame in exchange for {amount} of Willpower's")
            else:
                print(f"{self.name} doesn't have the willpower!")
        elif method == "bribe":
            if self.money >= amount:
                print(f"{self.name} bribed a 'friend' to distract the stranger!")
                self.shame = max(0, self.shame - amount)
                self.money -= amount
                print(f"{self.name} lost {amount} Shame in exchange for ${amount}.")
            else:
                print(f"You're too broke to bribe anyone!")

    def be_normal(self, amount):
        self.willpower += amount
        self.shame -= amount
        print(f"{self.name} gained {amount} of Willpower but gained {amount} of Shame in the process!")
        if self.willpower >= 100:
            print(f"{self.name} has turned into a Giga Chad and left!")
            exit()

    def __str__(self):
        return f"--- {self.name} | Battery: {self.battery} | Willpower: {self.willpower} | Shame: {self.shame} | Money: {self.money} ---"

    def support(self, target):
        if self.willpower >= 20:
            print(f"{self.name} plays a cool bass riff to distract the stranger!")
            target.battery += 10
            self.willpower -= 20
        else:
            print(f"{self.name} is staring blankly at a leaf.")        

bocchi = Character(name="Bocchi", battery=40, willpower=20, shame=30, money=100)
ryo = Character(name="Ryo", battery=100, willpower=60, shame=0, money=0)

print("--- A STRANGER APPROACHES BOCCHI! ---")

while True:
    print("\n" + str(bocchi))
    print(str(ryo))
    print("-" * 30)
    print("1. Be Normal (Bocchi)")
    print("2. Hide in Trash (Bocchi)")
    print("3. Bribe friends (Bocchi)")
    print("4. Ryo's Bass Support (Heal Bocchi's Battery)")
    player_choice = input("What will you do? (1-4): ")

    if player_choice == "1":
        bocchi.be_normal(10)
    elif player_choice == "2":
        bocchi.lower_shame("hide", 20)
    elif player_choice == "3":
        bocchi.lower_shame("bribe", 50)
    elif player_choice == "4":
        ryo.support(bocchi)
    else:
        print(f"{bocchi.name} panicked and did nothing!")

    move = choice(["Small Talk", "Intense Staring", "Close Talker", "Unexpected Wink"])
    print(f"\nStranger uses: {move}!")

    if move == "Small Talk":
        bocchi.take_damage(10)
    elif move == "Intense Staring":
        bocchi.gain_shame(15)
    elif move == "Close Talker":
        bocchi.take_damage(20)
        bocchi.gain_shame(10)
    elif move == "Unexpected Wink":
        bocchi.gain_shame(30)
