# n을 입력 받음
# for문을 통하여 range(n)까지 반복문
# element를 append 시킴
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
for i in sorted(arr):
    print(i)