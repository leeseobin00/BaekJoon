n = int(input())
result = []

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    result.append(a+b)

for i in result:
    print(i)