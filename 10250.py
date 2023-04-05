# 3개의 수를 입력 받음
# h, w
# 먼저 h = 1 ~ h, w = 1
# h = 1 ~ h, w = 2
# __ __ 앞에 __ 는 n % h
# __ __ 뒤에 __ 는 n / h + 1
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    if num[0] * num[1] >= num[2]:
        # 나머지가 0인 경우를 고려하지 않았다!
        if num[2] % num[0] == 0:
            room = 100 * num[0] + int(num[2] / num[0])
        else:
            room = 100 * (num[2] % num[0]) + int(num[2] / num[0]) + 1
        print(room)
