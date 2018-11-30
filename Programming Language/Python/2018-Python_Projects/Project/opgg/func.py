import requests
from string import ascii_letters
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

def get_champion_winrate(get_user):
    url = 'http://www.op.gg/summoner/champions/userName='
    user_name = get_user
    query = url + quote(user_name)
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'lxml')

    win_rate = soup.select('.WinRatioGraph span[class*=WinRatio]')

    return win_rate

def get_champion_kda(get_user):
    url = 'http://www.op.gg/summoner/champions/userName='
    user_name = get_user
    query = url + quote(user_name)
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'lxml')

    kda = soup.select('.KDA div[class*=KDA]')

    return kda

def get_kda_average(get_user):
    url = 'http://www.op.gg/summoner/champions/userName='
    user_name = get_user
    query = url + quote(user_name)
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'lxml')

    average = soup.select('.Row td[class*=KDA]')

    return average

def get_champion_average_winrate(champion):
    url = 'http://www.op.gg/champion/'
    query = url + quote(champion)
    
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'lxml')

    if soup.find('h1', {'class': 'SectionHeadLine'}) != None:
        return "고인이여서 확인이 불가능합니다."
    else:
        champ = soup.find('div', {'class': 'champion-stats-trend'})
        win_rate = champ.find('div', {'class': 'champion-stats-trend-rate'})

        return rm_escape_sequence(win_rate.text)

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

def remove_special_char(letter):
    temp = list(letter) # list('Zoe')
    check_ascii = ascii_letters
    removed_letter = ""

    for c in temp:
        if c in check_ascii:
            continue
        print(f"{letter}에서 {c}가 걸러졌습니다!")
        temp.remove(c)

    removed_letter = "".join(temp)

    return removed_letter

rm_escape_sequence = lambda x: x.replace('\n','').replace(' ', '').replace('\t', '')