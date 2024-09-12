import random

while True:
    answer = input("Roll the Dice ?? (Y/N): ").lower()
    
    if answer == "y":
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f"Dice numbers are: {num1} and {num2}")
        
    elif answer == "n":
        print("Thanks for playing!!")
        break
        
    else:
        print("Invalid Choice! Please enter 'Y' to roll or 'N' to quit.")
