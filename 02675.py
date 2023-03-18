t = int(input())

result = []
for i in range(t):
    r, s = map(str, input().split())
    r = int(r)
    list = list(s)
    for j in list:
        print(j*r, end="")
    print()
    del list
