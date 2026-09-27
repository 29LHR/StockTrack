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
        
        #Add Headings
        self.title = CTkLabel(self.tl, text=f"{ticker1} vs {ticker2}")
        self.title.configure(font=("Inter", 24))
        self.title.pack()
        
        self.prefferedFrame = CTkFrame(self.tl)
        
        self.preffered = buyComp(self.ticker1, self.ticker2, self.priority)
        self.preffered = self.preffered.split(" | ")[0]
        print(self.preffered)
        if self.preffered == self.ticker1 or self.preffered == self.ticker2:
            self.prefferedLabel = CTkLabel(self.prefferedFrame, text=f"Recommended Stock:\n{tickerToName(self.preffered)} ({self.preffered})")
            print(f"{self.preffered}")
            self.prefferedLabel.configure(font=("Inter", 18))
            self.prefferedLabel.pack(padx=5, pady=5)
            
            self.pricePref = CTkLabel(self.prefferedFrame, text=f"{getPrice(self.preffered)} ({getPriceIncrease(self.preffered)}%)")
            self.pricePref.configure(font=("Inter", 12))
            self.pricePref.pack()
        else:
            print('Not either')
            self.prefferedLabel = CTkLabel(self.prefferedFrame, text="Inconclusive")
            self.prefferedLabel.pack(padx=5, pady=5)
        
        self.prefferedFrame.pack(padx=100, pady=20)