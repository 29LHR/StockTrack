from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkFrame, StringVar, CTkRadioButton
import customtkinter as tk
import json

class setup():
    def __init__(self):
        #Initialise App
        self.root = tk.CTk()
        self.root.title("StockTrack Installer")
        
        #Create searches.txt
        with open("searches.txt", "w") as f:
            f.write("")
        
        self.__createGui()

    def __createGui(self):
        title = CTkLabel(self.root, text="StockTrack Installer")
        title.configure(font=("Inter", 20))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        nameLbl = CTkLabel(self.root, text="Name: ").grid(row=1, column=0, padx=5, pady=5)
        self.name = CTkEntry(self.root)
        self.name.grid(row=1, column=1, padx=5, pady=5)
        
        #Add favStocks entries
        self.favStocks = []
        self.favStocksFrame = CTkFrame(self.root)
        for i in range(3):
            self.createFavStock()
        self.favStocksFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=5)
        addBtn = CTkButton(self.root, text="+", command= self.createFavStock)
        addBtn.grid(row=3, column=0, columnspan=2, sticky="nsew")
        
        self.addDate() #Add date type radio
        
        #Add Exit Button
        exit = CTkButton(self.root, text="Done", command=self.exit)
        exit.grid(row=5, column=0, columnspan=2, sticky="nsew")
    
    def createFavStock(self):
        #Calculate i
        i = len(self.favStocks)
        
        #Create GUI
        favStockLbl = CTkLabel(self.favStocksFrame, text=f"Favourite Stock {i+1}: ").grid(row=(0+i), column=0, padx=5, pady=5)
        self.favStocks.append(CTkEntry(self.favStocksFrame, placeholder_text="Enter ticker"))
        self.favStocks[-1].grid(row=(0+i), column=1, padx=5, pady=5)
    
    def addDate(self):
        dateFrame = CTkFrame(self.root)
        dateFrame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.dateType = StringVar(dateFrame)
        dateLbl = CTkLabel(dateFrame, text="Date Type: ").grid(row=0, column=0, padx=5, pady=5)
        gbr = CTkRadioButton(dateFrame, text="GBR", variable=self.dateType, value="GBR").grid(row=0, column=1, padx=5, pady=5)
        usa = CTkRadioButton(dateFrame, text="USA", variable=self.dateType, value="USA").grid(row=0, column=2, padx=5, pady=5)
    
    def exit(self):
        data = {}
        data["name"] = self.name.get()
        print(data["name"])
        data["fav_stocks"] = [entry.get() for entry in self.favStocks]
        print(data["fav_stocks"])
        date = self.dateType.get()
        print(date)
        if date == "GBR":
            data["date"] = "dd/mm/yyyy"
        else:
            data["date"] = "mm/dd/yyyy"
        print(data["date"])
        
        with open("__setup.json", "w") as f:
            json.dump(data, f, indent=4)
        
        print("Closing Setup Wizard")
        self.root.destroy()
        

installer = setup()
installer.root.mainloop()