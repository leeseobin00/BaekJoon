# n을 입력받음
# for문을 range(n)까지 반복문 실행
# x, y를 list안의 list로 append
# x간의 크기 비교 후 sort
# y간의 크기 비교 후 sort
import sys
input = sys.stdin.readline

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
xy.sort(key=lambda x:(x[0], x[1]))
for i in xy:
    print(i[0], i[1])