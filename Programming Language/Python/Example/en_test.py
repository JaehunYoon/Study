import random

words = {
    'visible': 'able to be seen',  # 보이는
    'launch': 'to send into space',  # 발사하다
    'optical': 'connected with light and seeing',  # 시각의, 광학의
    'image': 'a picture',  # 사진
    'cancel out': 'to balance something out so that it has no effect',  # 상쇄되다, 상쇄시키다
    'artificial': 'created by people; not occurring naturally',  # 인공의
    'hemisphere': 'one half of the Earth',  # 반구
    'detectors': 'instruments used for finding and measuring things',  # 탐지기
    'bulge': 'to swell up higher than the surrounding area',  # 부풀다
    'proportion': 'a part',  # 부분
    'drill': 'to make a hole',  # 구멍 뚫다
    'mine': 'to dig a mineral (coal, gold etc) out of the ground',  # 캐다
    'remains': 'parts of an animal left after it has died',  # 유해, 유골
    'dependent on': 'needing something in order to survive',  # 의존하는
    'depleted': 'reduced in amount or size',  # 감소된, 감축된
    'mold': 'v. to change the shape of something to fit a pattern or space -syn. shape',  # 형상짓다, 틀에 넣어 만들다
    'unique': 'adj. unusual, not typical; the only one -syn. singular, unequaled',  # 희귀한, 회소성 있는
    'rich': 'adj. very creamy or sweet -syn. flavorful -ant. tasteless',  # 영양분이 풍부한, 맛있는
    'be associated with': 'idiom. to be connected with or to be related to -syn. be linked with',  # 연관되다
    'relaxation': 'n. refreshment of body or mind; recreation -syn. fun, amusement, pleasure',  # 긴장 풀기
    'consume': 'v. to eat or drink something -syn. eat up',  # 먹다, 소비하다
    'treat': 'n. special delight or pleasure, often food -syn. snack, surprise',  # 대접 (음식 등)
    'raw': 'adj. uncooked or in the most basic form -syn. uncooked, natural -ant. cooked',  # 생, 날것의
    'rare': 'adj. being available in small amounts -syn. uncommon exceptional',  # 드문, 희귀한
    'valuable': 'adj. high quality, value, or importance -syn. precious -ant. worthless',  # 가치 있는
    'bitter': 'adj. a harsh or disagreeeable taste; not sour, sweet, or salty -syn. distasteful',  # 쓴 맛의
    'present': 'v. to formally give something to someone -syn. give, offer',  # 제시하다, 발표하다
    'luxury': 'adj. expensive, rich, or hard to get',  # 사치스런
    'method': 'n. a procedure, technique, or way of doing something -syn. way, system',  # 방법
    'mass-produce': 'v. to make products in large quantities, usually by machinery',  # 대량생산하다
    'warn': 'v. to inform, give notice, or advise to be careful -syn. caution, alert',  # 경고하다, 알리다
    'moderately': 'adv. to do something within reasonable limits, not extreme or excessive',  # 적당하게, 알맞게
    'influence': 'n. the effect of one thing or person on another -syn. persuasion, control',  # 영향
    'prevent': 'v. to keep from happening -syn. avoid',  # 예방하다, 방지하다
    'individually': 'adv. separately, not together in a group -syn. independently, alone',  # 개별적으로
    'demanding': 'adj. needing a lot of ability, effort, or skill -syn. hard, challenging',  # 힘든, 벅찬
    'endurance': 'n. the ability to continue doing something difficult or painful -syn. perseverance',  # 지구력, 인내력
    'stamina': 'n. physical or mental energy and strength that allows somebody to do something for a long time',  # 힘, 에너지
    'competitive': 'adj. trying very hard to be more successful than other people or businesses',  # 경쟁이 심한, 경쟁력있는
    'athlete': 'n. a person trained to compete in sports -syn. sportsman',  # 운동선수
    'emerge': 'v. to appear or come out from somewhere'}  # 나타나다

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
        words.pop(temp[0])
        check = True

    if question == "exit":
        print("Bye~~")
        exit(1) 
    
print("끝!!")