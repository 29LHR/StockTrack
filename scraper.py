import requests
from bs4 import BeautifulSoup
from datetime import date

stockVals = ["open", "previous close", "analysts", "est. earnings"]

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
        
def getEstEarn(ticker : str) -> date:
    def moToNo(month : str) -> int:
        month = month.lower()
        if month == "jan" or month == "january":
            return 1
        elif month == "feb" or month == "february":
            return 2
        elif month == "mar" or month == "march":
            return 3
        elif month == "apr" or month == "april":
            return 4
        elif month == "may":
            return 5
        elif month == "jun" or month == "june":
            return 6
        elif month == "jul" or month == "july":
            return 7
        elif month == "aug" or month == "august":
            return 8
        elif month == "sep" or month == "sept" or month == "september":
            return 9
        elif month == "oct" or month == "october":
            return 10
        elif month == "nov" or month == "november":
            return 11
        elif month == "dec" or month == "december":
            return 12

    raw = getVal(ticker, "est. earnings")
    raw = raw.replace(",","")
    raw = raw.replace(",","").split(" ")
    return date(int(raw[2]),moToNo(raw[0]),int(raw[1]))
    