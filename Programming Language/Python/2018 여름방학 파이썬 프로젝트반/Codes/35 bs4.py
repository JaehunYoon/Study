import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page1.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
res_f = soup.find('h1').text
print(res_f)
