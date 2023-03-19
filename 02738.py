n, m = map(int, input().split())

arr1, arr2 = [], []
for i in range(n):
    arr1.append(list(map(int, input().split())))

for i in range(n):
    arr2.append(list(map(int, input().split())))

result = [[0 for j in range(n)] for i in range(m)]

for i in range(n):
    for j in range(m):
        #result[i][j] = arr1[i][j] + arr2[i][j]
        print(arr1[i][j] + arr2[i][j], end=" ")
    print()
#print(result)