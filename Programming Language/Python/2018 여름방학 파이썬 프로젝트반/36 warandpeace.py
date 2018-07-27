import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/warandpeace.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

res_f = soup.select('span[class*=green]')

for index, n in enumerate(res_f):
    print(index + 1, n.text)

'''
nameList = soup.find_all("span",{"class": "green"})

for name in nameList:
    print(name.get_text())
'''
