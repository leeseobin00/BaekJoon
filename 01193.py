# 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → …
# 분모와 분자의 합 2 : 1개 -> sum이 짝수
# 분모와 분자의 합 3 : 2개 -> sum이 홀수일 때 분자가 1부터 시작
# 분모와 분자의 합 4 : 3개 -> sum이 짝수일 때 분자가 sum-1부터 시작
# 분모와 분자의 합 5 : 4개 -> sum이 홀수일 때 분자가 1부터 시작
import sys
input = sys.stdin.readline

n = int(input())
fraction = []

molecular = 1
denominator = 1
sum = 2

for i in range(n):
    for j in range(i+1):
        if len(fraction) > n:
            break
        if sum % 2 == 0:
            molecular = sum - denominator
            fraction.append(str(molecular) + "/" + str(denominator))
            denominator += 1
        else:
            denominator = sum - molecular
            fraction.append(str(molecular) + "/" + str(denominator))
            molecular += 1
    sum += 1
print(fraction[n-1])