n, m = map(int, input().split())

list = [0]*(n)

for x in range(m):
    i, j, k = map(int, input().split())
    for y in range(i-1, j):
        list[y] = k

for x in list:
    print(x, end = " ")