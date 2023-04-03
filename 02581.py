import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

arr = []

for i in range(m, n+1):
    # i가 2보다 작을 때는 고려하지 않음
    if i < 2:
        continue
    # prime인지 아닌지를 판단하는 boolean 변수
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        # 한개라도 0으로 나누어 떨어지면 prime이 아니다.
        if i % j == 0:
            isPrime = False
            break
    # 마지막까지 prime 이 true이면 prime 수가 맞다.
    if isPrime == True:
        arr.append(i)

# arr의 길이가 0이 아니면 arr에 prime 수가 한개라도 존재한다
if len(arr) != 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
