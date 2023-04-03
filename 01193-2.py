import sys
input = sys.stdin.readline

n = int(input())

# 분수의 개수 계산
i = 1
while n > i:
    n -= i # n-1, n-1-2, n-1-2-3, n-1-2-3-4, ...
    i += 1 # 2, 3, 4, ...

# 분수 찾기
if i % 2 == 1:  # 홀수 번째 줄
    numerator = i - n + 1
    denominator = n
else:  # 짝수 번째 줄
    numerator = n
    denominator = i - n + 1

print(f"{numerator}/{denominator}")
