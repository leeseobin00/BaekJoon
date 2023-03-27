# n을 입력받음
# for문을 range(n)까지 반복문 실행

import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(set(x))
#for i in x:
#    print(sorted_x.index(i), end=" ")

dic = {sorted_x[i] : i for i in range(len(sorted_x))}
for i in x:
    print(dic[i], end = ' ')
