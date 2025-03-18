import random
import customtkinter
import threading
from PIL import Image
import configparser

app = customtkinter.CTk()
app.title("Login")
app.geometry("480x240")
app.resizable(0,0)
customtkinter.set_appearance_mode("dark")
CPUScore = 0
USRScore = 0
Round = 1

#Loads images
app.rock = customtkinter.CTkImage(light_image=Image.open("Icons/rock.png"), size = (30,30))
app.paper = customtkinter.CTkImage(light_image=Image.open("Icons/paper.png"), size = (30,30))
app.scissors = customtkinter.CTkImage(light_image=Image.open("Icons/scissors.png"), size = (30,30))
app.question = customtkinter.CTkImage(light_image=Image.open("Icons/Unknown.png"), size = (30,30))

#reads the credentials from a file
config = configparser.ConfigParser()
config.read('RPS-config.ini')


#ToDo
#Round selection (WIP)
#Other quality of life stuff



#For debugging 
def backendDebug():
    while True:
        debugin = input(">> ")
        exec(debugin)
        
BEdebugRun = threading.Thread(target=backendDebug)

    

#Login Logic
def logon():
    Infolabel.configure(text="")
    usr = UserInput.get()
    if UserInput.get() == "debug": #Used for debugging certain things (Not funcional RN)
        BEdebugRun.daemon = True
        RPS_load()

    elif config.has_option(usr, 'username') == True:
        print("Username correct")
        if config[usr]['password'] == PassInput.get():
            print("Password correct")
            message = config[usr]['message']
            Infolabel.configure(text=message)
            app.after(1000, RPS_load)
        else:
            PassInput.focus()
            Infolabel.configure(text="Password incorrect")
    else:
        UserInput.focus()
        Infolabel.configure(text="Username incorrect")


#Updates information
def InfoUpd(info, option, CPU):
    global Round, CPUScore, USRScore
    Round += 1
    Roundlabel.configure(text='Round : ' + str(Round))
    if info == 'draw':
        CPUresultLabel.configure(text='CPU : Tie')
        USRresultLabel.configure(text='USR : Tie')
        Scorelabel.configure(text=str(CPUScore) + " - " + str(USRScore))
    elif info == 'win':
        CPUresultLabel.configure(text='CPU : Loss')
        USRresultLabel.configure(text='USR : Win')
        USRScore += 1
        Scorelabel.configure(text=str(CPUScore) + " - " + str(USRScore))
    else:
        CPUresultLabel.configure(text='CPU : Win')
        USRresultLabel.configure(text='USR : Loss')
        CPUScore += 1
        Scorelabel.configure(text=str(CPUScore) + " - " + str(USRScore))

    result = [CPUresult, USRresult]
    select = [CPU , option]
    for i in range(2):
        if select[i] == 'rock':
            result[i].configure(image=app.rock)
            print("rock", result[i])
        elif select[i] == 'paper':
            result[i].configure(image=app.paper)
            print("paper", result[i])
        elif select[i] == 'scissors':
            result[i].configure(image=app.scissors)
            print("scissors", result[i])
    rockbtn.configure(state="normal")
    paperbtn.configure(state="normal")
    scissorsbtn.configure(state="normal")


#Round amount selection (WIP)
def UpdRound(rounds):
    amount.configure(text="Amount of Rounds : "+ str(int(rounds)))

def AmountOfRounds():
    app.title("RPS Game -- Round Amount Selection")
    PassInput.grid_forget()
    UserInput.grid_forget()
    Infolabel.grid_forget()
    SubmitCred.grid_forget()
    slider.grid()
    amount.grid()



#Sigma Game
def SubChoice(option):
    rockbtn.configure(state="disabled")
    paperbtn.configure(state="disabled")
    scissorsbtn.configure(state="disabled")
    CPU = random.choice(['rock','paper','scissors'])
    print(CPU)
    if option == CPU:
        print("Draw")
        InfoUpd('draw', option, CPU)
    elif (option == 'rock' and CPU == 'scissors') or (option == 'paper' and CPU == 'rock') or (option == 'scissors' and CPU == 'paper'):
        print("Player wins")
        InfoUpd('win', option, CPU)
    else:
        print("CPU wins")
        InfoUpd('loss', option, CPU)


#Login UI

Infolabel = customtkinter.CTkLabel(app, text="")
Infolabel.grid(row=3,column=0,pady=10)
UserInput = customtkinter.CTkEntry(app, placeholder_text="Username",width=240)
UserInput.grid(row=0,column=0, pady=(40,10),padx=120)
PassInput = customtkinter.CTkEntry(app, placeholder_text="Password",width=240)
PassInput.grid(row=1,column=0, pady=10)
SubmitCred = customtkinter.CTkButton(app, text="Submit", command=logon)
SubmitCred.grid(row=2,column=0, pady=10)

#RPS game UI
Roundlabel = customtkinter.CTkLabel(app,text="Round : 1")
Scorelabel = customtkinter.CTkLabel(app, text="0 - 0")
CPUresultLabel = customtkinter.CTkLabel(app,text="CPU : None")
USRresultLabel = customtkinter.CTkLabel(app,text="USR : None")
CPUresult = customtkinter.CTkButton(app, width=60, height=60, text="",state="disabled", image=app.question)
USRresult = customtkinter.CTkButton(app, width=60, height=60, text="",state="disabled", image=app.question)
rockbtn = customtkinter.CTkButton(app, width=50, height=50, text="", image=app.rock)
paperbtn = customtkinter.CTkButton(app, width=50, height=50, text="", image=app.paper)
scissorsbtn = customtkinter.CTkButton(app, width=50, height=50, text="", image=app.scissors)
amount = customtkinter.CTkLabel(app, text="")
slider = customtkinter.CTkSlider(app, from_=1, to=100, command=UpdRound, number_of_steps=99)



def RPS_load():
    app.title("RPS Game -- Loading")
    Roundlabel.grid(row=0,column=0,sticky = "wn",padx=205)
    Scorelabel.grid(row=1,column=0,sticky = "wn",padx=220)
    CPUresultLabel.grid(row=3,column=0, sticky = "nws",padx = 10,pady = 10)
    CPUresult.grid(row=4,column=0, sticky = "nws", padx = 10, pady = 10)
    USRresultLabel.grid(row=3,column=0, sticky = "nes",pady = 10, padx =405)
    USRresult.grid(row=4,column=0, sticky = "nes", pady = 10, padx =405)
    rockbtn.configure(command = lambda: SubChoice('rock'))
    paperbtn.configure(command = lambda: SubChoice('paper'))
    scissorsbtn.configure(command = lambda: SubChoice('scissors'))
    rockbtn.grid(row=5, sticky = "w",padx=145)
    paperbtn.grid(row=5, sticky = "w",padx=205)
    scissorsbtn.grid(row=5, sticky = "w",padx=265)
    app.title("RPS Game")
    

app.mainloop()