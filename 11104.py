# 0 번째 * 2의 0승
# 1 번째 * 2의 1승

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    binary = list(input())
    binary.reverse()
    sum = 0
    for i in range(1, len(binary)):
        sum += (int(binary[i]) * (2**(i-1)))
    print(sum)