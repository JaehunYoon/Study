import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
movie_rank = soup.select('.title div[class*=tit3]')

for index, n in enumerate(movie_rank):
    temp = n.text.replace('\n', '') 
    print(f"{index+1}위 : {temp}")
