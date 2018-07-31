import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def get_username(get_user):
    url = 'http://www.op.gg/summoner/userName='
    user_name = get_user
    query = url + quote(user_name)
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'lxml')
    summoner_name = soup.select('.Information span[class*=Name]')
	
    if summoner_name == []:
        return None
    else:
        return add_dict(summoner_name)

def add_dict(lists):
    for user in lists:
        return user.text

def check_unranked(lists):
    if lists == []:
        return "Unranked"
    else:
        return add_dict(lists)

rm_escape_sequence = lambda x: x.replace('\n','').replace(' ', '').replace('\t', '')