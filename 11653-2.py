import sys

input = sys.stdin.readline

n = int(input())

num = 2

while num != 1 and num <= (int(n ** 0.5) + 1):
    if n % num == 0:
        n = int(n / num)
        print(num)
    if n % num != 0:
        num += 1

if n != 1:
    print(n)