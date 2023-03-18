n, m = map(int, input().split())

basket = []

for x in range(n):
    basket.append(x+1)

for x in range(m):
    i, j = map(int, input().split())
    for x in range(i-1, int((i+j)/2)):
        temp = basket[int(i+j)-x-2]
        basket[int(i+j)-x-2] = basket[x]
        basket[x] = temp
print(*basket)