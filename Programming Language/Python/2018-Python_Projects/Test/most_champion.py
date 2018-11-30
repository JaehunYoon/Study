import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

url = 'http://www.op.gg/summoner/champions/userName='
user_name = input("소환사명을 입력하세요 >> ")
query = url + quote(user_name)
res = requests.get(query)
soup = BeautifulSoup(res.text, 'lxml')

# most = soup.select('.Body tr[class*=Row]')
most = soup.find_all('td', {'class': 'ChampionName Cell'})

for index, champion in enumerate(most):
    print(f"Most {index+1} : {champion['data-value']}")