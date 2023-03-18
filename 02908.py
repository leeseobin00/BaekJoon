a, b = map(int, input().split())

A = (a%10) * 100 + (int(a/10) - int(a/100)*10) * 10 + int(a/100)
B = (b%10) * 100 + (int(b/10) - int(b/100)*10) * 10 + int(b/100)

print(max(A, B))