num = list(map(int, input().split()))

print(min(abs(num[0]-num[2]), abs(num[1]-num[3]), num[0], num[1]))