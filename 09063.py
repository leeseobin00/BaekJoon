n = int(input())

x = []
y = []
for i in range(n):
    x_point, y_point = map(int, input().split())
    x.append(x_point)
    y.append(y_point)

print((max(x)-min(x))*(max(y)-min(y)))