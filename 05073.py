len = []

while True:
    len = list(map(int, input().split()))
    if len == [0,0,0]:
        break
    if max(len) < sum(len)-max(len):
        if len[0] == len[1] == len[2]:
            print('Equilateral')
        elif len[0] == len[1] or len[1] == len[2] or len[0] == len[2]:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')
    len.clear()