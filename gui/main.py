import tkinter as tk
from tkinter import Label, Frame, Entry, StringVar, Button, Toplevel
from scraper import getVal, getPrice, getPriceIncrease, tickerToName

class main():
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
            priceLbl = Label(self.__frame, text=str(price), font=("Inter", 14))
            priceLbl.pack()
            
            priceChg = getPriceIncrease(self.ticker)
            priceChgLbl = Label(self.__frame, text=str(priceChg), font=("Inter", 12))
            if priceChg[0] == "+":
                priceChgLbl.config(fg="green")
            else:
                priceChgLbl.config(fg="red")
            priceChgLbl.pack()
        
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
        
        #Added Custom Entry
        self.customText = StringVar(value="Enter ticker: e.g. AAPL")
        self.custom = Entry(self.root, textvariable=self.customText)
        self.custom.grid(column=0, columnspan=2, row=2)
        
        self.searchButton = Button(self.root, text="Evaluate Stock", command=self.createStockDisplay)
        self.searchButton.grid(column=2, row=2)
    
    def __setup1Page(self):
        h1 = Label(self.root, text=f"Hi {self.name}, here are today's stocks:")
        h1.config(font=("Inter", 24))
        h1.grid(row=0, column=0, columnspan=3)
        
        currentCol = 0
        for ticker in self.favTickers:
            self.__favQuickFrame(self.root, currentCol, ticker)
            currentCol += 1
    
    def createStockDisplay(self):
        stockDisplay(self.root, self.customText.get())
    
class stockDisplay():
    def __init__(self, root, ticker):
        #Create a toplevel
        self.tl = Toplevel(root)
        
        #Define Variables
        self.ticker = ticker
        self.name = tickerToName(self.ticker)
        
        #Setup Window
        self.tl.title(f"{self.name} Stock")
        
        #Get Vals
        self.vals = getVal(self.ticker, "full").split(" | ")
        self.createValsTable()
        
        #Add to searches.txt
        with open("searches.txt", "a") as f:
            f.write(self.ticker)
            
    def createValsTable(self):
        self.valsTable = Frame(self.tl)
        
        table = []
        for i in range(8):
            table.append([Label(self.valsTable, text=self.vals[0+(i*2)]).grid(column=0,row=i), Label(self.valsTable, text=self.vals[1+(i*2)]).grid(column=1,row=i), Label(self.valsTable, text=self.vals[16+(i*2)]).grid(column=2,row=i),Label(self.valsTable, text=self.vals[17+(i*2)]).grid(column=3,row=i)]) #adds a row to the table
            print(f"Added Row {i}")
        
        self.valsTable.pack()