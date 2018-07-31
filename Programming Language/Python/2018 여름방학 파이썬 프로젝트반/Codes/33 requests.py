import requests

url = 'https://github.com/JaehunYoon/'

res = requests.get(url)
print(res)
print(res.text)