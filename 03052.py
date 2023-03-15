list = []
remainder = []

for i in range(10):
    list.append(int(input()))
    remainder.append(list[i] % 42)

remainder = set(remainder)
print(len(remainder))