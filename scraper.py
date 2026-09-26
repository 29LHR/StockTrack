import requests
from bs4 import BeautifulSoup
from typing import Literal

stockVals = ["open", "previous close", "analysts"]

def getVal(ticker : str, val : str) -> str:
    if val.lower() not in stockVals:
        return "Invalid Stock Value"
    #Use requests to get html content of Ticker's website
    url = f"https://stockanalysis.com/stocks/{ticker.lower()}/"
    
    try:
        response = requests.get(url)
        html = response.content
        print("HTML Content Aquired")
    except Exception as e:
        print(str(e))
        return 0.00
    
    soup = BeautifulSoup(html, 'html.parser')
    
    tds = soup.find_all('td')
    tdVals = [td.text for td in tds]
    
    for i in range(len(tdVals)):
        if tdVals[i].lower() == val.lower():
            print(f"Found {val} Data")
            return str(tdVals[i+1])