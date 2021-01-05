# Creating Rock, Paper, Scissor game.

import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        else:
            return False  

    elif comp == 'p':
        if you == 's':
            return True
        else:
            return False  
    elif comp == 's':
            if you == 'r':
                return True
            else:
                return False

rand = random.randint(1,3)
if rand == 1:
    comp = "r"
elif rand == 2:
    comp = "p"
else:
    comp = "s"     

you = input("Enter (r) for rock, (p) for paper and (s) for scissor ")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is tie.")
elif a:
    print("You won")
else:
    print("You lose")
