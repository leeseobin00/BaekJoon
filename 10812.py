n, m = map(int, input().split())

basket = []
tmp = []

for x in range(n):
    basket.append(x+1)

for x in range(m):
    i, j, k = map(int, input().split())
    for y in range(k-1, j):
        tmp.append(basket[y])
    for y in range(i-1, k-1):
        tmp.append(basket[y])
    for y in range(i-1, j):
        basket[y] = tmp[y-(i-1)]
    tmp.clear()
print(*basket)