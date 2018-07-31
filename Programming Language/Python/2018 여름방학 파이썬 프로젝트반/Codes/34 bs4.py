from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page1.html'
soup = BeautifulSoup(urlopen(url), 'lxml')

res_f = soup.find_all('div')
print(res_f)