import configparser
import customtkinter
import subprocess
import os

applength = "480"
app = customtkinter.CTk()
app.title("Script launcher")
app.resizable(0, 0)
config = configparser.ConfigParser()
config.read("App-list.ini")
list_app = [app_name.replace('"', '').replace("'", '').replace("]", '').replace("[", '').strip() for app_name in config["List"]["list-app"].split(",")]
script_list = [script.replace('"', '').replace("'", '').replace("]", '').replace("[", '').strip() for script in config["List"]["python-name"].split(",")]
appheight = str(50 * len(list_app))
if int(appheight) > 480:
    appheight = str(int(appheight) / 2)
    applength = str(int(applength) + 240)
app.geometry(applength + "x" + appheight)

def launch_script(script_name):
    os.system("cls")
    try:
        subprocess.Popen(["python", script_name], shell=True)
        print(f"Launching {script_name}\n \n")
    except Exception as e:
        print(f"Failed to launch {script_name}: {e}")

for i in range(len(list_app)):
    button = customtkinter.CTkButton(
        app,
        text=list_app[i],
        width=200,
        command=lambda script_name=script_list[i]: launch_script(script_name)
    )
    button.grid(column=i % 2, row=i // 2, pady=5, padx=5)

app.mainloop()