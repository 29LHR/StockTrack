from customtkinter import CTkLabel, CTkFrame, CTkEntry, StringVar, CTkButton, CTkToplevel, CTkRadioButton
from scraper import getVal, getPrice, getPriceIncrease, tickerToName, buyComp

class compGUI():
    def __init__(self, root, ticker1, ticker2, priority):
        self.root = root
        self.ticker1 = str(ticker1)
        self.ticker2 = str(ticker2)
        self.priority = str(priority)
        
        print(ticker1, ticker2)
        
        self.tl = CTkToplevel(root)
        self.tl.title(f"{self.ticker1.upper()} vs {self.ticker2.upper()}")
        