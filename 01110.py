# 입력 받은 수가 10 미만이면 => ex) 6 => 06 => 66
# num * 10 + num
# 입력 받은 수가 10 이상이면 => int(n / 10) + n % 10이 더한 값
# 이때 1의 자리 수는 => (int(n / 10) + n % 10) % 10 => 새로운 수의 1의 자리 수
# num % 10 => 10의 자리 수
import sys
input = sys.stdin.readline

n = int(input())
count = 0
result = n

while True:
    if n < 10:
        n = n * 10 + n
    else:
        n = (n % 10) * 10 + (int(n / 10) + n % 10) % 10
    count += 1
    if result == n:
        print(count)
        break

