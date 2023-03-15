result = []

while True:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    result.append(a+b)

for i in result:
    print(i)