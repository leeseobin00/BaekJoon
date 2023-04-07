# print()에 기본적으로 줄바꿈이 포함되어있음
# str을 입력받을 때도 띄어쓰기가 포함됨
# => 띄어쓰기가 2번 나타남
import sys
input = sys.stdin.readline

for i in range(100):
    str = input()
    str = str.replace("\n", "")
    print(str)