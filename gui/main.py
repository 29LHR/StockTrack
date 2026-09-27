from customtkinter import CTkLabel, CTkFrame, CTkEntry, StringVar, CTkButton, CTkToplevel, CTkRadioButton
from scraper import getPrice, getPriceIncrease
from gui.stockDisplay import stockDisplay
from gui.comparison import compGUI

class main():
    class __favQuickFrame():
        def __init__(self, root, col : int, ticker : str):
            #Setup Frame
            self.__frame = CTkFrame(root)
            self.__frame.grid(column=col, row=0, padx=10, pady=5)
            
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
                priceChgLbl.configure(text_color="#dc2626")
            priceChgLbl.pack()
        
    def __init__(self, root, setupFile):
        #Setup App Base
        self.root = root
        self.root.title("StockTrack")
        
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
        self.customText = StringVar()
        self.custom = CTkEntry(self.root, placeholder_text="Enter ticker", placeholder_text_color="grey")
        self.custom.grid(column=0, columnspan=2, row=2, padx=10, pady=2)
        
        self.searchButton = CTkButton(self.root, text="Evaluate Stock", command=self.__createStockDisplay)
        self.searchButton.grid(column=2, row=2, padx=10, pady=2)
        
        #Add Comparison Form
        self.compFrame = CTkFrame(self.root)
        
        self.compLabel = CTkLabel(self.compFrame, text="Comparision:").grid(row=0, column=0)
        
        self.compEntryT1 = CTkEntry(self.compFrame, placeholder_text="Ticker 1", placeholder_text_color="grey")
        self.compEntryT1.grid(row=0, column=1)
        
        self.compEntryT2 = CTkEntry(self.compFrame, placeholder_text="Ticker 2", placeholder_text_color="grey")
        self.compEntryT2.grid(row=0, column=2)
        
        self.compButton = CTkButton(self.compFrame, text="Compare", command=self.__compare).grid(row=2, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        
        #Add Comparison radio
        self.compMethod = StringVar(value="Time")
        rbTime = CTkRadioButton(self.compFrame, text="Time", variable= self.compMethod, value="time").grid(row=1, column=0, pady=2, padx=2)
        rbPrice = CTkRadioButton(self.compFrame, text="Price", variable= self.compMethod, value="price").grid(row=1, column=1, pady=2, padx=2)
        rbAnalyst = CTkRadioButton(self.compFrame, text="Analyst", variable= self.compMethod, value="analyst").grid(row=1, column=2, pady=2, padx=2)
        
        self.compFrame.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        
    def __setup1Page(self):
        h1 = CTkLabel(self.root, text=f"Hi {self.name}, here are today's stocks:")
        h1.configure(font=("Inter", 20))
        h1.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
        
        self.favTickFrame = CTkFrame(self.root)
        currentCol = 0
        for ticker in self.favTickers:
            self.__favQuickFrame(self.favTickFrame, currentCol, ticker)
            currentCol += 1
        
        self.favTickFrame.grid(column=0, columnspan=3, row=1, padx=10, pady=5)
    
    def __createStockDisplay(self):
        stockDisplay(self.root, self.custom.get())
    
    def __compare(self):
        compGUI(self.root, self.compEntryT1.get(), self.compEntryT2.get(), self.compMethod.get())
