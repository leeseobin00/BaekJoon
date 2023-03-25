x = []
y = []
result = []

for i in range(3):
    x_point, y_point = map(int, input().split())
    x.append(x_point)
    y.append(y_point)

for i in range(3):
    if x.count(x[i]) == 1:
        # result.append(x[i])
        x_result = x[i]
    if y.count(y[i]) == 1:
        # result.append(y[i])
        y_result = y[i]
# print(str(result[0])+ " "+ str(result[1]))
print(x_result, y_result)