import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    sum = 0
    for j in range(1, n+1, 2):
        sum += j
    print(sum)