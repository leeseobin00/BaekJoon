# 0 9(2*5 - 1)
# 1 7(2*4 - 1)
# 2 5(2*3 - 1)
# 3 3(2*2 - 1)
# 4(5-1) 1(2*1 - 1) 10 - 5

# 3(5-2) 3 i가 6 5-6 10-6 = 4
# 2(5-3) 5 i가 7 5-7 10
# 1(5-4) 7
# 0(5-5) 9
import sys
input = sys.stdin.readline

n = int(input())

for i in range(2*n-1):
    if i < n:
        for j in range(0, i):
            print(" ", end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()
    else:
        for j in range(0, 2*(n-1) - i):
            print(" ", end="")
        for j in range(2*(i-n+1)+1):
            print("*", end="")
        print()