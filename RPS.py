import random
RPS = ["rock", "paper", "scissors"]
scoreUsr = 0
scoreCpu = 0
usr = "root"
passwrd = "root"
r = 0 #rounds
inc = 0

def choice():
    if inc == 0:

        r = r-1
    inc = 0
    choice.usrC = input("Please choose one of these options \n1 | Rock \n2 | Paper \n3 | Scissors\n>> ")
    if usrC == "1":
        usrC = "rock"
    elif usrC == "2":
        usrC = "paper"
    elif usrC == "3":
        usrC = "scissors"
    elif usrC == "stop":
        quit()
    else:
        print("Invalid choice, please choose 1, 2, or 3.")
        inc = 1
        choice()
        

def rps_game():
    inc_tmp = 0
    choice(inc)
    userchoice = choice.usrC
    cpuC = random.choice(RPS)
    print("CPU chose: ", cpuC)
    
    if userchoice == cpuC:
        print("Draw")
    elif (userchoice == "rock" and cpuC == "scissors") or (userchoice == "paper" and cpuC == "rock") or (userchoice == "scissors" and cpuC == "paper"):
        print("User wins")
        scoreUsr += 1
    else:
        print("CPU wins")
        scoreCpu += 1

#User login#
loginusr = input("Please enter your username \n>> ")
if (loginusr == usr) or (loginusr == "debug"):
    loginpass = input("Please enter your password \n>> ")
    if loginpass == passwrd:
        if loginusr == "debug":
            debug = 1
        print("Welcome to RPS")
        r = input("Enter amount of round you will like to play\n>>  ")
        r = int(r)
        while r != 0 :
            rps_game(inc_tmp)
            inc = inc + inc_tmp

        print("Final scores:\n User - CPU\n",scoreUsr," - ",scoreCpu)
    else:
        print("Incorrect password")
else:
    print("Incorrect username")
