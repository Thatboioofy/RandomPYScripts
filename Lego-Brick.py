import random 
import os
c1 = ["Yellow", "Green", "Blue", "Red"]
c2 = ["Yellow", "Green", "Blue", "Red", "White", "Black"]
lead = open("leaderboard.txt", "r+")
leader = lead.read()
def game():
    os.system('cls')
    score = 0
    for i in range(3):
        c1a = random.choice(c1)
        c2a = random.choice(c2)
        if c1a == c2a:
            score = score +3
        if c2a == "Black":
            score = score +2
        if c2a == "White":
            score = score +1
        print("\nRound",i+1,"results : \n  Pull 1 :", c1a,"\n  Pull 2 :", c2a)
        print("  Current Score:", score)

    print("You have...")
    if score <= 3:
        print("Nothing :c")
    elif score == 4:
        print("won a small prize :3")
    else:
        print("won a big prize")
    q = input("\nDo you want to play again? (y/N)\n>> ")
    if q == "y" or q == "Y":
        game()
    else:
        quit()

os.system('cls')
p = input("Do you want to play the game? (y/N) \n>> ")
if p == "Y" or p == "y":
    game()
else:
    quit()