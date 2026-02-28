import random

def trigger_random_event(player):
    events = [
        vintage_bass_temptation,
        kessoku_band_practice,
        the_bocchi_effect,
        fan_encounter,
        nijika_intervention
    ]
    
    # Pick a random function and run it
    event = random.choice(events)
    print("\n--- RANDOM EVENT ---")
    event(player)
    print("--------------------\n")

def vintage_bass_temptation(player):
    print(f"Ryo spots a vintage 1960s Fender Precision Bass in a shop window.")
    if player.money >= 5000:
        choice = input("It's 3000 Yen. Buy it for the 'aesthetic'? (y/n): ").lower()
        if choice == 'y':
            player.money -= 3000
            player.cool += 30
            print(f"Ryo is now broke, but she looks incredibly cool holding it. +30 COOL.")
        else:
            print("Ryo walks away. Her soul hurts, but her wallet is safe.")
    else:
        player.cool -= 5
        print("Ryo presses her face against the glass. She can't afford it. The shopkeeper asked her to leave. -5 COOL.")

def kessoku_band_practice(player):
    print("It's time for Kessoku Band practice!")
    if player.stamina > 30:
        player.stamina -= 20
        player.cool += 10
        print("Practice went great. Ryo's bass lines carried the song. -20 STAMINA, +10 COOL.")
    else:
        player.hp -= 10
        player.cool -= 10
        print("Ryo passed out mid-song due to hunger. Nijika is disappointed. -10 HP, -10 COOL.")

def the_bocchi_effect(player):
    print("Hitori (Bocchi) is glitching out in the corner of the room.")
    choice = input("Does Ryo help her (1) or take a photo for social media (2)? ")
    
    if choice == "1":
        player.stamina -= 10
        player.debt = max(0, player.debt - 100)
        print("Ryo calmed her down. Nijika saw this and forgave 100 Yen of debt. -10 STAMINA.")
    else:
        player.cool += 15
        print("The photo went viral. Ryo is a trendsetter. +15 COOL.")

def fan_encounter(player):
    print("A fan recognizes Ryo on the street!")
    if player.cool > 40:
        gift = random.randint(500, 1500)
        player.money += gift
        print(f"The fan bought Ryo a high-end curry! She pocketed the cash instead. +{gift} Yen.")
    else:
        print("The fan realized Ryo was just eating weeds and walked away awkwardly.")

def nijika_intervention(player):
    if player.debt > 2000:
        print("Nijika found Ryo's secret stash of expensive pedals while the debt remains unpaid.")
        player.money = 0
        player.debt -= 1000
        print("Nijika confiscated all of Ryo's pocket money to pay off the debt. Money reset to 0, Debt -1000.")
    else:
        print("Nijika bought Ryo a vending machine drink. Pure bassist fuel. +5 HP.")
        player.hp = min(100, player.hp + 5)