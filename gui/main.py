import tkinter as tk
from tkinter import Button, Label, Frame
from scraper import getPrice, getPriceIncrease

class main():
    def __init__(self, root, setupFile):
        #Setup App Base
        self.root = root
        self.root.title("Stocks App")
        self.root.geometry("400x300")
        
        #Gather Setup.json values
        self.name = setupFile["name"]
        self.favTickers = tuple(setupFile["fav_stocks"])
        match setupFile["date"]:
            case "dd/mm/yyyy":
                self.dateStyle = "GBR"
            case "mm/dd/yyyy":
                self.dateStyle = "USA"
        
        self.__setup1Page()
    
    def __setup1Page(self):
        h1 = Label(self.root, text=f"Hi {self.name}, here are today's stocks:")
        h1.config(font=("Arial", 24))
        h1.grid(row=0, column=0, columnspan=3)
        
        currentCol = 0
        for ticker in self.favTickers:
            __favQuickFrame(self.root, currentCol, ticker)

class __favQuickFrame():
    def __init__(self, root, col : int, ticker : str):
        #Setup Frame
        self.__frame = Frame(root)
        self.__frame.grid(column=col, row=1)
        
        #Initalise Variables
        self.ticker = ticker
        title = Label(self.__frame, text=ticker.upper())
        title.pack()
        
        self.__displayVals()
        
    def __displayVals(self):
        #Display the current price of the stock
        price = getPrice(self.ticker)
        priceLbl = Label(self.__frame, text=str(price))
        priceLbl.pack()
        
        priceChg = getPriceIncrease(self.ticker)
        priceChgLbl = Label(self.__frame, text=str(priceChg))
        priceChgLbl.pack()
        