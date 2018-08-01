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
    
    user = {}

    # Solo Rank
    solo_rank_tier = soup.select('.SummonerRatingMedium span[class*=tierRank]')
    solo_rank_point = soup.select('.SummonerRatingMedium span[class*=LeaguePoints]')

    # Flex 5 vs 5 Rank
    flex_rank_tier = soup.select('.TierRank div[class*=TierRank]')
    flex_rank_point = soup.select('.SummonerRatingLine div[class*=leaguePoints]')

    if summoner_name == []:
        return None
    else:
        user['summoner_name'] = add_dict(summoner_name)
        user['solo_rank_tier'] = add_dict(solo_rank_tier)
        if user['solo_rank_tier'] == 'Unranked':
            user['solo_rank_point'] = None
        else:
            user['solo_rank_point'] = rm_escape_sequence(add_dict(solo_rank_point))
        user['flex_rank_tier'] = check_unranked(flex_rank_tier)
        if user['flex_rank_tier'] == 'Unranked':
            user['flex_rank_point'] = None
        else:
            user['flex_rank_point'] = rm_escape_sequence(add_dict(flex_rank_point))
        return user

def get_most_champion(get_user):
    url = 'http://www.op.gg/summoner/champions/userName='
    user_name = get_user
    query = url + quote(user_name)
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'lxml')

    most = soup.find_all('td', {'class': 'ChampionName Cell'})

    return most

def add_dict(lists):
    if len(lists) > 1:
        temp = ""
        for user in lists:
            temp += " "
            temp += user.text
        return temp
    else:
        for user in lists:
            return user.text

def check_unranked(lists):
    if lists == []:
        return "Unranked"
    else:
        return add_dict(lists)

rm_escape_sequence = lambda x: x.replace('\n','').replace(' ', '').replace('\t', '')