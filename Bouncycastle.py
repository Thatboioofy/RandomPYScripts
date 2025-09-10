
running = 1
payments = []
amount = 0
while running == 1:
    height = input("Please enter your height : ")
    if height.isdigit():
        height = int(height)
        if height > 250 or height <60:
            print("Enter an appropriate height!")

        elif height >= 140:
            print("You can go")
            amount = amount +2

        elif height >= 120:
            ad = input("Do you hav an adult with you? ").lower()
            if ad in ["yes", "y"]:
                print("You can enter")
                amount = amount +2
            else:
                print("You cant enter")
        else:
            print("GET OUT !!!!!!!!!!!")
    else:
        print("Enter a number ong")