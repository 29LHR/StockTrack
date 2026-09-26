import requests
from bs4 import BeautifulSoup
from datetime import date

#Known Variables
stockVals = ["name", "open", "previous close", "analysts", "est. earnings"]

def tickerToName(ticker : str, **kwargs):
    if "html" in kwargs.keys():
            html = kwargs["html"]
    else:
        html = getHTML(ticker)
    
    #Find the title element and return the text within
    soup = BeautifulSoup(html, 'html.parser')
    h1 = str(soup.find("h1").text)
    return ' '.join(h1.split(' ')[:-1])
    
    
def getHTML(ticker : str):
    #Use requests to get html content of Ticker's website
        url = f"https://stockanalysis.com/stocks/{ticker.lower()}/"
        
        try:
            response = requests.get(url)
            html = response.content
            print("HTML Content Aquired")
            return html
        except Exception as e:
            print(str(e))

def getVal(ticker : str, val : str, **kwargs) -> str:
    val = val.lower()
    if val.lower() not in stockVals:
        return "Invalid Stock Value"
    
    #Not the right function for Name value therefore redirect
    if val.lower() == "name" and "html" in kwargs.keys():
        return tickerToName(ticker, html=kwargs["html"])
    
    if "html" in kwargs.keys():
        html = kwargs["html"]
    else:
        html = getHTML(ticker)
    soup = BeautifulSoup(html, 'html.parser')
    
    #Catch name val if not with html
    if val == "name":
        return tickerToName(ticker)
        
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

    raw = getVal(ticker, "est. earnings") #get raw data
    
    #turn raw string into a useable date
    raw = raw.replace(",","")
    raw = raw.replace(",","").split(" ")
    return date(int(raw[2]),moToNo(raw[0]),int(raw[1]))

def buyComp(ticker1 : str, ticker2 : str) -> str:
    t1html, t2html = getHTML(ticker1), getHTML(ticker2)
    t1soup, t2soup = BeautifulSoup(t1html, "html.parser"), BeautifulSoup(t2html, "html.parser")
    
    #1 Get analyst vals
    t1anal, t2anal = getVal(ticker1, "analysts", html=t1html).lower(), getVal(ticker2, "analysts", html=t2html).lower()
    if t1anal == "strong buy" and t2anal != "strong buy":
        return f"{getVal(ticker1, "name", html=t1html)} ({ticker1})"
    elif t1anal != "strong buy" and t2anal == "strong buy":
        return f"{getVal(ticker2, "name", html=t1html)} ({ticker2})"
    else:
        if t1anal == "buy" and t2anal != "buy":
            return f"{getVal(ticker1, "name", html=t1html)} ({ticker1})"
        elif t1anal != "buy" and t2anal == "buy":
            return f"{getVal(ticker2, "name", html=t1html)} ({ticker2})"
        else:
            print("Analysts were inconclusive")
            
    #2 Find User Priority
    