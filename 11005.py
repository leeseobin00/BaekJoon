import sys
input = sys.stdin.readline

alphabet = {'A': 10, 'B':11,'C':12,'D':13,'E':14,
            'F': 15, 'G':16,'H':17,'I':18,'J':19,
            'K': 20, 'L':21,'M':22,'N':23,'O':24,
            'P': 25, 'Q':26,'R':27,'S':28,'T':29,
            'U': 30, 'V':31,'W':32,'X':33,'Y':34,
            'Z': 35, }

alphabet_reverse = {v:k for k, v in alphabet.items()}

B, N = map(int, input().split())
B_list = []

while B >= N:
    if B%N >= 10:
        B_list.append(alphabet_reverse[B % N])
    else:
        B_list.append(B % N)
    B = int(B/N)
if B % N >= 10:
    B_list.append(alphabet_reverse[B % N])
else:
    B_list.append(B % N)

B_list.reverse()

for i in B_list:
    print(i, end="")