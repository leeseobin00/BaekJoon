# for문을 통하여 range(5)까지 반복문을 돌림
# arr에 append 해놓음
# mean()을 통하여 평균 값을 구함
# sorted()를 통하여 정렬한 후 중간값을 구함
import sys
input = sys.stdin.readline

arr = []

for i in range(5):
    arr.append(int(input()))

sorted_arr = sorted(arr)

print(int(sum(arr) / len(arr)))
print(sorted_arr[2])