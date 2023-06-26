import random

comp = random.randint(1,1000)
guess = int(input("Enter the number :"))
attempt = 1

while(True):
    
    if(comp > guess):
        guess = int(input("guess some higher number..."))
        attempt += 1
    elif(comp< guess):
        guess = int(input("guess some lesser number..."))
        attempt += 1
    else:
        print(f"you guessed the number in {attempt} attempts... ")
        break


