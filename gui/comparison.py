from customtkinter import CTkLabel, CTkFrame, CTkEntry, StringVar, CTkButton, CTkToplevel, CTkRadioButton
from scraper import getVal, getPrice, getPriceIncrease, tickerToName, buyComp

class compGUI():
    def __init__(self, root, ticker1, ticker2, priority):
        self.root = root
        self.ticker1 = ticker1
        self.ticker2 = ticker2
        self.priority = priority
        
        self.tl = CTkToplevel(root)
        