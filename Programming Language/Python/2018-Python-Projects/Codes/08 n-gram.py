word = list(input())  # iamveryhungry

for i in range(len(word)-2):
    print(word[i], word[i+1], word[i+2], sep='')