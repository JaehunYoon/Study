'''
* 책 딕셔너리

책의 가격이 20,000원 이상인 책의 ISBN, 책 제목, 가격을 출력

'''

books = {'394039': {'title': '파이썬 코딩의 기술', 'year': 2016, 'author': '브렛 슬라킨', 'price': 21600},
         '230999': {'title': '골빈해커의 3분 딥러닝', 'year': 2017, 'author': '김진중', 'price': 19800},
         '220333': {'title': 'C언어 트레이닝', 'year': 2017, 'author': '아서 줄라이니', 'price': 16200},
         '551139': {'title': '웹 해킹 입문', 'year': 2016, 'author': '이상환', 'price': 20500},
        }

for i in books:
    if books[i]['price'] >= 20000:
        print("ISBN : {} | 책 제목 : {} | 가격 : {:,}".format(i, books[i]['title'], books[i]['price']))
