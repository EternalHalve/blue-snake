from random import randint, random

money = 2000
pin = randint(1, 5)

print("...Oh. It's you.")
print("Welcome to the 2nd-Hand Bass Fund—I mean, the ATM.")
print(f"I forgot the PIN. It's like... 1 through 5. Whatever.")

try:
    guess = int(input("Guess it. If you're wrong, I'm buying weeds for dinner: "))
except ValueError:
    print("That's not even a number. My brain hurts. Bye.")
    exit()

if guess != pin:
    print(f"\nWrong. Thanks for the ${money}. I saw a vintage Precision Bass online... it's mine now.")
else:
    print("\n...Tch. Lucky guess. I guess I'll let you see your 'savings.'")
    
    while True:
        if random() < 0.20 and money > 50:
            robbery = 50
            money -= robbery
            print(f"\n(Note: ${robbery} disappeared for 'administrative expenses.' Don't ask.)")

        print(f"\n[ Balance: ${money} ]")
        action = input("What do you want? (deposit / borrow / quit): ").lower()

        if action == "deposit":
            try:
                amount = int(input("Giving me more? You're a saint: "))
                money += amount
                print(f"I'll keep this ${amount} very safe. *Clutches bass guitar*")
            except ValueError:
                print("Numbers only. I'm too tired for riddles.")

        elif action == "borrow" or action == "withdraw":
            try:
                amount = int(input("You want it back? How selfish: "))
                if amount > money:
                    print("I don't have that. I already spent—I mean, the system is down.")
                else:
                    money -= amount
                    print(f"Fine. Take your ${amount}. I'll just eat weeds today.")
            except ValueError:
                print("Use a number. Please.")

        elif action == "quit":
            print("Leaving already? Tell Nijika I'm 'practicing'. I'll return her money later (if I remember).")
            break 
        
        else:
            print(f"'{action}'? Is that a new genre of Math Rock? I don't get it.")