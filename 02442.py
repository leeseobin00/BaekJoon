# 공백
# 4(n-1) 1(0*2+1)
# 3 3(1*2+1)
# 2 5(2*2+1)
# 1 7(3*2+1)
# 0 9(4*2+1)
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    for j in range(n-i-1, 0, -1):
        print(" ", end="")
    for j in range(0, 2*i+1):
        print("*", end="")
    print()