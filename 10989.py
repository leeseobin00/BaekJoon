# n을 입력받음
# 방법 1
# sorted를 통하여 정렬 후 출력함

# 방법 2
# 계수 정렬(Counting Sort) 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for i in range(n):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)