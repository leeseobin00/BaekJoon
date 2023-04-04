import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    print('Pairs for '+str(n)+': ', end="")
    for j in range(1, int(n/2) + 1):
        r = n - j
        if j != r:
            if j != 1:
                print(', ', end="")
            print(j, r, end="")
    print()