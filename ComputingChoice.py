choices = ["yes", "y", "no" , "n"]
AttG = 0
ProgG = 0
MaGRG = 0
def main():
    MaGR = input("Whats your maths grade? \n >> ")
    Prog = input("Do you like programming? \n >> ").lower()
    Att = input("Whats your attedndance? \n >> ")
    if MaGR.isdigit():
        if int(MaGR) > 4:
            print("Your maths grade is good enough")
            MaGRG = 1
        else:
            print("You may wana get better at maths tbh")
    else:
        print("I dont think you entered a number for your maths grade")
        main()
    if Prog in choices:
        if Prog in ["yes", "y"]:
            print("Good that means you enjoy will computing")
            ProgG = 1
        else:
            print("You wont like computing to much then")
    else:
        print("I dont think you entered a yes or no answer")
        main()
    if Att.isdigit():
        if int(Att) > 100:
            print("Sure thing buddy")
        elif int(Att) > 92:
            print("You have a good enough attendance to do computing")
            AttG = 1
        else:
            print("You dont have a good enough attendance")
    else:
        print("You did not enter a number for your attendance")
    if AttG == 1 and ProgG == 1 and MaGRG == 1:
        print("\nYou should do computing")
    else:
        print("\nIf you improve you could do computing")
main()