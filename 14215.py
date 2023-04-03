len = list(map(int, input().split()))

if max(len) < sum(len) - max(len):
    print(sum(len))
else:
    print(2*(sum(len) - max(len))-1)