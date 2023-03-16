n, m = map(int, input().split())

basket = []

for x in range(n):
    basket.append(x)

for x in range(m):
    i, j = map(int, input().split())
    basket = basket[i:j:-1]
    print(basket)