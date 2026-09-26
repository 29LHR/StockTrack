import customtkinter as tk
import gui.main as mainGUI
from scraper import *
import json

#Process __setup__.json
with open("__setup__.json", "r") as f:
    setup = json.load(f)

#Initialise Main Class
root = tk.CTk()
mainGUI.main(root, setup)

#Start App
root.mainloop()