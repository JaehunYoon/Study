'''
- 첫 월급 300만원
- 매달 월급의 50% 저축 (기간 : 1년)
- 정기예금 금리 2.4%
'''

money = 3000000  # 월급
saving = money * 0.5  # 정기예금에 저축할 돈
bank = saving * 0.024  # 정기예금 금리
result = 0  # 장기예금 만기 금액을 저장할 변수

for i in range(12):
    result += saving + bank

print("{:,}".format(int(result)))
