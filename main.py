import customtkinter as tk
import gui.main as mainGUI
from scraper import *
import json,requests

#Internet Checker
def internetCheck() -> bool:
    try:
        requests.get("https://bbc.co.uk")
        return True
    except:
        print("noInternet")
        return False

def internetRetry():
    internetRetry = tk.CTkToplevel(root)
    tk.CTkLabel(internetRetry, text="Checking internet").pack()
    
    if internetCheck():
        noInternet.destroy()
        mainGUI.main(root, setup)
        tk.set_appearance_mode("dark")
        internetRetry.destroy()
    else:
        internetRetry.destroy()
        

#Process __setup__.json
with open("__setup__.json", "r") as f:
    setup = json.load(f)

#Initialise Main Class
root = tk.CTk()

if not internetCheck():
    noInternet = tk.CTkToplevel(root)
    tk.CTkLabel(noInternet, text="Please connect to the internet", text_color="#dc2626").pack()
    tk.CTkButton(noInternet, text="Retry", command=internetRetry).pack()
else:
    mainGUI.main(root, setup)
    tk.set_appearance_mode("dark")

#Start App
root.mainloop()