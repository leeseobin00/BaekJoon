# n을 입력받음
# for문을 range(n)까지 반복문 실행
# 입력 받은 값을 arr에 append함, 이때 len(입력받은 값)도 함께 넣어줌
# len에 따라서 먼저 정렬한 후, 길이가 같으면 사전 순 정렬
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    data = input()
    #if data in arr:
    #    continue
    arr.append(data)
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i, end="")