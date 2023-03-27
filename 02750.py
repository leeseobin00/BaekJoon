# n을 입력받음
# for문을 통하여 range(n)까지 반복문을 돌림
# 각각의 element들을 append함
# sorted를 통하여 정렬된 list를 return 받은 후 출력
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
sorted_arr = sorted(arr)
for i in sorted_arr:
    print(i)
