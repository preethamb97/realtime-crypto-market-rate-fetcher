import requests
from bs4 import BeautifulSoup
import re
url = 'https://coinmarketcap.com/all/views/all/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# fw = open('b.txt', 'w')
# fw.write(str(soup.encode("utf-8")))
soupData = soup.encode("utf-8")
jsonData = re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', str(soupData))
print(jsonData)
# fw.write(str(jsonData))
# fw.close()