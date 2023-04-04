# arr에 값을 하나씩 저장
# 0일 겨우 len(arr)-1을 없앰 => 0으로 만듬
# 지우는 값은 remove에 저장해놓기
import sys
input = sys.stdin.readline

t = int(input())

arr = []
remove = 0

for i in range(t):
    n = int(input())
    if n == 0:
        # while arr[remove] == 0:
        #     remove -= 1
        arr[remove] = 0
        remove -= 1
        print(arr)
        print(remove)
    else:
        arr.append(n)
        remove += 1
        print(arr)
        print(remove)
print(sum(arr))

