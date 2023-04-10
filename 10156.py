
lst = list(map(int, input().split()))

if lst[0] * lst[1] -lst[2] <= 0:
    print(0)
else:
    print(lst[0] * lst[1] -lst[2])