# 처음에는 words[0][0]
# words[1][0], words[2][0] ..
# Index가 넘어간다는 오류를 피하기 위해서 길이 비교 조건문 넣어주기

words = []

for i in range(5):
    word = input()
    words.append(list(word))

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end="")