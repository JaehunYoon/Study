import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

rm_escape_sequence = lambda x: x.replace('\n','').replace(' ', '').replace('\t', '')

c = input("챔피언명을 영어로 입력해주세요 >> ")

url = 'http://www.op.gg/champion/'

query = url + quote(c)

res = requests.get(query)
soup = BeautifulSoup(res.text, 'lxml')

champ = soup.find('div', {'class': 'champion-stats-trend'})
win_rate = champ.find('div', {'class': 'champion-stats-trend-rate'})
print(rm_escape_sequence(win_rate.text))