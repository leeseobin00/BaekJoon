# 1: 1
# 2: 2-7 (1-6)+1
# 3: 8-19 (1-12)+(6+1)
# 4: 20-37 (1-18) + (1+6+12)
# 5: 38- 61 (1-24) + (1+6+12+18)

# 1 -> (1+6) -> (1+6+12) ->
import sys
input = sys.stdin.readline

result = 1
i = 1

# 1 + 0 * 6
# 1 + 0 * 6 + 1 * 6
n = int(input())
while result < n:
    result += i * 6
    i += 1

print(i)
