import sys
import time
import random
from events import trigger_random_event
from char import Character 

def show_stats(p):
    print("\n" + "="*30)
    print(f" Name: {p.name}")
    print(f" HP: {p.hp}/100 | Stamina: {p.stamina}/100")
    print(f" Cool: {p.cool} | Money: {p.money} Yen")
    print(f" Debt: {p.debt} Yen")
    print("="*30)

def main():
    ryo = Character(name="Ryo", hp=100, stamina=50, cool=40, debt=500, money=200)

    print("--- WELCOME TO THE WEEDS EATING SIMULATOR ---")
    print("Goal: Don't die, pay your debts (maybe), and stay cool.")
    time.sleep(1)

    while True:
        show_stats(ryo)
        
        print("\nWhat will Ryo do today?")
        print("1. Eat weeds (Restore HP)")
        print("2. Rest (Restore Stamina)")
        print("3. Find a 'Creative' Job (Earn Money)")
        print("4. Borrow money from Nijika")
        print("5. Quit Game")

        choice = input("\nSelect an action (1-5): ")

        if choice == "1":
            ryo.eat_weeds(15)
        elif choice == "2":
            ryo.rest(20)
        elif choice == "3":
            ryo.find_job(2000)
        elif choice == "4":
            ryo.borrow_money()
        elif choice == "5":
            print("Ryo disappeared to a remote mountain to find a rare vintage bass. Game Over.")
            break
        else:
            print("Invalid choice. Ryo stared blankly into space.")
            time.sleep(1)
            continue

        time.sleep(1.5)

        if random.random() < 0.3:
            trigger_random_event(ryo)
            time.sleep(2)
        else:
            print("\n...The day passes quietly. No drama today.")
            time.sleep(1)

        if ryo.hp <= 0:
            print(f"\n{ryo.name} has collapsed. The dream is over.")
            sys.exit()

if __name__ == "__main__":
    main()