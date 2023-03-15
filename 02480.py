n1, n2, n3 = input().split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 == n2 and n2 == n3:
    prize = 10000 + n1 * 1000
elif n1 == n2 or n1 == n3:
    prize = 1000 + n1 * 100
elif n2 == n3:
    prize = 1000 + n2 * 100
else:
    prize = max(n1, n2, n3) * 100

print(prize)