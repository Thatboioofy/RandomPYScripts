import random 
import time
from pick import pick
#To do :
# Add list selection thing befor continueing with H or L cus thats gonna make life easier
# If not the 1st one suffer by adding a UI cus why not

title = 'Please choose one of the following'
ops = ['Lottery game', 'Euro millions game', 'Higher or lower (WIP)']
index = pick(ops, title)
print(index)

if 0 in index: # Lottery game
    print("Welcome to the lottery game thingy \nNow generating your numbers")
    prev = []

    for i in range(6):
        tmp = random.randint(1,59)

        while tmp in prev:
            tmp = random.randint(1,59)

        print("Ball " , i+1, " is " , tmp)
        prev.append(tmp)
        time.sleep(1)
    
    bonus = random.randint(1,59)

    while bonus in prev:
        bonus = random.randint(1,59)

    print("Your bonus ball is " , bonus)
    
if 1 in index: # Euro millions game
    print("Welcome to the euromilion game thingy")
    print("ima generate ur numbers real quick")
    prev = []
    for i in range(5):

        num = random.randint(1,50)
        while num in prev:
            num = random.randint(1,50)
        
        print("Num ", i+1, " is " , num)
        prev.append(num)
        time.sleep(2)
    print("\nYour lucky stars are")
    prev = []
    for i in range(2):

        num = random.randint(1,12)
        while num in prev:
            num = random.randint(1,12)
        
        print("Lucky star ", i+1, " is " , num)
        prev.append(num)
        time.sleep(2)

if 2 in index:
    life = 3
    print("Welcome to Higher or Lower")
    print("A num will be randomly generated and you need to choose\n wether its higher or lower")
    print("You have " , life, "lifes \nGood luck")
    numa = random.randint(1,10)
    print("Your num is " +num)
    while life > 0:
        numb = random.randint(1,10)
        inp = input("Higher or Lower\n>> ")
        if numa > numb and inp == "Higher" or "higher":
            print("Correct")
        elif numa < numb and inp == "Lower" or "lower":
            print("NUH UH")
        if numb > numa and inp == "Higher" or "higher":
            print("Correct")

k = input("\nPress enter to close")
 
    
