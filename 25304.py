total_price = int(input())
count = int(input())
sum = 0

for i in range(count):
    price, num = input().split()
    price = int(price)
    num = int(num)
    sum += (price * num)

if total_price == sum:
    print("Yes")
else:
    print("No")