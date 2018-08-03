import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

url = "http://www.op.gg/champion/mordekaiser/statistics"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

test = soup.find('h1', {'class': 'SectionHeadLine'})

print(test)