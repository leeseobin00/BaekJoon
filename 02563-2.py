rows = 101
cols = 101
arr = [[0 for j in range(cols)] for i in range(rows)]

n = int(input())

xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))

for i in xy:
    for j in range(i[0], i[0]+10):  # 3에서 13
        for l in range(i[1], i[1]+10):  # 7에서 17
            arr[j][l] = 1

sum = 0
for i in range(cols):
    for j in range(rows):
        sum += arr[i][j]
print(sum)