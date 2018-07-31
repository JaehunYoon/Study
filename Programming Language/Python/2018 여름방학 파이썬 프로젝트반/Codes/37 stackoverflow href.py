import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
# res_f = soup.select('.summary a[class*=question-hyperlink]')

# for index, n in enumerate(res_f):
#     print(index, n.text)
    
for index, a in enumerate(soup.find_all('a', {"class": "question-hyperlink"}, href=True)):
    print(f"[{index}]")
    print(a.text)
    print(f"URL : {a['href']}")
    print()
