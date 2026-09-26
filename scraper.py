import requests
from bs4 import BeautifulSoup

def getClose(ticker : str) -> float:
    
    #Use requests to get html content of Ticker's website
    url = f"https://stockanalysis.com/stocks/{ticker.lower()}/"
    response = requests.get(url)
    html = response.content
    
    