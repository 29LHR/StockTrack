import tkinter as tk
from tkinter import Button, Label, Frame

class main():
    def __init__(self, root, setupFile):
        self.root = root
        self.root.title("Stocks App")
        self.root.geometry("400x300")
        self.name = setupFile["name"]
        self.favTickers = tuple(setupFile["fav_stocks"])
        print(self.favTickers)
        