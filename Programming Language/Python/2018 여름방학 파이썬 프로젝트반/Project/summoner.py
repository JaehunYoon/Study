import requests
import tkinter
from urllib.parse import quote
from bs4 import BeautifulSoup
from func import *

def Summoner():
    url = 'http://www.op.gg/'
    user_name = input("소환사명을 입력하세요 >> ")

    query = url + "summoner/userName=" + quote(user_name)


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

    if summoner_name == []:
        print("OP.GG에 등록되지 않은 소환사입니다. 오타를 확인 후 다시 검색해주세요.")
    else:
        print(f"소환사명 : {user['summoner_name']}")

        # Solo Rank
        print(f"솔로랭크 : {user['solo_rank_tier']}", end=' ')
        if user['solo_rank_tier'] != 'Unranked':
            print(f"{user['solo_rank_point']}")
        else:
            print()
        # Flex 5 vs 5 Rank
        if user['flex_rank_tier'] != 'Unranked':
            print(f"자유 5:5 랭크 : {user['flex_rank_tier']} ", end='')
            print(f"{user['flex_rank_point']}")
        else:
            print(f"자유 5:5 랭크 : {user['flex_rank_tier']}")
    
