from customtkinter import CTkLabel, CTkFrame, CTkToplevel, CTkImage
from PIL import Image
from scraper import getPrice, getPriceIncrease, tickerToName, buyComp, getEstEarn
lazy import matplotlib.pyplot as plt

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
        
        self.getGraph()
        self.compGraph = CTkImage(light_image=Image.open("temp/compGraph.png"), dark_image=Image.open("temp/compGraph.png"), size=(640,480))
        self.compGraphLbl = CTkLabel(self.tl, text="", image=self.compGraph)
        self.compGraphLbl.pack(padx=30, pady=20)
    
    def getGraph(self):
        data = {
            #"time1": getEstEarn(self.ticker1),
            #"time2": getEstEarn(self.ticker2),
            "price1": getPrice(self.ticker1),
            "price2": getPrice(self.ticker2)
        }
        
        fig, axs = plt.subplots(nrows=1, ncols=2)
        #axs[0].bar(f"{self.ticker1} ({str(data["time1"])})", data["time1"], color="#367588")
        #axs[0].bar(f"{self.ticker2} ({str(data["time2"])})", data["time2"], color="#8B0000")
        axs[0].set_title("Time")
        
        axs[1].bar(f"{self.ticker1} ({str(data["price1"])})", data["price1"], color="#367588")
        axs[1].bar(f"{self.ticker2} ({str(data["price2"])})", data["price2"], color="#8B0000")
        axs[1].set_title("Price")
        fig.savefig("temp/compGraph.png")

        print(data)