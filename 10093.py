import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if b < a:
    tmp = b
    b = a
    a = tmp

# a == b일 때 b-a-1 = -1이므로 이때를 고려해줘야 함
if b-a-1 < 0:
    print(0)
else:
    print(b-a-1)

for i in range(a+1, b):
    print(i, end=" ")