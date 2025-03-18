from turtle import *
import random
import threading
GB = False
title("Torture")
def main():
    pendown()
    global GB
    while True:
        if GB == True:
            goto(0,0)
            GB = False
        
        forward(random.randint(1,100))
        left(random.randint(1,100))

art = threading.Thread(target=main)
art.daemon = True
art.start()

while True:
    i = input("GET BACK HERE (Y/N)")
    if i == "Y" or i == "y":
        GB = True

