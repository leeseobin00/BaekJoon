total = [1, 1, 2, 2, 2, 8]

list = list(map(int, input().split()))

for i in range(len(total)):
    print(total[i] - list[i], end=" ")