n, m = map(int, input().split())

list=[]

for i in range(n):
    list.append(i+1)

for x in range(m):
    i, j = map(int, input().split())
    tmp = list[i-1]
    list[i-1] = list[j-1]
    list[j-1] = tmp

for x in list:
    print(x, end=" ")