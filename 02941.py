# 크로아티아 알파벳을 배열로 정의함
# 단어를 입력받음

# 방법 1
# 입력 받은 문자열 내에서 croatia 수가 있는지 찾는다.
# 문자열을 찾으면 그 값을 문자열 내에서 제거한다.

# 방법 2
# 입력 받은 문자열을 가장 작은 단위로 쪼갠다.
# 쪼갠 작은 단위를 배열에 저장

croatia = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
word = input()

word_frag = []
i = 0
while i < len(word):
    if word[i:i+2] in croatia:
        word_frag.append(word[i:i+2])
        i = i + 1
    elif word[i:i+3] in croatia:
        word_frag.append(word[i:i + 3])
        i = i + 2
    else:
        word_frag.append(word[i])
    i = i+1

print(len(word_frag))