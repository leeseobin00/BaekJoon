# 단어의 개수 n을 입력 받는다
# n만큼 for 반복문을 돌릴 것이다.

# 첫번째 arr의 값을 새로운 배열에 저장해놓는다.
# 다음 arr의 값이 앞의 arr의 값과 같을 경우 continue
# 같지 않을 경우에는 새로운 배열에 다시 저장 해놓는다.
# 같지 않을 경우 새로운 배열에 값이 있는지 확인한다.

n = int(input())

alpha = []
isGroup = 0

for i in range(n):
    word = input()
    word_list = list(word)
    for j in range(len(word_list)):
        if j == 0:
            alpha.append(word_list[j])
        else:
            if word_list[j] != word_list[j-1]:
                if word_list[j] in alpha:
                    break
                else:
                    alpha.append(word_list[j])
        if j == len(word_list)-1:
            isGroup += 1
    alpha.clear()
    word_list.clear()
print(isGroup)
