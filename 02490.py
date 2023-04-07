import sys
input = sys.stdin.readline

for i in range(3):
    n = list(map(int, input().split()))

    if sum(n) == 3:
        print('A')
    elif sum(n) == 2:
        print('B')
    elif sum(n) == 1:
        print('C')
    elif sum(n) == 0:
        print('D')
    else:
        print('E')

