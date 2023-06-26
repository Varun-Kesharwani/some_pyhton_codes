import random

def decide(computer, mine):
    if(computer=="s" and mine =="p"):
        return True
    elif(computer=="p" and mine =="sr"):
        return True
    elif(computer=="sr" and mine =="s"):
        return True
    elif(computer == mine):
        return None
    else:
        return False




choice = ("s","p","sr") # s:- stone, p:- paper, sr:- sissor
computer = random.randint(0,2) 
#this will choose random either one zero or two one for s tow for sr and so on
computer = choice[computer]
mine = input("Choose:- \n s for stone \n p for paper \n sr for sissor \n ")

win = decide(computer,mine) #function calling
if win:
    print(f" You choose {mine} and Computer choose {computer} so")
    print("you win")
elif(win is None):
    print(f"You choose {mine} and Computer choose {computer} so ")
    print("Match drawn and you win")
else:
    print(f" You choose {mine} and Computer choose {computer} so")
    print("you loose")