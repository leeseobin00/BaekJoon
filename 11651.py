# n을 입력받음
# for문을 range(n)까지 반복문 실행
# xy.sort(key=lambda x:(x[1], x[0]))
import sys
input = sys.stdin.readline

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
xy.sort(key=lambda x:(x[1], x[0]))
for i in xy:
    print(i[0], i[1])