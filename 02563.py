# 2개가 다 겹칠 때 고려
# 3개가 다 겹칠 때 고려
n = int(input())

xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))

result = 100 * n

for i in range(n):
    for j in range(i):
        if abs(xy[i][0] - xy[j][0]) < 10:
            result = result - (min(xy[i][0], xy[j][0]) + 10 - max(xy[i][0], xy[j][0])) * (min(xy[i][1], xy[j][1]) + 10 - max(xy[i][1], xy[j][1]))
print(result)