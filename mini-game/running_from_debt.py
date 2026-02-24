from random import random, randint

debt = 1000
stamina = 100
money = 0
has_scooter = False

while True:
    print(f"\n--- Status: Money ${money} | Stamina {stamina} | Debt ${debt} ---")
    print("Nijika: Ryo!! Where is my money?!")

    choice = input("What would you do? (run, pay, work, rest, escape): ").lower().strip()

    if choice == "run":
        if stamina >= 20:
            print("Ryo: *Bolts away at high speed* Catch me if you can!")
            stamina -= 20
            if random() < 0.10:
                found_money = randint(200, 500)
                print("Ryo: *Trips over a discarded wallet* ...Wait, there's no ID in here.")
                print(f"Ryo: JACKPOT. I found ${found_money}!")
            else:
                found_money = randint(10, 20)
                print("Ryo: *Sliding into a back alley* Phew, she's gone.")
                print(f"Ryo: Oh, a shiny ${found_money} coin on the ground. Today is my lucky day.")
            money += found_money
        else:
            print("Nijika: Caught you! You're too tired to run.")
            debt += 50

    elif choice == "pay":
        if money <= 0:
            print("Ryo: I have no money. I spent it all on bass strings and weeds.")
        else:
            try:
                pay_amount = int(input(f"How much will you pay? (Debt: ${debt}): "))
                if pay_amount > money:
                    print("Ryo: I don't actually have that much...")
                else:
                    money -= pay_amount
                    debt -= pay_amount
                    print(f"Nijika: Thank you. Only ${debt} left to go...")
            except ValueError:
                print("Nijika: Give me a real number, Ryo!")

    elif choice == "work":
        if stamina >= 30:
            print("Ryo: *Sighs* Fine, I'll play a session gig...")
            money += 150
            stamina -= 30
            if random() < 0.20 and not has_scooter:
                print("\nSeika (Manager): Ryo, this old scooter is taking up space in the alley.")
                print("Seika: Take it and get out of my sight. Maybe use it to find a real job.")
                has_scooter = True
        else:
            print("Ryo: I'm too hungry/tired to hold my bass.")

    elif choice == "rest":
        print("Ryo: *Eating weeds in the park* Peaceful.")
        stamina = min(100, stamina + 40)

    elif choice == "disappear":
        if has_scooter:
            if stamina >= 70:
                print("Ryo: *Kickstarts the rusty engine* See ya, Nijika!")
                print("Nijika: HEY! GET BACK HERE YOU LITTLE!")
                print("\nEnding: You successfully fled to the next ward. Responsibility avoided.")
                break
            else:
                print("Ryo: I have the scooter... but I'm too tired to kickstart it.")
        else:
            print("Nijika: Running on foot? I'm the drummer, Ryo. My cardio is better than yours.")

    if debt <= 0:
        print("\nNijika: You actually paid it back?! Is the world ending?")
        break