import requests
from bs4 import BeautifulSoup
import re
import datetime
import time
keyvalue = {}
VS = 'USDJPY'
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
print(allcurrency)
inptType = input('ENTER THE CURRENCY TYPE : ')
VS = keyvalue[inptType]
while True:
# print('utc = ', time.gmtime())
    url = 'https://finance.yahoo.com/quote/'+VS+'=X'
    # url = 'https://finance.yahoo.com/quote/USDJPY=X/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    currency = re.findall('quote/(.*?)=', str(url))
    rate = re.findall(r'data-reactid="14">(.*?)</span>', str(soup))
    timeValue = re.findall(r'As of  (.*?) GMT. Market open.</span>', str(soup))
    daysRange = re.findall(r'data-test="DAYS_RANGE-value">(.*?)</td></tr>', str(soup))
    bid = re.findall(r'<span class="Trsdu\(0.3s\)" data-reactid="26">(.*?)</span></td></tr>', str(soup))
    ask = re.findall(r'data-test="ASK-value"><span class="Trsdu\(0.3s\)" data-reactid="42">(.*?)</span>', str(soup))
    datetimeVal = 'UTC:'+str(time.localtime().tm_year)+':'+str(time.localtime().tm_mon)+':'+str(time.localtime().tm_mday)+':'+str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec)
    curencyString = currency[0]
    currentRate = rate[0]
    utcTime = timeValue[0]
    daysRangeValue = daysRange[0]
    bidValue = bid[0]
    askValue = ask[0]
    allInOne = str(datetimeVal)+'-'+str(curencyString)+'-'+str(currentRate)+'-'+str(utcTime)+'-'+str(daysRangeValue)+'-'+str(bidValue)+'-'+str(askValue)
    print(allInOne)
    fileName = curencyString+'.txt'
    fw = open(fileName, 'a')
    fw.write(str(allInOne))
    fw.write('\n')
    fw.close()
    # print('time = ', time.localtime().tm_hour,':',time.localtime().tm_min,':',time.localtime().tm_sec)
    # print(currency[0])
    # print('rate = ', rate[0])
    # print('time = ', timeValue[0])
    # print('days Range = ', daysRange[0])
    # print('bid = ', bid[0])
    # print('ask = ', ask[0])
    # print('-----------------------------------')
    time.sleep(0.01)