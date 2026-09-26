import tkinter as tk
from customtkinter import CTkLabel, CTkFrame, CTkEntry, StringVar, CTkButton, CTkToplevel
from scraper import getVal, getPrice, getPriceIncrease, tickerToName

class main():
    class __favQuickFrame():
        def __init__(self, root, col : int, ticker : str):
            #Setup Frame
            self.__frame = CTkFrame(root)
            self.__frame.grid(column=col, row=0)
            
            #Initalise Variables
            self.ticker = ticker
            title = CTkLabel(self.__frame, text=ticker.upper())
            title.pack()
            
            self.__displayVals()
            
        def __displayVals(self):
            #Display the current price of the stock
            price = getPrice(self.ticker)
            priceLbl = CTkLabel(self.__frame, text=str(price), font=("Inter", 14))
            priceLbl.pack()
            
            priceChg = getPriceIncrease(self.ticker)
            priceChgLbl = CTkLabel(self.__frame, text=str(priceChg), font=("Inter", 12))
            if priceChg[0] == "+":
                priceChgLbl.configure(text_color="green")
            else:
                priceChgLbl.configure(text_color="red")
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
        self.custom = CTkEntry(self.root, textvariable=self.customText)
        self.custom.grid(column=0, columnspan=2, row=2)
        
        self.searchButton = CTkButton(self.root, text="Evaluate Stock", command=self.createStockDisplay)
        self.searchButton.grid(column=2, row=2)
    
    def __setup1Page(self):
        h1 = CTkLabel(self.root, text=f"Hi {self.name}, here are today's stocks:")
        h1.configure(font=("Inter", 24))
        h1.grid(row=0, column=0, columnspan=3)
        
        self.favTickFrame = CTkFrame(self.root)
        currentCol = 0
        for ticker in self.favTickers:
            self.__favQuickFrame(self.favTickFrame, currentCol, ticker)
            currentCol += 1
        
        self.favTickFrame.grid(column=0, columnspan=3, row=1)
    
    def createStockDisplay(self):
        stockDisplay(self.root, self.customText.get())
    
class stockDisplay():
    class __tableElement():
        def __init__(self, root, text, row, col):
            self.frame = CTkFrame(root)
            self.CTkLabel = CTkLabel(self.frame, text=text)
            self.CTkLabel.pack()
            self.frame.grid(column=col, row=row)
    
    def __init__(self, root, ticker):
        #Create a CTkToplevel
        self.tl = CTkToplevel(root)
        
        #Define Variables
        self.ticker = ticker
        self.name = tickerToName(self.ticker)
        self.price = getPrice(self.ticker)
        self.priceInc = getPriceIncrease(self.ticker)
        
        #Setup Window
        self.tl.title(f"{self.name} Stock")
        
        #Add Headings
        self.title = CTkLabel(self.tl, text=self.ticker)
        self.subtitle = CTkLabel(self.tl, text=self.name)
        self.price = CTkLabel(self.tl, text=str(self.price))
        
        #Get Vals
        self.vals = getVal(self.ticker, "full").split(" | ")
        self.createValsTable()
        
        #Add to searches.txt
        with open("searches.txt", "a") as f:
            f.write(self.ticker + ",")
            
    def createValsTable(self):
        self.valsTable = CTkFrame(self.tl, relief="solid", borderwidth=1)
        
        table = []
        for i in range(8):
            table.append([self.__tableElement(self.valsTable, text=self.vals[0+(i*2)], row=i, col=0), self.__tableElement(self.valsTable, text=self.vals[1+(i*2)], row=i, col=1), self.__tableElement(self.valsTable, text=self.vals[16+(i*2)], row=i, col=2), self.__tableElement(self.valsTable, text=self.vals[17+(i*2)], row=i, col=3)]) #adds a row of tableElements to the table
            print(f"Added Row {i}")
        
        self.valsTable.grid(row=1, column=0, columnspan=2)