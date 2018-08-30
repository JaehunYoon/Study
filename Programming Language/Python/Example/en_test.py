import random

words = {
    'emerge': '나타나다, 출현하다',
    'possess': '소유하다',
    'daring': '대담한, 위험한',
    'voyage': '여행, 여행하다',
    'demigod': '반신반인',
    'warrior': '전사',
    'trickster': '사기꾼',
    'shape shift': '변신하다, 형태를 바꾸다',
    'crumble': '빻다, 부수다, 가루로 만들다',
    'give birth to ~': '낳다',
    'confront': '직면하다, 마주하다',
    'sought': 'seek의 과거형',
    'demon': '악령, 악마',
    'chase away': '쫓아내다, 뒤쫓다',
    'drain': '배수시키다, 고갈시키다',
    'devour': '걸신들린 듯 먹다',
    'inescapable': '피할 수 없는',
    'reef': '암초',
    'restore': '복원하다, 회복시키다',
    'sacred': '신성한',
    'chief': '추장, 부족장',
    'harvest': '수확하다, 수확물',
    'husk': '껍질을 벗기다',
    'diseased': '병든',
    'grove': '숲, 수풀',
    'suit': '맞다, 알맞다, 적합하다',
    'lagoon': '석호, 작은 늪',
    'windward': '바람 불어오는 쪽의',
    'shallow': '얕은, 얕은 곳',
    'channel': '해협',
    'bait': '미끼',
    'council': '자문 위원회',
    'endanger': '위험에 빠뜨리다',
    'be hard on ~': '엄하게 굴다'}

check = True
count = 0

while True:
    if len(words) == 0:
        break

    if check == True:
        temp = random.choice(list(words.items()))
        check = False
        print(temp[1])
    
    question = input("I think.. >> ")

    if question == temp[0]:
        print(f"정답! {len(words)-1}문제 남았습니다!")
        check = True
        count = 0
        words.pop(temp[0])
    elif question != temp[0]:
        print("다시 생각해~")
        count += 1
    
    if count == 5:
        print(f"힌트 드릴게요.. 첫 번째 글자는 {temp[0][0]}입니다.")
    if count == 7:
        print(f"아직도 못 맞추셨어요? 단어의 길이는 {len(temp[0])}입니다.")
    if count == 10:
        print(f"안타깝네요.. 정답은 {temp[0]} 였습니다.")
        check = True

    if question == "exit":
        print("Bye~~")
        exit(1) 
    
print("끝!!")