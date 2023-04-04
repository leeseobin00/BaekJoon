import sys
input = sys.stdin.readline

count = 1

while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2 == 0:
        n2 = n1 / 2
        n3 = 3 * n2
        n4 = int(n3 / 9)
        print(str(count) + '. even ' + str(n4))
    else:
        n2 = (n1 + 1) / 2
        n3 = 3 * n2
        n4 = int(n3 / 9)
        print(str(count) + '. odd ' + str(n4))
    count += 1