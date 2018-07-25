# 회문 판별

# temp = list(input("회문을 판별 할 단어를 넣으세요 : "))
# reverse_temp = temp.reverse()
# # print("회문입니다." if temp == temp.reverse() else "회문이 아닙니다")
# print(reverse_temp)

word = input('회문을 판별 할 단어를 넣으세요 : ')

is_palindrome = True

for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        print("회문이 아닙니다.")       # 회문이 아님
        is_palindrome = False
        break

if is_palindrome: print("회문입니다.")