choices = ["yes", "y", "no" , "n"]
def main():
    Term = input("Is it a term date? \n >> ").lower()
    Week = input("Is it a week day? \n >> ").lower()
    Inset = input("Is it an inset day? \n >> ").lower()
    if Term in choices and Week in choices and Inset in choices:
        if Term in ["yes", "y"]:
            if Week in ["yes", "y"]:
                if Inset in ["no", "n"]:
                    print("Go to school")
                else:
                    print("its inset day")
            else:
                print("Its the weekend ig")
        else:
            print("Its not the term yet then :/")
    else:
        print("Something doesnt seem right...\nOnly use : " + ", ".join(choices))
        main()
main()
