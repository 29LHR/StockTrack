from customtkinter import CTkLabel, CTkFrame, CTkEntry, StringVar, CTkButton, CTkToplevel, CTkRadioButton
from scraper import getVal, getPrice, getPriceIncrease, tickerToName, buyComp

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
        self.title = CTkLabel(self.tl, text=f"{self.name} ({self.ticker.upper()})")
        self.title.configure(font=("Inter", 24))
        self.title.grid(row=0, column=0, padx=10, pady=10)
        
        self.price = CTkLabel(self.tl, text=str(self.price))
        self.price.configure(font=("Inter", 24))
        self.price.grid(row=0, column=1, padx=10, pady=10)
        
        #Get Vals
        self.vals = getVal(self.ticker, "full").split(" | ")
        self.createValsTable()
        
        #Add to searches.txt
        with open("searches.txt", "a") as f:
            f.write(self.ticker + ",")
        
        self.quickFrame = CTkFrame(self.tl)
        self.createSearchFrame()
        self.createTrendFrame()
        self.quickFrame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
    def createValsTable(self):
        self.valsTable = CTkFrame(self.tl)
        
        table = []
        for i in range(8):
            table.append([self.__tableElement(self.valsTable, text=self.vals[0+(i*2)], row=i, col=0), self.__tableElement(self.valsTable, text=self.vals[1+(i*2)], row=i, col=1), self.__tableElement(self.valsTable, text=self.vals[16+(i*2)], row=i, col=2), self.__tableElement(self.valsTable, text=self.vals[17+(i*2)], row=i, col=3)]) #adds a row of tableElements to the table
            print(f"Added Row {i}")
        
        self.valsTable.grid(row=1, column=0, columnspan=2, padx=10, pady= 10)
    
    def calcSearches(self):
        with open("searches.txt", "r") as f:
            all = f.read().split(",")
        
        number = all.count(self.ticker)
        return number
    
    def createSearchFrame(self):
        self.searchFrame = CTkFrame(self.quickFrame, border_width=1)
        self.searches = self.calcSearches()
        
        self.searchLabel = CTkLabel(self.searchFrame, text=str(self.searches), font=("Inter", 24))
        self.searchLabel.pack(padx=5, pady=5)

        self.searchDesc = CTkLabel(self.searchFrame, text="Searches", font=("Inter",12))
        self.searchDesc.pack(padx=5, pady=5)
        
        self.searchFrame.grid(row=2, column=0, padx=100, pady=10)
    
    def createTrendFrame(self):
        if self.priceInc[0] == "+":
            self.color = "green"
        else:
            self.color = "#dc2626"
            
        self.trendFrame = CTkFrame(self.quickFrame, border_width=1)
        self.trend = self.calcSearches()
        
        if self.color == "green":
            self.trendLabel = CTkLabel(self.trendFrame, text="⬆︎", font=("Inter", 24), text_color=self.color)
        else:
            self.trendLabel = CTkLabel(self.trendFrame, text="⬇︎", font=("Inter", 24), text_color=self.color)
            
        self.trendLabel.pack(padx=5, pady=5)

        self.trendDesc = CTkLabel(self.trendFrame, text=self.priceInc, font=("Inter",12), text_color=self.color)
        self.trendDesc.pack(padx=5, pady=5)
        
        self.trendFrame.grid(row=2, column=1, padx=100, pady=10)
        
