import customtkinter
import configparser


global tmp, tmpa, tmpw
tmp = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
tmpa = []
tmpw = []


app = customtkinter.CTk()
app.title("Guessing Game (UI Version)")
app.geometry("400x200")
app.resizable(0,0)
app.config(bg="gray")
customtkinter.set_appearance_mode("dark")


#functions

def submit():
    ans = str(tmpa) 
    ans.replace("[", "")
    ans.replace("]", "")
    ans.replace("'", "")
    if a.get() is tmpa:
        ad.configure(text="That already in the list of guessed !")
        app.after(2000, lambda: ad.configure(text="Guessed : " + ans ))
        a.delete(0, "end")
    elif a.get() is tmpw:
        ad.configure(text="That already in the list of wrong guesses !")
        app.after(2000, lambda: ad.configure(text="Guessed : " + ans ))
        a.delete(0, "end")
    elif a.get() in tmp:
        ad.configure(text="Correct !")
        tmpa.append(a.get())
        app.after(2000, lambda: ad.configure(text="Guessed : " + ans ))
        a.delete(0, "end")
    else:
        ad.configure(text="Incorrect !")
        tmpw.append(a.get())
        app.after(2000, lambda: ad.configure(text="Guessed : " + ans ))
        a.delete(0, "end")




#inputs for the user
a = customtkinter.CTkEntry(app, width=360)
a.grid(row=2, column=0, pady=10, padx=20)

ad = customtkinter.CTkLabel(app, text="")
ad.grid(row=1, column=0, pady=10)

q = customtkinter.CTkLabel(app, text="Place Holder")
q.grid(row=0, column=0, pady=10)

b = customtkinter.CTkButton(app, text="Submit", command=submit)
b.grid(row=3, column=0, pady=5)

app.mainloop()