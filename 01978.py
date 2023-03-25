n = int(input())

num = list(map(int, input().split()))
isPrime = 0
count = 0

# for i in range(n):
#     for j in range(2, num[i]):
#         # if num[i] == 1:
#         #     continue
#         if num[i] > 1:
#             if num[i] % j == 0:
#                 count += 1
#                 continue
#             if j == num[i]-1 and count == 0:
#                 isPrime += 1
#     count = 0

for i in num:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            isPrime += 1

print(isPrime)


