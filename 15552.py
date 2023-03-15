import sys

n = int(sys.stdin.readline().rstrip())
result = []

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    result.append(a + b)

for i in result:
    print(i)