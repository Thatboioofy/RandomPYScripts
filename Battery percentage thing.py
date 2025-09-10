import time
import os
TimeToIncrement = 1.6
Battperc = int(input("Whats the current battery perccentage : "))
while Battperc <= 100:
    os.system("cls")
    if int(Battperc+0.000000006) >= 100:
        print("Current percentage : 100%")
        print("Battery Fully charged")
        break
    else:
        TimeToGo = (100-Battperc) *10
        Hours = TimeToGo // 60
        Minutes = int(TimeToGo - (Hours * 60))
        print("Current percentage : " , int(Battperc), "%")
        if int(Hours) == 0:
            print("This will take " , Minutes , " Mins ")
        else:
            print("This will take " , int(Hours), " Hrs " , Minutes , " Mins ")
        time.sleep(TimeToIncrement)
        Battperc = Battperc + .1

