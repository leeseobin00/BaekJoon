n = int(input())

scores = list(map(int, input().split()))
sum = 0

for score in scores:
    sum += score / max(scores) * 100

print(sum / n)