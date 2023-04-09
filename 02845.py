
l, p = map(int, input().split())

people = list(map(int, input().split()))
result = []

for i in people:
    result.append(i-l*p)
print(*result)