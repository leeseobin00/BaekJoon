import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
result = A
day = 1

while result < V:
    result -= B
    result += A
    day += 1

print(day)