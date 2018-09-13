import random

words = {
    'blame': '탓하다',
    'talk me out of~': '~ 못하게 말리다',
    'weird': '기묘한, 이상한 (또라이)',
    'but': '=except (~만 제외하고)',
    'lurk': '숨다, 잠복하다',
    'forbid': '금지하다',
    'journey': '여행, 여정',
    'bottom': '바닥',
    'make it': '가다, 해내다',
    'cavern': '동굴',
    'should have pp': '~했어야 했는데, ~할 걸',
    'board': '승선하다, 탑승하다',
    'armpit': '겨드랑이',
    'curse': '저주',
    'blast': '세게 치다, 강타하다',
    'smite': '세게 치다, 때리다',
    'homing beacon': '회귀 유도 장치',
    'beacon': '무선 송신 장치',
    'curly': '곱슬곱슬한',
    'take back': '취소하다, 철회하다',
    'not to mention ~': '~는 말할 것도 없고',
    'mortal': '죽을 운명의, 인간',
    'immortal': '불사의, 죽지 않는',
    'shot': '시도, 한 번 해보기',
    'bottom feeder': '밑바닥 인생',
    'wayfinding': '길찾기',
    'sidekick': '조수, 비서',
    'current': '흐름, 해류',
    'disgusting': '역겨운, 징그러운'}

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