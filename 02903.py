n = int(input())

# 0 -> 2**2
# 1 -> (2*2-1)**2
# 2 -> 5**2 = (3*2 -1)**2
# 3 -> (5*2-1)**2
# 4 -> (9*2-1)**2
# 5 -> (17*2-1)**2

result = 2
for i in range(n):
    result = (result * 2 -1)
print(result**2)