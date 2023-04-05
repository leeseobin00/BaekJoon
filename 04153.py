# while True로 입력 받음
# 만약 입력 값이 0, 0, 0 이면 break
# 세개의 수를 배열로 입력 받고 => sort를 함
# 제일 큰 수의 제곱이 나머지 수들의 제곱의 합과 같으면 직각 삼각형
import sys
input = sys.stdin.readline

while True:
    num = list(map(int, input().split()))
    if num == [0, 0, 0]:
        break
    num.sort()
    if num[2]**2 == (num[0]**2 + num[1]**2):
        print("right")
    else:
        print("wrong")