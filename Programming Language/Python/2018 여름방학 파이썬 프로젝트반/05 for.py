# 60점 이상일 때 합격 메시지 출력하기

marks = [90, 25, 67, 50, 70]
num = 1

# for mark in marks:
#     print(f"{num}번 학생은 합격입니다" if mark >= 60 else f"{num}번 학생은 불합격입니다")
#     num += 1


# enumerate()

for x, y in enumerate(marks):
    print(f"{x+1}번 학생은 합격입니다" if y >= 60 else f"{x+1}번 학생은 불합격입니다")
