# n, k를 입력받음
# element들을 list에 넣음 map(int, input().split())
# sorted()를 통하여 정렬 후 2번째 원소를 출력함
import sys
input = sys.stdin.readline

N, k = map(int, input().split())

arr = list(map(int, input().split()))
sorted_arr = sorted(arr, reverse=True)
print(sorted_arr[k-1])