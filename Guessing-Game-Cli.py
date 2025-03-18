import os
import time
tmp = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
tmpa = []
tmpw = []

running = 1


while running == 1:
    os.system("cls")
    ans = str(tmpa)
    ans.replace("[", "")
    ans.replace("]", "")
    ans.replace("'", "")
    if len(tmpa) == 0:
        print("Guessed : None")
    else:
        print("Guessed : " + ans)
    i = input("Enter a color : ")
    if i in tmpa:
        print("Already guessed !")
    elif i in tmpw:
        print("Already guessed !")
    elif i in tmp:
        print("Correct !")
        tmpa.append(i)
    else:
        print("Incorrect !")
        tmpw.append(i)
    if tmpa == tmp:
        print("You have guessed all the colors !")
        running = 0
    time.sleep(2)