import requests
from bs4 import BeautifulSoup
import re
import datetime
import time

def urlMaker(currencyName):
    url = 'https://finance.yahoo.com/quote/'+currencyName+'=X'
    # url = 'https://finance.yahoo.com/quote/USDJPY=X/'
    return url

def render(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def regexRenderedData(soup, currency):
    rate = re.findall(r'data-reactid="14">(.*?)</span>', str(soup))
    timeValue = re.findall(r'As of  (.*?) GMT. Market open.</span>', str(soup))
    daysRange = re.findall(r'data-test="DAYS_RANGE-value">(.*?)</td></tr>', str(soup))
    bid = re.findall(r'<span class="Trsdu\(0.3s\)" data-reactid="26">(.*?)</span></td></tr>', str(soup))
    ask = re.findall(r'data-test="ASK-value"><span class="Trsdu\(0.3s\)" data-reactid="42">(.*?)</span>', str(soup))
    datetimeVal = 'UTC:'+str(time.localtime().tm_year)+':'+str(time.localtime().tm_mon)+':'+str(time.localtime().tm_mday)+':'+str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec)
    curencyString = currency
    currentRate = rate[0]
    daysRangeValue = daysRange[0]
    bidValue = bid[0]
    askValue = ask[0]
    allInOne = str(datetimeVal)+'-'+str(curencyString)+'-'+str(currentRate)+'-'+str(daysRangeValue)+'-'+str(bidValue)+'-'+str(askValue)
    return allInOne

keyvalue = {}
allcurrency = '''
    1 GBPNZD
    2 GBPUSD
    3 GBPAUD
    4 EURGBP
    5 GBPCAD
    6 GBPJPY
    7 GBPCHF
    8 EURGBP
    9 EURUSD
    10 USDJPY
    11 EURJPY
    12 EURGBP
    13 AUDUSD
    14 EURCHF
    15 EURCHF
    16 EURAUD
    17 CADJPY
    18 EURCAD
    '''
individualcurrency = allcurrency.split()
for i in range(0,len(individualcurrency),2):
    keyvalue[individualcurrency[i]] = individualcurrency[i+1]

while True:
    for i in keyvalue:
        # print(keyvalue[i])
        url = urlMaker(keyvalue[i])
        soup = render(url)
        allInOne = regexRenderedData(soup, keyvalue[i])
        
        
        print(allInOne)
    time.sleep(0.01)