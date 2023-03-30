# B의 값을 한자리씩 자름
# A, B, C, ... Z일 경우는 dictionay에 정수 값을 저장해둔다
alphabet = {'A': 10, 'B':11,'C':12,'D':13,'E':14,
            'F': 15, 'G':16,'H':17,'I':18,'J':19,
            'K': 20, 'L':21,'M':22,'N':23,'O':24,
            'P': 25, 'Q':26,'R':27,'S':28,'T':29,
            'U': 30, 'V':31,'W':32,'X':33,'Y':34,
            'Z': 35, }
B, N = input().split()
N = int(N)
B_list = list(B)
B_list.reverse()
result = 0

for i in range(len(B_list)):
    print(B_list[i])
    if B_list[i] in alphabet:
        print(alphabet[B_list[i]])
        result += int(alphabet[B_list[i]])*(N**i)
        print(N**i)
        print(result)
    else:
        print(B_list[i])
        result += int(B_list[i])*(N**i)
        print(N ** i)
        print(result)
print(result)