import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

print(sum(num)-max(num)-min(num))